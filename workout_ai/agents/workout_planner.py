import os

from langchain_openai.chat_models import ChatOpenAI

from workout_ai.models.workout_state import WorkoutState
from workout_ai.models import WorkoutPlannerLLM
from workout_ai.utils import profile_to_string
from workout_ai.models import WorkoutAIPlans

class WorkoutPlannerAgent:
    def __init__(self, llm_model: str = "gpt-4", temperature: float = 0.7):
        self.workout_planner_llm = WorkoutPlannerLLM(model=llm_model, temperature=temperature)
        

    def plan_workout(self, state: WorkoutState) -> WorkoutState:
        """
        Generates a personalized workout plan based on user profile.
        
        Args:
            state: Current workflow state containing user profile
            
        Returns:
            state: Updated workflow state with generated workout plan
        """
        if WorkoutAIPlans.WORKOUT_PLAN not in state['remained_selected_plans']:
            return state  # Skip if workout plan is not selected
        
        user_profile = state['user_profile']

        try:
            prompt = self._get_workout_planner_prompt(user_profile)
            response = self.workout_planner_llm.llm.invoke(prompt)

            state['workout_plan'] = response.content
            state['workflow_status'] = "WORKOUT_PLAN_GENERATED"
        except Exception as e:
            state['error_message'] = str(e)
            state['workflow_status'] = "WORKOUT_PLAN_ERROR"

        state['remained_selected_plans'].remove(WorkoutAIPlans.WORKOUT_PLAN)

        return state
    
    def _get_workout_planner_prompt(self, user_profile) -> str:
        user_profile_str = profile_to_string(user_profile)
        return WORKOUT_PLANNER_PROMPT.format(user_profile=user_profile_str)
    
WORKOUT_PLANNER_PROMPT = """
You are a world-class certified personal trainer with 20+ years of experience. Create a completely personalized workout plan based on this user profile:

{user_profile}

INSTRUCTIONS:
- Design a workout plan that perfectly matches this user's profile, goals, and capabilities
- Determine the optimal number of workout days, session durations, and exercise selection
- Create a comprehensive plan with proper structure and progression
- Make all decisions based on what's best for THIS specific user
- DO NOT consider about a nutrition plan or meal suggestions

FORMAT YOUR RESPONSE AS A COMPLETE WORKOUT PLAN:

## PERSONALIZED WORKOUT PLAN

[Design the complete plan structure, schedule, exercises, durations, progressions, and all details as you see fit for this user's specific needs and goals]

Remember: You have complete freedom to design the perfect plan for this individual. Make every decision based on their unique profile and what will help them achieve their goals most effectively.
"""