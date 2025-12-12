import streamlit as st
from datetime import datetime, timedelta

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="AI Dashboard - LifeTune",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# PREMIUM CSS — Matches Onboarding & Plan
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
   ”) .dashboard-header {
        text-align: center; margin: 2rem 0 3rem 0;
    }
    .dashboard-title {
        font-size: 3.8rem; font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 2px;
    }
    .dashboard-subtitle {
        font-size: 1.4rem; color: #9ca3c0; font-weight: 300;
    }

    /* Stats Grid */
    .stats-grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem; margin: 3rem 0;
    }
    .stat-card {
        background: linear-gradient(135deg, #1a1d35 0%, #252945 100%);
        border-radius: 25px; padding: 2.5rem; text-align: center;
        border: 2px solid rgba(255,255,255,0.05); transition: all 0.4s;
        position: relative; overflow: hidden;
    }
    .stat-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
        background: linear-gradient(90deg, #00ff87 0%, #60efff 100%); transform: scaleX(0);
        transition: transform 0.3s;
    }
    .stat-card:hover {
        transform: translateY(-12px); border-color: rgba(0,255,135,0.5);
        box-shadow: 0 25px 70px rgba(0,255,135,0.25);
    }
    .stat-card:hover::before {transform: scaleX(1);}
    .stat-value {
        font-size: 3.5rem; font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 1rem 0;
    }
    .stat-label {
        font-size: 1.1rem; color: #9ca3c0; text-transform: uppercase; letter-spacing: 1px;
    }

    /* Today's Plan */
    .today-container {
        background: linear-gradient(135deg, rgba(0,255,135,0.1), rgba(96,239,255,0.1));
        border-radius: 25px; padding: 3rem; border: 2px solid #00ff87;
        margin: 3rem 0; box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }
    .today-title {
        font-size: 2rem; font-weight: 800; color: white; margin-bottom: 1.5rem;
        display: flex; align-items: center; gap: 0.8rem;
    }
    .today-focus {
        display: inline-block; padding: 0.5rem 1.5rem; background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; border-radius: 30px; font-weight: 700; font-size: 0.95rem;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .today-time {
        color: #00ff87; font-size: 1.1rem; font-weight: 600; margin: 1rem 0;
    }

    /* Exercise / Meal Items */
    .item-card {
        background: rgba(255,255,255,0.03); border-left: 5px solid #00ff87;
        padding: 1.5rem; border-radius: 12px; margin: 1rem 0;
        transition: all 0.3s;
    }
    .item-card:hover {
        background: rgba(0,255,135,0.08); transform: translateX(8px);
    }
    .item-name {
        font-size: 1.3rem; font-weight: 700; color: white;
    }
    .item-detail {
        color: #00ff87; font-size: 1rem; font-weight: 600;
    }
    .meal-card {border-left-color: #60efff;}
    .meal-card .item-detail {color: #60efff;}

    /* Checkboxes */
    .stCheckbox > label > div {
        background: #1a1d35 !important; border: 2px solid #333 !important;
        border-radius: 12px !important; padding: 1rem !important;
    }
    .stCheckbox > label > div[data-checked="true"] {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%) !important;
        border-color: transparent !important;
    }

    /* Progress Table */
    .progress-table {
        background: #1a1d35; border-radius: 20px; overflow: hidden;
        border: 2px solid rgba(255,255,255,0.1); margin: 3rem 0;
    }
    .progress-table th {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27; padding: 1.2rem; font-weight: 700; text-transform: uppercase;
    }
    .progress-table td {
        padding: 1rem; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .check {color: #00ff87; font-weight: 900;}
    .cross {color: #ff4444; font-weight: 900;}

    /* Save Button */
    .save-btn {
        text-align: center; margin: 2rem 0;
    }

    /* Navigation */
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

    @media (max-width: 768px) {
        .block-container {padding: 1rem !important;}
        .dashboard-title {font-size: 2.5rem;}
        .stats-grid {grid-template-columns: 1fr;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# DATA & VALIDATION
# ========================================
if 'plan_data' not in st.session_state or not st.session_state.plan_data:
    st.warning("No plan found. Please generate your plan first.")
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
        <h1 class="dashboard-title">AI Fitness Dashboard</h1>
        <p class="dashboard-subtitle">Track your progress. Crush your goals. Transform your life.</p>
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
    (f"{completion:.0f}%", "Completion Rate")
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
        <div class="today-title">Today's Mission</div>
''', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Workout")
    if workout_plan and current_day < len(workout_plan):
        day = workout_plan[current_day]
        st.markdown(f'<div class="today-focus">{day.get("focus", "Full Body")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="today-time">Time: {day.get("time_of_day", "Anytime")}</div>', unsafe_allow_html=True)
        with st.expander("View Exercises"):
            for ex in day.get('workout', []):
                name = ex.get('exercise', '')
                detail = ex.get('duration') or ex.get('sets_reps', '')
                st.markdown(f'<div class="item-card"><div class="item-name">{name}</div><div class="item-detail">{detail}</div></div>', unsafe_allow_html=True)
    workout_done = st.checkbox("Completed Workout", key="w_check")

with col2:
    st.markdown("### Meals")
    if diet_plan and current_day < len(diet_plan):
        day = diet_plan[current_day]
        st.markdown(f'<div class="today-focus">Fire {day.get("daily_calorie_target", "N/A")}</div>', unsafe_allow_html=True)
        with st.expander("View Meals"):
            for meal, desc in day.get('meals', {}).items():
                icon = {"Breakfast": "Sunrise", "Lunch": "Sun", "Snack": "Cookie", "Dinner": "Moon"}.get(meal, "Plate")
                st.markdown(f'<div class="item-card meal-card"><div class="item-name">{icon} {meal}</div><div class="item-detail">{desc}</div></div>', unsafe_allow_html=True)
    diet_done = st.checkbox("Followed Diet", key="d_check")

st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# SAVE PROGRESS
# ========================================
st.markdown('<div class="save-btn">', unsafe_allow_html=True)
if st.button("SAVE TODAY'S PROGRESS", use_container_width=True):
    st.session_state.progress_data[today_key] = {
        'workout': workout_done,
        'diet': diet_done,
        'day': current_day + 1
    }
    st.success("Progress saved!")
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# WEEKLY PROGRESS
# ========================================
st.markdown('''
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: white; font-weight: 800;">Weekly Overview</h2>
    </div>
    <div class="progress-table">
''', unsafe_allow_html=True)

table_html = '<table class="progress-table"><tr><th>Day</th><th>Workout</th><th>Diet</th></tr>'
for i in range(7):
    date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    p = progress.get(date, {})
    w = "Check" if p.get('workout') else "Cross"
    d = "Check" if p.get('diet') else "Cross"
    table_html += f'<tr><td>Day {i+1}</td><td class="{w.lower()}">{w}</td><td class="{d.lower()}">{d}</td></tr>'
table_html += '</table>'
st.markdown(table_html, unsafe_allow_html=True)

# ========================================
# NAVIGATION
# ========================================
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("View Plan", use_container_width=True):
        st.switch_page("pages/2_YourPlan.py")
with col2:
    if st.button("Start New Plan", use_container_width=True):
        st.session_state.clear()
        st.switch_page("pages/1_Onboarding.py")
st.markdown('</div>', unsafe_allow_html=True)