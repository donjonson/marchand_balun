import numpy as np
Z0 = 50
Z1 = 50
Fo = 20e9
Zr = 100


#calculated values
C=1/np.sqrt((2*Z1)/(Z0+1))
Zodd = Z0*np.sqrt((1-C)/(1+C))
Zeven = Z0*(Z0/Zodd)

print('C = ' + str(C))
print('Zodd = ' + str(Zodd))
print('Zeven = ' + str(Zeven))