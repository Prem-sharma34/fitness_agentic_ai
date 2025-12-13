import streamlit as st

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Your AI Plan - LifeTune",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# REFINED CSS - Matching Home.py Aesthetic
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
        text-align: center; 
        margin: 2rem 0 3rem 0;
    }
    .plan-title {
        font-size: 3.5rem; 
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem; 
        text-transform: uppercase; 
        letter-spacing: 2px;
    }
    .plan-subtitle {
        font-size: 1.2rem; 
        color: #9ca3c0; 
        font-weight: 400;
    }

    /* Tabs - Cleaner, Square Design */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center; 
        gap: 1.5rem; 
        margin-bottom: 3rem;
        border-bottom: 2px solid rgba(255,255,255,0.1);
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent; 
        color: #9ca3c0; 
        border: none;
        border-bottom: 3px solid transparent;
        padding: 1rem 2.5rem; 
        font-size: 1rem; 
        font-weight: 700;
        text-transform: uppercase; 
        letter-spacing: 1.5px; 
        transition: all 0.3s;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #00ff87;
        border-bottom-color: rgba(0,255,135,0.3);
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #00ff87;
        border-bottom-color: #00ff87;
        background: transparent;
    }

    /* Day Selector - Square Design */
    .day-selector {
        display: flex; 
        justify-content: center; 
        gap: 1rem; 
        flex-wrap: wrap; 
        margin: 2rem 0 3rem 0;
    }
    .day-btn {
        background: #1a1d35; 
        color: #b0b8d4; 
        border: 2px solid rgba(255,255,255,0.1);
        padding: 0.9rem 1.8rem; 
        font-weight: 700; 
        font-size: 0.95rem;
        transition: all 0.3s; 
        min-width: 90px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .day-btn:hover {
        border-color: #00ff87; 
        color: #00ff87;
        background: rgba(0,255,135,0.05);
        transform: translateY(-2px);
    }
    .day-btn.active {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        border-color: transparent;
    }

    /* Content Containers - Square, Clean */
    .workout-container {
        background: #1a1d35;
        padding: 3rem; 
        border: 1px solid rgba(255,255,255,0.1);
        margin: 2rem 0;
    }
    .workout-focus {
        display: inline-block; 
        padding: 0.6rem 1.5rem; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        font-weight: 700; 
        font-size: 0.95rem;
        text-transform: uppercase; 
        letter-spacing: 1.5px; 
        margin-bottom: 1.5rem;
    }
    .workout-time {
        color: #00ff87; 
        font-size: 1rem; 
        font-weight: 600; 
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .exercise-item {
        background: rgba(0,255,135,0.03); 
        border-left: 3px solid #00ff87;
        padding: 1.5rem; 
        margin: 1rem 0;
        transition: all 0.3s;
    }
    .exercise-item:hover {
        background: rgba(0,255,135,0.08); 
        transform: translateX(8px);
    }
    .exercise-name {
        font-size: 1.2rem; 
        font-weight: 700; 
        color: white; 
        margin-bottom: 0.5rem;
    }
    .exercise-detail {
        color: #00ff87; 
        font-size: 0.95rem; 
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Meal Container */
    .meal-container {
        background: #1a1d35;
        padding: 3rem; 
        border: 1px solid rgba(255,255,255,0.1);
        margin: 2rem 0;
    }
    .meal-calories {
        display: inline-block; 
        padding: 0.6rem 1.5rem; 
        background: linear-gradient(135deg, #60efff 0%, #00ff87 100%);
        color: #0a0e27; 
        font-weight: 700; 
        font-size: 0.95rem;
        text-transform: uppercase; 
        letter-spacing: 1.5px; 
        margin-bottom: 1.5rem;
    }
    .meal-item {
        background: rgba(96,239,255,0.03); 
        border-left: 3px solid #60efff;
        padding: 1.5rem; 
        margin: 1rem 0;
        transition: all 0.3s;
    }
    .meal-item:hover {
        background: rgba(96,239,255,0.08); 
        transform: translateX(8px);
    }
    .meal-title {
        font-size: 1.2rem; 
        font-weight: 700; 
        color: white; 
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .meal-desc {
        color: #b0b8d4; 
        font-size: 1rem; 
        line-height: 1.6;
    }

    /* Navigation Buttons */
    .nav-buttons {
        display: flex; 
        justify-content: space-between; 
        gap: 1.5rem;
        margin: 3rem 0;
    }
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

    /* Responsive */
    @media (max-width: 768px) {
        .block-container {padding: 1rem !important;}
        .plan-title {font-size: 2.5rem;}
        .day-selector {gap: 0.5rem;}
        .day-btn {padding: 0.8rem 1.2rem; font-size: 0.85rem;}
        .nav-buttons {flex-direction: column;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# DATA VALIDATION
# ========================================
if 'plan_data' not in st.session_state or not st.session_state.plan_data:
    st.warning("⚠️ No plan found. Please complete onboarding first.")
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
        <p class="plan-subtitle">Personalized workout and nutrition program</p>
    </div>
''', unsafe_allow_html=True)

# ========================================
# TABS
# ========================================
tab1, tab2 = st.tabs(["💪 WORKOUT", "🍽️ MEALS"])

# ========================================
# WORKOUT TAB
# ========================================
with tab1:
    if not workout_plan:
        st.info("📋 No workout plan available.")
    else:
        # Day Selector
        st.markdown('<div class="day-selector">', unsafe_allow_html=True)
        selected_day = st.session_state.get('selected_workout_day', 0)
        cols = st.columns(7)
        for i in range(7):
            with cols[i]:
                day_data = workout_plan[i] if i < len(workout_plan) else {}
                day_name = day_data.get('day', f'Day {i+1}')
                if st.button(day_name, key=f"wd{i}", use_container_width=True):
                    st.session_state.selected_workout_day = i
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Selected Day Content
        day = workout_plan[selected_day]
        st.markdown(f'''
            <div class="workout-container">
                <div class="workout-focus">{day.get('focus', 'Full Body')}</div>
                <div class="workout-time">⏰ {day.get('time_of_day', 'Anytime')} • {len(day.get('workout', []))} exercises</div>
        ''', unsafe_allow_html=True)

        for ex in day.get('workout', []):
            name = ex.get('exercise', 'Exercise')
            detail = ex.get('duration') or ex.get('sets_reps', '')
            st.markdown(f'''
                <div class="exercise-item">
                    <div class="exercise-name">🏋️ {name}</div>
                    <div class="exercise-detail">{detail}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# MEALS TAB
# ========================================
with tab2:
    if not diet_plan:
        st.info("📋 No meal plan available.")
    else:
        # Day Selector
        st.markdown('<div class="day-selector">', unsafe_allow_html=True)
        selected_day = st.session_state.get('selected_meal_day', 0)
        cols = st.columns(7)
        for i in range(7):
            with cols[i]:
                day_data = diet_plan[i] if i < len(diet_plan) else {}
                day_name = day_data.get('day', f'Day {i+1}')
                if st.button(day_name, key=f"md{i}", use_container_width=True):
                    st.session_state.selected_meal_day = i
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Selected Day Content
        day = diet_plan[selected_day]
        calories = day.get('daily_calorie_target', 'N/A')
        st.markdown(f'''
            <div class="meal-container">
                <div class="meal-calories">🔥 {calories} CALORIES</div>
        ''', unsafe_allow_html=True)

        meals = day.get('meals', {})
        icons = {"Breakfast": "🌅", "Lunch": "☀️", "Snack": "🍪", "Dinner": "🌙"}
        for meal_type, desc in meals.items():
            icon = icons.get(meal_type, "🍽️")
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
col1, col2 = st.columns(2)
with col1:
    if st.button("← BACK TO PROFILE", use_container_width=True):
        st.switch_page("pages/1_Onboarding.py")
with col2:
    if st.button("DASHBOARD →", use_container_width=True):
        st.switch_page("pages/3_Dashboard.py")
st.markdown('</div>', unsafe_allow_html=True)