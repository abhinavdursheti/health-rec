"""
Utility functions for recommendation system
"""
from .ml_models.diet_model import DietRecommendationModel
from .ml_models.exercise_model import ExerciseRecommendationModel
from .ml_models.sleep_model import SleepRecommendationModel
from .ml_models.recovery_stability_model import RecoveryStabilityModel
from .ml_models.correlation_model import CorrelationModel
from .ml_models.habit_sensitivity_model import HabitSensitivityModel
from .ml_models.disease_prediction_model import DiseasePredictionModel
from .ml_models.simulator_model import HealthSimulatorModel


def generate_diet_recommendation(user_profile):
    """Generate diet recommendation for user"""
    model = DietRecommendationModel()
    
    # Calculate calories based on TDEE (Total Daily Energy Expenditure)
    # TDEE is already calculated correctly using Mifflin-St Jeor equation
    base_calories = user_profile.tdee
    
    # Adjust based on health goal
    if user_profile.health_goal == 'weight_loss':
        # 15-20% deficit for weight loss (500-700 calories deficit)
        calories = base_calories - 500
    elif user_profile.health_goal == 'muscle_gain':
        # 10-15% surplus for muscle gain (300-500 calories surplus)
        calories = base_calories + 400
    else:  # maintenance or general
        # Use TDEE as is for maintenance
        calories = base_calories
    
    # Ensure minimum calories for health (1200 for women, 1500 for men)
    min_calories = 1200 if user_profile.gender == 'F' else 1500
    calories = max(min_calories, round(calories, 0))
    
    # Get macronutrients
    macros = model.get_macronutrients(calories, user_profile.health_goal)
    
    # Generate meal plan
    allergies_list = [a.strip() for a in user_profile.allergies.split(',')] if user_profile.allergies else []
    meal_plan = model.generate_meal_plan(calories, user_profile.dietary_preference, allergies_list)
    
    return {
        'calories': calories,
        'macronutrients': macros,
        'meal_plan': meal_plan,
        'tdee': user_profile.tdee,
        'bmr': user_profile.bmr,
    }


def generate_exercise_recommendation(user_profile):
    """Generate exercise recommendation for user"""
    model = ExerciseRecommendationModel()
    
    fitness_level = model.get_fitness_level(
        user_profile.activity_level,
        user_profile.age,
        user_profile.bmi
    )
    
    # Default available time based on activity level
    time_map = {
        'sedentary': 30,
        'light': 45,
        'moderate': 60,
        'active': 75,
        'very_active': 90,
    }
    available_time = time_map.get(user_profile.activity_level, 45)
    
    recommendation = model.recommend_exercises(
        fitness_level,
        user_profile.health_goal,
        available_time,
        user_profile.age,
        user_profile.bmi
    )
    
    return recommendation


def generate_sleep_recommendation(user_profile, exercise_minutes=0):
    """Generate sleep recommendation for user"""
    model = SleepRecommendationModel()
    
    sleep_hours = model.predict_sleep_hours(
        user_profile.age,
        user_profile.activity_level,
        user_profile.bmi,
        exercise_minutes
    )
    
    sleep_schedule = model.get_sleep_schedule(sleep_hours)
    sleep_tips = model.get_sleep_tips(user_profile.age, user_profile.activity_level)
    
    return {
        'sleep_hours': sleep_hours,
        'schedule': sleep_schedule,
        'tips': sleep_tips,
    }


