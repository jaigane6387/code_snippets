                   ##Knn Imputation code Snippet

#importing necessary libraries
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold

        
def knn_impute(features,target):
    x=features
    y=target
        
    #iterate  over the k values range fromm 1-23
    scores=list()
    values=list()
    seq=[str(i) for i in [1,3,5,7,9,15,18,21,23]]

    #loop over sequence of k values

    for i in seq:
        #createt a pipeline to avoid data leakage
        pipe=Pipeline(steps=[('imp',KNNImputer(n_neighbors=int(i))),('m',RandomForestClassifier())])

        #model Evaluation
        cv=RepeatedStratifiedKFold(n_splits=10,n_repeats=3, random_state=1)
        score=cross_val_score(pipe,x,y,scoring='accuracy', cv=cv, n_jobs=-1)

        #storing results
        values.append(i)
        mean_score=np.mean(score)
        scores.append(mean_score)

    #returning results
    results=dict({'k_value':values,"score":scores})
    return results
