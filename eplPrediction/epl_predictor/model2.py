# -*- coding: utf-8 -*-
"""7sem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/191d74ZgLjMa-CuIqOfBPPCQk-ZH8J2x6
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('dataset/results_r_copy.csv')
# df
# df = df.drop(['Season','DateTime','home_team_name','away_team_name','FTR','FTHG','FTAG','HTHG','HTAG','HTR'], axis = 1)
# df = df.ewm(alpha = 0.1).mean()

X = df.drop(['Season','DateTime','home_team_name','away_team_name','FTR','FTHG','FTAG','HTHG','HTAG','HTR'], axis = 1)
# X
y= df['FTR']
# X
# y

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85, random_state=42)
X_train.shape, X_test.shape
# y_train
# X_test.head(1)
# a

def models(x_train, y_train):
  from sklearn.ensemble import GradientBoostingClassifier
  from sklearn.model_selection import GridSearchCV
  from sklearn.metrics import f1_score
  classifier_rf = GradientBoostingClassifier(random_state=10,max_depth=5,
                                       n_estimators=100)
  classifier_rf.fit(X_train, y_train)
  # op = classifier_rf.predict(X_test)
  rf = GradientBoostingClassifier(random_state=10)
  params = {
    'max_depth': [2,3,5,10,15,20],
    'min_samples_leaf': [5,10,20,50,100,200],
    'n_estimators': [10,25,30,50,100,200]
}
  grid_search = GridSearchCV(estimator=rf,
                           param_grid=params,
                           cv = 4,
                           n_jobs=-1, verbose=1, scoring="accuracy")
  grid_search.fit(X_train, y_train)
#   # ok = grid_search.predict(X_test)
#   rf_best = grid_search.best_estimator_
#   imp_df = pd.DataFrame({
#     "Features": X_train.columns,
#     "Imp": classifier_rf.feature_importances_
# })
#   imp_df.sort_values(by="Imp", ascending=False)
  # f1_score(ok,y_test, average='weighted')
  print("Accuracy of xgb before: ",classifier_rf.score(X_train,y_train))
  print("Accuracy of xgb after Grid Search: ",grid_search.score(X_train,y_train))

  arraymodels = [['xgb',classifier_rf],['Grid Search',grid_search]]
  return arraymodels

model = models(X_train, y_train)

ok = model[1][1].predict(X_test)
# ok

from sklearn.metrics import accuracy_score, classification_report

print(classification_report(y_test, model[1][1].predict(X_test)))
print(accuracy_score(y_test, model[1][1].predict(X_test)))

# combined = pd.DataFrame(dict(actual=y_test, predicted=ok))
# pd.crosstab(index=combined["actual"], columns=combined["predicted"])

import pickle
with open('model2','wb') as f:
    pickle.dump(model[1][1], f)













# from sklearn.ensemble import RandomForestClassifier

# from sklearn.linear_model import LogisticRegression

# classifier_rf = RandomForestClassifier(random_state=10,max_depth=5,
#                                        n_estimators=100, oob_score=True)

# %%time
# classifier_rf.fit(X_train, y_train)
# op = classifier_rf.predict(X_test)

# classifier_rf.oob_score_

# rf = RandomForestClassifier(random_state=4, n_jobs=-1)

# params = {
#     'max_depth': [2,3,5,10,20],
#     'min_samples_leaf': [5,10,20,50,100,200],
#     'n_estimators': [10,25,30,50,100,200]
# }

# from sklearn.model_selection import GridSearchCV

# grid_search = GridSearchCV(estimator=rf,
#                            param_grid=params,
#                            cv = 3,
#                            n_jobs=-1, verbose=1, scoring="accuracy")

# samp = pd.read_csv('test.csv')
# samp_test = samp.drop(['Season','DateTime','home_team_name','away_team_name','FTR','FTHG','FTAG','HTHG','HTAG','HTR'], axis = 1)
# samp_test

# %%time
# grid_search.fit(X_train, y_train)
# ok = grid_search.predict(X_test)
# ok

# ok.shape

# grid_search.best_score_

# rf_best = grid_search.best_estimator_
# rf_best

# from sklearn.tree import plot_tree
# plt.figure(figsize=(80,40))
# plot_tree(rf_best.estimators_[5], feature_names = X.columns,class_names=['Home', "Away","Draw"],filled=True);

# from sklearn.tree import plot_tree
# plt.figure(figsize=(80,40))
# plot_tree(rf_best.estimators_[7], feature_names = X.columns,class_names=['Home',"Away", "Draw"],filled=True);

# rf_best.feature_importances_

# imp_df = pd.DataFrame({
#     "Features": X_train.columns,
#     "Imp": rf_best.feature_importances_
# })

# imp_df.sort_values(by="Imp", ascending=False)

# combined = pd.DataFrame(dict(actual=y_test, predicted=ok))

# pd.crosstab(index=combined["actual"], columns=combined["predicted"])

# from sklearn.metrics import f1_score

# f1_score(ok,y_test, average='weighted')

# lr = LogisticRegression(C=0.01, solver='liblinear')
# lr.fit(X_train, y_train)
# pre_probs = lr.predict_proba(X_test)
# # pre_probs
# pre_odds = 1 / pre_probs
# pre_odds.shape[0]

# pre_odds_tab = (X_test.assign(homeWinOdds=[i[2] for i in pre_odds],
#                            drawOdds=[i[1] for i in pre_odds],
#                            awayWinOdds=[i[0] for i in pre_odds]))
# pre_odds_tab