def generate_recovery_stability_analysis(user_profile, health_data_list):
    """Generate recovery and stability analysis"""
    model = RecoveryStabilityModel()
    
    # Calculate metrics
    metrics = model.calculate_metrics(health_data_list)
    
    # Predict recovery time
    recovery_days = model.predict_recovery_time(
        metrics['consistency_score'],
        metrics['adherence_rate'],
        metrics['days_active'],
        user_profile.age,
        user_profile.activity_level,
        user_profile.health_goal
    )
    
    # Predict stability
    stability = model.predict_stability(
        metrics['consistency_score'],
        metrics['adherence_rate'],
        metrics['days_active'],
        user_profile.age,
        user_profile.activity_level,
        user_profile.health_goal
    )
    
    # Get recommendations
    recommendations = model.get_recovery_recommendations(recovery_days, stability['stability_score'])
    
    return {
        'recovery_days': recovery_days,
        'stability_score': stability['stability_score'],
        'is_stable': stability['is_stable'],
        'risk_level': stability['risk_level'],
        'consistency_score': metrics['consistency_score'],
        'adherence_rate': metrics['adherence_rate'],
        'streak_days': metrics['streak_days'],
        'missed_days': metrics['missed_days'],
        'recommendations': recommendations,
        'metrics': metrics,
    }


def generate_correlation_analysis(health_data_list):
    """Generate behavior-cause correlation analysis"""
    model = CorrelationModel()
    return model.analyze_correlations(health_data_list)


def generate_habit_sensitivity_analysis(user_profile, health_data_list):
    """Generate habit sensitivity analysis"""
    model = HabitSensitivityModel()
    return model.analyze_habits(health_data_list, user_profile)


def assess_progress(user_profile, health_data_list):
    """Assess user progress and provide status"""
    if not health_data_list or len(health_data_list) < 2:
        return {
            'status': 'insufficient_data',
            'message': 'Add more data to track progress',
            'improvement': 0
        }
    
    # Get first and last entries
    first_entry = health_data_list[0]
    last_entry = health_data_list[-1]
    
    # Calculate weight change
    weight_change = last_entry.weight - first_entry.weight
    weight_change_pct = (weight_change / first_entry.weight) * 100 if first_entry.weight > 0 else 0
    
    # Determine status based on goal
    if user_profile.health_goal == 'weight_loss':
        if weight_change < -1:
            status = 'excellent'
            message = f'Great progress! Lost {abs(weight_change):.1f} kg'
        elif weight_change < 0:
            status = 'good'
            message = f'Good progress! Lost {abs(weight_change):.1f} kg'
        elif weight_change < 1:
            status = 'maintaining'
            message = 'Weight is stable. Keep going!'
        else:
            status = 'needs_improvement'
            message = f'Weight increased by {weight_change:.1f} kg. Review your plan.'
    elif user_profile.health_goal == 'muscle_gain':
        if weight_change > 1:
            status = 'excellent'
            message = f'Great progress! Gained {weight_change:.1f} kg'
        elif weight_change > 0:
            status = 'good'
            message = f'Good progress! Gained {weight_change:.1f} kg'
        elif weight_change > -0.5:
            status = 'maintaining'
            message = 'Weight is stable. Increase calories and exercise.'
        else:
            status = 'needs_improvement'
            message = f'Weight decreased by {abs(weight_change):.1f} kg. Increase calorie intake.'
    else:  # maintenance or general
        if abs(weight_change) < 1:
            status = 'excellent'
            message = 'Excellent! Weight is well maintained.'
        elif abs(weight_change) < 2:
            status = 'good'
            message = 'Good! Weight is relatively stable.'
        else:
            status = 'needs_improvement'
            message = f'Weight changed by {abs(weight_change):.1f} kg. Focus on consistency.'
    
    return {
        'status': status,
        'message': message,
        'weight_change': round(weight_change, 1),
        'weight_change_pct': round(weight_change_pct, 1),
        'improvement': weight_change if user_profile.health_goal == 'weight_loss' else -weight_change
    }


