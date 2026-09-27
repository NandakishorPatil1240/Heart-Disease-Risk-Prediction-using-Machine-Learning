import joblib
import pandas as pd

from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from sqlalchemy.orm import declarative_base, sessionmaker


# ============================================================
# 1. INITIALIZE FASTAPI
# ============================================================

app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0"
)


# ============================================================
# 2. DATABASE CONFIGURATION
# ============================================================

DATABASE_URL = "sqlite:///./heart_disease.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ============================================================
# 3. DATABASE TABLE
# ============================================================

class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    age = Column(Integer)

    sex = Column(String)

    chest_pain_type = Column(String)

    resting_bp = Column(Float)

    cholesterol = Column(Float)

    fasting_bs = Column(Integer)

    resting_ecg = Column(String)

    max_hr = Column(Integer)

    exercise_angina = Column(String)

    oldpeak = Column(Float)

    st_slope = Column(String)

    prediction = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# Create database and table automatically
Base.metadata.create_all(bind=engine)


# ============================================================
# 4. LOAD ML MODEL
# ============================================================

try:

    model = joblib.load("KNN_heart.pkl")

    scaler = joblib.load("scaler.pkl")

    expected_columns = joblib.load("columns.pkl")

    print(
        "SUCCESS: All model files loaded correctly with Joblib!"
    )

except Exception as e:

    print(
        f"Error loading model files: {e}"
    )


# ============================================================
# 5. PYDANTIC INPUT SCHEMA
# ============================================================

class PatientData(BaseModel):

    Age: int

    RestingBP: float

    Cholesterol: float

    FastingBS: int

    MaxHR: int

    Oldpeak: float

    Sex: str

    ChestPainType: str

    RestingECG: str

    ExerciseAngina: str

    ST_Slope: str


# ============================================================
# 6. HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Heart Disease Prediction API is running!"
    }


# ============================================================
# 7. HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    try:

        db = SessionLocal()

        db.execute(
            __import__("sqlalchemy").text(
                "SELECT 1"
            )
        )

        db.close()

        return {
            "status": "healthy",
            "api": "running",
            "database": "connected",
            "model": "loaded"
        }

    except Exception as e:

        return {
            "status": "error",
            "database": "not connected",
            "error": str(e)
        }


# ============================================================
# 8. PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_heart_disease(
    patient: PatientData
):

    db = None

    try:

        # ----------------------------------------------------
        # Convert input to dictionary
        # ----------------------------------------------------

        data = patient.dict()


        # ----------------------------------------------------
        # Initialize expected encoded columns
        # ----------------------------------------------------

        encoded_data = {
            col: 0
            for col in expected_columns
        }


        # ----------------------------------------------------
        # Numerical features
        # ----------------------------------------------------

        encoded_data["Age"] = data["Age"]

        encoded_data["RestingBP"] = data["RestingBP"]

        encoded_data["Cholesterol"] = data["Cholesterol"]

        encoded_data["FastingBS"] = data["FastingBS"]

        encoded_data["MaxHR"] = data["MaxHR"]

        encoded_data["Oldpeak"] = data["Oldpeak"]


        # ----------------------------------------------------
        # Categorical One-Hot Encoding
        # ----------------------------------------------------

        sex_column = "Sex_" + data["Sex"]

        if sex_column in encoded_data:

            encoded_data[sex_column] = 1


        chest_pain_column = (
            "ChestPainType_"
            + data["ChestPainType"]
        )

        if chest_pain_column in encoded_data:

            encoded_data[chest_pain_column] = 1


        ecg_column = (
            "RestingECG_"
            + data["RestingECG"]
        )

        if ecg_column in encoded_data:

            encoded_data[ecg_column] = 1


        angina_column = (
            "ExerciseAngina_"
            + data["ExerciseAngina"]
        )

        if angina_column in encoded_data:

            encoded_data[angina_column] = 1


        slope_column = (
            "ST_Slope_"
            + data["ST_Slope"]
        )

        if slope_column in encoded_data:

            encoded_data[slope_column] = 1


        # ----------------------------------------------------
        # Create DataFrame
        # ----------------------------------------------------

        df_input = pd.DataFrame(
            [encoded_data]
        )[expected_columns]


        # ----------------------------------------------------
        # Scale input
        # ----------------------------------------------------

        scaled_input = scaler.transform(
            df_input
        )


        # ----------------------------------------------------
        # ML Prediction
        # ----------------------------------------------------

        prediction = model.predict(
            scaled_input
        )

        prediction_value = int(
            prediction[0]
        )


        # ====================================================
        # SAVE PREDICTION TO DATABASE
        # ====================================================

        db = SessionLocal()


        new_prediction = PredictionHistory(

            age=data["Age"],

            sex=data["Sex"],

            chest_pain_type=data[
                "ChestPainType"
            ],

            resting_bp=data[
                "RestingBP"
            ],

            cholesterol=data[
                "Cholesterol"
            ],

            fasting_bs=data[
                "FastingBS"
            ],

            resting_ecg=data[
                "RestingECG"
            ],

            max_hr=data[
                "MaxHR"
            ],

            exercise_angina=data[
                "ExerciseAngina"
            ],

            oldpeak=data[
                "Oldpeak"
            ],

            st_slope=data[
                "ST_Slope"
            ],

            prediction=prediction_value,

            created_at=datetime.utcnow()
        )


        db.add(
            new_prediction
        )

        db.commit()

        db.refresh(
            new_prediction
        )


        # ----------------------------------------------------
        # Return prediction
        # ----------------------------------------------------

        return {

            "status": "success",

            "prediction": prediction_value,

            "message": (
                "Prediction generated and "
                "saved successfully."
            ),

            "record_id": new_prediction.id
        }


    except Exception as e:

        if db:

            db.rollback()

        raise HTTPException(

            status_code=400,

            detail=(
                "Prediction error occurred: "
                + str(e)
            )
        )


    finally:

        if db:

            db.close()


# ============================================================
# 9. GET PREDICTION HISTORY
# ============================================================

@app.get("/history")
def get_prediction_history():

    db = SessionLocal()

    try:

        records = (
            db.query(
                PredictionHistory
            )
            .order_by(
                PredictionHistory.id.desc()
            )
            .all()
        )


        result = []


        for record in records:

            result.append({

                "id": record.id,

                "age": record.age,

                "sex": record.sex,

                "chest_pain_type":
                    record.chest_pain_type,

                "resting_bp":
                    record.resting_bp,

                "cholesterol":
                    record.cholesterol,

                "fasting_bs":
                    record.fasting_bs,

                "resting_ecg":
                    record.resting_ecg,

                "max_hr":
                    record.max_hr,

                "exercise_angina":
                    record.exercise_angina,

                "oldpeak":
                    record.oldpeak,

                "st_slope":
                    record.st_slope,

                "prediction":
                    record.prediction,

                "created_at":
                    record.created_at
            })


        return {

            "status": "success",

            "total_records":
                len(result),

            "data":
                result
        }


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=(
                "Could not retrieve history: "
                + str(e)
            )
        )


    finally:

        db.close()


