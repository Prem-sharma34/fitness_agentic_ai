import streamlit as st

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Your AI Plan - LifeTune",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# PREMIUM CSS — Matches Onboarding
# ========================================
st.markdown("""
<style>
    .main {
        padding: 0 !important;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
    }
    .block-container {
        padding: 2rem 4rem !important;
        max-width: 1400px !important;
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Header */
    .plan-header {
        text-align: center; margin: 2rem 0 3rem 0;
    }
    .plan-title {
        font-size: 3.8rem; font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 2px;
    }
    .plan-subtitle {
        font-size: 1.4rem; color: #9ca3c0; font-weight: 300;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center; gap: 2rem; margin-bottom: 3rem;
    }
    .stTabs [data-baseweb="tab"] {
        background: #1a1d35; color: #9ca3c0; border: 2px solid rgba(255,255,255,0.1);
        border-radius: 20px; padding: 1rem 3rem; font-size: 1.1rem; font-weight: 700;
        text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s;
    }
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #00ff87; color: white;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; border-color: transparent;
        box-shadow: 0 0 30px rgba(0,255,135,0.4);
    }

    /* Day Selector */
    .day-selector {
        display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;
    }
    .day-btn {
        background: #1a1d35; color: white; border: 2px solid rgba(255,255,255,0.1);
        border-radius: 15px; padding: 1rem 1.5rem; font-weight: 700; font-size: 1rem;
        transition: all 0.3s; min-width: 80px;
    }
    .day-btn:hover {
        border-color: #00ff87; transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0,255,135,0.2);
    }
    .day-btn.active {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; border-color: transparent;
        box-shadow: 0 0 25px rgba(0,255,135,0.5);
    }

    /* Workout Section */
    .workout-container {
        background: linear-gradient(135deg, #1a1d35 0%, #252945 100%);
        border-radius: 25px; padding: 3rem; border: 2px solid rgba(0,255,135,0.3);
        margin: 2rem 0; box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }
    .workout-focus {
        display: inline-block; padding: 0.6rem 1.8rem; background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; border-radius: 30px; font-weight: 700; font-size: 1rem;
        text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1.5rem;
    }
    .workout-time {
        color: #00ff87; font-size: 1.1rem; font-weight: 600; margin-bottom: 2rem;
    }
    .exercise-item {
        background: rgba(0,255,135,0.05); border-left: 5px solid #00ff87;
        padding: 1.5rem; border-radius: 12px; margin: 1rem 0;
        transition: all 0.3s;
    }
    .exercise-item:hover {
        background: rgba(0,255,135,0.1); transform: translateX(10px);
    }
    .exercise-name {
        font-size: 1.3rem; font-weight: 700; color: white; margin-bottom: 0.5rem;
    }
    .exercise-detail {
        color: #00ff87; font-size: 1rem; font-weight: 600;
    }

    /* Meal Section */
    .meal-container {
        background: linear-gradient(135deg, #1a1d35 0%, #252945 100%);
        border-radius: 25px; padding: 3rem; border: 2px solid rgba(96,239,255,0.3);
        margin: 2rem 0; box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }
    .meal-calories {
        display: inline-block; padding: 0.6rem 1.8rem; background: linear-gradient(135deg, #60efff 0%, #00ff87 100%);
        color: #0a0e27; border-radius: 30px; font-weight: 700; font-size: 1rem;
        text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1.5rem;
    }
    .meal-item {
        background: rgba(96,239,255,0.05); border-left: 5px solid #60efff;
        padding: 1.5rem; border-radius: 12px; margin: 1rem 0;
        transition: all 0.3s;
    }
    .meal-item:hover {
        background: rgba(96,239,255,0.1); transform: translateX(10px);
    }
    .meal-title {
        font-size: 1.3rem; font-weight: 700; color: white; margin-bottom: 0.5rem;
        display: flex; align-items: center; gap: 0.5rem;
    }
    .meal-desc {
        color: #b0b8d4; font-size: 1.1rem; line-height: 1.6; font-style: italic;
    }

    /* Navigation Buttons */
    .nav-buttons {
        display: flex; justify-content: space-between; margin: 3rem 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%) !important;
        color: #0a0e27 !important; border: none !important; padding: 1.2rem 3rem !important;
        font-size: 1.1rem !important; font-weight: 700 !important; border-radius: 50px !important;
        text-transform: uppercase !important; letter-spacing: 2px !important;
        box-shadow: 0 10px 30px rgba(0,255,135,0.3) !important; transition: all 0.3s !important;
        width: auto !important; min-width: 200px;
    }
    .stButton>button:hover {
        transform: translateY(-3px) !important; box-shadow: 0 15px 40px rgba(0,255,135,0.5) !important;
    }
    .back-btn button {
        background: transparent !important; border: 2px solid rgba(255,255,255,0.2) !important;
        color: white !important; box-shadow: none !important;
    }
    .back-btn button:hover {
        border-color: #00ff87 !important; background: rgba(0,255,135,0.1) !important;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .block-container {padding: 1rem !important;}
        .plan-title {font-size: 2.5rem;}
        .day-selector {gap: 0.5rem;}
        .day-btn {padding: 0.8rem 1rem; font-size: 0.9rem;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# DATA VALIDATION
# ========================================
if 'plan_data' not in st.session_state or not st.session_state.plan_data:
    st.warning("No plan found. Please complete onboarding.")
    if st.button("Go to Onboarding"):
        st.switch_page("pages/1_Onboarding.py")
    st.stop()

plan = st.session_state.plan_data
workout_plan = plan.get('workout_plan', [])
diet_plan = plan.get('diet_plan', [])

# ========================================
# HEADER
# ========================================
st.markdown('''
    <div class="plan-header">
        <h1 class="plan-title">Your 7-Day AI Plan</h1>
        <p class="plan-subtitle">Crafted by intelligent agents for your transformation</p>
    </div>
''', unsafe_allow_html=True)

# ========================================
# TABS
# ========================================
tab1, tab2 = st.tabs(["WORKOUT", "MEALS"])

# ========================================
# WORKOUT TAB
# ========================================
with tab1:
    if not workout_plan:
        st.info("No workout plan available.")
    else:
        # Day Selector
        st.markdown('<div class="day-selector">', unsafe_allow_html=True)
        selected_day = st.session_state.get('selected_workout_day', 0)
        for i in range(7):
            day_data = workout_plan[i] if i < len(workout_plan) else {}
            day_name = day_data.get('day', f'Day {i+1}')
            active = "active" if i == selected_day else ""
            if st.button(day_name, key=f"wd{i}", help=f"Select {day_name}"):
                st.session_state.selected_workout_day = i
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Selected Day Content
        day = workout_plan[selected_day]
        st.markdown(f'''
            <div class="workout-container">
                <div class="workout-focus">{day.get('focus', 'Full Body')}</div>
                <div class="workout-time">Time: {day.get('time_of_day', 'Anytime')} • {len(day.get('workout', []))} exercises</div>
        ''', unsafe_allow_html=True)

        for ex in day.get('workout', []):
            name = ex.get('exercise', 'Exercise')
            detail = ex.get('duration') or ex.get('sets_reps', '')
            st.markdown(f'''
                <div class="exercise-item">
                    <div class="exercise-name">{name}</div>
                    <div class="exercise-detail">{detail}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# MEALS TAB
# ========================================
with tab2:
    if not diet_plan:
        st.info("No meal plan available.")
    else:
        # Day Selector
        st.markdown('<div class="day-selector">', unsafe_allow_html=True)
        selected_day = st.session_state.get('selected_meal_day', 0)
        for i in range(7):
            day_data = diet_plan[i] if i < len(diet_plan) else {}
            day_name = day_data.get('day', f'Day {i+1}')
            active = "active" if i == selected_day else ""
            if st.button(day_name, key=f"md{i}", help=f"Select {day_name}"):
                st.session_state.selected_meal_day = i
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Selected Day Content
        day = diet_plan[selected_day]
        calories = day.get('daily_calorie_target', 'N/A')
        st.markdown(f'''
            <div class="meal-container">
                <div class="meal-calories">Calories: {calories}</div>
        ''', unsafe_allow_html=True)

        meals = day.get('meals', {})
        icons = {"Breakfast": "Sunrise", "Lunch": "Sun", "Snack": "Cookie", "Dinner": "Moon"}
        for meal_type, desc in meals.items():
            icon = icons.get(meal_type, "Plate")
            st.markdown(f'''
                <div class="meal-item">
                    <div class="meal-title">{icon} {meal_type}</div>
                    <div class="meal-desc">{desc}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# NAVIGATION
# ========================================
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("Back to Profile", use_container_width=True):
        st.switch_page("pages/1_Onboarding.py")
with col3:
    if st.button("Go to Dashboard", use_container_width=True):
        st.switch_page("pages/3_Dashboard.py")
st.markdown('</div>', unsafe_allow_html=True)