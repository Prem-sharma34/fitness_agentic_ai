import streamlit as st
import requests

st.set_page_config(page_title="Setup Your Profile", page_icon="📝", layout="wide")

if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {}
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1

st.markdown("""
    <style>
    .step-indicator {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
        gap: 1rem;
    }
    .step {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 10px;
        font-weight: bold;
        font-size: 1.2rem;
        transition: all 0.3s;
    }
    .step.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: scale(1.2);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.5);
    }
    .step.completed {
        background: #4caf50;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        padding: 1.5rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        min-height: 80px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-align: center;
    }
    .section-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .info-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    div[data-testid="column"] {
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

def show_progress(current):
    steps = ["🎯", "📊", "⏰", "🍽️", "✨"]
    progress_html = '<div class="step-indicator">'
    for i in range(1, 6):
        if i < current:
            progress_html += f'<div class="step completed">{steps[i-1]}</div>'
        elif i == current:
            progress_html += f'<div class="step active">{steps[i-1]}</div>'
        else:
            progress_html += f'<div class="step">{steps[i-1]}</div>'
    progress_html += '</div>'
    st.markdown(progress_html, unsafe_allow_html=True)

show_progress(st.session_state.current_step)
st.markdown("---")

# ============================================
# STEP 1: Choose Your Goal
# ============================================
if st.session_state.current_step == 1:
    st.markdown('<h1 class="section-title">🎯 What\'s Your Fitness Goal?</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Let\'s start with what you want to achieve</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 💪")
        st.markdown("**Gain Weight**")
        st.caption("Build muscle mass and strength")
        if st.button("Select Gain Weight", key="gain", use_container_width=True):
            st.session_state.profile_data['goal'] = 'gain weight'
            st.session_state.current_step = 2
            st.rerun()
    
    with col2:
        st.markdown("### 🔥")
        st.markdown("**Lose Weight**")
        st.caption("Burn fat and get lean")
        if st.button("Select Lose Weight", key="lose", use_container_width=True):
            st.session_state.profile_data['goal'] = 'lose weight'
            st.session_state.current_step = 2
            st.rerun()
    
    with col3:
        st.markdown("### ⚡")
        st.markdown("**Stay Fit**")
        st.caption("Maintain health and wellness")
        if st.button("Select Stay Fit", key="fit", use_container_width=True):
            st.session_state.profile_data['goal'] = 'stay fit'
            st.session_state.current_step = 2
            st.rerun()

# ============================================
# STEP 2: Basic Info
# ============================================
elif st.session_state.current_step == 2:
    st.markdown('<h1 class="section-title">📊 Tell Us About Yourself</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="section-subtitle">Goal: <strong>{st.session_state.profile_data["goal"].title()}</strong></p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("🎂 Age (years)", min_value=15, max_value=80, value=25, step=1, help="Your current age")
        height = st.number_input("📏 Height (cm)", min_value=140, max_value=220, value=170, step=1, help="Your height in centimeters")
    
    with col2:
        weight = st.number_input("⚖️ Weight (kg)", min_value=40, max_value=150, value=65, step=1, help="Your current weight in kilograms")
        
        if height > 0:
            bmi = weight / ((height/100) ** 2)
            
            st.markdown("---")
            st.metric("📈 Your BMI", f"{bmi:.1f}")
            
            if bmi < 18.5:
                st.info("💡 You're underweight. Building muscle is a great goal!")
            elif 18.5 <= bmi < 25:
                st.success("✅ You're in a healthy weight range!")
            elif 25 <= bmi < 30:
                st.warning("⚠️ You're slightly overweight. Let's work on it together!")
            else:
                st.error("🚨 Please consult a doctor before starting intense workouts")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_step = 1
            st.rerun()
    with col2:
        if st.button("Next →", use_container_width=True):
            st.session_state.profile_data['age'] = age
            st.session_state.profile_data['height'] = float(height)
            st.session_state.profile_data['weight'] = float(weight)
            st.session_state.current_step = 3
            st.rerun()


elif st.session_state.current_step == 3:
    st.markdown('<h1 class="section-title">⏰ Your Workout Preferences</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">When and how long can you workout?</p>', unsafe_allow_html=True)
    
    st.markdown("### ⏱️ Daily Time Available")
    
    col1, col2, col3, col4 = st.columns(4)
    
    if 'temp_time' not in st.session_state:
        st.session_state.temp_time = 30
    
    with col1:
        if st.button("**20 mins**\n\nQuick & effective", key="time_20", use_container_width=True):
            st.session_state.temp_time = 20
            st.rerun()
    with col2:
        if st.button("**30 mins**\n\nBalanced routine", key="time_30", use_container_width=True):
            st.session_state.temp_time = 30
            st.rerun()
    with col3:
        if st.button("**45 mins**\n\nComprehensive", key="time_45", use_container_width=True):
            st.session_state.temp_time = 45
            st.rerun()
    with col4:
        if st.button("**60 mins**\n\nFull training", key="time_60", use_container_width=True):
            st.session_state.temp_time = 60
            st.rerun()
    
    st.success(f"✅ Selected: **{st.session_state.temp_time} minutes** per day")
    
    st.markdown("---")
    st.markdown("### 🌅 Preferred Workout Time")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌅")
        st.markdown("**Morning Workout**")
        st.caption("Start your day energized and fresh")
        if st.button("Select Morning", key="morning_btn", use_container_width=True):
            st.session_state.profile_data['preference'] = 'morning'
            st.session_state.profile_data['time'] = st.session_state.temp_time
            st.session_state.current_step = 4
            st.rerun()
    
    with col2:
        st.markdown("### 🌙")
        st.markdown("**Evening Workout**")
        st.caption("Unwind after a long day")
        if st.button("Select Evening", key="evening_btn", use_container_width=True):
            st.session_state.profile_data['preference'] = 'evening'
            st.session_state.profile_data['time'] = st.session_state.temp_time
            st.session_state.current_step = 4
            st.rerun()
    
    st.markdown("---")
    if st.button("← Back", use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()

# ============================================
# STEP 4: Diet Preferences
# ============================================
elif st.session_state.current_step == 4:
    st.markdown('<h1 class="section-title">🍽️ Your Food Preferences</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Let\'s customize your meal plan with Indian foods</p>', unsafe_allow_html=True)
    
    st.markdown("### 🥗 Dietary Type")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🥗")
        st.markdown("**Vegetarian**")
        st.caption("Delicious plant-based Indian meals")
        if st.button("Select Vegetarian", key="veg_btn", use_container_width=True):
            st.session_state.profile_data['diet_type'] = 'veg'
            st.session_state.current_step = 5
            st.rerun()
    
    with col2:
        st.markdown("### 🍗")
        st.markdown("**Non-Vegetarian**")
        st.caption("Includes chicken, fish & eggs")
        if st.button("Select Non-Vegetarian", key="nonveg_btn", use_container_width=True):
            st.session_state.profile_data['diet_type'] = 'non-veg'
            st.session_state.current_step = 5
            st.rerun()
    
    st.info("💡 All meal plans feature authentic Indian cuisine tailored to your goals!")
    
    st.markdown("---")
    if st.button("← Back", use_container_width=True):
        st.session_state.current_step = 3
        st.rerun()

# ============================================
# STEP 5: Generate Plan
# ============================================
elif st.session_state.current_step == 5:
    st.markdown('<h1 class="section-title">✨ Ready to Generate Your Plan!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Review your profile and let our AI create your personalized plan</p>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Your Profile Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="info-card">
        <strong>🎯 Fitness Goal:</strong> {st.session_state.profile_data['goal'].title()}<br><br>
        <strong>🎂 Age:</strong> {st.session_state.profile_data['age']} years<br><br>
        <strong>📏 Height:</strong> {st.session_state.profile_data['height']} cm<br><br>
        <strong>⚖️ Weight:</strong> {st.session_state.profile_data['weight']} kg
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="info-card">
        <strong>⏱️ Workout Time:</strong> {st.session_state.profile_data['time']} minutes/day<br><br>
        <strong>🌅 Preference:</strong> {st.session_state.profile_data['preference'].title()}<br><br>
        <strong>🍽️ Diet Type:</strong> {st.session_state.profile_data['diet_type'].upper()}<br><br>
        <strong>🇮🇳 Cuisine:</strong> Indian
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("← Edit Profile", use_container_width=True):
            st.session_state.current_step = 1
            st.rerun()
    
    with col2:
        if st.button("🚀 Generate My Plan", use_container_width=True, type="primary"):
            with st.spinner("🤖 Our AI agents are crafting your personalized plan... This may take 60-90 seconds..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/generate-plan",
                        json=st.session_state.profile_data,
                        timeout=120
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        st.session_state.plan_data = result
                        
                        st.success("✅ Your personalized plan is ready!")
                        st.balloons()
                        
                        import time
                        time.sleep(1)
                        
                        st.switch_page("pages/2_YourPlan.py")
                    else:
                        st.error(f"❌ Server Error: {response.status_code}")
                        with st.expander("Show error details"):
                            st.code(response.text)
                
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. The AI agents are taking longer than expected. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 **Cannot connect to backend server.**")
                    st.code("Make sure FastAPI is running:\ncd backend\nuvicorn app.main:app --reload")
                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {str(e)}")
                    with st.expander("Show full error"):
                        st.exception(e)