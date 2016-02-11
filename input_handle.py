from hash_code.warehouse import Warehouse


rows = 0
columns = 0
drone_num
drones = []
turns = 0
payload = 0
num_of_products = 0
product_weight = []
num_of_warehouses = 0
warehouses = []
num_of_customers = 0
customers = []


def opener(filename):
	with open(filename) as f:
		line = f.readline()
		line = line.strip().split()
		rows = int(line[0])
		columns = int(line[1])
		drone_num = int(line[2])
		turns = int(line[3])
		payload = int(line[4])
		num_of_products = int(f.readline().strip())
		product_weight = list(map(int, f.readline().strip().split()))
		num_of_warehouses = int(f.readline().strip())
		for i in range(num_of_warehouses):
			x, y = tuple(map(int, f.readline().strip().split()))
			products = list(map(int, f.readline().strip().split()))
			warehouses.append(Warehouse(x, y, products))
		num_of_customers = int(f.readline().strip())
		for i in range(num_of_customers):
			x, y = tuple(map(int, f.readline().strip().split()))
			num_of_items = int(f.readline().strip())
			items = list(map(int, f.readline().strip().split()))
			customers.append(Customer(x, y, num_of_items, item))