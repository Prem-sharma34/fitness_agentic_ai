import streamlit as st
from datetime import datetime, timedelta
import json

st.set_page_config(page_title="Your Dashboard", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    .dashboard-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #e0e0e0;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
    }
    .stat-label {
        color: #666;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .today-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #667eea;
        margin: 1rem 0;
    }
    .checkbox-item {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    </style>
""", unsafe_allow_html=True)

if 'progress_data' not in st.session_state:
    st.session_state.progress_data = {}

if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now().strftime("%Y-%m-%d")

if 'plan_data' not in st.session_state or st.session_state.plan_data is None:
    st.warning("⚠️ No plan found. Please generate your plan first.")
    if st.button("← Go to Onboarding"):
        st.switch_page("pages/1_Onboarding.py")
    st.stop()

try:
    plan_data = st.session_state.plan_data
    workout_plan = plan_data.get('workout_plan', [])
    diet_plan_list = plan_data.get('diet_plan', [])
    
except Exception as e:
    st.error(f"Error loading plan data: {e}")
    st.stop()

start_date = datetime.strptime(st.session_state.start_date, "%Y-%m-%d")
today = datetime.now()
days_elapsed = (today - start_date).days
current_day = min(days_elapsed, 6)  

st.markdown(f"""
    <div class="dashboard-header">
        <h1>📊 Your Fitness Dashboard</h1>
        <p>Track your daily progress and stay motivated!</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

today_key = datetime.now().strftime("%Y-%m-%d")
workout_done = st.session_state.progress_data.get(today_key, {}).get('workout', False)
diet_done = st.session_state.progress_data.get(today_key, {}).get('diet', False)

total_days = len([d for d in st.session_state.progress_data.values() if d.get('workout') or d.get('diet')])
workout_streak = sum(1 for d in st.session_state.progress_data.values() if d.get('workout'))
diet_streak = sum(1 for d in st.session_state.progress_data.values() if d.get('diet'))

completion_rate = ((workout_streak + diet_streak) / (total_days * 2) * 100) if total_days > 0 else 0

with col1:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{current_day + 1}</div>
            <div class="stat-label">Current Day</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{workout_streak}</div>
            <div class="stat-label">Workouts Done</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{diet_streak}</div>
            <div class="stat-label">Diet Days</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{completion_rate:.0f}%</div>
            <div class="stat-label">Completion</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 📅 Today's Plan")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏋️ Workout")
    
    if workout_plan and len(workout_plan) > current_day:
        today_workout = workout_plan[current_day]
        
        st.markdown(f"**Focus:** {today_workout.get('focus', 'Workout')}")
        st.markdown(f"**Time:** {today_workout.get('time_of_day', 'Anytime')}")
        
        with st.expander("View Exercises"):
            for exercise in today_workout.get('workout', []):
                ex_name = exercise.get('exercise', '')
                detail = exercise.get('duration', exercise.get('sets_reps', ''))
                st.markdown(f"- **{ex_name}** - {detail}")
        
        workout_done = st.checkbox("✅ Completed today's workout", 
                                   value=st.session_state.progress_data.get(today_key, {}).get('workout', False),
                                   key="workout_check")
    else:
        st.info("Rest day or no workout available")
        workout_done = False

with col2:
    st.markdown("### 🍽️ Meals")
    
    if diet_plan_list and len(diet_plan_list) > current_day:
        today_diet = diet_plan_list[current_day]
        
        st.markdown(f"**Target:** {today_diet.get('daily_calorie_target', 'N/A')}")
        
        with st.expander("View Meals"):
            meals = today_diet.get('meals', {})
            for meal_type, meal_desc in meals.items():
                st.markdown(f"**{meal_type}:**")
                st.markdown(f"_{meal_desc}_")
                st.markdown("")
        
        diet_done = st.checkbox("✅ Followed today's diet plan", 
                               value=st.session_state.progress_data.get(today_key, {}).get('diet', False),
                               key="diet_check")
    else:
        st.info("No meal plan available")
        diet_done = False

if st.button("💾 Save Today's Progress", use_container_width=True):
    st.session_state.progress_data[today_key] = {
        'workout': workout_done,
        'diet': diet_done,
        'day': current_day + 1
    }
    st.success("✅ Progress saved!")
    st.rerun()

st.markdown("---")

if workout_done and diet_done:
    st.success("🎉 Amazing! You crushed both workout and diet today! Keep it up!")
elif workout_done or diet_done:
    st.info("👍 Good job! You're making progress. Try to complete both tomorrow!")
else:
    st.warning("💪 Don't give up! Every journey starts with a single step. You've got this!")

st.markdown("## 📈 Weekly Progress")

progress_data = []
for i in range(7):
    day_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    day_progress = st.session_state.progress_data.get(day_date, {})
    progress_data.append({
        'Day': f"Day {i+1}",
        'Workout': '✅' if day_progress.get('workout') else '⬜',
        'Diet': '✅' if day_progress.get('diet') else '⬜'
    })

st.table(progress_data)

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("← View Plan", use_container_width=True):
        st.switch_page("pages/2_YourPlan.py")

with col2:
    if st.button("🔄 Start New Plan", use_container_width=True):
        st.session_state.plan_data = None
        st.session_state.progress_data = {}
        st.session_state.current_step = 1
        st.switch_page("pages/1_Onboarding.py")