from workout_ai.models import UserProfile

def profile_to_string(profile: UserProfile) -> str:
    """
    Convert UserProfile object to a formatted string for LLM prompts.
    
    Args:
        profile: UserProfile object containing user data
        
    Returns:
        Formatted string with user profile information for AI consumption
    """
    # Format fitness goals
    goals_formatted = ", ".join([
        goal.value.replace("_", " ").title() 
        for goal in profile.fitness_goals
    ])
    
    profile_string = f"""USER PROFILE:
- Age: {profile.age} years old
- Gender: {profile.gender.value.title()}
- Height: {profile.height} cm
- Weight: {profile.weight} kg
- Fitness Level: {profile.fitness_level}
- Fitness Goals: {goals_formatted}
- Workout Days Per Week: {profile.workout_days_per_week}
- Workout Duration: {profile.workout_duration_minutes} minutes
"""

    return profile_string.strip()

def profile_summary(profile: UserProfile) -> str:
    """
    Create a brief summary of user profile for logging/display purposes.
    
    Args:
        profile: UserProfile object
        
    Returns:
        Brief summary string
    """
    goals_str = ", ".join([goal.value.replace("_", " ").title() for goal in profile.fitness_goals])
    return f"{profile.age}yr {profile.gender.value} - {profile.fitness_level.value} level - Goals: {goals_str}"