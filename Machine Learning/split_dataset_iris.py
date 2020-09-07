from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print(load_iris())

# create a pipeline object
pipe = make_pipeline(
     StandardScaler(),
     LogisticRegression(random_state=0))

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
print(len(X))
print(len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
print(len(X_train))
print(len(X_test))


# fit the whole pipeline
pipe.fit(X_train, y_train)
print(pipe.fit(X_train, y_train))

score=accuracy_score(pipe.predict(X_test), y_test)
print(score)
