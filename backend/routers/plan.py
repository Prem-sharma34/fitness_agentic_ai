from fastapi import APIRouter, HTTPException
from models.profile import UserProfile
from plan.generator import generate_weekly_plan

router = APIRouter()

@router.post("/generate-plan")
def generate_plan(profile: UserProfile):
    """
    POST /generate-plan
    Body: UserProfile JSON
    Returns: JSON output from CrewAI (workout + diet)
    """
    try:
        crew_result = generate_weekly_plan(profile)
        return {"status": "ok", "result": crew_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
