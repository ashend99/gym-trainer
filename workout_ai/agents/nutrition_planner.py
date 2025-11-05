from workout_ai.models import WorkoutState
from workout_ai.models import NutritionPlannerLLM
from workout_ai.models import WorkoutAIPlans
from workout_ai.utils import profile_to_string

class NutritionPlannerAgent:
    def __init__(self, llm_model: str = "gpt-4", temperature: float = 0.7):
        self.nutrition_planner_llm = NutritionPlannerLLM(model=llm_model, temperature=temperature)

    def plan_nutrition(self, state: WorkoutState) -> WorkoutState:
        """
        Generates a personalized nutrition plan based on user profile.
        
        Args:
            state: Current workflow state containing user profile
            
        Returns:
            state: Updated workflow state with generated nutrition plan
        """
        if WorkoutAIPlans.NUTRITION_PLAN not in state['remained_selected_plans']:
            return state  # Skip if nutrition plan is not selected
        
        user_profile = state['user_profile']

        try:
            workout_plan = state.get('workout_plan', None)
            prompt = self._get_nutrition_planner_prompt(user_profile, workout_plan)
            response = self.nutrition_planner_llm.llm.invoke(prompt)

            state['nutrition_plan'] = response.content
            state['workflow_status'] = "NUTRITION_PLAN_GENERATED"
        except Exception as e:
            state['error_message'] = str(e)
            state['workflow_status'] = "NUTRITION_PLAN_ERROR"
        
        state['remained_selected_plans'].remove(WorkoutAIPlans.NUTRITION_PLAN)

        return state

    def _get_nutrition_planner_prompt(self, user_profile, workout_plan) -> str:
        user_profile_str = profile_to_string(user_profile)
        workout_plan = workout_plan if workout_plan else 'No workout plan available.'
        return NUTRITION_PLANNER_PROMPT.format(
            user_profile_str=user_profile_str,
            workout_plan=workout_plan
        )

NUTRITION_PLANNER_PROMPT = """
You are a world-class certified nutritionist and registered dietitian with 20+ years of experience. Create a comprehensive meal plan that perfectly supports this user's fitness goals and lifestyle.

USER PROFILE:
{user_profile_str}

CURRENT WORKOUT PLAN:
{workout_plan}

INSTRUCTIONS:
- Design a complete nutrition plan that optimally supports their fitness goals
- Determine ideal meal timing, portion sizes, and food choices
- Consider their age, gender, weight, height, and activity level for caloric needs
- Create a sustainable, practical meal plan they can follow long-term
- Include everything: meals, snacks, hydration, and any relevant supplements

FORMAT YOUR RESPONSE AS A COMPLETE NUTRITION PLAN:

## PERSONALIZED NUTRITION PLAN

[Design the complete meal plan, caloric guidelines, meal timing, food choices, and all nutritional details as you see fit for this user's specific needs and goals]

Remember: You have complete freedom to design the perfect nutrition plan for this individual. Make every decision based on their unique profile and what will help them achieve their goals most effectively alongside their workout routine.
"""