from fastapi import APIRouter, HTTPException
from models.profile import UserProfile
from plan.generator import generate_weekly_plan
import json
import re

router = APIRouter()

def extract_json_from_text(text):
    """Extract JSON from text that may contain markdown code blocks"""
    if not text:
        return None
    
    json_pattern = r'```json\s*(.*?)\s*```'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    if matches:
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    try:
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            json_str = text[start:end+1]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    
    return None

@router.post("/generate-plan")
def generate_plan(profile: UserProfile):
    """
    POST /generate-plan
    Body: UserProfile JSON
    Returns: Properly structured JSON output from CrewAI (workout + diet)
    """
    try:
        result = generate_weekly_plan(profile)
        
        print("\n" + "="*80)
        print("PARSING CREWAI OUTPUTS")
        print("="*80)
        
        workout_plan = []
        workout_output = result.get('workout_output', '')
        if workout_output:
            print(f"📋 Workout output length: {len(workout_output)}")
            workout_data = extract_json_from_text(workout_output)
            if workout_data and 'workout_plan' in workout_data:
                workout_plan = workout_data['workout_plan']
                print(f"✅ Successfully extracted {len(workout_plan)} workout days")
            else:
                print("Could not parse workout JSON")
                print("First 500 chars of workout output:")
                print(workout_output[:500])
        else:
            print("No workout output captured")
        
        diet_plan = []
        diet_output = result.get('diet_output', '')
        if diet_output:
            print(f"📋 Diet output length: {len(diet_output)}")
            diet_data = extract_json_from_text(diet_output)
            if diet_data and 'diet_plan' in diet_data:
                diet_plan = diet_data['diet_plan']
                print(f"Successfully extracted {len(diet_plan)} diet days")
            else:
                print("Could not parse diet JSON")
        
        if not diet_plan:
            final_output = result.get('final_output', '')
            if final_output:
                print("Trying to extract diet from final output...")
                diet_data = extract_json_from_text(final_output)
                if diet_data and 'diet_plan' in diet_data:
                    diet_plan = diet_data['diet_plan']
                    print(f" Extracted {len(diet_plan)} diet days from final output")
        
        print("="*80)
        print(f"FINAL: Workout days={len(workout_plan)}, Diet days={len(diet_plan)}")
        print("="*80 + "\n")
        
        return {
            "success": True,
            "workout_plan": workout_plan,
            "diet_plan": diet_plan,
            "raw": result.get('final_output', '')
        }
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))