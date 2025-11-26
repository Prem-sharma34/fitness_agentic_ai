from fastapi import APIRouter, HTTPException
from models.profile import UserProfile
from plan.generator import generate_weekly_plan
import json
import re

router = APIRouter()

@router.post("/generate-plan")
def generate_plan(profile: UserProfile):
    """
    POST /generate-plan
    Body: UserProfile JSON
    Returns: Properly structured JSON output from CrewAI (workout + diet)
    """
    try:
        # Get result from CrewAI
        result = generate_weekly_plan(profile)
        
        # CrewAI returns a CrewOutput object, convert to string
        raw_result = str(result)
        
        # Extract workout and diet plans from the raw output
        workout_plan = None
        diet_plan = None
        
        # Try to parse the raw result which contains JSON blocks
        # The output contains two JSON blocks - one from workout agent, one from diet agent
        
        # Find all JSON blocks in the output
        json_pattern = r'```json\s*(.*?)\s*```'
        json_matches = re.findall(json_pattern, raw_result, re.DOTALL)
        
        if len(json_matches) >= 1:
            # The last JSON block should be the diet plan (as it runs last)
            try:
                diet_data = json.loads(json_matches[-1])
                diet_plan = diet_data.get('diet_plan', [])
            except json.JSONDecodeError as e:
                print(f"Error parsing diet plan: {e}")
            
            # If there are 2 JSON blocks, first one is workout
            if len(json_matches) >= 2:
                try:
                    workout_data = json.loads(json_matches[0])
                    workout_plan = workout_data.get('workout_plan', [])
                except json.JSONDecodeError as e:
                    print(f"Error parsing workout plan: {e}")
        
        # Fallback: try to extract from the raw text directly
        if not workout_plan or not diet_plan:
            # Look for workout_plan and diet_plan in the raw output
            workout_match = re.search(r'"workout_plan"\s*:\s*\[(.*?)\]', raw_result, re.DOTALL)
            diet_match = re.search(r'"diet_plan"\s*:\s*\[(.*?)\]', raw_result, re.DOTALL)
            
            if workout_match and not workout_plan:
                try:
                    workout_json = f'{{"workout_plan":[{workout_match.group(1)}]}}'
                    workout_data = json.loads(workout_json)
                    workout_plan = workout_data.get('workout_plan', [])
                except:
                    pass
            
            if diet_match and not diet_plan:
                try:
                    diet_json = f'{{"diet_plan":[{diet_match.group(1)}]}}'
                    diet_data = json.loads(diet_json)
                    diet_plan = diet_data.get('diet_plan', [])
                except:
                    pass
        
        # Return properly structured response
        return {
            "success": True,
            "workout_plan": workout_plan if workout_plan else [],
            "diet_plan": diet_plan if diet_plan else [],
            "raw": raw_result  # Keep raw for debugging
        }
        
    except Exception as e:
        print(f"Error in generate_plan: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))