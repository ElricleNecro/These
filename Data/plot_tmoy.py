# coding: utf-8

from matplotlib import pyplot as plt
import numpy as np

data = np.loadtxt("temperature_multi.dat", usecols=(0,2))

plt.figure(figsize=(4, 2.8))
plt.plot(data[:, 0], data[:, 1], "-")
plt.ylabel(r"$T_{K,\mathrm{moy}}$")
plt.xlim(0., 20)
plt.yscale("log")
plt.xlabel(r"$W_0$")

plt.savefig(
        "../graphe/king_temperature_moy_v3.pdf",
        transparent=True,
        bbox_inches="tight"
)
plt.savefig(
        "../graphe/king_temperature_moy_v3.png",
        transparent=True,
        bbox_inches="tight"
)
