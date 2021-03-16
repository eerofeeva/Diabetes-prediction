
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
# import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

def diabetesPrediction(pregnancies, glucose, bloodPressure, skinThickness, 
insulin, BMI, diabetesPedigree, age):
    diabetes_clean = "Resources/diabetes_clean.csv"
    diabetes_clean = pd.read_csv(diabetes_clean, encoding="utf-8")

    X = diabetes_clean.loc[:, diabetes_clean.columns != 'Outcome']
    y = diabetes_clean['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=diabetes_clean['Outcome'], random_state=42)
    X_scaler = StandardScaler().fit(X_train)

    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    #K Nearest Neighbors
    train_scores = []
    test_scores = []

    for k in range(1,20,2):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        train_score = knn.score(X_train_scaled, y_train)
        test_score = knn.score(X_test_scaled, y_test)
        train_scores.append(train_score)
        test_scores.append(test_score)
        print(f"k: {k}, Train/Test Score: {train_score:.3f}/{test_score:.3f}")

    #Using k=7
    knn = KNeighborsClassifier(n_neighbors=7)
    knn.fit(X_train_scaled, y_train)

    #new_diabetes_data = [[2,145,85,25,94,28.1,0.200,40]]
    new_diabetes_data = [[pregnancies, glucose, bloodPressure, skinThickness, 
    insulin, BMI, diabetesPedigree, age]]
    return knn.predict(new_diabetes_data)