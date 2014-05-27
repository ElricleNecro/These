#!/usr/bin/env python
# encoding: utf-8

import numpy as np

from glob import glob
from InitialCond import Gadget as gad
# from IPython import embed
from matplotlib import pyplot as plt

SIMU_REP = "/media/Boulot/BackUp/OldSimulation/Thierry/Fujiwara/"
N = 300000

files = sorted(glob(SIMU_REP + "res-tsout/fuji_*"))

res = np.zeros(shape=(N, 2))

ind = 1000

for i, a in enumerate(files):
    snap = gad.Gadget(a)
    try:
        snap._read_format1(1, bdt=True)
    except Exception as e:
        print("Exception while reading '" + a + "'.")
        raise e
    snap.Part.SortById()
    res[i, 0] = snap.time
    res[i, 1] = snap.Part.NumpyTimeStep[ind]
    snap.Part.Release()
    del snap

plt.plot(res[:, 0], res[:, 1], "-")
plt.savefig(
    "graphe/vlasov_gadget/timestep.png",
    transparent=True,
    # bbox="tight"
)
plt.savefig(
    "graphe/vlasov_gadget/timestep.pdf",
    transparent=True,
    # bbox="tight"
)
plt.savefig(
    "graphe/vlasov_gadget/timestep.jpg",
    transparent=True,
    # bbox="tight"
)

# embed()
