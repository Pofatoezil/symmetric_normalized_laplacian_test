# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:24:52 2019

@author: harrylee
"""

import numpy as np

A = np.matrix([
    [0, 1, 0, 0],
    [0, 0, 1, 1], 
    [0, 1, 0, 0],
    [1, 0, 1, 0]],
    dtype=float
)

X = np.matrix([
            [i, -i]
            for i in range(A.shape[0])
        ], dtype=float)

I = np.matrix(np.eye(A.shape[0]))

A_hat=A+I

D = np.array(np.sum(A, axis=0))[0]
D = np.matrix(np.diag(D))
D_hat= np.array(np.sum(A_hat, axis=0))[0]
D_hat = np.matrix(np.diag(D_hat))
L=D-A

#testing
print ("matrix D:\n{}".format(D))
print ("matrix D**-0.5:\n{}".format(np.sqrt(D**-1)))
Lsym_wiki_1=np.sqrt(D**-1)*L*np.sqrt(D**-1)
print ("Lsym wiki: D**-0.5 * L * D**-0.5\n{}".format(Lsym_wiki_1))
Lsym_wiki_2=np.eye(4)-np.sqrt(D**-1)*A*np.sqrt(D**-1)
print ("Lsym wiki: Eye-D**-0.5 * A * D**-0.5\n{}".format(Lsym_wiki_2))
Lsym_3=np.sqrt(D_hat**-1)*A_hat*np.sqrt(D_hat**-1)
print ("Lsym web : D_hat**-0.5 * A_hat * D_hat**-0.5\n{}".format(Lsym_3))
Lsym_4=np.sqrt(D_hat**-1)*(D-A)*np.sqrt(D_hat**-1)
print ("Lsym web : D_hat**-0.5 * (D-A) * D_hat**-0.5\n{}".format(Lsym_4))
Lsym_5=np.eye(4)-np.sqrt(D_hat**-1)*(A)*np.sqrt(D_hat**-1)
print ("Lsym web : Eye-D_hat**-0.5 * (A) * D_hat**-0.5\n{}".format(Lsym_5))