def assess_health_risks(user_profile, health_data_list):
    """Assess health risks and generate alerts"""
    alerts = []
    
    # BMI Risk
    if user_profile.bmi < 18.5:
        alerts.append({
            'risk_level': 'medium',
            'alert_type': 'bmi',
            'message': f'Your BMI is {user_profile.bmi:.1f} (Underweight). Consider consulting a healthcare provider.',
            'recommendations': ['Increase calorie intake', 'Focus on nutrient-dense foods', 'Consult nutritionist']
        })
    elif user_profile.bmi > 30:
        alerts.append({
            'risk_level': 'high',
            'alert_type': 'bmi',
            'message': f'Your BMI is {user_profile.bmi:.1f} (Obese). This increases risk of various health conditions.',
            'recommendations': ['Weight loss program', 'Regular exercise', 'Consult healthcare provider', 'Diet modification']
        })
    elif user_profile.bmi > 25:
        alerts.append({
            'risk_level': 'medium',
            'alert_type': 'bmi',
            'message': f'Your BMI is {user_profile.bmi:.1f} (Overweight). Consider weight management.',
            'recommendations': ['Increase physical activity', 'Calorie deficit', 'Regular exercise']
        })
    
    # Sleep Risk
    if health_data_list:
        sleep_data = [d.sleep_hours for d in health_data_list if d.sleep_hours]
        if sleep_data:
            avg_sleep = sum(sleep_data) / len(sleep_data)
            if avg_sleep < 6:
                alerts.append({
                    'risk_level': 'high',
                    'alert_type': 'sleep',
                    'message': f'Average sleep is only {avg_sleep:.1f} hours. Chronic sleep deprivation increases disease risk.',
                    'recommendations': ['Improve sleep schedule', 'Aim for 7-9 hours', 'Sleep hygiene practices', 'Consult sleep specialist if persistent']
                })
            elif avg_sleep < 7:
                alerts.append({
                    'risk_level': 'medium',
                    'alert_type': 'sleep',
                    'message': f'Average sleep is {avg_sleep:.1f} hours. Aim for 7-9 hours for optimal health.',
                    'recommendations': ['Improve sleep duration', 'Consistent sleep schedule', 'Better sleep hygiene']
                })
    
    # Exercise Risk
    if health_data_list:
        exercise_data = [d.exercise_minutes for d in health_data_list if d.exercise_minutes and d.exercise_minutes > 0]
        if exercise_data:
            avg_exercise = sum(exercise_data) / len(exercise_data)
            if avg_exercise < 20:
                alerts.append({
                    'risk_level': 'high',
                    'alert_type': 'exercise',
                    'message': f'Average exercise is only {avg_exercise:.0f} minutes/day. Insufficient physical activity increases health risks.',
                    'recommendations': ['Increase exercise to 30+ minutes daily', 'Start with walking', 'Gradually increase intensity', 'Consult fitness trainer']
                })
        elif user_profile.activity_level in ['sedentary', 'light']:
            alerts.append({
                'risk_level': 'medium',
                'alert_type': 'exercise',
                'message': 'Low activity level detected. Regular exercise is essential for health.',
                'recommendations': ['Start with 15-20 min daily', 'Gradually increase', 'Find activities you enjoy']
            })
    
    return alerts


def predict_disease_risks(user_profile, health_data_list):
    """Predict disease risks using ML model"""
    model = DiseasePredictionModel()
    
    # Calculate averages from health data
    sleep_data = [d.sleep_hours for d in health_data_list if d.sleep_hours]
    exercise_data = [d.exercise_minutes for d in health_data_list if d.exercise_minutes and d.exercise_minutes > 0]
    calories_data = [d.calories_consumed for d in health_data_list if d.calories_consumed]
    
    avg_sleep = sum(sleep_data) / len(sleep_data) if sleep_data else 7
    exercise_frequency = len(exercise_data) / len(health_data_list) if health_data_list else 0.5
    diet_quality = 0.7  # Default, can be improved with more data
    
    predictions = model.predict_risk(
        user_profile.age,
        user_profile.bmi,
        user_profile.activity_level,
        avg_sleep,
        exercise_frequency,
        diet_quality,
        0  # family_history - can be added to profile later
    )
    
    return predictions

