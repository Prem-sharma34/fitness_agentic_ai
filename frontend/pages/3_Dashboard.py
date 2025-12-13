import streamlit as st
from datetime import datetime, timedelta

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="AI Dashboard - LifeTune",
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
    .dashboard-header {
        text-align: center; 
        margin: 2rem 0 3rem 0;
    }
    .dashboard-title {
        font-size: 3.5rem; 
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem; 
        text-transform: uppercase; 
        letter-spacing: 2px;
    }
    .dashboard-subtitle {
        font-size: 1.2rem; 
        color: #9ca3c0; 
        font-weight: 400;
    }

    /* Stats Grid - Clean Square Design */
    .stats-grid {
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem; 
        margin: 3rem 0;
    }
    .stat-card {
        background: #1a1d35;
        padding: 2.5rem; 
        text-align: center;
        border: 2px solid rgba(255,255,255,0.05); 
        transition: all 0.3s;
        position: relative; 
        overflow: hidden;
    }
    .stat-card::before {
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
    .stat-card:hover {
        transform: translateY(-5px); 
        border-color: rgba(0,255,135,0.5);
    }
    .stat-card:hover::before {
        transform: scaleX(1);
    }
    .stat-value {
        font-size: 3rem; 
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin: 1rem 0;
    }
    .stat-label {
        font-size: 0.9rem; 
        color: #9ca3c0; 
        text-transform: uppercase; 
        letter-spacing: 1px;
    }

    /* Today's Plan - Square, Clean */
    .today-container {
        background: #1a1d35;
        padding: 3rem; 
        border: 2px solid rgba(0,255,135,0.3);
        margin: 3rem 0;
    }
    .today-title {
        font-size: 1.8rem; 
        font-weight: 800; 
        color: white; 
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .today-focus {
        display: inline-block; 
        padding: 0.5rem 1.5rem; 
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        font-weight: 700; 
        font-size: 0.9rem;
        text-transform: uppercase; 
        letter-spacing: 1.5px;
        margin-bottom: 1rem;
    }
    .today-time {
        color: #00ff87; 
        font-size: 1rem; 
        font-weight: 600; 
        margin: 1rem 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Exercise / Meal Items - Square */
    .item-card {
        background: rgba(255,255,255,0.03); 
        border-left: 3px solid #00ff87;
        padding: 1.5rem; 
        margin: 1rem 0;
        transition: all 0.3s;
    }
    .item-card:hover {
        background: rgba(0,255,135,0.08); 
        transform: translateX(8px);
    }
    .item-name {
        font-size: 1.2rem; 
        font-weight: 700; 
        color: white;
    }
    .item-detail {
        color: #00ff87; 
        font-size: 0.95rem; 
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .meal-card {
        border-left-color: #60efff;
    }
    .meal-card .item-detail {
        color: #60efff;
    }

    /* Checkboxes - Cleaner Design */
    .stCheckbox > label {
        background: #1a1d35 !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        padding: 1rem 1.5rem !important;
        transition: all 0.3s !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        font-size: 0.95rem !important;
    }
    .stCheckbox > label:hover {
        border-color: #00ff87 !important;
        background: rgba(0,255,135,0.05) !important;
    }

    /* Progress Table - Square Design */
    .progress-table {
        background: #1a1d35; 
        overflow: hidden;
        border: 2px solid rgba(255,255,255,0.1); 
        margin: 3rem 0;
    }
    .progress-table th {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; 
        padding: 1.2rem; 
        font-weight: 700; 
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.9rem;
    }
    .progress-table td {
        padding: 1rem; 
        text-align: center; 
        border-bottom: 1px solid rgba(255,255,255,0.05);
        color: #b0b8d4;
        font-weight: 600;
    }
    .check {
        color: #00ff87; 
        font-weight: 900;
    }
    .cross {
        color: #ff4444; 
        font-weight: 900;
    }

    /* Section Headers */
    .section-header {
        text-align: center; 
        margin: 3rem 0 2rem 0;
    }
    .section-title {
        color: white; 
        font-weight: 800; 
        font-size: 1.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
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

    /* Navigation */
    .nav-buttons {
        display: flex; 
        justify-content: space-between; 
        gap: 1.5rem;
        margin: 3rem 0;
    }

    /* Expander - Cleaner */
    .streamlit-expanderHeader {
        background: rgba(0,255,135,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    @media (max-width: 768px) {
        .block-container {padding: 1rem !important;}
        .dashboard-title {font-size: 2.5rem;}
        .stats-grid {grid-template-columns: 1fr;}
        .nav-buttons {flex-direction: column;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# DATA & VALIDATION
# ========================================
if 'plan_data' not in st.session_state or not st.session_state.plan_data:
    st.warning("⚠️ No plan found. Please generate your plan first.")
    if st.button("Go to Onboarding"):
        st.switch_page("pages/1_Onboarding.py")
    st.stop()

if 'progress_data' not in st.session_state:
    st.session_state.progress_data = {}
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now().strftime("%Y-%m-%d")

plan = st.session_state.plan_data
workout_plan = plan.get('workout_plan', [])
diet_plan = plan.get('diet_plan', [])
start_date = datetime.strptime(st.session_state.start_date, "%Y-%m-%d")
current_day = min((datetime.now() - start_date).days, 6)
today_key = datetime.now().strftime("%Y-%m-%d")

# ========================================
# HEADER
# ========================================
st.markdown('''
    <div class="dashboard-header">
        <h1 class="dashboard-title">Fitness Dashboard</h1>
        <p class="dashboard-subtitle">Track your progress and crush your goals</p>
    </div>
''', unsafe_allow_html=True)

# ========================================
# STATS
# ========================================
progress = st.session_state.progress_data
total_done = sum(1 for v in progress.values() if v.get('workout') or v.get('diet'))
w_streak = sum(1 for v in progress.values() if v.get('workout'))
d_streak = sum(1 for v in progress.values() if v.get('diet'))
completion = (w_streak + d_streak) / (total_done * 2) * 100 if total_done else 0

st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
stats = [
    (current_day + 1, "Current Day"),
    (w_streak, "Workouts Done"),
    (d_streak, "Diet Days"),
    (f"{completion:.0f}%", "Completion")
]
for value, label in stats:
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-value">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# TODAY'S PLAN
# ========================================
st.markdown('''
    <div class="today-container">
        <div class="today-title">🎯 Today's Mission</div>
''', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💪 Workout")
    if workout_plan and current_day < len(workout_plan):
        day = workout_plan[current_day]
        st.markdown(f'<div class="today-focus">{day.get("focus", "Full Body")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="today-time">⏰ {day.get("time_of_day", "Anytime")}</div>', unsafe_allow_html=True)
        with st.expander("View Exercises"):
            for ex in day.get('workout', []):
                name = ex.get('exercise', '')
                detail = ex.get('duration') or ex.get('sets_reps', '')
                st.markdown(f'<div class="item-card"><div class="item-name">🏋️ {name}</div><div class="item-detail">{detail}</div></div>', unsafe_allow_html=True)
    else:
        st.info("No workout scheduled for today")
    
    workout_done = st.checkbox("✅ Completed Workout", key="w_check", value=progress.get(today_key, {}).get('workout', False))

with col2:
    st.markdown("### 🍽️ Meals")
    if diet_plan and current_day < len(diet_plan):
        day = diet_plan[current_day]
        st.markdown(f'<div class="today-focus">🔥 {day.get("daily_calorie_target", "N/A")}</div>', unsafe_allow_html=True)
        with st.expander("View Meals"):
            for meal, desc in day.get('meals', {}).items():
                icon = {"Breakfast": "🌅", "Lunch": "☀️", "Snack": "🍪", "Dinner": "🌙"}.get(meal, "🍽️")
                st.markdown(f'<div class="item-card meal-card"><div class="item-name">{icon} {meal}</div><div class="item-detail">{desc}</div></div>', unsafe_allow_html=True)
    else:
        st.info("No meals scheduled for today")
    
    diet_done = st.checkbox("✅ Followed Diet", key="d_check", value=progress.get(today_key, {}).get('diet', False))

st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# SAVE PROGRESS
# ========================================
if st.button("💾 SAVE TODAY'S PROGRESS", use_container_width=True):
    st.session_state.progress_data[today_key] = {
        'workout': workout_done,
        'diet': diet_done,
        'day': current_day + 1
    }
    st.success("✅ Progress saved successfully!")
    st.rerun()

# ========================================
# WEEKLY PROGRESS
# ========================================
st.markdown('''
    <div class="section-header">
        <h2 class="section-title">Weekly Overview</h2>
    </div>
    <div class="progress-table">
''', unsafe_allow_html=True)

table_html = '<table class="progress-table" style="width: 100%;"><thead><tr><th>Day</th><th>Date</th><th>Workout</th><th>Diet</th></tr></thead><tbody>'
for i in range(7):
    date = start_date + timedelta(days=i)
    date_key = date.strftime("%Y-%m-%d")
    date_display = date.strftime("%b %d")
    p = progress.get(date_key, {})
    w = "✓" if p.get('workout') else "✗"
    d = "✓" if p.get('diet') else "✗"
    w_class = "check" if p.get('workout') else "cross"
    d_class = "check" if p.get('diet') else "cross"
    table_html += f'<tr><td>Day {i+1}</td><td>{date_display}</td><td class="{w_class}">{w}</td><td class="{d_class}">{d}</td></tr>'
table_html += '</tbody></table></div>'
st.markdown(table_html, unsafe_allow_html=True)

# ========================================
# NAVIGATION
# ========================================
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 VIEW PLAN", use_container_width=True):
        st.switch_page("pages/2_YourPlan.py")
with col2:
    if st.button("🔄 START NEW PLAN", use_container_width=True):
        st.session_state.clear()
        st.switch_page("pages/1_Onboarding.py")
st.markdown('</div>', unsafe_allow_html=True)