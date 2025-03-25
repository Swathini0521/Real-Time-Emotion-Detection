# Real-Time-Emotion-Detection
________________________________________
1. Project Overview
Introduction
This project focuses on real-time emotion detection and analysis for employees, integrating speech recognition, facial expression analysis, and historical mood tracking. It provides insights into employee well-being and recommends tasks based on detected emotions.
Problem Statement
Employee well-being is crucial for workplace productivity. However, organizations lack real-time insights into employee emotions. This project aims to bridge that gap by providing:
•	Live emotion recognition from video and speech.
•	Task recommendations based on detected moods.
•	Stress alerts to help prevent burnout.
•	Historical mood tracking to analyze long-term emotional trends.
Dataset Used
This project does not rely on a predefined dataset but operates in real-time using:
•	Live video feed from a webcam.
•	Real-time speech analysis using a microphone.
•	Historical emotion logs stored in a database.
________________________________________
2. Implementation Details
Methodology & Approach
1. Real-Time Emotion Detection
•	Speech Recognition: Uses speech recognition to convert spoken words into text.
•	Facial Emotion Detection: Uses DeepFace to classify emotions from live video.
2. Task Recommendation System
•	Emotion-based suggestions: A predefined mapping recommends tasks based on the detected mood.
•	AI-based Task Matching: Uses sentence-transformers to improve task allocation.
3. Historical Mood Tracking
•	Stores detected emotions in a SQLite database.
•	Analyzes trends to identify long-term mood patterns.
4. Stress Management Alerts
•	Triggers alerts if an employee shows prolonged stress.
•	Uses threshold-based detection (e.g., 3 out of 5 recent emotions are negative).
________________________________________
3. Technologies & Libraries Used
•	Programming Language: Python
•	Computer Vision: OpenCV (cv2)
•	Emotion Recognition: DeepFace
•	Speech-to-Text: SpeechRecognition
•	Machine Learning: Transformers (sentence-transformers for task recommendations)
•	Database Management: SQLite for historical mood tracking
•	Visualization & Display: OpenCV for real-time results
________________________________________
4. Results and Observations
Findings & Insights
•	Employees display different emotions based on workload and task engagement.
•	Real-time emotion detection helps in identifying stress patterns early.
•	Task recommendations improve engagement by aligning work with emotional states.
•	Stress alerts help HR teams proactively support employees.

Graphical Results
•	Live Emotion Detection (Displayed on Screen)
•	Task Recommendations Based on Mood
•	Stress Alerts for HR Notification
________________________________________
5. How the Project Works (Step-by-Step)
1.	User Starts the System:
o	Webcam and microphone activate to capture real-time data.
2.	Emotion Detection Process:
o	Facial analysis: Detects emotions from video.
o	Speech analysis: Converts speech to text and evaluates sentiment.
3.	Task Recommendation:
o	Suggests work activities suited to the detected emotion.
4.	Historical Mood Tracking:
o	Saves detected emotions into a database for long-term analysis.
5.	Stress Alert System:
o	Sends alerts to HR if prolonged stress patterns are detected.
