from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

"""------AI generated text--------"""
text = """
# 📊 Linear Regression: Comprehensive Notes

Linear Regression is one of the most fundamental algorithms in statistics and machine learning. It models the relationship between a dependent variable (target) and one or more independent variables (features).

---

## 1. 🔍 Introduction
- **Definition**: Linear regression attempts to fit a straight line (or hyperplane in higher dimensions) that best describes the relationship between variables.
- **Equation (Simple Linear Regression)**:
\[
  y = \beta_0 + \beta_1 x + \epsilon
  \]


  - \(y\): Dependent variable  
  - \(x\): Independent variable  
  - \(\beta_0\): Intercept  
  - \(\beta_1\): Slope (coefficient)  
  - \(\epsilon\): Error term

---

## 2. 📐 Types of Linear Regression
- **Simple Linear Regression**: One independent variable.
- **Multiple Linear Regression**: Multiple independent variables.
- **Polynomial Regression**: Extends linear regression by adding polynomial terms.
- **Regularized Regression**:
  - **Ridge Regression (L2 penalty)**: Shrinks coefficients to reduce variance.
  - **Lasso Regression (L1 penalty)**: Performs feature selection by driving some coefficients to zero.
  - **Elastic Net**: Combination of L1 and L2 penalties.

---

## 3. ⚙️ Assumptions of Linear Regression
1. **Linearity**: Relationship between predictors and target is linear.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: Constant variance of errors.
4. **Normality of Errors**: Residuals are normally distributed.
5. **No Multicollinearity**: Independent variables should not be highly correlated.

---

## 4. 📊 Model Estimation
- **Ordinary Least Squares (OLS)**:
  - Minimizes the sum of squared residuals:
    

\[
    \min_{\beta} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    \]


- **Gradient Descent**:
  - Iterative optimization method for large datasets.
  - Update rule:
    

\[
    \beta_j := \beta_j - \alpha \frac{\partial}{\partial \beta_j} J(\beta)
    \]


    where \(\alpha\) is the learning rate.

---

## 5. 📈 Evaluation Metrics
- **Mean Absolute Error (MAE)**:
  

\[
  MAE = \frac{1}{n} \sum |y_i - \hat{y}_i|
  \]


- **Mean Squared Error (MSE)**:
  

\[
  MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2
  \]


- **Root Mean Squared Error (RMSE)**:
  

\[
  RMSE = \sqrt{MSE}
  \]


- **R² (Coefficient of Determination)**:
  

\[
  R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
  \]


  - Measures proportion of variance explained by the model.

---

## 6. 🧩 Challenges
- **Overfitting**: Model fits training data too closely, fails to generalize.
- **Underfitting**: Model too simple, fails to capture relationships.
- **Multicollinearity**: High correlation among predictors distorts coefficient estimates.
- **Outliers**: Can heavily influence regression line.

---

## 7. 📚 Applications
- Predicting house prices based on features (size, location, etc.).
- Forecasting sales or demand.
- Estimating relationships in economics (e.g., income vs. expenditure).
- Risk modeling in finance.

---

## 8. 🧮 Example in Python

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Model training
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Evaluation
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("MSE:", mean_squared_error(y, y_pred))
print("R²:", r2_score(y, y_pred))

"""


splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size = 370, 
    language=Language.MARKDOWN,
    chunk_overlap = 0 , 
)

chunks = splitter.split_text(text)

for i ,  chunk  in enumerate(chunks):
    print(f" Chunk_No - { i } -\n {chunk}")