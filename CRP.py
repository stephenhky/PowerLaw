# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 15:13:06 2015

@author: hok1
"""

# Chinese Restaurant Process
# B Bassetti, M Zarei, M C Lagomarsino, G Bianconi, Physical Review E 80, 066118 (2009)

import numpy as np

def probsTableCRP(karray, alpha, theta):
    T = np.sum(karray)
    N = len(karray)
    probs = (karray-alpha)/(T+theta) if N > 0 else np.array([])
    probs = np.append(probs, (alpha*N+theta)/(T+theta))
    return probs

def sampleTableCRP(karray, alpha, theta):
    probs = probsTableCRP(karray, alpha, theta)
    return np.random.choice(len(probs), 1, p=probs)
