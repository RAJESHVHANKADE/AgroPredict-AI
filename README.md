# **AgroPredict AI**

AgroPredict AI is an advanced machine learning-powered solution designed to predict crop yields based on various environmental and agricultural factors. This project provides valuable insights for farmers, agronomists, and policymakers to optimize agricultural productivity and decision-making.

---

## **Key Features**
- **Accurate Yield Predictions**: Predicts crop yields using historical data, weather patterns, and farming practices.
- **Interactive Web Interface**: Intuitive and user-friendly interface built with Streamlit for real-time predictions.
- **Advanced Preprocessing**: Implements scaling and encoding for robust handling of numerical and categorical data.
- **Multiple Model Support**: Compares the performance of regression models (Decision Tree, KNN, Lasso, Ridge, etc.).
- **Reusable Pipeline**: Modular design using `sklearn` pipelines and model persistence with `pickle`.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - **Machine Learning**: Scikit-learn
  - **Data Processing**: Pandas, NumPy
  - **Web Development**: Streamlit
  - **Model Persistence**: Pickle
- **Tools**: GitHub, GitHub Desktop

---

## **Project Workflow**
1. **Data Preprocessing**:
   - Standardizes numerical columns using `StandardScaler`.
   - Encodes categorical columns using `OneHotEncoder`.
   - Built a preprocessing pipeline with `ColumnTransformer`.

2. **Model Training**:
   - Trained multiple regression models:
     - Decision Tree Regressor
     - K-Nearest Neighbors (KNN)
     - Lasso
     - Ridge
     - Linear Regression
   - Evaluated models using metrics such as Mean Absolute Error (MAE) and R² Score.

3. **Web Application**:
   - Deployed a Streamlit-based web interface.
   - Accepts user inputs like year, rainfall, pesticide usage, temperature, area, and crop type.
   - Predicts crop yield based on user inputs.

4. **Deployment**:
   - Models and preprocessing pipeline serialized using `pickle`.
   - Real-time predictions available via the Streamlit app.


