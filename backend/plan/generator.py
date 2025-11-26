from crewai import Task, Crew , Process
from plan.agents import workout_agent, diet_agent

def _workout_task_for(profile):
    return Task(
        description=f"""
Generate a 7-day workout plan for a user with the following profile:
- Goal: {profile.goal}
- Age: {getattr(profile, 'age', 'unknown')}
- Height (cm): {profile.height}
- Weight (kg): {profile.weight}
- Time per day (minutes): {profile.time}
- Preference: {profile.preference}

Requirements:
1) Produce a day-by-day (Day 1..7) workout listing (exercise name, duration or sets/reps).
2) Keep it beginner-friendly; provide morning/evening option if relevant.
3) Keep descriptions short and clear.
4) Output in JSON-like structure (key: workout_plan -> list of 7 items).
""",
        agent=workout_agent,
        expected_output="JSON-like workout_plan"
    )






def _diet_task_for(profile):
    return Task(
        description=f"""
Generate a 7-day diet plan for a user with the following profile:
- Goal: {profile.goal}
- Diet type: {profile.diet_type}
- Height (cm): {profile.height}
- Weight (kg): {profile.weight}
- Time per day (minutes): {profile.time}

Requirements:
1) Provide 3 meals per day + one snack; make it Indian-friendly (local foods).
2) Mention approximate portioning (e.g., 1 cup, 2 rotis) and a rough daily calorie target if possible.
3) For vegetarian users, keep meals fully veg; for non-veg include simple chicken/fish options.
4) Output in JSON-like structure (key: diet_plan -> list of 7 items).
""",
        agent=diet_agent,
        expected_output="JSON-like diet_plan"
    )

def generate_weekly_plan(profile):
    """
    Runs two tasks (workout + diet) via a Crew and returns a dict:
    {
      "workout_result": <raw_result_from_workout_agent>,
      "diet_result": <raw_result_from_diet_agent>
    }
    """

    workout_task = _workout_task_for(profile)
    diet_task = _diet_task_for(profile)


    crew = Crew(
        agents=[workout_agent, diet_agent],
        tasks=[workout_task, diet_task],
        process=Process.sequential,
        verbose=True
    )

 
    result = crew.kickoff()


    return result
