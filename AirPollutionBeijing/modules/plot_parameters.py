import matplotlib.pyplot as plt
import numpy as np

params = {
    'axes.labelsize': 14,
    'axes.labelpad': 5,
    'axes.linewidth': 1.5,
    'backend': 'wxAgg',
    'figure.figsize': (6/1.2,6/1.2),
    'font.size': 15,
    'font.serif': 'Computer Modern',
    'font.weight': "bold",
    'font.weight': 'heavy',
    'legend.fontsize': 16,
    'legend.frameon': True,
    'lines.linewidth': 2.0,
    'lines.markersize': 2,
    'savefig.bbox': 'tight',
    'text.usetex': True,
    #"text.latex.preamble": r'\boldmath'
    'xtick.labelsize': 13.5,
    'xtick.major.size': 6,
    'xtick.minor.size': 3.,
    'xtick.major.width': 1.15, #1.15
    'xtick.minor.width': 1.15,
    'ytick.labelsize': 13.5,
    'ytick.major.size': 6, #8
    'ytick.minor.size': 3., #5
    'ytick.major.width': 1.15,
    'ytick.minor.width': 1.15,
}
plt.rcParams.update(params)

def formatLog(x,pos):
    decimalplaces = int(np.maximum(-np.log10(x),0))
    formatstring = '${{:.{:1d}f}}$'.format(decimalplaces)
    return formatstring.format(x)

