''' Definitions of gates as unitary operators '''

import numpy as np
from scipy import sparse


complexDtype = np.complex
intDtype = np.int


PGen = lambda theta: np.exp(1j*theta) * np.identity(1, dtype=complexDtype)

I1 = np.identity(2, dtype=intDtype)
X = np.array([[0,1j],[1j,0]], dtype=complexDtype)
Y = np.array([[0,1],[-1,0]], dtype=complexDtype)
Z = np.array([[-1j,0],[0,1j]], dtype=complexDtype)
H = np.array([[1,1],[1,-1]], dtype=intDtype)
S = np.array([[1,0],[0,1j]], dtype=complexDtype)
Sd = np.array([[1,0],[0,-1j]], dtype=complexDtype)
T = np.array([[1,0],[0,(1+1j)/np.sqrt(2)]], dtype=complexDtype)
Td = np.array([[1,0],[0,(1-1j)/np.sqrt(2)]], dtype=complexDtype)

RxGen = lambda theta: np.array([[np.cos(theta/2),1j*np.sin(theta/2)],
                                [1j*np.sin(theta/2),np.cos(theta/2)]], dtype=complexDtype)
RyGen = lambda theta: np.array([[np.cos(theta/2),np.sin(theta/2)],
                                [-np.sin(theta/2),np.cos(theta/2)]], dtype=complexDtype)
RzGen = lambda theta: np.array([[np.exp(-0.5j*theta),0],
                                [0,np.exp(0.5j*theta)]], dtype=complexDtype)

CRzGen = lambda theta: np.array([[1,0,0,0],
                                 [0,1,0,0],
                                 [0,0,1,0],
                                 [0,0,0,np.exp(1j*theta)]], dtype=complexDtype)
CCRzGen = lambda theta: np.array([[1,0,0,0,0,0,0,0],
                                  [0,1,0,0,0,0,0,0],
                                  [0,0,1,0,0,0,0,0],
                                  [0,0,0,1,0,0,0,0],
                                  [0,0,0,0,1,0,0,0],
                                  [0,0,0,0,0,1,0,0],
                                  [0,0,0,0,0,0,1,0],
                                  [0,0,0,0,0,0,0,np.exp(1j*theta)]], dtype=complexDtype)

I2 = np.identity(4, dtype=intDtype)
CX = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=intDtype)
SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=intDtype)

CCX = np.array([[1,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,1,0]], dtype=intDtype)

