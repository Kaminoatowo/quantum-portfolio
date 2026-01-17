import numpy as np

def X() -> np.ndarray:

    return np.array([[0., 1.], [1., 0.]])

def Y() -> np.ndarray:
    
    return np.array([[0., -1.j],[-1.j, 0.]])

def Z() -> np.ndarray:

    return np.array([[1., 0.], [0., -1.]])

def H() -> np.ndarray:

    return 1/np.sqrt(2)*np.array([[1., 1.], [1., -1.]])

def RX(theta: float) -> np.ndarray:

    return np.array([[np.cos(theta/2),-1.j*np.sin(theta/2)], [-1.j*np.sin(theta/2),np.cos(theta/2)]])

def RY(theta: float) -> np.ndarray: 

    return np.array([[np.cos(theta/2),-1.*np.sin(theta/2)], [np.sin(theta/2),np.cos(theta/2)]])

def RZ(theta: float) -> np.ndarray:

    return np.array([[np.exp(-1.j*theta/2),0.], [0.,np.exp(1.j*theta/2)]])

