#%% このままだと、xはfloatしか取れず配列を入力できない
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

#%%numpyを使用したステップ関数
import numpy as np

def step_function2(x):
    y = x > 0
    return y.astype(np.int)
