## Implementation of SGHMC
Reference to this paper: https://tqchen.com/data/pdf/SGHMC-ICML14.pdf  

This package includes several different parts. 

The Package is inside of the Algorithm part. To implement the package,   
!pip install --index-url https://test.pypi.org/simple/ presnie  
from algorithm import sghmc  
sghmc.sghmc() is our algorithm.

Optimization is a jit and numba version of SGHMC algorithm 

Test includes a test case for the package

Comparison includes our result for implementing SGLD, SGD and SGHMC. It's an attempted replicate of original author's figure 4.  

Simulation includes a simulation data set to test for different HMC dynamics. It's an attempted replicate of original author's figure 2.  

Real data is a SGHMC implementation on real data. This folder includes the dataset from 
https://www.kaggle.com/dileep070/heart-disease-prediction-using-logistic-regression
