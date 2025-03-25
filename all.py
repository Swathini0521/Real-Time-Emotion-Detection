import cv2
import numpy as np
import speech_recognition as sr
from deepface import DeepFace
import datetime
import json
import os

# Ensure the historical mood tracking file exists and is correctly formatted
mood_history_file = "mood_history.json"
if not os.path.exists(mood_history_file):
    with open(mood_history_file, "w") as f:
        json.dump({}, f)

# Function to load mood history safely
def load_mood_history():
    try:
        with open(mood_history_file, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

# Function to update historical mood tracking
def update_mood_history(employee_id, emotion):
    history = load_mood_history()
    
    if employee_id not in history:
        history[employee_id] = []
    
    history[employee_id].append({"timestamp": str(datetime.datetime.now()), "emotion": emotion})
    
    with open(mood_history_file, "w") as f:
        json.dump(history, f, indent=4)

# Function to recommend tasks based on mood
def recommend_task(emotion):
    recommendations = {
        "happy": "Collaborate on a new project or brainstorm new ideas.",
        "sad": "Take a short break or engage in light work.",
        "angry": "Avoid stressful tasks and focus on routine work.",
        "neutral": "Continue with the assigned tasks.",
        "fear": "Seek support from a colleague or manager."
    }
    return recommendations.get(emotion, "Maintain productivity with your usual tasks.")

# Function for stress management alerts
def check_stress_alert(employee_id):
    history = load_mood_history()
    
    if employee_id in history and len(history[employee_id]) >= 5:
        last_moods = [entry["emotion"] for entry in history[employee_id][-5:]]
        if last_moods.count("sad") >= 3 or last_moods.count("angry") >= 3:
            return f"⚠️ Alert: Employee {employee_id} may be under stress. Consider intervention."
    return None

# Initialize webcam for real-time emotion detection
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

recognizer = sr.Recognizer()
employee_id = "EMP123"  # Example employee ID

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture frame.")
        break
    
    try:
        # Perform emotion detection
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list) and len(result) > 0:
            emotion = result[0]['dominant_emotion']
        else:
            emotion = "neutral"  # Default fallback
        
        # Update mood history
        update_mood_history(employee_id, emotion)
        
        # Get task recommendation
        task_suggestion = recommend_task(emotion)
        
        # Check for stress alerts
        alert_message = check_stress_alert(employee_id)
        
        # Display results
        cv2.putText(frame, f"Emotion: {emotion}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Task: {task_suggestion}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        if alert_message:
            cv2.putText(frame, alert_message, (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        cv2.imshow("Emotion Detection", frame)
    except Exception as e:
        print("Error:", str(e))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
