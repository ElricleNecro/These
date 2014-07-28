#!/usr/bin/env python
# encoding: utf-8

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import gridspec as gridspec
from matplotlib.ticker import MaxNLocator, ScalarFormatter
from scipy.interpolate import interp1d
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
temp = data.get("data", "temperature")

plt.figure(figsize=(4., 2.8))

plt.plot(dens[:, 0], dens[:, 1], "b-")
plt.plot(king.data[:,0], king.data[:,3], "r-")
plt.plot(rho[:,0], rho[:,1], "g-")

plt.xlim(1e15, 3e17)
plt.ylim(1e-22, 5e-16)

plt.ylabel(r"$\rho(r)$ [$\mathrm{kg}.\mathrm{m}^{-3}$]")
plt.xlabel(r"$r$ [$\mathrm{m}$]")

# plt.savefig("../../graphe/verif_densite_new.pdf", transparent=True, bbox_inches="tight")
# plt.savefig("../../graphe/verif_densite_new.png", transparent=True, bbox_inches="tight")

######
# With relative errors:
#######################
f_v = interp1d(king.data[:, 0], king.data[:, 3], kind='linear')

to_plot = rho[ rho[:, 1] > 0, :]
to_plot2 = dens[ dens[:, 1] > 0, :]

fig = plt.figure(figsize=(4, 3.8))
fig.subplots_adjust(hspace=0.0, wspace=0.0)

gs = gridspec.GridSpec(2, 1, height_ratios=[2,1])

ax = fig.add_subplot(gs[0], xscale="log", xlim=(1e15, 3e17), ylim=(1e-22, 5e-16))
ax.grid()
ax.set_yscale("log")
plt.setp(ax.get_xticklabels(), visible=False)

ax.plot(king.data[:, 0], king.data[:, 3], "r-")
ax.plot(to_plot[:, 0], to_plot[:, 1], "g-")
ax.plot(to_plot2[:, 0], to_plot2[:, 1], "b-")
ax.set_ylabel(r"$\rho(r)$ [$\mathrm{kg}.\mathrm{m}^{-3}$]")

ax = fig.add_subplot(
        gs[1],
        xscale="log",
        xlim=(1e15, 3e17),
        ylim=(-1, 1),
        sharex=ax
)
ax.grid()
# ax.set_ylim(y2min, y2max)
ax.yaxis.set_major_locator(MaxNLocator(5, prune="upper"))

to_plot = to_plot[ to_plot[:, 0] >= king.data[:,0].min() , :]
to_plot = to_plot[ to_plot[:, 0] <= king.data[:,0].max() , :]

to_plot2 = to_plot2[ to_plot2[:, 0] >= king.data[:,0].min() , :]
to_plot2 = to_plot2[ to_plot2[:, 0] <= king.data[:,0].max() , :]

ax.plot(to_plot[:, 0], (to_plot[:, 1] - f_v(to_plot[:, 0])) / f_v(to_plot[:, 0]), "g-")
ax.plot(to_plot2[:, 0], (to_plot2[:, 1] - f_v(to_plot2[:, 0])) / f_v(to_plot2[:, 0]), "b-")
ax.set_xlabel(r"$r$ [$\mathrm{m}$]")
ax.set_ylabel(r"$\frac{\rho(r) - \rho_t(r)}{\rho_t(r)}$")

fig.savefig(
        "../../graphe/verif_densite_new_error.pdf",
        transparent=True,
        bbox_inches="tight"
)
fig.savefig(
        "../../graphe/verif_densite_new_error.png",
        transparent=True,
        bbox_inches="tight"
)









plt.figure(figsize=(4., 2.8))

plt.plot(pot[np.argsort(pot[:,0]),0], pot[np.argsort(pot[:,0]),1], "b+")
plt.plot(king.data[:,0], king.data[:,1], "r-")

plt.xlabel(r"$r$ [$\mathrm{m}$]")
plt.ylabel(r"$\psi(r)$ [$\mathrm{m}^{2}.\mathrm{s}^{-2}$]")

# plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/verif_potentiel_new.png", bbox_inches="tight", transparent=True)
# plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/verif_potentiel_new.pdf", bbox_inches="tight", transparent=True)


f_v = interp1d(king.data[:, 0], king.data[:, 1], kind='linear')

to_plot = pot[ np.argsort(pot[:,0]), :]

fig = plt.figure(figsize=(4, 3.8))
fig.subplots_adjust(hspace=0.0, wspace=0.0)

gs = gridspec.GridSpec(2, 1, height_ratios=[2,1])

ax = fig.add_subplot(
        gs[0],
        # xscale="log",
        # xlim=(1e15, 3e17),
        # ylim=(1e-22, 5e-16)
)
ax.grid()
# ax.set_yscale("log")
plt.setp(ax.get_xticklabels(), visible=False)

ax.plot(king.data[:, 0], king.data[:, 1], "r-")
ax.plot(to_plot[:, 0], to_plot[:, 1], "b-")
plt.setp(ax.get_xticklabels(), visible=False)
# ax.set_ylabel(r"$\rho(r)$ [$\mathrm{kg}.\mathrm{m}^{-3}$]")
ax.set_ylabel(r"$\psi(r)$ [$\mathrm{m}^{2}.\mathrm{s}^{-2}$]")
ax.xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.xaxis.offsetText.set_visible(False)

ax = fig.add_subplot(
        gs[1],
        # xscale="log",
        # xlim=(1e15, 3e17),
        ylim=(-0.2, 0.2),
        sharex=ax
)
ax.grid()
# ax.set_ylim(y2min, y2max)
ax.yaxis.set_major_locator(MaxNLocator(4, prune="upper"))

to_plot = to_plot[ to_plot[:, 0] >= pot[:,0].min() , :]
to_plot = to_plot[ to_plot[:, 0] <= pot[:,0].max() , :]

ax.plot(to_plot[:, 0], (to_plot[:, 1] - f_v(to_plot[:, 0])) / f_v(to_plot[:, 0]), "b-")
ax.set_xlabel(r"$r$ [$\mathrm{m}$]")
ax.set_ylabel(r"$\frac{\psi(r) - \psi_t(r)}{\psi_t(r)}$")

fig.savefig(
        "../../graphe/verif_potentiel_new_error.pdf",
        transparent=True,
        bbox_inches="tight"
)
fig.savefig(
        "../../graphe/verif_potentiel_new_error.png",
        transparent=True,
        bbox_inches="tight"
)

