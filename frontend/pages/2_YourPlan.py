import streamlit as st
import json

st.set_page_config(page_title="Your Fitness Plan", page_icon="📅", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .plan-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    .day-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    .day-card:hover {
        border-color: #667eea;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
        transform: translateY(-3px);
    }
    .day-card.active {
        border-color: #667eea;
        border-width: 3px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    .day-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    .focus-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        margin: 0.5rem 0;
    }
    .exercise-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .meal-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #764ba2;
    }
    .tab-button {
        padding: 1rem 2rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        background: white;
        cursor: pointer;
        transition: all 0.3s;
        margin: 0.5rem;
    }
    .tab-button.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: #667eea;
    }
    .calorie-badge {
        background: #ffd700;
        color: #333;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Check if plan data exists
if 'plan_data' not in st.session_state or st.session_state.plan_data is None:
    st.warning("⚠️ No plan found. Please complete the onboarding first.")
    if st.button("← Go to Onboarding"):
        st.switch_page("pages/1_Onboarding.py")
    st.stop()

# Extract plan data
plan_data = st.session_state.plan_data

# Parse workout and diet plans
try:
    # Backend now returns properly structured data
    workout_plan = plan_data.get('workout_plan', [])
    diet_plan_list = plan_data.get('diet_plan', [])
    
    # Validate data
    if not workout_plan:
        st.warning("⚠️ Workout plan not available")
    if not diet_plan_list:
        st.warning("⚠️ Diet plan not available")
    
except Exception as e:
    st.error(f"Error loading plan data: {e}")
    if st.checkbox("Show debug info"):
        st.write("Raw data:", plan_data)
    st.stop()

# Header
st.markdown("""
    <div class="plan-header">
        <h1>🎯 Your Personalized 7-Day Fitness Plan</h1>
        <p>Follow this plan consistently for the best results!</p>
    </div>
""", unsafe_allow_html=True)

# Tab selection
tab1, tab2 = st.tabs(["🏋️ Workout Plan", "🍽️ Meal Plan"])

# WORKOUT PLAN TAB
with tab1:
    st.markdown("## 💪 Your Weekly Workout Schedule")
    
    # Day selector
    day_cols = st.columns(7)
    selected_day = st.session_state.get('selected_workout_day', 0)
    
    for idx, col in enumerate(day_cols):
        with col:
            if st.button(f"Day {idx + 1}", key=f"workout_day_{idx}", use_container_width=True):
                st.session_state.selected_workout_day = idx
                selected_day = idx
                st.rerun()
    
    st.markdown("---")
    
    # Display selected day workout
    if workout_plan and isinstance(workout_plan, list) and len(workout_plan) > selected_day:
        day_data = workout_plan[selected_day]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"<div class='day-header'>{day_data.get('day', f'Day {selected_day + 1}')}</div>", unsafe_allow_html=True)
            st.markdown(f"<span class='focus-badge'>{day_data.get('focus', 'Workout')}</span>", unsafe_allow_html=True)
        
        with col2:
            st.info(f"⏰ {day_data.get('time_of_day', 'Anytime')}")
        
        st.markdown("### Exercises")
        
        exercises = day_data.get('workout', [])
        for exercise in exercises:
            exercise_name = exercise.get('exercise', 'Exercise')
            
            if 'duration' in exercise:
                detail = f"⏱️ {exercise['duration']}"
            elif 'sets_reps' in exercise:
                detail = f"🔢 {exercise['sets_reps']}"
            else:
                detail = ""
            
            st.markdown(f"""
                <div class='exercise-item'>
                    <strong>{exercise_name}</strong><br>
                    <small>{detail}</small>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No workout data available for this day.")

# MEAL PLAN TAB
with tab2:
    st.markdown("## 🍽️ Your Weekly Meal Plan")
    
    # Day selector
    day_cols = st.columns(7)
    selected_meal_day = st.session_state.get('selected_meal_day', 0)
    
    for idx, col in enumerate(day_cols):
        with col:
            if st.button(f"Day {idx + 1}", key=f"meal_day_{idx}", use_container_width=True):
                st.session_state.selected_meal_day = idx
                selected_meal_day = idx
                st.rerun()
    
    st.markdown("---")
    
    # Display selected day meals
    if diet_plan_list and len(diet_plan_list) > selected_meal_day:
        day_data = diet_plan_list[selected_meal_day]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"<div class='day-header'>{day_data.get('day', f'Day {selected_meal_day + 1}')}</div>", unsafe_allow_html=True)
        
        with col2:
            calories = day_data.get('daily_calorie_target', 'Not specified')
            st.markdown(f"<span class='calorie-badge'>🔥 {calories}</span>", unsafe_allow_html=True)
        
        st.markdown("### Meals")
        
        meals = day_data.get('meals', {})
        
        for meal_type, meal_desc in meals.items():
            icon = "🌅" if meal_type == "Breakfast" else "☀️" if meal_type == "Lunch" else "🍪" if meal_type == "Snack" else "🌙"
            
            st.markdown(f"""
                <div class='meal-item'>
                    <strong>{icon} {meal_type}</strong><br>
                    <p style='margin-top: 0.5rem; color: #555;'>{meal_desc}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No meal data available for this day.")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("← Back to Profile", use_container_width=True):
        st.switch_page("pages/1_Onboarding.py")

with col3:
    if st.button("Go to Dashboard →", use_container_width=True):
        st.switch_page("pages/3_Dashboard.py")

# Tips Section
st.markdown("---")
st.markdown("### 💡 Quick Tips for Success")

tip_cols = st.columns(3)

with tip_cols[0]:
    st.info("""
    **Stay Hydrated**  
    Drink 8-10 glasses of water daily
    """)

with tip_cols[1]:
    st.success("""
    **Be Consistent**  
    Follow the plan for at least 4 weeks
    """)

with tip_cols[2]:
    st.warning("""
    **Rest Well**  
    Get 7-8 hours of sleep each night
    """)