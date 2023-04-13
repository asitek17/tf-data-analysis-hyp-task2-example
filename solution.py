import pandas as pd 
import numpy as np 
from scipy.stats import kruskal 
 
chat_id = 694905952 # Ваш chat ID, не меняйте название переменной 
 
def solution(x: np.array, y: np.array) -> bool: 
    alpha = 0.07 
    pvalue = kruskal(x, y).pvalue 
     
    return pvalue < alpha
