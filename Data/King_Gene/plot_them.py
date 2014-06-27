#!/usr/bin/env python
# encoding: utf-8

import numpy as np

from matplotlib import pyplot as plt
from LibThese.Plot import hdf5 as h
from InitialCond import Generation as icg
from astropy import constants as cte

king = icg.GKing(6.0, 3.5 * cte.pc.value, 2.9 * 1000)
king.SolveAll(100000)

data = h.Data("data.hdf5")
rho = data.get("data", "densite_log")
rho = rho[rho[:,1] != 0.0, :]
dens = data.get_densite("data", "r", "densite")
pot = data.get("data", "potentiel")

plt.figure(figsize=(4., 2.8))

plt.plot(dens[:, 0], dens[:, 1], "b-")
plt.plot(king.data[:,0], king.data[:,3], "r-")
plt.plot(rho[:,0], rho[:,1], "g-")

plt.xlim(1e15, 3e17)
plt.ylim(1e-22, 5e-16)

plt.ylabel(r"$\rho(r)$ [$\mathrm{kg}.\mathrm{m}^{-3}$]")
plt.xlabel(r"$r$ [$\mathrm{m}$]")

plt.savefig("../../graphe/verif_densite_new.pdf", transparent=True, bbox_inches="tight")
plt.savefig("../../graphe/verif_densite_new.png", transparent=True, bbox_inches="tight")


plt.figure(figsize=(4., 2.8))

plt.plot(pot[np.argsort(pot[:,0]),0], pot[np.argsort(pot[:,0]),1], "b+")
plt.plot(king.data[:,0], king.data[:,1], "r-")

plt.xlabel(r"$r$ [$\mathrm{m}$]")
plt.ylabel(r"$\psi(r)$ [$\mathrm{m}^{2}.\mathrm{s}^{-2}$]")

plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/verif_potentiel_new.png", bbox_inches="tight", transparent=True)
plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/verif_potentiel_new.pdf", bbox_inches="tight", transparent=True)
