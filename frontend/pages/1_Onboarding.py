# pages/1_Onboarding.py
import streamlit as st
import requests
import time

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Setup Your Profile - LifeTune",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {}
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'temp_time' not in st.session_state:
    st.session_state.temp_time = 30

# ========================================
# REFINED CSS - Matching Home.py Aesthetic
# ========================================
st.markdown("""
<style>
    /* Global */
    .main {
        padding: 0 !important;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
    }
    .block-container {
        padding: 2rem 4rem !important;
        max-width: 1400px !important;
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Progress Bar - Clean Square Design */
    .progress-container {
        display: flex; 
        justify-content: center; 
        align-items: center; 
        margin: 2rem 0 3rem 0; 
        position: relative;
    }
    .progress-line {
        position: absolute; 
        height: 2px; 
        background: rgba(255,255,255,0.1); 
        width: 60%; 
        z-index: 0;
    }
    .progress-line-active {
        position: absolute; 
        height: 2px; 
        background: linear-gradient(90deg, #00ff87 0%, #60efff 100%);
        width: 0%; 
        z-index: 0; 
        transition: width 0.5s ease;
    }
    .step-indicator {
        display: flex; 
        justify-content: center; 
        gap: 3rem; 
        position: relative; 
        z-index: 1;
    }
    .step-circle {
        width: 60px; 
        height: 60px; 
        background: #1a1d35;
        border: 2px solid rgba(255,255,255,0.1); 
        display: flex; 
        align-items: center;
        justify-content: center; 
        font-size: 1.5rem; 
        transition: all 0.4s;
        position: relative;
    }
    .step-circle.active {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        border-color: transparent; 
        transform: scale(1.15);
    }
    .step-circle.completed {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        border-color: transparent;
    }
    .step-label {
        position: absolute; 
        bottom: -28px; 
        font-size: 0.7rem; 
        color: #7a8199;
        text-transform: uppercase; 
        letter-spacing: 1px; 
        white-space: nowrap;
    }
    .step-circle.active .step-label {
        color: #00ff87; 
        font-weight: 700;
    }

    /* Header */
    .page-header {
        text-align: center; 
        margin: 2rem 0 3rem 0;
    }
    .page-title {
        font-size: 3.5rem; 
        font-weight: 900; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin-bottom: 0.5rem;
        text-transform: uppercase; 
        letter-spacing: 2px;
    }
    .page-subtitle {
        font-size: 1.2rem; 
        color: #9ca3c0; 
        font-weight: 400;
    }
    .current-goal {
        display: inline-block; 
        padding: 0.5rem 1.5rem; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        font-weight: 700; 
        margin-top: 1rem;
        text-transform: uppercase; 
        letter-spacing: 1.5px;
        font-size: 0.9rem;
    }

    /* Selection Cards - Square, Clean */
    .selection-grid {
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
        gap: 2rem; 
        margin: 2rem 0;
    }
    .selection-card {
        background: #1a1d35; 
        padding: 3rem 2rem;
        text-align: center; 
        border: 2px solid rgba(255,255,255,0.1); 
        transition: all 0.3s; 
        cursor: pointer;
        position: relative; 
        overflow: hidden;
    }
    .selection-card::before {
        content: ''; 
        position: absolute; 
        top: 0; 
        left: 0; 
        right: 0; 
        height: 3px;
        background: linear-gradient(90deg, #00ff87 0%, #60efff 100%); 
        transform: scaleX(0); 
        transition: transform 0.3s;
    }
    .selection-card:hover {
        transform: translateY(-5px); 
        border-color: rgba(0,255,135,0.5);
    }
    .selection-card:hover::before {
        transform: scaleX(1);
    }
    .card-icon {
        font-size: 3.5rem; 
        margin-bottom: 1.5rem;
    }
    .card-title {
        font-size: 1.5rem; 
        font-weight: 700; 
        color: white; 
        margin-bottom: 0.8rem; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }
    .card-desc {
        font-size: 0.95rem; 
        color: #9ca3c0; 
        line-height: 1.5;
    }

    /* Form Section */
    .form-section {
        max-width: 900px; 
        margin: 0 auto;
    }
    .stNumberInput > div > div > input {
        background: #1a1d35 !important; 
        border: 2px solid rgba(255,255,255,0.1) !important;
        color: white !important; 
        padding: 1rem !important; 
        font-size: 1.1rem !important;
        transition: all 0.3s !important;
    }
    .stNumberInput > div > div > input:focus {
        border-color: #00ff87 !important;
    }
    .stNumberInput label {
        color: white !important; 
        font-size: 1rem !important; 
        font-weight: 600 !important; 
        margin-bottom: 0.5rem !important; 
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* BMI Card */
    .bmi-card {
        background: #1a1d35;
        padding: 2rem; 
        margin-top: 1.5rem; 
        border: 2px solid rgba(0,255,135,0.2); 
        text-align: center;
    }
    .bmi-value {
        font-size: 2.5rem; 
        font-weight: 900; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin: 1rem 0;
    }
    .bmi-label {
        font-size: 0.9rem; 
        color: #9ca3c0; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }

    /* Time Pills - Square */
    .time-pill {
        background: #1a1d35; 
        border: 2px solid rgba(255,255,255,0.1);
        padding: 2rem 1.5rem; 
        text-align: center; 
        transition: all 0.3s; 
        cursor: pointer;
    }
    .time-pill:hover {
        border-color: #00ff87; 
        transform: scale(1.05);
    }
    .time-value {
        font-size: 2rem; 
        font-weight: 900; 
        color: white; 
        margin-bottom: 0.5rem;
    }
    .time-label {
        font-size: 0.85rem; 
        color: #9ca3c0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Success Badge */
    .success-badge {
        display: inline-block; 
        padding: 0.8rem 2rem; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        font-weight: 700; 
        font-size: 1rem; 
        margin: 1rem 0;
        text-transform: uppercase; 
        letter-spacing: 1.5px;
    }

    /* Summary Section */
    .summary-grid {
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); 
        gap: 2rem; 
        margin: 2rem 0;
    }
    .summary-card {
        background: #1a1d35;
        padding: 2.5rem; 
        border: 2px solid rgba(0,255,135,0.2);
    }
    .summary-item {
        display: flex; 
        justify-content: space-between; 
        padding: 1rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .summary-item:last-child {
        border-bottom: none;
    }
    .summary-label {
        font-size: 0.95rem; 
        color: #9ca3c0; 
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .summary-value {
        font-size: 1rem; 
        color: white; 
        font-weight: 700;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%) !important;
        color: #0a0e27 !important; 
        border: none !important; 
        padding: 1rem 2.5rem !important;
        font-size: 1rem !important; 
        font-weight: 700 !important; 
        text-transform: uppercase !important; 
        letter-spacing: 2px !important;
        transition: all 0.3s !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important; 
        box-shadow: 0 10px 30px rgba(0,255,135,0.3) !important;
    }
    div[data-testid="column"]:first-child .stButton>button {
        background: transparent !important; 
        border: 2px solid rgba(255,255,255,0.2) !important;
        color: white !important;
    }
    div[data-testid="column"]:first-child .stButton>button:hover {
        border-color: #00ff87 !important; 
        background: rgba(0,255,135,0.1) !important;
    }

    .stAlert {
        background: #1a1d35 !important;
        border: 2px solid rgba(0,255,135,0.3) !important; 
        color: white !important;
    }

    .stSpinner > div {
        border-color: #00ff87 transparent transparent transparent !important;
    }

    @media (max-width: 768px) {
        .block-container {padding: 1rem !important;}
        .page-title {font-size: 2rem;}
        .step-indicator {gap: 1rem;}
        .step-circle {width: 50px; height: 50px; font-size: 1.2rem;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# PROGRESS INDICATOR - FIXED & SAFE
# ========================================
def show_progress(current):
    steps = ["Goal", "Info", "Time", "Diet", "Generate"]
    icons = ["🎯", "📊", "⏰", "🍽️", "✨"]
    
    progress_html = '<div class="progress-container">'
    progress_html += '<div class="progress-line"></div>'
    progress_html += f'<div class="progress-line-active" style="width: {(current-1)*25}%;"></div>'
    progress_html += '<div class="step-indicator">'
    
    for i in range(1, 6):
        if i == current:
            cls = "step-circle active"
        elif i < current:
            cls = "step-circle completed"
        else:
            cls = "step-circle"
            
        progress_html += f'<div class="{cls}">'
        progress_html += f'<span>{icons[i-1]}</span>'
        progress_html += f'<div class="step-label">{steps[i-1]}</div>'
        progress_html += '</div>'
    
    progress_html += '</div></div>'
    
    st.markdown(progress_html, unsafe_allow_html=True)

show_progress(st.session_state.current_step)

# ========================================
# STEP 1: GOAL
# ========================================
if st.session_state.current_step == 1:
    st.markdown('''
        <div class="page-header">
            <h1 class="page-title">What's Your Fitness Goal?</h1>
            <p class="page-subtitle">Choose your primary objective to get started</p>
        </div>
    ''', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    goals = [
        ("💪 Gain Weight", "Build muscle mass and strength", "gain"),
        ("🔥 Lose Weight", "Burn fat and get lean", "lose"),
        ("✨ Stay Fit", "Maintain health and wellness", "fit")
    ]
    for col, (title, desc, key) in zip([col1, col2, col3], goals):
        with col:
            st.markdown(f'''
                <div class="selection-card">
                    <div class="card-icon">{title.split()[0]}</div>
                    <h3 class="card-title">{title.split(' ', 1)[1]}</h3>
                    <p class="card-desc">{desc}</p>
                </div>
            ''', unsafe_allow_html=True)
            if st.button("Select", key=key, use_container_width=True):
                st.session_state.profile_data['goal'] = title.split(' ', 1)[1].lower()
                st.session_state.current_step = 2
                st.rerun()

# ========================================
# STEP 2: BASIC INFO
# ========================================
elif st.session_state.current_step == 2:
    st.markdown(f'''
        <div class="page-header">
            <h1 class="page-title">Tell Us About Yourself</h1>
            <p class="page-subtitle">We'll use this to create your perfect plan</p>
            <div class="current-goal">{st.session_state.profile_data["goal"].upper()}</div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age (years)", min_value=15, max_value=80, value=25, step=1)
        height = st.number_input("Height (cm)", min_value=140, max_value=220, value=170, step=1)

    with col2:
        weight = st.number_input("Weight (kg)", min_value=40, max_value=150, value=65, step=1)
        if height > 0:
            bmi = weight / ((height/100) ** 2)
            st.markdown(f'''
                <div class="bmi-card">
                    <div class="bmi-label">Your BMI</div>
                    <div class="bmi-value">{bmi:.1f}</div>
                </div>
            ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← BACK", use_container_width=True):
            st.session_state.current_step = 1
            st.rerun()
    with col2:
        if st.button("NEXT →", use_container_width=True):
            st.session_state.profile_data.update({'age': age, 'height': float(height), 'weight': float(weight)})
            st.session_state.current_step = 3
            st.rerun()

# ========================================
# STEP 3: TIME & PREFERENCE
# ========================================
elif st.session_state.current_step == 3:
    st.markdown('''
        <div class="page-header">
            <h1 class="page-title">Workout Preferences</h1>
            <p class="page-subtitle">When and how long can you train?</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown("### Daily Time Available")
    col1, col2, col3, col4 = st.columns(4)
    times = [20, 30, 45, 60]
    for col, t in zip([col1, col2, col3, col4], times):
        with col:
            active = st.session_state.temp_time == t
            st.markdown(f'''
                <div class="time-pill" style="border-color: {'#00ff87' if active else 'rgba(255,255,255,0.1)'}">
                    <div class="time-value">{t}</div>
                    <div class="time-label">Minutes</div>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"Select {t} min", key=f"time_{t}", use_container_width=True):
                st.session_state.temp_time = t
                st.rerun()

    st.markdown(f'<div style="text-align: center; margin: 2rem 0;"><span class="success-badge">Selected: {st.session_state.temp_time} Minutes</span></div>', unsafe_allow_html=True)

    st.markdown("### Preferred Workout Time")
    col1, col2 = st.columns(2)
    prefs = [("🌅 Morning", "Start your day energized", "morning"), ("🌙 Evening", "Unwind after work", "evening")]
    for col, (title, desc, key) in zip([col1, col2], prefs):
        with col:
            st.markdown(f'''
                <div class="selection-card">
                    <div class="card-icon">{title.split()[0]}</div>
                    <h3 class="card-title">{title.split(' ', 1)[1]}</h3>
                    <p class="card-desc">{desc}</p>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"SELECT {title.split(' ', 1)[1].upper()}", key=key, use_container_width=True):
                st.session_state.profile_data.update({'time': st.session_state.temp_time, 'preference': key})
                st.session_state.current_step = 4
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← BACK", use_container_width=True):
            st.session_state.current_step = 2
            st.rerun()

# ========================================
# STEP 4: DIET
# ========================================
elif st.session_state.current_step == 4:
    st.markdown('''
        <div class="page-header">
            <h1 class="page-title">Food Preferences</h1>
            <p class="page-subtitle">Customize your nutrition plan</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown("### Dietary Type")
    col1, col2 = st.columns(2)
    diets = [("🥗 Vegetarian", "Plant-based Indian meals", "veg"),
             ("🍗 Non-Vegetarian", "High-protein with meat", "non-veg")]
    for col, (title, desc, key) in zip([col1, col2], diets):
        with col:
            st.markdown(f'''
                <div class="selection-card">
                    <div class="card-icon">{title.split()[0]}</div>
                    <h3 class="card-title">{title.split(' ', 1)[1]}</h3>
                    <p class="card-desc">{desc}</p>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"SELECT {title.split(' ', 1)[1].upper()}", key=key, use_container_width=True):
                st.session_state.profile_data['diet_type'] = key
                st.session_state.current_step = 5
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← BACK", use_container_width=True):
            st.session_state.current_step = 3
            st.rerun()

# ========================================
# STEP 5: GENERATE PLAN
# ========================================
elif st.session_state.current_step == 5:
    st.markdown('''
        <div class="page-header">
            <h1 class="page-title">Ready to Transform</h1>
            <p class="page-subtitle">Review your profile and generate your AI plan</p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="summary-grid">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'''
            <div class="summary-card">
                <div class="summary-item"><span class="summary-label">Goal</span><span class="summary-value">{st.session_state.profile_data['goal'].title()}</span></div>
                <div class="summary-item"><span class="summary-label">Age</span><span class="summary-value">{st.session_state.profile_data['age']} years</span></div>
                <div class="summary-item"><span class="summary-label">Height</span><span class="summary-value">{st.session_state.profile_data['height']} cm</span></div>
                <div class="summary-item"><span class="summary-label">Weight</span><span class="summary-value">{st.session_state.profile_data['weight']} kg</span></div>
            </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown(f'''
            <div class="summary-card">
                <div class="summary-item"><span class="summary-label">Time</span><span class="summary-value">{st.session_state.profile_data['time']} min/day</span></div>
                <div class="summary-item"><span class="summary-label">Schedule</span><span class="summary-value">{st.session_state.profile_data['preference'].title()}</span></div>
                <div class="summary-item"><span class="summary-label">Diet</span><span class="summary-value">{st.session_state.profile_data['diet_type'].upper()}</span></div>
                <div class="summary-item"><span class="summary-label">Cuisine</span><span class="summary-value">Indian</span></div>
            </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← EDIT PROFILE", use_container_width=True):
            st.session_state.current_step = 1
            st.rerun()
    with col2:
        if st.button("GENERATE MY PLAN →", use_container_width=True, type="primary"):
            with st.spinner("Creating your personalized plan... (60-90s)"):
                try:
                    response = requests.post(
                        "http://localhost:8000/generate-plan",
                        json=st.session_state.profile_data,
                        timeout=120
                    )
                    if response.status_code == 200:
                        st.session_state.plan_data = response.json()
                        st.success("✅ Your plan is ready!")
                        st.balloons()
                        time.sleep(1)
                        st.switch_page("pages/2_YourPlan.py")
                    else:
                        st.error(f"❌ Server Error: {response.status_code}")
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Cannot connect to backend. Is FastAPI running?")
                except Exception as e:
                    st.error("❌ An error occurred.")
                    with st.expander("Details"):
                        st.exception(e)