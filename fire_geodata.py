import pandas as pd

stations = pd.DataFrame([
  {"id":1,"name":"Fairland Station 621","lat":39.5844416,"lon":-85.8572277},
  {"id":2,"name":"Moral Township Station 681","lat":39.6387254,"lon":-85.9070139},
  {"id":3,"name":"Needham Station 81","lat":39.529953,"lon":-85.9709754},
  {"id":4,"name":"Marietta Station 671","lat":39.4406702,"lon":-85.8810707},
  {"id":5,"name":"Shelbyville Station 691","lat":39.5227097,"lon":-85.7786288},
  {"id":6,"name":"IFD Station 16","lat":39.6691316,"lon":-86.0065276},
  {"id":7,"name":"Needham Station 82","lat":39.6040567,"lon":-85.9990409},
  {"id":8,"name":"Fountaintown Station 612","lat":39.6937218,"lon":-85.779439},
  {"id":9,"name":"IFD Station 55","lat":39.6962247,"lon":-85.9795233},
  {"id":10,"name":"Morristown Station 651","lat":39.6760901,"lon":-85.7045637},
  {"id":11,"name":"Waldron Station 641","lat":39.4537326,"lon":-85.6662435},
  {"id":12,"name":"Flat Rock Station 631","lat":39.3641328,"lon":-85.8309059},
  {"id":13,"name":"Sugar Creek Township Station 45","lat":39.7338448,"lon":-85.9131422},
  {"id":14,"name":"Manilla Station 61","lat":39.5710743,"lon":-85.617652},
  {"id":15,"name":"Whiteland Station 71","lat":39.5484272,"lon":-86.0747433},
  {"id":16,"name":"Shelbyville Station 692","lat":39.51627,"lon":-85.7434899},
  {"id":17,"name":"Shelbyville Station 693","lat":39.5055857,"lon":-85.7945173},
  {"id":18,"name":"Franklin Station 23","lat":39.523629,"lon":-86.0737878},
  {"id":19,"name":"Greenwood Station 91","lat":39.6134433,"lon":-86.1040209},
  {"id":20,"name":"St Paul Station 41","lat":39.4282778,"lon":-85.6285885},
  {"id":21,"name":"Sugar Creek Township Station 42","lat":39.7762501,"lon":-85.896068},
  {"id":22,"name":"Greenwood Station 94","lat":39.625805791286666,"lon":-86.06305093068505},
  {"id":23,"name":"New Whiteland Station 11","lat":39.5577404582559,"lon":-86.09102800041359},
  {"id":24,"name":"Franklin Station 22","lat":39.482230271604614,"lon":-86.02353331575846},
])

apparatus = pd.DataFrame([
  {"id":1,"name":"73-Fairland-E621","station_id":1,"types":"engine"},
  {"id":2,"name":"73-Fairland-R621","station_id":1,"types":"engine,rescue"},
  {"id":3,"name":"73-Moral-E681","station_id":2,"types":"engine"},
  {"id":4,"name":"73-Moral-E682","station_id":2,"types":"engine"},
  {"id":5,"name":"73-Shelbyville-E691","station_id":5,"types":"engine"},
  {"id":6,"name":"73-Morristown-E651","station_id":10,"types":"engine"},
  {"id":7,"name":"73-Morristown-E652","station_id":10,"types":"engine"},
  {"id":8,"name":"73-Waldron-E641","station_id":11,"types":"engine"},
  {"id":9,"name":"30-Sugar Creek-E445","station_id":13,"types":"engine"},
  {"id":10,"name":"73-Shelbyville-E693","station_id":17,"types":"engine"},
  {"id":11,"name":"41-Franklin-E23","station_id":18,"types":"engine"},
  {"id":12,"name":"16-St. Paul-E841","station_id":20,"types":"engine"},
  {"id":13,"name":"30-Sugar Creek-E442","station_id":21,"types":"engine"},
  {"id":14,"name":"41-Needham-PT81","station_id":3,"types":"engine"},
  {"id":15,"name":"41-Needham-E82","station_id":7,"types":"engine"},
  {"id":16,"name":"73-Marietta-E671","station_id":4,"types":"engine"},
  {"id":17,"name":"49-IFD-E16","station_id":6,"types":"engine"},
  {"id":18,"name":"41-Whiteland-E71","station_id":15,"types":"engine"},
  {"id":19,"name":"41-Greenwood-E94","station_id":22,"types":"engine"},
  {"id":20,"name":"41-New Whiteland-E11","station_id":23,"types":"engine"},
  {"id":21,"name":"41-Franklin-E22","station_id":24,"types":"engine"},
  {"id":22,"name":"73-Shelbyville-L692","station_id":16,"types":"ladder,rescue"},
  {"id":23,"name":"41-Franklin-L23","station_id":18,"types":"ladder"},
  {"id":24,"name":"41-Greenwood-L91","station_id":19,"types":"ladder"},
  {"id":25,"name":"30-Sugar Creek-L445","station_id":13,"types":"ladder"},
  {"id":26,"name":"49-IFD-L55","station_id":9,"types":"ladder"},
])

tankers = pd.DataFrame([
  {"id":1,"name":"73-Fairland-T622","lat":39.5844416,"lon":-85.8572277},
  {"id":2,"name":"73-Fairland-T621","lat":39.5844416,"lon":-85.8572277},
  {"id":3,"name":"73-Moral-T681","lat":39.6387254,"lon":-85.9070139},
  {"id":4,"name":"41-Needham-PT81","lat":39.529953,"lon":-85.9709754},
  {"id":5,"name":"41-Needham-T82","lat":39.6040567,"lon":-85.9990409},
  {"id":6,"name":"73-Marietta-T671","lat":39.4406702,"lon":-85.8810707},
  {"id":7,"name":"41-Whiteland-T71","lat":39.5484272,"lon":-86.0747433},
  {"id":8,"name":"49-IFD-T16","lat":39.6691316,"lon":-86.0065276},
  {"id":9,"name":"73-Fountaintown-T612","lat":39.6937218,"lon":-85.779439},
  {"id":10,"name":"73-Fountaintown-T613","lat":39.6937218,"lon":-85.779439},
  {"id":11,"name":"49-IFD-T55","lat":39.6962247,"lon":-85.9795233},
  {"id":12,"name":"73-Morristown-T651","lat":39.6760901,"lon":-85.7045637},
  {"id":13,"name":"73-Morristown-T652","lat":39.6760901,"lon":-85.7045637},
  {"id":14,"name":"73-Waldron-T641","lat":39.4537326,"lon":-85.6662435},
  {"id":15,"name":"30-Sugar Creek-T442","lat":39.7762501,"lon":-85.896068},
  {"id":16,"name":"73-Flatrock-T631","lat":39.3641328,"lon":-85.8309059},
])

def get_station_locations():
  return list(zip(stations.lat, stations.lon))

def get_stations():
  return stations.drop(columns=['id'])

def get_engines():
  return apparatus[apparatus['types'].str.contains("engine")].join(stations.set_index('id'), on='station_id', lsuffix='_engine', rsuffix='_station')[['name_engine','lat','lon']].rename(columns={'name_engine':'name'})

def get_tankers():
  return tankers.drop(columns=['id'])

def get_ladders():
  return apparatus[apparatus['types'].str.contains("ladder")].join(stations.set_index('id'), on='station_id', lsuffix='_ladder', rsuffix='_station')[['name_ladder','lat','lon']].rename(columns={'name_ladder':'name'})

if __name__ == '__main__':
  print(get_engines())
  print(get_ladders())
