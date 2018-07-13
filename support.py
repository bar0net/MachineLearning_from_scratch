import numpy as np

# Generates a clustered dataset
# argv: a tuple defining the characteristics of each cluster
# defined as: tuple(number_of_points, center_of_cluster)
def ClusteredDataset(*args):
    X = None
    y = []
    i = 0
    for points, center in args:
        if X is None:
            X = GenerateSet(points, center)
        else:
            X = np.vstack( (X, GenerateSet(points, center)) )
        y += [i] * points
        i += 1
    return X, np.array(y)

# Generate a set of points around a center position
def GenerateSet(points, center):
    output = np.random.randn(points, np.size(center))
    return np.array(center) + output

# Compute RGB colors for a labels 
def Paint(x):
    r = int((100000 * np.abs(np.tan(x))) % 256)
    g = int((100000 * np.abs(np.sin(x))) % 256)
    b = int((100000 * np.abs(np.cos(x))) % 256)
    
    return '#%02x%02x%02x' % (r,g,b)

# Paint a set of labels
def Colors(y):
    return list(map(Paint,y))
