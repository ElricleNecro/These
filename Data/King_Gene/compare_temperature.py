# coding: utf-8
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
# plt.savefig("../../graphe/verif_dispersion.png", bbox_inches="tight", transparent=True)
# plt.savefig("../../graphe/verif_dispersion.pdf", bbox_inches="tight", transparent=True)
# plt.savefig("../../graphe/verif_dispersion.jpg", bbox_inches="tight", transparent=True)


f_v = interp1d(test2.x * 3.5 * cte.pc.value, T / T[0], kind='linear')

to_plot = all2

fig = plt.figure(figsize=(4, 3.8))
fig.subplots_adjust(hspace=0.0, wspace=0.0)

gs = gridspec.GridSpec(2, 1, height_ratios=[2,1])

ax = fig.add_subplot(
        gs[0],
        xscale="log",
        # xlim=(1e15, 3e17),
        # ylim=(1e-22, 5e-16)
)
ax.grid()
ax.set_yscale("log")
plt.setp(ax.get_xticklabels(), visible=False)

ax.plot(test2.x * 3.5 * cte.pc.value, T / T[0], "r-")
ax.plot(to_plot[:, 0], to_plot[:, 5] / to_plot[0, 5], "b-")
plt.setp(ax.get_xticklabels(), visible=False)
# ax.set_ylabel(r"$\rho(r)$ [$\mathrm{kg}.\mathrm{m}^{-3}$]")
ax.set_ylabel(r"$T(r) / T(0)$ ")
# ax.xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
# ax.xaxis.offsetText.set_visible(False)

ax = fig.add_subplot(
        gs[1],
        # xscale="log",
        # xlim=(1e15, 3e17),
        ylim=(-1., 1.),
        sharex=ax
)
ax.grid()
# ax.set_ylim(y2min, y2max)
ax.yaxis.set_major_locator(MaxNLocator(4, prune="upper"))

to_plot = to_plot[ to_plot[:, 0] >= (test2.x * 3.5 * cte.pc.value)[:].min() , :]
to_plot = to_plot[ to_plot[:, 0] <= (test2.x * 3.5 * cte.pc.value)[:].max() , :]

ax.plot(to_plot[:, 0], (to_plot[:, 5] / to_plot[0, 5] - f_v(to_plot[:, 0])) / f_v(to_plot[:, 0]), "b-")
ax.set_xlabel(r"$r$ [$\mathrm{m}$]")
ax.set_ylabel(r"$\frac{\frac{T_t(0)}{T(0)}T(r) - T_t(r)}{T_t(r)}$")

fig.savefig(
        "../../graphe/verif_dispersion_error.pdf",
        transparent=True,
        bbox_inches="tight"
)
fig.savefig(
        "../../graphe/verif_dispersion_error.png",
        transparent=True,
        bbox_inches="tight"
)

