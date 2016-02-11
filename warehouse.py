from math import sqrt, ceil

class Warehouse():
    def __init__(self, x, y, products):
        this.x = x
        this.y = y
        this.products = products

class Customer():
    def __init__(self, x, y, product_num, items):
        this.x = x
        this.y = y
        this.product_num = product_num
        this.items = items

    def get_weight(self, item2weight)
        sum = 0
        for item in self.items:
            sum += item2weight[item]
        return sum


class Drone():
    def __init__(self, x, y, payload):
        this.x = x
        this.y = y
        this.current_payload = payload
        this.loaded_items = {}
        this.available = 0

    def load(self, items):
        for item in items:
            item = str(item)
            if this.loaded_items.has_key(item):
                this.loaded_items[item] +=1
            else:
                this.loaded_items.update("{}".format(item): 1)





def distance((x1, y1), (x2, y2)):
    diff_x = x1 - x2
    diff_y = y1 - y2
    euclidean_distance = sqrt(diff_x * diff_x + diff_y * diff_y)
    dis = ceil(euclidean_distance)
    return dis