# coding: utf-8
import numpy as np
from matplotlib import pyplot as plt
from LibThese.Plot import hdf5 as h
from InitialCond import Generation as icg
from astropy import constants as cte
king = icg.GKing(6.0, 3.5 * cte.pc.value, 2.9 * 1000)
king.SolveAll(100000)
from LibThese import Models as m
test2 = m.ADimKing(6.0)#, 2.9 * 1000, N=100000)
test2.Solve()
zeta = (1. / test2.rho(test2.X[:, 0])) * test2.X[:, 0] ** 2.5
T = 3. * (2.9 * 1000)**2 * ( 1 - 8./(15.*np.sqrt(np.pi)) * zeta )
data = h.Data("datav3.hdf5")
all2 = data.get("data", "densite")
plt.figure(figsize=(4., 2.8))
plt.xscale("log")
plt.yscale("log")
plt.plot(all2[:,0], all2[:,5] / all2[0,5], "g+")
plt.plot(test2.x * 3.5 * cte.pc.value, T / T[0], "-")
plt.xlabel(r"$r$ [$\mathrm{m}$]")
plt.ylabel(r"$<v^2>$ [$\mathrm{m}^2.\mathrm{s}^{-2}$]")
plt.savefig("../../graphe/verif_dispersion.png", bbox_inches="tight", transparent=True)
plt.savefig("../../graphe/verif_dispersion.pdf", bbox_inches="tight", transparent=True)
plt.savefig("../../graphe/verif_dispersion.jpg", bbox_inches="tight", transparent=True)
