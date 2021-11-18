"""
Dissertation plotting class
"""

#################
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
plt.ion()
##################

class DissertationPlots:

    def __init__(self, greyscale=False):
        self._attributes = {'figsize': (8,5), 'grid': True, 'greyscale': greyscale}

    def plot(self, arr, shape, save=None, **kwargs):
        fig, axs = plt.subplots(shape[0], shape[1], figsize=(8*shape[1], 5*shape[0]))
        if self._attributes['greyscale']:
            plt.style.use('grayscale')
            fig.patch.set_facecolor('white')

        for i,x in enumerate(arr):
            axs[i].plot(x)
            if 'grid' in kwargs:
                axs[i].grid(kwargs['grid'])
            else:
                axs[i].grid(self._attributes['grid'])
        fig.tight_layout()
