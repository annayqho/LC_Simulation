""" For z = 0.2, r-band, generate a SN Ia light curve """

import numpy as np
import sncosmo
from astropy.table import Table

# choose a built-in source
model = sncosmo.Model(source='hsiao')

# set model parameters
model.set(z=0.2)

# plot
sncosmo.plot_lc(model=model, bands=['sdssr'])
