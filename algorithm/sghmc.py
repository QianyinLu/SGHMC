import numpy as np
def batch(X,Y, nbatch):
    nrow = X.shape[0]
    idx = np.random.choice(nrow, nbatch, replace = False)
    X_sample = X[idx,:]
    Y_sample = Y[idx]
    return X_sample, Y_sample
def sghmc(theta0,X,Y,nbatch,gradU,M,C,V,eps,step = 10, niter = 10):
    B = 1/2 * V * eps
    sigma = np.sqrt(2*eps*(C-B))
    n, p = X.shape
    theta = theta0 #set an initial value of theta
    thetas =np.zeros([step,p])
    Minv = np.linalg.inv(M)
    np.random.seed(10)
    #simulate dynamics
    for t in range(step):
        r = np.random.multivariate_normal(np.zeros(p),np.sqrt(M))
        for i in range(niter):
            theta = theta + eps*Minv@r
            X_sample,Y_sample = batch(X,Y,nbatch)
            r =  r - eps*gradU(X_sample, Y_sample,theta,n,V) - eps*C @ Minv @ r 
            + np.random.multivariate_normal(np.zeros(p),sigma,1).ravel()
        thetas[t,:] = theta
    return thetas