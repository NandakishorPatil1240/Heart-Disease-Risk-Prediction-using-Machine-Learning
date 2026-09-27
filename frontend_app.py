
import streamlit as st
import requests

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HeartGuard AI",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 100%);
        }

        /* Hide Streamlit default menu/footer */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        /* Main container */
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Hero section */
        .hero {
            background: linear-gradient(135deg, #b51735, #e63956);
            padding: 35px 40px;
            border-radius: 24px;
            color: white;
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(181, 23, 53, 0.20);
        }

        .hero-title {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .hero-subtitle {
            font-size: 18px;
            opacity: 0.92;
            margin-bottom: 0;
        }

        /* Section cards */
        .section-card {
            background: white;
            padding: 24px;
            border-radius: 20px;
            margin-bottom: 20px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.06);
            border: 1px solid #e8edf5;
        }

        .section-title {
            font-size: 22px;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 5px;
        }

        .section-description {
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 18px;
        }

        /* Input labels */
        label {
            font-weight: 600 !important;
            color: #374151 !important;
        }

        /* Predict button */
        .stButton > button {
            width: 100%;
            border-radius: 14px;
            height: 55px;
            background: linear-gradient(135deg, #b51735, #e63956);
            color: white;
            font-size: 18px;
            font-weight: 700;
            border: none;
            box-shadow: 0 7px 18px rgba(181, 23, 53, 0.25);
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(181, 23, 53, 0.35);
        }

        /* Form submit button */
        .stFormSubmitButton > button {
            width: 100%;
            height: 58px;
            border-radius: 15px;
            background: linear-gradient(135deg, #b51735, #e63956);
            color: white;
            font-size: 19px;
            font-weight: 800;
            border: none;
            box-shadow: 0 8px 20px rgba(181, 23, 53, 0.25);
        }

        .stFormSubmitButton > button:hover {
            transform: translateY(-2px);
        }

        /* Result cards */
        .result-high {
            background: #fff1f2;
            border: 2px solid #fecdd3;
            padding: 28px;
            border-radius: 20px;
            text-align: center;
            margin-top: 20px;
        }

        .result-low {
            background: #ecfdf5;
            border: 2px solid #a7f3d0;
            padding: 28px;
            border-radius: 20px;
            text-align: center;
            margin-top: 20px;
        }

        .result-icon {
            font-size: 48px;
        }

        .result-title {
            font-size: 28px;
            font-weight: 800;
            margin: 10px 0;
        }

        .result-text {
            font-size: 16px;
            color: #4b5563;
        }

        /* Info cards */
        .info-card {
            background: white;
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        }

        .info-number {
            font-size: 28px;
            font-weight: 800;
            color: #b51735;
        }

        .info-label {
            font-size: 13px;
            color: #6b7280;
        }

        /* Disclaimer */
        .disclaimer {
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-radius: 14px;
            padding: 15px 18px;
            color: #7c2d12;
            font-size: 13px;
            margin-top: 20px;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #6b7280;
            font-size: 13px;
            padding: 25px 0 5px 0;
        }

        /* Mobile */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 30px;
            }

            .hero {
                padding: 25px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">❤️ HeartGuard AI</div>
        <div class="hero-subtitle">
            Intelligent Heart Disease Risk Prediction System
        </div>
        <div style="margin-top:12px; font-size:14px; opacity:0.85;">
            Powered by Machine Learning • FastAPI • Streamlit
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">🩺 Patient Health Assessment</div>
        <div class="section-description">
            Enter the patient's clinical information below to generate
            a machine-learning-based risk prediction.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# QUICK INFORMATION CARDS
# ============================================================

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-number">11</div>
            <div class="info-label">Health Parameters</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with info2:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-number">AI</div>
            <div class="info-label">Machine Learning Model</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with info3:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-number">API</div>
            <div class="info-label">FastAPI Backend</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with info4:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-number">⚡</div>
            <div class="info-label">Real-Time Prediction</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# ============================================================
# PATIENT FORM
# ============================================================

with st.form("patient_form"):

    # --------------------------------------------------------
    # PERSONAL INFORMATION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">👤 Personal Information</div>
        <div class="section-description">
            Basic patient information
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=40,
            step=1
        )

    with col2:
        sex = st.selectbox(
            "Gender",
            ["M", "F"]
        )

    with col3:
        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"]
        )

    st.write("")

    # --------------------------------------------------------
    # VITAL / CLINICAL INFORMATION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">🩸 Clinical Information</div>
        <div class="section-description">
            Enter the patient's cardiovascular measurements
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        resting_bp = st.number_input(
            "Resting Blood Pressure",
            min_value=50,
            max_value=250,
            value=120,
            step=1
        )

    with col2:
        cholesterol = st.number_input(
            "Cholesterol (mg/dl)",
            min_value=100,
            max_value=600,
            value=200,
            step=1
        )

    with col3:
        max_hr = st.number_input(
            "Maximum Heart Rate",
            min_value=60,
            max_value=220,
            value=150,
            step=1
        )

    st.write("")

    # --------------------------------------------------------
    # TEST RESULTS
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">🔬 Diagnostic Results</div>
        <div class="section-description">
            Select the patient's diagnostic test results
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

    with col2:
        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

    with col3:
        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            ["Y", "N"],
            format_func=lambda x: "Yes" if x == "Y" else "No"
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        oldpeak = st.number_input(
            "ST Depression (Oldpeak)",
            min_value=0.0,
            max_value=6.2,
            value=1.0,
            step=0.1
        )

    with col2:
        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

    st.write("")

    # --------------------------------------------------------
    # PREDICT BUTTON
    # --------------------------------------------------------

    submit = st.form_submit_button(
        "🔮  Predict Heart Disease Risk"
    )

# ============================================================
# PREDICTION
# ============================================================

if submit:

    # Payload expected by FastAPI
    payload = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }

    # FastAPI endpoint
    API_URL = "http://127.0.0.1:8000/predict"

    with st.spinner("🔄 Analyzing patient information..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            # ------------------------------------------------
            # SUCCESS
            # ------------------------------------------------

            if response.status_code == 200:

                result = response.json()

                prediction = result.get("prediction")

                st.markdown(
                    "<br>",
                    unsafe_allow_html=True
                )

                # HIGH RISK
                if prediction == 1:

                    st.markdown(
                        """
                        <div class="result-high">
                            <div class="result-icon">⚠️</div>
                            <div class="result-title">
                                Higher Risk Indicated
                            </div>
                            <div class="result-text">
                                The machine learning model has predicted
                                a higher likelihood of heart disease based
                                on the information provided.
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.warning(
                        "Please consult a qualified healthcare professional "
                        "for proper medical evaluation."
                    )

                # LOW RISK
                else:

                    st.markdown(
                        """
                        <div class="result-low">
                            <div class="result-icon">💚</div>
                            <div class="result-title">
                                Lower Risk Indicated
                            </div>
                            <div class="result-text">
                                The machine learning model has predicted
                                a lower likelihood of heart disease based
                                on the information provided.
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.success(
                        "Continue maintaining a healthy lifestyle and "
                        "follow appropriate medical advice."
                    )

                # ------------------------------------------------
                # SHOW INPUT SUMMARY
                # ------------------------------------------------

                st.markdown(
                    """
                    <br>
                    <div class="section-title">
                        📋 Assessment Summary
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                summary_col1, summary_col2, summary_col3 = st.columns(3)

                with summary_col1:
                    st.metric("Age", age)

                with summary_col2:
                    st.metric("Blood Pressure", resting_bp)

                with summary_col3:
                    st.metric("Cholesterol", cholesterol)

            # ------------------------------------------------
            # BACKEND ERROR
            # ------------------------------------------------

            else:

                st.error(
                    f"Backend Server Error ({response.status_code})"
                )

                st.code(response.text)

        # ----------------------------------------------------
        # CONNECTION ERROR
        # ----------------------------------------------------

        except requests.exceptions.ConnectionError:

            st.error(
                """
                ❌ Could not connect to the FastAPI backend.

                Please make sure your FastAPI server is running at:

                http://127.0.0.1:8000
                """
            )

        # ----------------------------------------------------
        # TIMEOUT
        # ----------------------------------------------------

        except requests.exceptions.Timeout:

            st.error(
                "⏳ The backend server took too long to respond."
            )

        # ----------------------------------------------------
        # OTHER ERROR
        # ----------------------------------------------------

        except Exception as e:

            st.error(
                f"Unexpected error: {str(e)}"
            )

# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        ⚕️ <b>Medical Disclaimer:</b>
        This application is an educational machine-learning project
        and is not a medical diagnostic tool. Predictions should not
        be used as a substitute for professional medical advice,
        diagnosis, or treatment.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        ❤️ HeartGuard AI &nbsp;•&nbsp;
        Machine Learning Healthcare Project
        <br>
        Built with Python • Streamlit • FastAPI • Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)

