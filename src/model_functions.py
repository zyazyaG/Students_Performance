#!/usr/bin/env python
# coding: utf-8

# # Functions to Check Assumptions of LR Model

# This file contains functions that will help to check the assumptions of the Linear Regression Model: linearity, normality, homoscadasticity and independance.

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats


from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score



# 

# In[4]:


def print_metrics(labels, preds):
    
    print("Precision Score: {}".format(precision_score(labels, preds)))
    print("Recall Score: {}".format(recall_score(labels, preds)))
    print("Accuracy Score: {}".format(accuracy_score(labels, preds)))
    print("F1 Score: {}".format(f1_score(labels, preds)))
    print("\n")
    return

def confusion_mtx (pipe, x, y):
    
    plt.figure(figsize =(10,10))
    plot_confusion_matrix(pipe, x, y,
                     cmap=plt.cm.Blues, display_labels=
                          ['Pass', 'Fail'], normalize = 'true')
    plt.xticks(horizontalalignment='right', fontsize='small')
    plt.show()




