# coding: utf-8

from matplotlib import pyplot as plt
import numpy as np
from LibThese import Models as m

W_0 = [1, 5, 9, 14]

plt.figure(figsize=(4, 2.8))

plt.ylabel(r"$\zeta(x)$")
plt.xlabel(r"$x$")

for w in W_0:
    test2 = m.ADimKing(w)
    test2.Solve()
    zeta = (1. / test2.rho(test2.X[:, 0])) * test2.X[:, 0] ** 2.5
    plt.plot(test2.x, zeta, "-")

plt.xscale("log")
plt.yscale("log")

plt.savefig(
        "../graphe/zeta_func.png",
        transparent=True,
        bbox_inches="tight"
)
plt.savefig(
        "../graphe/zeta_func.pdf",
        transparent=True,
        bbox_inches="tight"
)
