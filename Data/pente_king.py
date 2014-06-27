# coding: utf-8
get_ipython().system(" sed -e 's:None:0.0:g' pente-ci.dat > /tmp/toto.dat")
data = np.loadtxt("/tmp/toto.dat")
f = -10.0698 * np.exp( -0.220152 * data[:,0]) - 1.63409
plt.figure(figsize=(3., 1.8))
plt.ylabel(r"Pente $\alpha$")
plt.xlabel("$W_0$")
plt.plot(data[:,0], data[:,1], "+")
plt.plot(data[:,0], f, "-")
plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/king_pente_w0.png", transparent=True, bbox_inches="tight"
)
plt.savefig("/home/plum/Documents/These/Latex/Manuscrit_GPLUM/graphe/king_pente_w0.pdf", transparent=True, bbox_inches="tight")
