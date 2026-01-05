# Personalized Health Recommendation System - Complete Project Explanation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [System Architecture](#system-architecture)
4. [How It Works](#how-it-works)
5. [Machine Learning Models](#machine-learning-models)
6. [Database Structure](#database-structure)
7. [Features Breakdown](#features-breakdown)
8. [Workflow & User Journey](#workflow--user-journey)

---

## 🎯 Project Overview

**Personalized Health Recommendation System** is an intelligent web application that uses **Machine Learning** to provide personalized health recommendations for diet, exercise, and sleep. The system analyzes user health data, lifestyle patterns, and goals to generate customized recommendations that adapt over time.

### Key Purpose
- Help users achieve their health goals (weight loss, muscle gain, maintenance)
- Provide data-driven insights into health behaviors
- Predict future health outcomes
- Track progress and identify patterns

---

## 🛠️ Technology Stack

### **Backend Framework**
- **Django 4.2.7** - High-level Python web framework
  - Handles routing, views, templates, authentication
  - Built-in admin panel for data management
  - ORM (Object-Relational Mapping) for database operations

### **Machine Learning & Data Science**
- **scikit-learn (≥1.4.0)** - ML library
  - Random Forest Regressor/Classifier
  - Decision Tree Classifier
  - Linear Regression
  - Gradient Boosting Classifier
  - Statistical correlation analysis

- **pandas (≥2.0.0)** - Data manipulation and analysis
- **numpy (≥1.24.0)** - Numerical computations
- **scipy (≥1.10.0)** - Scientific computing (correlation analysis)
- **joblib (≥1.3.0)** - Model persistence (save/load trained models)

### **Database**
- **SQLite** (Development) - Lightweight, file-based database
- **PostgreSQL** (Production Ready) - Can be easily switched

### **Frontend Technologies**
- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **JavaScript (Vanilla)** - Client-side interactivity
- **Bootstrap 5.3.0** - Responsive UI framework
- **Bootstrap Icons** - Icon library
- **Chart.js 4.4.0** - Data visualization (graphs and charts)

### **API Framework**
- **Django REST Framework 3.14.0** - For building RESTful APIs

### **Additional Tools**
- **Pillow (≥10.0.0)** - Image processing (if needed)
- **datetime** - Date/time handling
- **json** - Data serialization

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                          │
│  HTML5 + CSS3 + JavaScript + Bootstrap + Chart.js            │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Requests
                       │ (GET/POST)
┌──────────────────────▼──────────────────────────────────────┐
│              DJANGO WEB FRAMEWORK                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   URLs       │→ │    Views     │→ │  Templates   │       │
│  │  (Routing)   │  │  (Logic)     │  │  (HTML)      │       │
│  └──────────────┘  └──────┬───────┘  └──────────────┘       │
│                           │                                  │
│  ┌───────────────────────▼──────────────────────────────┐  │
│  │              ML MODELS LAYER                           │  │
│  │  • Diet Model (Random Forest)                         │  │
│  │  • Exercise Model (Decision Tree)                     │  │
│  │  • Sleep Model (Linear Regression)                    │  │
│  │  • Recovery Model (Random Forest)                    │  │
│  │  • Correlation Model (Statistical)                    │  │
│  │  • Habit Sensitivity Model (Gradient Boosting)        │  │
│  │  • Disease Prediction Model (Random Forest)           │  │
│  │  • Simulator Model (Random Forest)                    │  │
│  └───────────────────────┬──────────────────────────────┘  │
│                           │                                  │
│  ┌───────────────────────▼──────────────────────────────┐  │
│  │              DATABASE LAYER (SQLite)                   │  │
│  │  • UserProfile  • HealthData  • Recommendation      │  │
│  │  • FoodEntry    • Reminder    • HealthRiskAlert     │  │
│  │  • RecoveryStabilityAnalysis                         │  │
│  │  • BehaviorCorrelationAnalysis                       │  │
│  │  • HabitSensitivityAnalysis                          │  │
│  │  • DiseasePrediction                                 │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works

### **1. User Registration & Authentication**
- User creates account with username/email and password
- Django's built-in authentication system handles security
- Session-based authentication maintains user login state

### **2. Profile Setup**
- User provides:
  - Personal info: Age, Gender, Height, Weight
  - Health goals: Weight loss, Muscle gain, Maintenance, General wellness
  - Activity level: Sedentary, Light, Moderate, Active, Very Active
  - Dietary preferences: Vegetarian, Vegan, Keto, Paleo, None
  - Medical conditions and allergies
- System calculates:
  - **BMI** (Body Mass Index) = Weight(kg) / Height(m)²
  - **BMR** (Basal Metabolic Rate) using Mifflin-St Jeor Equation
  - **TDEE** (Total Daily Energy Expenditure) = BMR × Activity Multiplier

### **3. Health Data Collection**
- Users log daily:
  - Weight (kg)
  - Sleep hours
  - Exercise minutes
  - Water intake (liters)
  - Food entries (breakfast, lunch, dinner, snacks)
- System automatically:
  - Calculates nutrition totals (calories, protein, carbs, fats, fiber)
  - Auto-increments dates for consecutive entries
  - Tracks trends over time

### **4. Machine Learning Processing**

#### **Diet Recommendations**
1. **Input**: Age, weight, height, activity level, gender, health goal
2. **ML Model**: Random Forest Regressor
3. **Process**:
   - Predicts optimal daily calorie intake
   - Adjusts based on goal (weight loss = TDEE - 500, muscle gain = TDEE + 400)
   - Calculates macronutrient distribution (protein, carbs, fats)
   - Generates meal plan based on dietary preferences
4. **Output**: Daily calories, macro breakdown, sample meal plan

#### **Exercise Recommendations**
1. **Input**: Activity level, age, BMI, health goal, available time
2. **ML Model**: Decision Tree Classifier
3. **Process**:
   - Determines fitness level (beginner/intermediate/advanced)
   - Selects exercise type (cardio/strength/mixed) based on goal
   - Chooses exercises from database (60+ exercises)
   - Fits exercises within available time
4. **Output**: Exercise list, sets, reps, duration, frequency

#### **Sleep Recommendations**
1. **Input**: Age, activity level, BMI, exercise minutes
2. **ML Model**: Linear Regression
3. **Process**:
   - Predicts optimal sleep duration
   - Calculates bedtime and wake time
   - Generates sleep schedule
4. **Output**: Sleep hours, schedule, tips

#### **Recovery & Stability Analysis**
1. **Input**: Historical health data, user profile
2. **ML Model**: Random Forest Regressor + Gradient Boosting
3. **Process**:
   - Calculates consistency score
   - Measures adherence rate
   - Tracks streaks and missed days
   - Predicts recovery time from setbacks
   - Calculates stability score (0-100%)
4. **Output**: Recovery days, stability score, risk level, recommendations

#### **Behavior-Cause Correlation**
1. **Input**: Historical health data
2. **ML Model**: Statistical Correlation Analysis
3. **Process**:
   - Calculates correlations between:
     - Sleep vs Weight
     - Exercise vs Weight
     - Calories vs Weight
     - Sleep vs Exercise
   - Identifies root causes of health changes
4. **Output**: Correlation scores, root causes, insights

#### **Habit Sensitivity Analysis**
1. **Input**: Historical health data, user profile
2. **ML Model**: Gradient Boosting Classifier + Regressor
3. **Process**:
   - Analyzes habit consistency
   - Calculates fragility vs resilience scores
   - Measures impact of each habit
   - Identifies high-impact habits
4. **Output**: Fragile habits, resilient habits, impact scores, recommendations

#### **Disease Prediction**
1. **Input**: Age, BMI, activity level, sleep, exercise frequency
2. **ML Model**: Random Forest Classifier
3. **Process**:
   - Predicts risk for:
     - Type 2 Diabetes
     - Cardiovascular Disease
     - Hypertension
     - Obesity
   - Calculates risk scores (0-100%)
4. **Output**: Disease risks, risk levels, recommendations

#### **What-If Health Simulator**
1. **Input**: Current health data + hypothetical scenario (sleep, exercise, days)
2. **ML Model**: Random Forest Regressor (3 models)
3. **Process**:
   - Predicts weight change
   - Calculates stability score
   - Predicts recovery speed
4. **Output**: Predicted weight, stability score, recovery days

### **5. Recommendation Generation**
- System generates recommendations using ML models
- Recommendations stored in database
- Displayed on dashboard and recommendations page
- Can be regenerated as user data changes

### **6. Progress Tracking**
- Charts visualize:
  - Weight trends over time
  - Sleep patterns
  - Exercise frequency
  - Nutrition intake
- Progress assessment:
  - Compares current vs past data
  - Provides status (Excellent/Good/Needs Improvement)
  - Shows weight change and percentage

### **7. Analytics & Insights**
- Advanced analytics page shows:
  - Recovery & stability predictions
  - Behavior-cause correlations
  - Habit sensitivity analysis
- Risk alerts for:
  - High BMI
  - Low sleep
  - Insufficient exercise
- Disease predictions with risk scores

---

## 🤖 Machine Learning Models

### **Model Training Process**
1. **Synthetic Data Generation**: Models trained on 500-1000 synthetic samples
2. **Feature Engineering**: Input features normalized and encoded
3. **Model Training**: Algorithms learn patterns from data
4. **Model Persistence**: Trained models saved as `.pkl` files using joblib
5. **Model Loading**: Models loaded when needed for predictions

### **Model Details**

| Model | Algorithm | Purpose | Input Features | Output |
|-------|-----------|---------|---------------|--------|
| **Diet Model** | Random Forest Regressor | Calorie prediction | Age, weight, height, activity, gender, goal | Daily calories |
| **Exercise Model** | Decision Tree Classifier | Exercise selection | Fitness level, goal, time, age, BMI | Exercise type & list |
| **Sleep Model** | Linear Regression | Sleep duration | Age, activity, BMI, exercise | Sleep hours |
| **Recovery Model** | Random Forest Regressor | Recovery prediction | Consistency, adherence, days, age, activity | Recovery days |
| **Stability Model** | Gradient Boosting | Stability scoring | Consistency, adherence, days, age, activity | Stability score (0-100%) |
| **Correlation Model** | Statistical Analysis | Correlation detection | Historical health data | Correlation coefficients |
| **Habit Sensitivity** | Gradient Boosting | Habit analysis | Historical data, profile | Fragility/resilience scores |
| **Disease Prediction** | Random Forest Classifier | Disease risk | Age, BMI, activity, sleep, exercise | Risk scores |
| **Simulator Model** | Random Forest Regressor (3x) | Future prediction | Current data + scenario | Weight, stability, recovery |

---

## 💾 Database Structure

### **Models (Tables)**

1. **UserProfile**
   - Links to Django User (OneToOne)
   - Stores: age, gender, height, weight, activity_level, health_goal, dietary_preference, allergies, medical_conditions
   - Calculated: BMI, BMR, TDEE (as properties)

2. **HealthData**
   - Daily health entries
   - Stores: date, weight, sleep_hours, exercise_minutes, water_intake_liters, calories_consumed, notes
   - Calculated: total_calories, total_protein, total_carbs, total_fats, total_fiber (from food entries)

3. **FoodEntry**
   - Individual food items logged
   - Stores: date, meal_type (breakfast/lunch/dinner/snacks), food_name, quantity, unit (serving/gram)
   - Calculated: total_calories, total_protein, total_carbs, total_fats, total_fiber

4. **Recommendation**
   - Generated recommendations
   - Stores: recommendation_type (diet/exercise/sleep), title, description, details (JSON), is_active

5. **RecoveryStabilityAnalysis**
   - Recovery and stability predictions
   - Stores: recovery_days, stability_score, is_stable, risk_level, consistency_score, adherence_rate, recommendations

6. **BehaviorCorrelationAnalysis**
   - Correlation analysis results
   - Stores: correlations (JSON), root_causes (JSON), insights

7. **HabitSensitivityAnalysis**
   - Habit sensitivity results
   - Stores: fragile_habits (JSON), resilient_habits (JSON), impact_scores (JSON)

8. **Reminder**
   - User reminders
   - Stores: reminder_type (food/water/exercise/medication/sleep), time, message, days_of_week, is_active

9. **HealthRiskAlert**
   - Health risk alerts
   - Stores: risk_level, alert_type, message, recommendations, is_read

10. **DiseasePrediction**
    - Disease risk predictions
    - Stores: disease_type, risk_score, risk_level, recommendations

---

## ✨ Features Breakdown

### **1. Dashboard**
- **Stats Cards**: BMI, BMR, TDEE, Health Goal
- **Active Recommendations**: Latest diet/exercise/sleep recommendations
- **Add Health Data**: Form to log daily health metrics
- **Food Tracking**: 
  - Add food entries by meal type
  - View nutrition summary (calories, protein, carbs, fats, fiber, water)
  - Display food entries grouped by meal
- **Progress Assessment**: Status update (Excellent/Good/Needs Improvement)
- **Risk Alerts**: High/Medium risk health alerts
- **Disease Predictions**: Risk scores for various diseases
- **Reminders**: Create and manage health reminders
- **Recent Health Data**: Table with all entries (can delete)
- **Progress Charts**: Visual graphs for weight, sleep, exercise trends

### **2. Recommendations Page**
- **Generate Recommendations**: Buttons to generate diet/exercise/sleep recommendations
- **Display Recommendations**: Shows detailed recommendations with:
  - Diet: Calories, macros, meal plan
  - Exercise: Exercises, sets, reps, duration
  - Sleep: Sleep hours, schedule, tips

### **3. Analytics Page**
- **Recovery & Stability**: 
  - Recovery days prediction
  - Stability score (0-100%)
  - Risk level assessment
  - Recommendations
- **Behavior-Cause Correlation**:
  - Correlation coefficients
  - Root causes identified
  - Insights and recommendations
- **Habit Sensitivity**:
  - Fragile habits (need attention)
  - Resilient habits (well-established)
  - Impact scores
  - Recommendations

### **4. Simulator Page** ⭐ NEW
- **Scenario Input**: Enter hypothetical sleep, exercise, days
- **Current Status Display**: Shows current health metrics
- **Example Scenarios**: Quick-load buttons for common scenarios
- **Results Display**:
  - Predicted weight and change
  - Stability score with level
  - Recovery speed
  - Key insights

### **5. Profile Setup**
- **Health Information**: Age, gender, height, weight
- **Goals & Preferences**: Health goal, activity level, dietary preference
- **Medical Info**: Allergies, medical conditions
- **Auto-calculation**: BMI, BMR, TDEE calculated automatically

---

## 🔄 Workflow & User Journey

### **Step 1: Registration**
```
User → Register → Create Account → Login
```

### **Step 2: Profile Setup**
```
User → Setup Profile → Enter Health Info → System Calculates BMI/BMR/TDEE
```

### **Step 3: Add Health Data**
```
User → Dashboard → Add Health Data → Enter Weight/Sleep/Exercise/Water
     → Add Food Entries → System Calculates Nutrition Totals
```

### **Step 4: Generate Recommendations**
```
User → Recommendations Page → Click "Generate" → ML Models Process Data
     → Recommendations Created → Displayed to User
```

### **Step 5: View Analytics**
```
User → Analytics Page → Click "Generate Analysis" → ML Models Analyze Data
     → Results Displayed (Recovery, Correlation, Habit Sensitivity)
```

### **Step 6: Use Simulator**
```
User → Simulator Page → Enter Scenario (sleep/exercise/days)
     → Click "Run Simulation" → ML Models Predict Outcomes
     → Results Displayed (Weight, Stability, Recovery)
```

### **Step 7: Track Progress**
```
User → Dashboard → View Charts → See Trends → Progress Assessment
     → Risk Alerts → Disease Predictions → Reminders
```

---

## 🔐 Security Features

- **Authentication**: Django's built-in user authentication
- **CSRF Protection**: Cross-Site Request Forgery protection
- **Session Management**: Secure session handling
- **Password Validation**: Django password validators
- **Login Required**: Protected views require authentication

---

## 📊 Data Flow

```
User Input → Django Views → ML Models → Predictions → Database → Display
     ↓
  Validation
     ↓
  Processing
     ↓
  Storage
     ↓
  Retrieval
     ↓
  Visualization
```

---

## 🎨 UI/UX Features

- **Responsive Design**: Works on desktop, tablet, mobile
- **Modern Gradients**: Beautiful color schemes
- **Interactive Charts**: Chart.js for data visualization
- **Real-time Updates**: AJAX for seamless interactions
- **Card-based Layout**: Clean and organized
- **Bootstrap Components**: Buttons, forms, modals, alerts
- **Icon Library**: Bootstrap Icons for visual elements
- **Smooth Animations**: CSS transitions and transforms

---

## 🚀 Performance Optimizations

- **Model Caching**: ML models loaded once and reused
- **Database Indexing**: Efficient queries
- **Static Files**: CSS/JS served efficiently
- **Lazy Loading**: Charts load on demand
- **Pagination**: Large datasets paginated

---

## 📈 Scalability

- **Modular Design**: Easy to add new features
- **ML Model Separation**: Each model in separate file
- **Database Ready**: Can switch to PostgreSQL
- **API Ready**: REST framework for mobile apps
- **Template System**: Reusable components

---

## 🎓 Educational Value

This project demonstrates:
- **Full-stack Development**: Backend + Frontend
- **Machine Learning Integration**: ML in web applications
- **Database Design**: Relational database modeling
- **API Development**: RESTful endpoints
- **Data Visualization**: Charts and graphs
- **User Experience**: Modern UI/UX design
- **Software Engineering**: Best practices and patterns

---

## 📝 Summary

**Personalized Health Recommendation System** is a complete, production-ready web application that combines:
- **Django** for robust backend
- **Machine Learning** for intelligent predictions
- **Modern Frontend** for great user experience
- **Comprehensive Features** for health management

The system uses **8 different ML models** to provide personalized recommendations, predictions, and insights, making it a sophisticated health management platform suitable for final year projects and real-world applications.

---

**Project Status**: ✅ Complete and Fully Functional

**Total Features**: 15+ major features
**ML Models**: 8 models
**Database Tables**: 10 models
**Pages**: 6 main pages
**API Endpoints**: 15+ endpoints

