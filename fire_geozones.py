from math import sqrt
import fire_geodata as gd
from visualize_voronoi import visualize

def main() -> None:
  engines = gd.get_engines()
  
  sample_point = (-85.86555, 39.58414)
  
  response_order = coverage_list(sample_point, engines)
  
  for engine in response_order:
    print(engine)
  
  visualize(engines)

def get_distance(a: tuple, b: tuple) -> float:
  inside = 0
  for i in range(len(a)):
    x = a[i]
    y = b[i]
    d = x - y
    d2 = d ** 2
    inside += d2
  distance = sqrt(inside)
  return distance

def coverage_list(location: tuple, apparati: list) -> list:
  apparatus_locations = []
  apparatus_names = []
  for apparatus in apparati:
    coordinates = (apparatus['lon'], apparatus['lat'])
    apparatus_locations.append(coordinates)
    apparatus_names.append(apparatus['name'])
  
  response_order = []
  
  distances = []
  for apparatus in apparatus_locations:
    distance = get_distance(location, apparatus)
    distances.append(distance)

  while len(distances) > 0:
    closest_location = min(distances)
    closest_index = distances.index(closest_location)
    response_order.append(apparatus_names.pop(closest_index))
    distances.pop(closest_index)
  
  return response_order

if __name__ == '__main__':
  main()