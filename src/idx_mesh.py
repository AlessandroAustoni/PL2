from read_funcs import spherdist
import numpy as np

# Find corner indices in grids
def idx_mesh(x, y, X, Y, maxdist=None):
    """
    Find indices in mesh nearest to coordinates

    x: float, first coordinate target value
    y: float, second coordinate target value
    X: ndarray, first array of the mesh
    Y: ndarray, second array of the mesh
    maxdist: float, difference allowed (in meters)
    
    out_idx: list, indices for lon and lat
    """
    distance = (X-x)**2 + (Y-y)**2
    idxs = np.argwhere(distance == np.amin(distance))[0]
    out_idx = (idxs[0], idxs[1])
    
    # Calculate distance in meters with the haversine formula
    diffm = 1000.*spherdist(x, y, X[idxs[0], idxs[1]], Y[idxs[0], idxs[1]])

    if maxdist is not None and diffm > maxdist:
        print('Tolerance {} m exceeded!'.format(maxdist))

    return out_idx