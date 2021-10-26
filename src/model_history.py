#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, make_scorer
from sklearn.model_selection import train_test_split, cross_validate, cross_val_score, KFold



class ModelHistory:
    
    def __init__(self, random_state=2021):
        self.scorer = ['accuracy', 'recall', 'precision', 'f1']
        self.history = pd.DataFrame(columns=['Name', 'Accuracy_Score', 'Recall_Score', 
                                             'Precision_Score', 'F1_Score', 'Notes'])
        

    def report(self, pipeline, X, y, name, notes='', cv=10,):
        kf = KFold(n_splits=cv, random_state=2021, shuffle=True)
        self.scores = cross_validate(pipeline, X, y, 
                                 scoring=self.scorer, cv=kf)
        
        frame = pd.DataFrame([[name, self.scores['test_accuracy'].mean(),
                               self.scores['test_recall'].mean(),
                               self.scores['test_precision'].mean(), 
                               self.scores['test_f1'].mean(), notes]],
                               columns=['Name', 'Accuracy_Score', 'Recall_Score',
                                        'Precision_Score', 'F1_Score', 'Notes'])
        
        self.history = self.history.append(frame)
        self.history = self.history.reset_index(drop=True)
        self.history = self.history.sort_values('Recall_Score')
        
        
        
        print('Average Accuracy Score:', self.scores['test_accuracy'].mean())
        print('Average Recall Score:', self.scores['test_recall'].mean())
        print('Average Precision Score:', self.scores['test_precision'].mean())
        print('Average F1 Score:', self.scores['test_f1'].mean())
        
        
    

