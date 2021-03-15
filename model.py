
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


diabetes_clean = "Resources/diabetes_clean.csv"
diabetes_clean = pd.read_csv(diabetes_clean, encoding="utf-8")


X = diabetes_clean.loc[:, diabetes_clean.columns != 'Outcome']
y = diabetes_clean['Outcome']


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=diabetes_clean['Outcome'], random_state=42)


# In[14]:


X_scaler = StandardScaler().fit(X_train)


# In[15]:


X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[18]:


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


# In[21]:


# plt.plot(range (1, 20, 2), train_scores, marker='o')
# plt.plot(range (1, 20, 2), test_scores, marker='x')
# plt.xlabel("k neighbors")
# plt.ylabel("Testing accuracy Score")
# plt.show()


# In[22]:


#Using k=7
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train_scaled, y_train)
# print('k=7 Test Acc: %.3f' % knn.score(X_test_scaled, y_test))


# In[24]:


new_diabetes_data = [[2,145,85,25,94,28.1,0.200,40]]
predicted_outcome = knn.predict(new_diabetes_data)
print(predicted_outcome)

