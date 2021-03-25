import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, y):
    '''Function which takes in an array of x values and an array of y values.'''
    return 5*np.exp(-(x-1)**2 - 2*(y-3)**2) + 3*np.exp(-2*(x-4)**2 - (y-1)**2)

def gradient(f, x, y, h):
    '''Takes in a function, an array of x values, an array of y values, and
        a step size h, and returns the gradient in the form of a list of tuples
        of vectors.'''
    dx = []
    dy = []
    for i in range(len(x[:-1])):
        answerx = (f((x[i]+h), y[i]) - f((x[i]-h), y[i]))/(2*h)
        dx.append(answerx)
    for i in range(len(y[:-1])):
        answery = (f(x[i], (y[i]+h)) - f(x[i], (y[i]-h)))/(2*h)
        dy.append(answery)
    gradVector = list(zip(dx, dy))
    return gradVector

def gradientDescent(initialGuess, initialGamma, gradient):
    '''Function which takes in an initial guess(as tuple), initial gamma, and
    the gradient (a list of tuples of vectors), and performs gradient descent
    to find the minimum point.'''
    guess = list(initialGuess)
    for i in range(len(gradient)):
        guessList = []
        for j in range(2):
            guess1 = guess[j] - initialGamma*gradient[i][j]
            guessList.append(guess1)
        guess = guessList
    return guess
    
               
if __name__ == '__main__':
    x = np.arange(0, 5, 0.1)
    y = np.arange(0, 5, 0.1)
    xs, ys = np.meshgrid(x, y)
    zs = f(xs, ys)
    grad = gradient(f, x, y, 0.1)
    plt.contourf(xs, ys, zs)
    #plt.plot(x, f(x, y))
    #plt.savefig('Contour.png')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.colorbar()
    plt.show()

    minimum = gradientDescent((0.5, 2.5), 0.5, grad)
    print("The minimum found from gradient descent is", minimum)
    #maximum = scipy.optimize.fmin(lambda x: -f(x, y), 0, 1)
    #print(maximum)
