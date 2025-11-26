from crewai import Task, Crew, Process
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
4) Output ONLY valid JSON with this exact structure (no extra text):
```json
{{
  "workout_plan": [
    {{
      "day": "Day 1",
      "focus": "Full Body Strength",
      "time_of_day": "Morning Workout",
      "workout": [
        {{"exercise": "Push-ups", "sets_reps": "3 sets of 10 reps"}},
        {{"exercise": "Squats", "duration": "5 minutes"}}
      ]
    }}
  ]
}}
```
""",
        agent=workout_agent,
        expected_output="JSON workout_plan"
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
4) Output ONLY valid JSON with this exact structure (no extra text):
```json
{{
  "diet_plan": [
    {{
      "day": "Day 1",
      "daily_calorie_target": "2500-2700 kcal",
      "meals": {{
        "Breakfast": "Oats with milk...",
        "Lunch": "Rice and dal...",
        "Snack": "Fruits...",
        "Dinner": "Roti and vegetables..."
      }}
    }}
  ]
}}
```
""",
        agent=diet_agent,
        expected_output="JSON diet_plan"
    )

def generate_weekly_plan(profile):
    """
    Runs two separate crews (one for workout, one for diet).
    This is the most reliable method as each crew returns its own output.
    """
    
    print("\n" + "="*80)
    print("🏋️ STARTING WORKOUT AGENT")
    print("="*80)
    
    workout_task = _workout_task_for(profile)
    workout_crew = Crew(
        agents=[workout_agent],
        tasks=[workout_task],
        process=Process.sequential,
        verbose=True
    )
    workout_result = workout_crew.kickoff()
    
    print("\n" + "="*80)
    print("✅ WORKOUT AGENT COMPLETED")
    print(f"Output length: {len(str(workout_result))}")
    print("="*80 + "\n")
    
    print("\n" + "="*80)
    print("🍽️ STARTING DIET AGENT")
    print("="*80)
    
    diet_task = _diet_task_for(profile)
    diet_crew = Crew(
        agents=[diet_agent],
        tasks=[diet_task],
        process=Process.sequential,
        verbose=True
    )
    diet_result = diet_crew.kickoff()
    
    print("\n" + "="*80)
    print("✅ DIET AGENT COMPLETED")
    print(f"Output length: {len(str(diet_result))}")
    print("="*80 + "\n")
    
    return {
        'workout_output': str(workout_result),
        'diet_output': str(diet_result)
    }