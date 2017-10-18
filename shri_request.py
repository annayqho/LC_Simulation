""" For z = 0.2, r-band, generate a SN Ia light curve """

import sncosmo

# I'm using the "Fitting a light curve" tutorial
data = sncosmo.load_example_data()
print(data)

# OK, let's only take the sdssr data
data_r = data[data['band'] == 'sdssr']
print(data_r)

# OK, that's just how to plot the example data.


