#!/usr/bin/env python
# encoding: utf-8

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from LibThese import Models as m

sib = m.SIB(300)
sib.Solve()

fig = plt.figure(figsize=(5., 2.8))
ax = fig.add_subplot(111)

ax.set_ylabel(r"$\mu(-\lambda)$")
ax.set_xlabel(r"$\lambda$")
ax.set_xlim(-0.4, 1)
ax.set_ylim(0.8, 2.6)

# ax.xaxis.set_major_locator(MaxNLocator(4))
# ax.yaxis.set_major_locator(MaxNLocator(5))

ax.plot(-sib.Lambda, sib.Mu, "-")
ax.plot([-1/4], [2], "+")
ax.plot(np.linspace( -0.199 - 0.1, -0.199 + 0.1, 5), [2.52]*5, "-")
ax.plot([-0.335]*5, np.linspace( 2.032 - 0.15, 2.032 + 0.15, 5), "-")

fig.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/calorique.png", transparent=True, bbox_inches="tight")
fig.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/calorique.pdf", transparent=True, bbox_inches="tight")
