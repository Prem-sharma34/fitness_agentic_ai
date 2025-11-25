from pydantic import BaseModel

class UserProfile(BaseModel):
    goal: str          # e.g. "lose weight", "gain muscle"
    height: float      # cm
    weight: float      # kg
    time: int          # minutes per day available (e.g. 30)
    preference: str    # "morning" or "evening"
    diet_type: str     # "veg" / "non-veg" / "eggetarian"
    age: int = 25      # optional, default provided
