from typing import TypedDict, Optional, Dict
from enum import Enum
from workout_ai.models import UserProfile

class WorkoutAIPlans(str, Enum):
    WORKOUT_PLAN = "workout_plan"
    NUTRITION_PLAN = "nutrition_plan"

class WorkoutState(TypedDict):
    user_profile: Optional[UserProfile]
    remained_selected_plans: Optional[Dict[str, bool]]
    workout_plan: Optional[str]
    nutrition_plan: Optional[str]
    error_message: Optional[str]
    workflow_status: Optional[str]