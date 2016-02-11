from math import sqrt, ceil

class Warehouse():
    def __init__(x, y, products):
        this.x = x
        this.y = y
        this.products = products

def distance((x1, y1), (x2, y2)):
    diff_x = x1 - x2
    diff_y = y1 - y2
    euclidean_distance = sqrt(diff_x * diff_x + diff_y * diff_y)
    dis = ceil(euclidean_distance)
    return dis

