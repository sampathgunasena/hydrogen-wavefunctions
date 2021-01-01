################################################################################################################
#
#script that computes first few fundamental wave functions of Hydrogen atom and plots wave function in x-z plane 
#
################################################################################################################



import numpy as np
from scipy.special import legendre
from scipy.special import genlaguerre
import math
from matplotlib import pyplot as plt


print(legendre(0)(5))
print(genlaguerre(0,1))

n = 4.2
x = np.linspace(-n,n,100)
z = np.linspace(-n,n,100)


x_meshed, z_meshed = np.meshgrid(x, z)
##r_meshed = np.exp(-np.sqrt(x_meshed**2 + z_meshed**2))

##1,0,0 --> 1s
r_meshed1 = np.exp(-np.sqrt(x_meshed**2 + z_meshed**2)/0.529) * 2 * 1 * genlaguerre(0,1) * np.sqrt(1/(4*np.pi)) * 1 * 1
##2,1,0 --> 2p^0
r_meshed2 = np.exp(-np.sqrt(x_meshed**2 + z_meshed**2)/0.529/2) * np.sqrt(1/24) * (np.sqrt(x_meshed**2 + z_meshed**2) / (2 * 0.529)) * genlaguerre(0,3) * np.sqrt(3/(4*np.pi)) * (z_meshed / np.sqrt(x_meshed**2 + z_meshed**2)) * 1
##3,2,0 --> 3d^0
r_meshed3 = np.exp(-np.sqrt(x_meshed**2 + z_meshed**2)/0.529/3) * np.sqrt((2/3)**3 / (6 * math.factorial(5))) * (np.sqrt(x_meshed**2 + z_meshed**2) / (3 * 0.529))**2 * genlaguerre(0,5) * np.sqrt(5/(4*np.pi)) * legendre(2)(z_meshed / np.sqrt(x_meshed**2 + z_meshed**2)) * 1


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos1 = ax1.imshow(r_meshed1, cmap='inferno', interpolation='none', extent=[x[0],x[-1],z[0],z[-1]], aspect="auto")
pos2 = ax2.imshow(r_meshed2, cmap='inferno', interpolation='none', extent=[x[0],x[-1],z[0],z[-1]], aspect="auto")
pos3 = ax3.imshow(r_meshed3, cmap='inferno', interpolation='none', extent=[x[0],x[-1],z[0],z[-1]], aspect="auto")
##ax1.invert_yaxis()

ax1.set_title("1s")
ax2.set_title("2p")
ax3.set_title("3d")

ax1.tick_params(axis='both', which='major', labelsize=6)
ax2.tick_params(axis='both', which='major', labelsize=6)
ax3.tick_params(axis='both', which='major', labelsize=6)


# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
fig.colorbar(pos1, ax=ax1)
fig.colorbar(pos2, ax=ax2)
fig.colorbar(pos3, ax=ax3)

# repeat everything above for the negative data


plt.show()
