from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class FitnessLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class FitnessGoal(str, Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    STRENGTH = "strength"
    ENDURANCE = "endurance"
    FLEXIBILITY = "flexibility"

class WorkoutDaysPerWeek(int, Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

class UserProfile(BaseModel):
    age: int = Field(..., description="Age of the user in years")
    gender: Gender = Field(..., description="Gender of the user")
    height: float = Field(..., description="Height of the user in centimeters")
    weight: float = Field(..., description="Weight of the user in kilograms")
    fitness_level: FitnessLevel = Field(..., description="Current fitness level of the user")
    fitness_goals: List[FitnessGoal] = Field(..., description="List of fitness goals for the user")
    workout_days_per_week: WorkoutDaysPerWeek = Field(..., description="Number of days per week the user can work out")
    workout_duration_minutes: Optional[int] = Field(None, description="Preferred duration of each workout session in minutes")
