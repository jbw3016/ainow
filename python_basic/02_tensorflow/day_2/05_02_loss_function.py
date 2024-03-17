# 05_02_loss_function.py

import numpy as np
import matplotlib.pyplot as plt

def cross_entropy(y):
    def log_a():
        return "a"
    
    def log_b():
        return "b"
    
    print(y * log_a() + (1-y) * log_b())
    
cross_entropy(y=0)
cross_entropy(y=1)