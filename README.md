# Aquarium Fish Compatibility Predictor

A machine learning-powered web application that predicts the compatibility of freshwater aquarium fish species to help aquarium hobbyists build healthy community tanks.

Developed as a capstone project for the Western Governors University (WGU) Bachelor of Science in Computer Science program.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Dataset](#dataset)
- [Machine Learning Model](#machine-learning-model)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Model Evaluation](#model-evaluation)
- [Future Improvements](#future-improvements)
- [License](#license)

---

# Overview

Choosing compatible fish species for a community aquarium can be difficult due to differences in:

- Aggression levels
- Water parameter requirements
- Schooling behavior
- Tank size requirements
- Territorial behavior
- Habitat preferences

This project applies supervised machine learning to predict compatibility between fish species using biological and behavioral characteristics.

The application provides aquarium hobbyists with compatibility predictions and community tank recommendations through an easy-to-use Streamlit interface.

---

# Features

- Predicts compatibility between aquarium fish species
- Random Forest machine learning model
- Interactive Streamlit web interface
- Community tank evaluation
- Habitat recommendation logic
- Compatibility explanations
- Visual model evaluation
- Feature importance analysis
- Confusion matrix visualization

---

# Project Architecture

```
Excel Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Random Forest Classifier
      │
      ▼
Saved Model (.pkl)
      │
      ▼
Streamlit Web Application
      │
      ▼
Compatibility Prediction
```

---

# Dataset

The model was trained using an aquarium fish dataset containing species characteristics and compatibility information.

The dataset includes features such as:

- Species
- Aggression
- Minimum Tank Size
- Water Temperature
- pH Range
- Schooling Behavior
- Habitat Preferences
- Compatibility Labels

Dataset location:

```
data/
└── aquarium_fish_ml_dataset.xlsx
```

---

# Machine Learning Model

This project uses a **Random Forest Classifier** from Scikit-Learn.

### Why Random Forest?

Random Forest was selected because it:

- Handles nonlinear relationships
- Performs well on mixed feature types
- Reduces overfitting
- Provides feature importance scores
- Produces reliable classification performance

The trained model is stored in:

```
models/
└── compatibility_model.pkl
```

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| Streamlit | Web application |
| Scikit-Learn | Machine learning |
| Pandas | Data processing |
| NumPy | Numerical computing |
| Matplotlib | Data visualization |
| OpenPyXL | Excel dataset handling |
| Joblib | Model serialization |

---

# Project Structure

```
Capstone_Project/
│
├── app.py
├── notebook.ipynb
├── README.md
├── requirements.txt
│
├── data/
│   └── aquarium_fish_ml_dataset.xlsx
│
├── models/
│   └── compatibility_model.pkl
│
├── graphs/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   ├── classification_report.txt
│   └── compatibility_score_distribution.png
│
├── images/
│   └── aquarium_background.png
│
└── utils/
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/SSarcos115/WGU_capstone.git
```

Navigate into the project directory

```bash
cd WGU_capstone/Capstone_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

Once started, Streamlit will open a browser window where users can interact with the compatibility predictor.

---

# Model Evaluation

Model performance was evaluated using several standard classification metrics.

Included evaluation artifacts:

- Classification Report
- Confusion Matrix
- Feature Importance Plot
- Compatibility Score Distribution

These files can be found inside:

```
graphs/
```

---

# Example Workflow

1. Launch the application.
2. Select one or more aquarium fish species.
3. Generate compatibility predictions.
4. Review compatibility scores.
5. Receive recommendations for community tank composition.

---

# Future Improvements

Potential enhancements include:

- Support for saltwater species
- Larger training dataset
- Live fish database integration
- Species image recognition
- Explainable AI (SHAP values)
- User accounts
- Cloud deployment
- REST API
- Mobile-friendly interface

---

# Learning Outcomes

This project demonstrates experience with:

- Machine Learning
- Data preprocessing
- Feature engineering
- Classification algorithms
- Model evaluation
- Python development
- Streamlit application development
- Software engineering best practices

---

# License

This project was developed for educational purposes as part of the Western Governors University Computer Science Capstone.

Feel free to fork the repository for educational or personal learning purposes.

---

# Author

**Sebastian Sarcos**

Bachelor of Science in Computer Science  
Western Governors University

GitHub:
https://github.com/SSarcos115

---

## Acknowledgments

- Western Governors University
- Scikit-Learn
- Streamlit
- Pandas
- OpenPyXL
