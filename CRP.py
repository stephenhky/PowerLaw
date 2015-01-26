# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 15:13:06 2015

@author: hok1
"""

# Chinese Restaurant Process
# B Bassetti, M Zarei, M C Lagomarsino, G Bianconi, Physical Review E 80, 066118 (2009)

import numpy as np
from scipy.optimize import curve_fit

def probsTableCRP(karray, alpha, theta):
    T = np.sum(karray)
    N = len(karray)
    probs = (karray-alpha)/(T+theta) if N > 0 else np.array([])
    probs = np.append(probs, (alpha*N+theta)/(T+theta))
    return probs

def sampleTableCRP(karray, alpha, theta):
    probs = probsTableCRP(karray, alpha, theta)
    return np.int(np.random.choice(len(probs), 1, p=probs))
    
def zipfexpr(x, f0, alpha):
    return f0*x**(-alpha)
    
class ChineseRestaurantProcess:
    def __init__(self, alpha=0.75, theta=0.5):
        self.reset(alpha, theta)
        
    def reset(self, alpha=0.75, theta=0.5):
        self.alpha = alpha
        self.theta = theta
        self.karray = []
        
    def proceed(self, numtimes=1):
        for i in range(numtimes):
            tablenum = sampleTableCRP(self.karray, self.alpha, self.theta)
            if tablenum < len(self.karray):
                self.karray[tablenum] += 1
            else:
                self.karray = np.append(self.karray, 1)
            yield self.karray
            
    def fit_powerlaw(self):
        freq, bins = np.histogram(self.karray, 
                                  bins=range(int(np.min(self.karray)), 
                                             int(np.max(self.karray))))
        ndim = min(len(bins), len(freq))
        result = curve_fit(zipfexpr, bins[:ndim], freq[:ndim], 
                           p0=[freq[0], 1.0])
        return result
