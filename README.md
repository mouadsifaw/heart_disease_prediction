🏥 Heart Disease Prediction Model
🚀 Overview
This project aims to predict the likelihood of heart disease using a Random Forest Classifier. The model was built using feature selection, outlier handling, and data transformation techniques to improve accuracy. It is deployed on Streamlit Cloud for real-time predictions.

📊 Key Insights
Women tend to be at a higher risk of heart disease than men, which was a surprising insight derived from the data.
The initial model used 14 features, but feature selection based on correlation reduced it to 8 key features, significantly improving performance.
Clipping technique was used to handle outliers instead of removing them.
Yeo-Johnson Power Transformation was applied to normalize skewed features.
The final Random Forest model achieved over 96% accuracy, precision, recall, and F1-score.
📌 Features Used
The model was trained on an initial set of 14 features, which were later refined to 8 relevant features:

Chest Pain Type (cp)
Maximum Heart Rate Achieved (thalach)
Exercise Induced Angina (exang)
Oldpeak (oldpeak)
Slope of the Peak Exercise ST Segment (slope)
Number of Major Vessels (ca)
Thalassemia (thal)
Target (Heart Disease: 0 = No, 1 = Yes)
🛠️ Technologies Used
Python 3.12
Pandas & NumPy (Data Processing)
Scikit-Learn (Machine Learning)
Matplotlib & Seaborn (Visualization)
Streamlit (Web App Deployment)
