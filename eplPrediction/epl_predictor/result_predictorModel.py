# -*- coding: utf-8 -*-
"""model_result.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Q-fnpc9K9ciaOVLzRKQj130XJLwk3eR
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('./dataset/results_r_copy.csv')
df.tail(2)

X = df.drop(['Season','DateTime','home_team_name','away_team_name','FTR','FTHG','FTAG','HTHG','HTAG','HTR'], axis = 1)
# X
y= df['FTR']
# y

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85, random_state=27)
X_train.shape, X_test.shape
# y_train
# X_test.head(1)
# a

def models(x_train, y_train):
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.model_selection import GridSearchCV
  from sklearn.ensemble import GradientBoostingClassifier
  from sklearn.neural_network import MLPClassifier
  from sklearn.tree import DecisionTreeClassifier

  tree = DecisionTreeClassifier(max_depth=2,random_state =57)
  tree.fit(X_train, y_train)


  xgBoost = GradientBoostingClassifier(learning_rate = 0.01,
                                       random_state = 57,
                                        max_depth = 5,n_estimators=100, min_samples_leaf=2,
                                        min_samples_split=5,)
  xgBoost.fit(X_train,y_train)

  # mlp = MLPClassifier(activation='relu', solver='adam', alpha=0.001, batch_size='auto',
  #                     learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=10000,
  #                     shuffle=True, random_state=37
  #                     ,early_stopping=False, validation_fraction=0.1,
  #                     beta_1=0.9, beta_2=0.999, epsilon=1e-08)
  # mlp.fit(X_train,y_train)

  classifier_rf = RandomForestClassifier(max_depth=5,random_state = 57,
                                       n_estimators=80, oob_score=True)
  classifier_rf.fit(X_train, y_train)

  rf = RandomForestClassifier(random_state = 57,n_jobs=-1)
  rf_params = {
    'max_depth': [2,3,5,7,10],
    'min_samples_leaf': [5,10,25,50,100],
    'n_estimators': [10,25,50,100,200]
}

  xgBoost_algo = GradientBoostingClassifier(random_state = 57,learning_rate = 0.01)
  xgBoost_algo_params = {
      'max_depth': [3,4,5,6,7,8,10],
      'n_estimators': [10,25,50,100,200]
  }

  grid_search_rf = GridSearchCV(estimator=rf,
                           param_grid=rf_params,
                           cv = 4,
                           n_jobs=-1, verbose=1, scoring="accuracy")
  grid_search_rf.fit(X_train, y_train)

  tree_algo = DecisionTreeClassifier(random_state = 57,max_features = "auto")
  tree_algo_params = {
      'min_samples_leaf':[3,5,7,10,25,50],
      'max_depth': [5,7,10,15,100,200],
  }
  grid_search_tree = GridSearchCV(estimator=tree_algo,
                           param_grid=tree_algo_params,
                           cv = 4,
                           n_jobs=-1, verbose=1, scoring="accuracy")
  grid_search_tree.fit(X_train, y_train)


  grid_search_xgBoost = GridSearchCV(estimator=xgBoost_algo,
                           param_grid=xgBoost_algo_params,
                           cv = 4,
                           n_jobs=-1, verbose=1, scoring="accuracy")
  grid_search_xgBoost.fit(X_train, y_train)

  print("Accuracy of Decision Tree: ",tree.score(X_train,y_train))
  print("Accuracy of Decision Tree after Grid Search: ",grid_search_tree.score(X_train,y_train))
  print("Accuracy of Random Forest: ",classifier_rf.score(X_train,y_train))
  print("Accuracy of Random Forest after Grid Search: ",grid_search_rf.score(X_train,y_train))
  print("Accuracy of Gradient Boosting: ",xgBoost.score(X_train,y_train))
  print("Accuracy of Gradient Boosting after Grid Search: ",grid_search_xgBoost.score(X_train,y_train))

  arraymodels = [['Decision_tree',tree],['Grid_SearchCV for Decision Tree Classifier',grid_search_tree],
                 ['Random_forest',classifier_rf],['Grid_SearchCV for Random Forest',grid_search_rf],
                 ['Gradient Boosting',xgBoost],['Grid_SearchCV for Gradient Boosting',grid_search_xgBoost]]
  return arraymodels

# from sklearn.neural_network import MLPClassifier  
# MLPClassifier().get_params()

model = models(X_train, y_train)



# xgBoost = GradientBoostingClassifier(learning_rate = 0.01,
#                                         max_depth = 5,n_estimators=100, min_samples_leaf=1,
#                                         min_samples_split=5,)
# xgBoost.fit(X_train,y_train)
# xgBoost.score(X_train,y_train)

# from sklearn.metrics import confusion_matrix
# for i in range(len(model)):
    # print('\nConfusion matrix of model: ', model[i][0])
    # print('\t')
    # cm = confusion_matrix(y_test, model[i][1].predict(X_test)) 
    # print(cm)

# from sklearn.metrics import classification_report

# for i in range(len(model)):
    # print("Model: ",model[i][0])
    # print(classification_report(y_test, model[i][1].predict(X_test)))
    # print('\n')

model[5][1].predict(X_test)

# combined = pd.DataFrame(dict(actual=y_test, predicted=model[5][1].predict(X_test)))
# pd.crosstab(index=combined["actual"], columns=combined["predicted"])

# from sklearn import metrics

# confusion_matrix = metrics.confusion_matrix(y_test, model[5][1].predict(X_test))

# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['A','D','H'])

# cm_display.plot()
# plt.show()

# import seaborn as sns
# sns.heatmap(df.corr())

# corr = df.corr()
# corr.style.background_gradient(cmap='coolwarm')

# import pickle
# with open('epl_prediction_random_forest','wb') as f:
#     pickle.dump(model[1], f)

# from sklearn.ensemble import GradientBoostingClassifier
# xgBoost_algo = GradientBoostingClassifier(random_state = 57,learning_rate = 0.06)
# xgBoost_algo_params = {
    #   'max_depth': [3,4,5,6,7,8,10],
    #   'n_estimators': [10,25,50,100,200]
#   }

# from sklearn.model_selection import GridSearchCV
# grid_search_xgBoost = GridSearchCV(estimator=xgBoost_algo,
                        #    param_grid=xgBoost_algo_params,
                        #    cv = 4,
                        #    n_jobs=-1, verbose=1, scoring="accuracy")

# Commented out IPython magic to ensure Python compatibility.
# %%time
# grid_search_xgBoost.fit(X_train, y_train)
# # ok = grid_search.predict(X_test)
# # ok
#

# rf_best = grid_search_xgBoost.best_estimator_
# rf_best

# rf_best.feature_importances_

# imp_df = pd.DataFrame({
    # "Features": X_train.columns,
    # "Imp": rf_best.feature_importances_
# })

# imp_df.sort_values(by="Imp", ascending=False)

# combined = pd.DataFrame(dict(actual=y_test, predicted=ok))

# pd.crosstab(index=combined["actual"], columns=combined["predicted"])

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

# for col in df.select_dtypes('number').columns:
    # sns.distplot(df[col])
    # plt.title(f"Distribution for {col}")
    # plt.show()


# import pickle
# with open('result_prediction_RandomForest','wb') as f:
#     pickle.dump(model[3][1], f)