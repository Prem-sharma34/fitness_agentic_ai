import requests
import json
from typing import Dict, Any, Optional

BACKEND_URL = "http://localhost:8000"

class FitnessAPI:
    """Helper class to interact with FastAPI backend"""
    
    @staticmethod
    def generate_plan(profile: Dict[str, Any], timeout: int = 120) -> Optional[Dict]:
        """
        Generate workout and diet plan from user profile
        
        Args:
            profile: User profile dictionary with keys:
                - goal: str
                - age: int
                - height: float
                - weight: float
                - time: int
                - preference: str
                - diet_type: str
            timeout: Request timeout in seconds
            
        Returns:
            Dictionary containing workout_plan, diet_plan, and raw data
        """
        try:
            response = requests.post(
                f"{BACKEND_URL}/generate-plan",
                json=profile,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Cannot connect to backend. Make sure FastAPI is running on port 8000.")
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out. The AI agents might be taking longer than expected.")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")
    
    @staticmethod
    def parse_plan_response(response: Dict) -> Dict:
        """
        Parse the raw response from backend into structured format
        
        Args:
            response: Raw response from /generate-plan endpoint
            
        Returns:
            Parsed dictionary with workout_plan and diet_plan as lists
        """
        parsed = {
            'workout_plan': [],
            'diet_plan': []
        }
        
        try:
            raw = response.get('raw', '')
            
            if '```json' in raw:
                json_str = raw.split('```json')[1].split('```')[0].strip()
                data = json.loads(json_str)
            else:
                data = json.loads(raw)
            
            if 'diet_plan' in data:
                parsed['diet_plan'] = data['diet_plan']
            
            if 'workout_plan' in response:
                parsed['workout_plan'] = response['workout_plan']
            
            return parsed
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {e}")
        except Exception as e:
            raise Exception(f"Error parsing plan response: {e}")
    
    @staticmethod
    def health_check() -> bool:
        """Check if backend is running"""
        try:
            response = requests.get(f"{BACKEND_URL}/docs", timeout=5)
            return response.status_code == 200
        except:
            return False

def validate_profile(profile: Dict) -> tuple[bool, str]:
    """
    Validate user profile data
    
    Returns:
        (is_valid, error_message)
    """
    required_fields = ['goal', 'age', 'height', 'weight', 'time', 'preference', 'diet_type']
    
    for field in required_fields:
        if field not in profile:
            return False, f"Missing required field: {field}"
    
    if not (15 <= profile['age'] <= 80):
        return False, "Age must be between 15 and 80"
    
    if not (140 <= profile['height'] <= 220):
        return False, "Height must be between 140 and 220 cm"
    
    if not (40 <= profile['weight'] <= 150):
        return False, "Weight must be between 40 and 150 kg"
    
    if profile['goal'] not in ['gain weight', 'lose weight', 'stay fit']:
        return False, "Invalid goal"
    
    if profile['preference'] not in ['morning', 'evening']:
        return False, "Invalid preference"
    
    if profile['diet_type'] not in ['veg', 'non-veg']:
        return False, "Invalid diet type"
    
    return True, ""

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI from weight (kg) and height (cm)"""
    height_m = height / 100
    return weight / (height_m ** 2)

def get_bmi_category(bmi: float) -> str:
    """Get BMI category from BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"