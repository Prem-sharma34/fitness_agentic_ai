import streamlit as st
from utils.api import generate_plan

st.title("🧠 AI Fitness Plan Generator")

st.write("Fill your details to generate your 7-day personalized plan.")

goal = st.selectbox("Goal", ["lose weight", "gain weight", "stay fit"])
height = st.number_input("Height (cm)", 140, 220)
weight = st.number_input("Weight (kg)", 30, 180)
time = st.selectbox("Daily workout time", [20, 30, 40, 60])
preference = st.selectbox("Workout preference", ["morning", "evening"])
diet_type = st.selectbox("Diet Type", ["veg", "non-veg"])

if st.button("Generate Plan"):
    user_data = {
        "goal": goal,
        "height": height,
        "weight": weight,
        "time": time,
        "preference": preference,
        "diet_type": diet_type
    }

    with st.spinner("Generating your AI powered plan..."):
        result = generate_plan(user_data)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Plan Generated Successfully!")

        st.subheader("🏋️ Workout Plan")
        st.json(result["workout_plan"])

        st.subheader("🥗 Diet Plan")
        st.json(result["diet_plan"])
