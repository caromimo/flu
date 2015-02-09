# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import scipy
import scipy.integrate
import pylab as plt

# <codecell>

beta = 0.003

# <codecell>

gamma = 0.1

# <codecell>

def SIR_model(X,t=0):
    r=scipy.array([-beta*X[0]*X[1]
                   , beta*X[0]*X[1] - gamma*X[1]
                   , gamma*X[1]])
    return r

# <codecell>

if __name__ == "__name__":
    time = scipy.linspace(0,60,num=100)
    parameters = scipy.array([225,1,0])
    X = scipy.integrate.odeint(SIR_model, parameters, time)

# <codecell>

plt.plot(range(0,100), X[:,0],'o', color="green")
plt.plot(range(0,100), X[:,1],'x', color="red")
plt.plot(range(0,100), X[:,2],'*', color="blue")
plt.show()

# <rawcell>

# Below is the plot that was generated from the above script:
# 
# So my understanding at this point is that the:
# green os represent the susceptible individuals
# red xs represent the infected individuals
# blue *s represent the recovered individuals

# <markdowncell>

# ![caption](files/figure_flu_SIR.png)

# <codecell>


# <codecell>


