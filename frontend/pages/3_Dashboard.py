# pages/3_Dashboard.py
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
# MODERN WIDGET-STYLE CSS
# ========================================
st.markdown("""
<style>
    .main {
        padding: 0 !important;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
    }
    .block-container {
        padding: 1.5rem 2rem !important;
        max-width: 1400px !important;
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Header */
    .dashboard-header {
        text-align: center; 
        margin: 1rem 0 2rem 0;
    }
    .dashboard-title {
        font-size: 2.5rem; 
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem; 
        text-transform: uppercase; 
        letter-spacing: 2px;
    }
    .dashboard-subtitle {
        font-size: 1rem; 
        color: #9ca3c0; 
        font-weight: 400;
    }

    /* Widget Grid */
    .widget-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }

    /* Base Widget Card */
    .widget-card {
        background: rgba(26, 29, 53, 0.8);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .widget-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 255, 135, 0.3);
        box-shadow: 0 10px 30px rgba(0, 255, 135, 0.15);
    }

    /* Widget Title */
    .widget-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #9ca3c0;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Progress Circle Widget */
    .progress-circle-widget {
        text-align: center;
    }
    .progress-circle {
        width: 180px;
        height: 180px;
        margin: 1rem auto;
        position: relative;
    }
    .progress-circle svg {
        transform: rotate(-90deg);
    }
    .progress-circle-bg {
        fill: none;
        stroke: rgba(255, 255, 255, 0.1);
        stroke-width: 12;
    }
    .progress-circle-fill {
        fill: none;
        stroke: url(#gradient);
        stroke-width: 12;
        stroke-linecap: round;
        transition: stroke-dashoffset 1s ease;
    }
    .progress-percentage {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 3rem;
        font-weight: 900;
        color: white;
    }
    .progress-label {
        font-size: 0.9rem;
        color: #9ca3c0;
        margin-top: 0.5rem;
    }

    /* Stats Widget */
    .stat-value {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin: 1rem 0;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #9ca3c0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Line Chart Widget */
    .chart-container {
        height: 120px;
        margin: 1rem 0;
        position: relative;
    }
    .chart-line {
        stroke: url(#gradient);
        stroke-width: 3;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }
    .chart-area {
        fill: url(#areaGradient);
    }

    /* Today's Mission Widget */
    .mission-widget {
        grid-column: span 2;
    }
    .mission-tabs {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .mission-tab {
        flex: 1;
        padding: 0.8rem 1.5rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        font-weight: 600;
        color: #9ca3c0;
    }
    .mission-tab.active {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27;
        border-color: transparent;
    }
    .mission-content {
        margin-top: 1rem;
    }
    .mission-focus {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: rgba(0, 255, 135, 0.1);
        color: #00ff87;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .item-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .item-entry {
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem;
        margin-bottom: 0.8rem;
        border-radius: 12px;
        border-left: 3px solid #00ff87;
        transition: all 0.3s;
    }
    .item-entry:hover {
        background: rgba(0, 255, 135, 0.08);
        transform: translateX(5px);
    }
    .item-name {
        font-size: 1rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.3rem;
    }
    .item-detail {
        font-size: 0.85rem;
        color: #00ff87;
        font-weight: 600;
    }

    /* Weekly Progress Widget */
    .weekly-widget {
        grid-column: span 2;
    }
    .week-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 0.8rem;
        margin-top: 1rem;
    }
    .day-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s;
    }
    .day-card.completed {
        background: rgba(0, 255, 135, 0.1);
        border-color: #00ff87;
    }
    .day-card.current {
        border: 2px solid #60efff;
        box-shadow: 0 0 20px rgba(96, 239, 255, 0.3);
    }
    .day-number {
        font-size: 0.75rem;
        color: #9ca3c0;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .day-date {
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.8rem;
    }
    .day-icons {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
    }
    .status-icon {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.7rem;
    }
    .status-icon.check {
        background: #00ff87;
        color: #0a0e27;
    }
    .status-icon.cross {
        background: rgba(255, 68, 68, 0.2);
        color: #ff4444;
    }

    /* Action Widget */
    .action-widget {
        text-align: center;
    }
    .checkbox-group {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        margin: 1.5rem 0;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%) !important;
        color: #0a0e27 !important; 
        border: none !important; 
        padding: 1rem 2rem !important;
        font-size: 1rem !important; 
        font-weight: 700 !important; 
        text-transform: uppercase !important; 
        letter-spacing: 1.5px !important;
        border-radius: 12px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 255, 135, 0.3);
    }

    /* Navigation */
    .nav-section {
        margin-top: 3rem;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
    }

    @media (max-width: 1024px) {
        .mission-widget, .weekly-widget {
            grid-column: span 1;
        }
        .week-grid {
            grid-template-columns: repeat(4, 1fr);
        }
    }

    @media (max-width: 768px) {
        .widget-grid {
            grid-template-columns: 1fr;
        }
        .week-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .nav-section {
            grid-template-columns: 1fr;
        }
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
progress = st.session_state.progress_data

# Calculate stats
w_streak = sum(1 for v in progress.values() if v.get('workout'))
d_streak = sum(1 for v in progress.values() if v.get('diet'))
total_done = len([k for k in progress.keys() if k <= today_key])
completion = ((w_streak + d_streak) / (total_done * 2) * 100) if total_done else 0

# ========================================
# HEADER
# ========================================
st.markdown('''
    <div class="dashboard-header">
        <h1 class="dashboard-title">Fitness Dashboard</h1>
        <p class="dashboard-subtitle">Track your progress • Stay motivated • Achieve your goals</p>
    </div>
''', unsafe_allow_html=True)

# ========================================
# WIDGET GRID - ROW 1
# ========================================
st.markdown('<div class="widget-grid">', unsafe_allow_html=True)

# Progress Circle Widget
circumference = 2 * 3.14159 * 70
offset = circumference - (completion / 100 * circumference)
st.markdown(f'''
    <div class="widget-card progress-circle-widget">
        <div class="widget-title">Overall Progress</div>
        <div class="progress-circle">
            <svg width="180" height="180">
                <defs>
                    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#00ff87;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#60efff;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <circle class="progress-circle-bg" cx="90" cy="90" r="70"/>
                <circle class="progress-circle-fill" cx="90" cy="90" r="70"
                    style="stroke-dasharray: {circumference}; stroke-dashoffset: {offset};"/>
            </svg>
            <div class="progress-percentage">{completion:.0f}%</div>
        </div>
        <div class="progress-label">Week Completion</div>
    </div>
''', unsafe_allow_html=True)

# Current Day Widget
st.markdown(f'''
    <div class="widget-card">
        <div class="widget-title">Current Day</div>
        <div class="stat-value">{current_day + 1}</div>
        <div class="stat-label">of 7 Days</div>
    </div>
''', unsafe_allow_html=True)

# Workouts Completed Widget
st.markdown(f'''
    <div class="widget-card">
        <div class="widget-title">Workouts Done</div>
        <div class="stat-value">{w_streak}</div>
        <div class="stat-label">Sessions Completed</div>
    </div>
''', unsafe_allow_html=True)

# Diet Days Widget
st.markdown(f'''
    <div class="widget-card">
        <div class="widget-title">Diet Followed</div>
        <div class="stat-value">{d_streak}</div>
        <div class="stat-label">Days on Track</div>
    </div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# WIDGET GRID - ROW 2
# ========================================
st.markdown('<div class="widget-grid">', unsafe_allow_html=True)

# Today's Mission Widget
st.markdown('<div class="widget-card mission-widget">', unsafe_allow_html=True)
st.markdown('<div class="widget-title">📋 Today\'s Mission</div>', unsafe_allow_html=True)

# Create tabs
col1, col2 = st.columns(2)
with col1:
    workout_tab = st.button("💪 Workout", key="workout_tab", use_container_width=True)
with col2:
    diet_tab = st.button("🍽️ Nutrition", key="diet_tab", use_container_width=True)

# Default to workout view
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'workout'

if workout_tab:
    st.session_state.active_tab = 'workout'
if diet_tab:
    st.session_state.active_tab = 'diet'

# Display content based on active tab
if st.session_state.active_tab == 'workout':
    if workout_plan and current_day < len(workout_plan):
        day = workout_plan[current_day]
        focus = day.get("focus", "Full Body")
        time_of_day = day.get("time_of_day", "Anytime")
        
        st.markdown(f'''
            <div class="mission-content">
                <div class="mission-focus">{focus.upper()}</div>
                <div style="color: #60efff; font-weight: 600; margin-bottom: 1rem;">⏰ {time_of_day}</div>
                <ul class="item-list">
        ''', unsafe_allow_html=True)
        
        for ex in day.get('workout', []):
            name = ex.get('exercise', 'Unknown')
            detail = ex.get('duration') or ex.get('sets_reps', 'N/A')
            st.markdown(f'''
                <li class="item-entry">
                    <div class="item-name">{name}</div>
                    <div class="item-detail">{detail}</div>
                </li>
            ''', unsafe_allow_html=True)
        
        st.markdown('</ul></div>', unsafe_allow_html=True)
    else:
        st.info("🎉 Rest day - recovery is important!")
else:
    if diet_plan and current_day < len(diet_plan):
        day = diet_plan[current_day]
        calorie_target = day.get("daily_calorie_target", "N/A")
        
        st.markdown(f'''
            <div class="mission-content">
                <div class="mission-focus">🔥 {calorie_target} CAL</div>
                <ul class="item-list">
        ''', unsafe_allow_html=True)
        
        meal_icons = {"Breakfast": "🌅", "Lunch": "☀️", "Snack": "🍪", "Dinner": "🌙"}
        for meal, desc in day.get('meals', {}).items():
            icon = meal_icons.get(meal, "🍽️")
            st.markdown(f'''
                <li class="item-entry" style="border-left-color: #60efff;">
                    <div class="item-name">{icon} {meal}</div>
                    <div class="item-detail" style="color: #60efff;">{desc}</div>
                </li>
            ''', unsafe_allow_html=True)
        
        st.markdown('</ul></div>', unsafe_allow_html=True)
    else:
        st.info("No meals scheduled for today")

st.markdown('</div>', unsafe_allow_html=True)

# Action Widget (Progress Checkboxes)
st.markdown('<div class="widget-card action-widget">', unsafe_allow_html=True)
st.markdown('<div class="widget-title">✅ Log Today\'s Progress</div>', unsafe_allow_html=True)

workout_done = st.checkbox("💪 Completed Workout", value=progress.get(today_key, {}).get('workout', False), key="w_check")
diet_done = st.checkbox("🍽️ Followed Diet Plan", value=progress.get(today_key, {}).get('diet', False), key="d_check")

if st.button("💾 SAVE PROGRESS"):
    st.session_state.progress_data[today_key] = {
        'workout': workout_done,
        'diet': diet_done,
        'day': current_day + 1
    }
    st.success("✅ Progress saved successfully!")
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ========================================
# WEEKLY PROGRESS WIDGET
# ========================================
st.markdown('<div class="widget-grid">', unsafe_allow_html=True)
st.markdown('<div class="widget-card weekly-widget">', unsafe_allow_html=True)
st.markdown('<div class="widget-title">📊 Weekly Progress</div>', unsafe_allow_html=True)
st.markdown('<div class="week-grid">', unsafe_allow_html=True)

for i in range(7):
    date = start_date + timedelta(days=i)
    date_key = date.strftime("%Y-%m-%d")
    date_display = date.strftime("%d")
    day_name = date.strftime("%a")
    p = progress.get(date_key, {})
    
    is_current = i == current_day
    is_completed = p.get('workout') and p.get('diet')
    card_class = "day-card"
    if is_current:
        card_class += " current"
    elif is_completed:
        card_class += " completed"
    
    w_icon = '✓' if p.get('workout') else '✗'
    d_icon = '✓' if p.get('diet') else '✗'
    w_class = 'check' if p.get('workout') else 'cross'
    d_class = 'check' if p.get('diet') else 'cross'
    
    st.markdown(f'''
        <div class="{card_class}">
            <div class="day-number">{day_name}</div>
            <div class="day-date">{date_display}</div>
            <div class="day-icons">
                <div class="status-icon {w_class}">{w_icon}</div>
                <div class="status-icon {d_class}">{d_icon}</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div></div></div>', unsafe_allow_html=True)

# ========================================
# NAVIGATION
# ========================================
st.markdown('<div class="nav-section">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 VIEW FULL PLAN"):
        st.switch_page("pages/2_YourPlan.py")
with col2:
    if st.button("🔄 START NEW PLAN"):
        st.session_state.clear()
        st.switch_page("pages/1_Onboarding.py")
st.markdown('</div>', unsafe_allow_html=True)