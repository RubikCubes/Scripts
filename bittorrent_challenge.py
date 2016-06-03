from Queue import Queue

def paths():
  diction = {}
  q = Queue()
  starting_point = (0,0)
  q.put(starting_point)
  while not q.empty():
    point = q.get()
    x_node = point[0]
    y_node = point[1]
    routes = [(x_node+1,y_node), (x_node-1,y_node), (x_node,y_node+1), (x_node,y_node-1)]
    for route in routes:
      if sum_coordinates(route) <=19:
        if diction.has_key(route):
          pass
        else:
          diction[route] = True
          q.put(route)
  return len(diction)

def sum_coordinates(coordinates):
  count = 0
  for num in coordinates:
    x = int(math.fabs(num))
    count = count + sum_coordinate(x)
  return count
    
def sum_coordinate(num):
    count = 0
    abs_number = num
    if abs_number >= 10:
      remainder = abs_number % 10
      number_1 = abs_number / 10
      count = remainder + sum_coordinate(number_1)
      return count
    else:
      return num
    


