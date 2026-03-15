from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

class StatisticalClassifier:
    def __init__(self, n_estimators=100):
        self.model = RandomForestClassifier(n_estimators=n_estimators)
        print("Initialized Random Forest Classifier for Capacit AI Core.")

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

if __name__ == "__main__":
    print("Classical Statistical Model Module Ready.")