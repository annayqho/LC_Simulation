""" For z = 0.2, r-band, generate a SN Ia light curve """

import numpy as np
import matplotlib.pyplot as plt
import sncosmo
from astropy.table import Table


def simple():
    # choose a built-in source
    model = sncosmo.Model(source='hsiao')

    # set model parameters
    model.set(z=0.2)

    # plot
    sncosmo.plot_lc(model=model, bands=['sdssr', 'sdssg'])
    plt.savefig("z02_gr.png")
    plt.show()


def multiple_z():
    # choose a built-in source
    models = []
    npts = 3
    zs = np.linspace(0, 0.5, npts)
    for ii in np.arange(npts):
        model = sncosmo.Model(source='hsiao')
        model.set(z=zs[ii])
        models.append(model)

    # plot
    sncosmo.plot_lc(
            model=models, bands=['sdssr']*npts, model_label=zs, 
            color='k')
    plt.show()


if __name__=="__main__":
    simple()
