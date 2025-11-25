import os
from dotenv import load_dotenv
from crewai import LLM, Agent


load_dotenv()


llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.1
)

workout_agent = Agent(
    role="Workout Agent",
    goal="Design a 7-day workout plan matched to the user's time and goal",
    backstory="Certified personal trainer experienced with home and gym routines",
    llm=llm,
    verbose=False,
    allow_delegation=False
)


diet_agent = Agent(
    role="Diet Agent",
    goal="Design a 7-day Indian-friendly diet plan matching calorie needs and diet_type",
    backstory="Registered dietitian specializing in Indian cuisine and simple meal swaps",
    llm=llm,
    verbose=False,
    allow_delegation=False
)
