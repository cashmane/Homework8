import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def potential(a, b, c, R):
    '''Function which returns the potential energy in electron volts.
        r must be in angstroms.'''
    return (a*np.exp(-b*R)) - (c/R**6)

if __name__ == '__main__':
    A = 1
    B = 1
    C = 1
    rs = np.arange(0.8, 3.1, 0.1)
    print(rs[:10])
    phis = []
    for r in rs:
        phi = potential(A, B, C, r)
        phis.append(phi)
    plt.plot(rs, phis)
    #plt.yscale('log')
    plt.title("Potential vs. Distance")
    plt.xlabel("R in Angstrom")
    plt.ylabel("Potential in Ev")
    plt.show()

    maximum = scipy.optimize.fmin(lambda x : -potential(A, B, C, x), 0)
    print('The maximum is', maximum)
    
