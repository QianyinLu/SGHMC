## This is a description of the package organization.
This package includes several different parts. 

Package is inside of the Algorithm part. To implement the package,   
!pip install --index-url https://test.pypi.org/simple/ presnie  
from algorithm import sghmc  
sghmc.sghmc() is our algorithm.

optimization is a jit and numba version of SGHMC algorithm 

test includes some test cases for the package

comparison includes our result for implementing SGLD, SGD and SGHMC

simulation includes a simulation data set to test for different HMC dynamics 

real data is a SGHMC implementation on real data
