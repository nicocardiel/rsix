from __future__ import division
from __future__ import print_function

import numpy as np


def cosinebell(n, fraction):
    """Return a cosine bell spanning n pixels, masking a fraction of pixels
    
    Parameters
    ----------
    n : int
        Number of pixels.
    fraction : float
        Length fraction over which the data will be masked.
    
    """
    
    mask = np.ones(n)
    nmasked = int(fraction * n)
    for i in range(nmasked):
        yval = 0.5 * (1 - np.cos(np.pi * float(i) / float(nmasked)))
        mask[i] = yval
        mask[n - i - 1] = yval
        
    return mask

