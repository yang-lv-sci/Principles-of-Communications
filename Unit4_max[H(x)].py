# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 11:51:48 2023

@author: lvyan
"""

import numpy as np
from scipy.optimize import minimize

def objective(x):
    return np.sum(x * np.log2(x))

# 约束条件: Σp(x_i) = 1
def constraint1(x):
    return np.sum(x) - 1

# 每个 p(x_i) 必须大于 0 的约束
bounds = [(0.0001, 1)] * 4  # 设定一个很小的正数避免log(0)

# 设置约束条件
con1 = {'type': 'eq', 'fun': constraint1}
constraints = [con1]

# 选择初始猜测值
x0 = [0.1, 0.20, 0.35, 0.30]

# 调用优化器
solution = minimize(objective, x0, bounds=bounds, constraints=constraints)

# 输出结果
if solution.success:
    optimized_p = solution.x
    print('Optimized p(x_i):', optimized_p)
    print('Maximum of objective function:', -solution.fun)
else:
    print('Optimization failed:', solution.message)
