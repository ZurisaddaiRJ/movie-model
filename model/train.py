from os import PathLike
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path('data/movie_success_rate.csv'))
df=df.dropna(axis=0, how='any')
y = df.pop('Success')
X = df
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

#Data for Evaluation
X = df[df.columns[6:32]]
Y=df.iloc[:,-1]

#Train and Test Splitting
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Model and Training - Adaboost
adaboost_model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2))
adaboost_model.fit(X_train, Y_train)
y_pred = adaboost_model.predict(X_test)

#Model and Training - Random Forest
randomforest_model = RandomForestClassifier(n_estimators=60)
randomforest_model.fit(X_train, Y_train)
y_pred_rf = randomforest_model.predict(X_test)

#print ('Training model.. ')
#clf = RandomForestClassifier(n_estimators = 10,
                            #max_depth=2,
                            #random_state=0)
#clf.fit(X_train, y_train)
print ('Saving model..')

dump(y_pred_rf, pathlib.Path('model/movie_success_rate_v1.joblib'))
