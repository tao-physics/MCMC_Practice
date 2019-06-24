import numpy as np

# s = 1.
# sunmass = 1.
# kpc = 1.
# gy = 1e9*365*24*60*60*s
# km = 1/(3.0857*1e16)*kpc
# m = 1/(3.0857*1e16*1e3)*kpc
# cm = 1/(3.0857*1e16*1e3*1e2)*kpc
# Mpc=1000.*kpc
# kg = 1/(1.989*1e30)*sunmass
# g = 1/(1.989*1e30*1e3)*sunmass
# ng = 6.67408*1e-11*m**3/(kg*s**2)

# input units:
# r kpc
# v km / s
# g m / s^2

# think about what function you want to realize
# input and output


class MOND:
	def __init__(self, gplus): # gplus = 1.2 * 10 ** -10 m / s^-2
		self.gplus = gplus

	def g_bar(self, v, r): # {r : kpc, v : km / s}
		return (v * 1000) ** 2 / (r * (3.0857*1e16*1e3))
	

	def g_obs(self, v, r):
		return self.g_bar(v, r)/ (1 - np.exp(-np.sqrt(self.g_bar(v, r)/self.gplus)))


	def v_obs(self, v, r):
		return np.sqrt(self.g_obs(v, r) / 1000 * (r * (3.0857*1e16)))  # km / s