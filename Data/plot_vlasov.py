#!/usr/bin/env python3
# coding: utf-8

import argparse as ap

from matplotlib import use
use('agg')
from matplotlib import pyplot as plt
from LibThese.Carte import PhaseSpace as ps
from LibThese.Plot.hdf5 import Data
from os.path import basename


def argument():
    parser = ap.ArgumentParser(
           formatter_class=ap.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
            "Data",
            help="Gadget files to plot.",
    )
    parser.add_argument(
            "Hdf5",
            help="HDF5 files in which the script will get needed value.",
    )
    parser.add_argument(
            "--j-edges",
            dest="j_edges",
            help="File containing wanted $j$ bins edges.",
    )
    parser.add_argument(
            "-J",
            default=0.244,
            type=float,
            help="Angular momentum to use.",
    )
    parser.add_argument(
            "-o", "--out",
            help="Output files (without extension).",
            default="out",
    )
    parser.add_argument(
            "--format",
            help="Output file format.",
            default="pdf",
    )
    parser.add_argument(
        "--figure-size",
        help="Set the figure size (unfortunately, it's in inches).",
        nargs=2,
        default=(3., 1.8),
        dest="figsize",
        type=float,
    )
    parser.add_argument(
            "--r-min",
            help="Minimum value of r.",
            type=float,
    )
    parser.add_argument(
            "--r-max",
            help="Maximum value of r.",
            type=float,
    )
    parser.add_argument(
            "--v-min",
            help="Minimum value of v.",
            type=float,
    )
    parser.add_argument(
            "--v-max",
            help="Maximum value of v.",
            type=float,
    )
    parser.add_argument(
            "--nb-bin",
            help="Number of bins to use for the image.",
            type=int,
            default=300,
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = argument()
    s01 = Data(args.Hdf5)
    depl = s01.get_time(basename( args.Data ), "x", "y", "z", "vx", "vy", "vz")
    print("Getting data at time:", s01.get_time(basename( args.Data ), "time"))

    if args.j_edges:
        j_edges = ps.LoadEdge(args.j_edges)
    else:
        j_edges = None

    map = ps.PSPlot(
            args.Data,

            AxsLog=True,

            move_pos=depl[:3],
            move_vel=depl[3:],

            r_min=args.r_min,
            r_max=args.r_max,

            v_min=args.v_min,
            v_max=args.v_max,

            edge_j=j_edges,

            nbbin=args.nb_bin,
    )
    map.GetSliceJ(
            args.J
    )
    f, a, c = map.Plot()
    f.savefig(args.out + "_phasespace." + args.format, format=args.format, transparent=True, bbox_inches="tight")

    densite_log = s01.get(basename( args.Data ), "densite_log")
    fig = plt.figure(figsize=args.figsize)
    ax = fig.add_subplot(111, xscale="log", yscale="log")
    ax.plot(densite_log[:, 0], densite_log[:, 1], "-")
    fig.savefig(args.out + "_density." + args.format, format=args.format, transparent=True, bbox_inches="tight")
