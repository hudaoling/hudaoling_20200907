from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate


X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()
print(X)
print('**************')
print(y)
print(len(X),len(y))


result = cross_validate(lr, X, y)  # defaults to 5-fold CV
print(result['test_score']) # r_squared score is high because dataset is easy

print(result)