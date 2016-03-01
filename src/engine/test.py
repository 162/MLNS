from attention import *
from feature_map import draw_multiple
from time import clock, sleep
import multiprocessing.dummy as mp


def run_test(filename, width, height, scale, radius, cell_size, save_as=None, status=False, mode='rgb'):
    start = clock()
    if status:
        print "STATUS: STARTING TO LOOK AT", filename
        local = clock()
    if 'r' in mode:
        red = FeatureMap()
        red.load(filename, width, height, 'r')
    if 'g' in mode:
        green = FeatureMap()
        green.load(filename, width, height, 'g')
    if 'b' in mode:
        blue = FeatureMap()
        blue.load(filename, width, height, 'b')
    if 'c' in mode:
        contrast = FeatureMap()
        contrast.load(filename, width, height, 'c')
    if status:
        print "STATUS: PICTURES RECIEVED IN", clock()-local
        local = clock()
    if 'r' in mode:
        red = get_saliency_map(red, fc, fd, radius, cell_size)
        red.normalize()
        if status:
            print "STATUS: RED IS DONE IN", clock()-local
            local = clock()
    if 'g' in mode:
        green = get_saliency_map(green, fc, fd, radius, cell_size)
        green.normalize()
        if status:
            print "STATUS: GREEN IS DONE IN", clock()-local
            local = clock()
    if 'b' in mode:
        blue = get_saliency_map(blue, fc, fd, radius, cell_size)
        blue.normalize()
        if status:
            print "STATUS: BLUE IS DONE IN", clock()-local
            local = clock()
    if 'c' in mode:
        contrast.normalize()
        contrast = get_saliency_map(contrast, fc, fd, radius, cell_size)
        contrast.normalize()
        if status:
            print "STATUS: CONTRAST IS DONE IN", clock()-local
            local = clock()
    try:
        features = []
        if 'r' in mode:
            features.append(red)
        if 'g' in mode:
            features.append(green)
        if 'b' in mode:
            features.append(blue)
        if 'c' in mode:
            features.append(contrast)
        draw_multiple(features, 0, 0, scale, save_as, bw=True)
    except SystemExit:
        if status:
            print "STATUS: DRAWN IN", clock()-local
        print "STATUS: ENDED IN", clock()-start


def thread_function(filename, width, height, feature, radius, cell_size):
    feature_map = FeatureMap()
    feature_map.load(filename, width, height, feature)
    feature_map.normalize()
    get_saliency_map(feature_map, fc, fd, radius, cell_size)
    feature_map.normalize()
    return feature_map


def run_multiprocess_test(filename, width, height, scale, radius, cell_size, save_as=None, status=False, mode='rgb'):
    print "STARTING: ", filename
    start = clock()
    p = mp.Pool()
    features = p.map(lambda f: thread_function(filename, width, height, f, radius, cell_size), mode)
    try:
        draw_multiple(features, 0, 0, scale, save_as, bw=True)
    except SystemExit:
        print "STATUS: ENDED IN", clock()-start
