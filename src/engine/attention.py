from feature_map import FeatureMap
from math import log, exp


def d(v0, v1):
    if v0 == 0:
        v0 = 0.0001
    if v1 == 0:
        v1 = 0.0001
    return abs(log(float(v0)/float(v1)))


def F(dx, dy, sigma):
    if dx == dy == 0:
        return 0
    return 1/(dx**2+dy**2)**sigma
    #return exp(-((dx*dx+dy*dy)/(2*sigma*sigma)))


def fc(a, b, sigma=0.05):
    x0, y0, v0 = a
    x1, y1, v1 = b
    #return d(v0, v1)
    return d(v0, v1)*F(x1-x0, y1-y0, sigma)


def fd(a, b, sigma=0.01):
    x0, y0, v0 = a
    x1, y1, v1 = b
    #return d(v0, v1)
    return d(v0, v1)*F((x1-x0)/2, (y1-y0)/2, sigma)


def get_close_map(feature, radius, function):
    w = len(feature.map)
    h = len(feature.map[0])
    saliency = FeatureMap()
    saliency.map = [[0 for i in range(h)] for j in range(w)]
    for x0 in range(w):
        for y0 in range(h):
            n = 0
            for x in range(max(0, x0-radius), min(x0+radius+1, w-1)):
                for y in range(max(0, y0-radius), min(y0+radius+1, h-1)):
                    saliency.map[x0][y0] += function([x0, y0, feature.map[x0][y0]], [x, y, feature.map[x][y]])
                    n += 1
            saliency.map[x0][y0] /= n
    saliency.normalize(True)
    return saliency


def get_distant_map(feature, cell_size, function):
    w = len(feature.map)
    h = len(feature.map[0])
    saliency = FeatureMap()
    saliency.map = [[0 for i in range(h)] for j in range(w)]
    cw = w/cell_size
    ch = h/cell_size
    cells = FeatureMap()
    cells.map = [[0 for i in range(ch)] for j in range(cw)]
    for x in range(w):
        for y in range(h):
            cells.map[x/cell_size][y/cell_size] += feature.map[x][y]/float(cell_size)**2
    for x0 in range(w):
        for y0 in range(h):
            n = 0
            for x in range(cell_size/2, w, cell_size):
                for y in range(cell_size/2, h, cell_size):
                    saliency.map[x0][y0] += function([x0, y0, feature.map[x0][y0]], [x, y, feature.map[x][y]])
                    n += 1
            saliency.map[x0][y0] /= n
    saliency.normalize(True)
    return saliency


def get_saliency_map(feature, close_function, distant_function, radius, cell_size):
    dm = get_distant_map(feature, cell_size, distant_function)
    return get_close_map(feature, radius, close_function)+dm