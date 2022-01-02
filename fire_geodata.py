stations = [
  {"name":"Fairland Station 621","lat":39.5844416,"lon":-85.8572277},
  {"name":"Moral Township Station 681","lat":39.6387254,"lon":-85.9070139},
  {"name":"Needham Station 81","lat":39.529953,"lon":-85.9709754},
  {"name":"Marietta Station 671","lat":39.4406702,"lon":-85.8810707},
  {"name":"Shelbyville Station 691","lat":39.5227097,"lon":-85.7786288},
  {"name":"IFD Station 16","lat":39.6691316,"lon":-86.0065276},
  {"name":"Needham Station 82","lat":39.6040567,"lon":-85.9990409},
  {"name":"Whiteland Station 71","lat":39.5484272,"lon":-86.0747433},
  {"name":"Fountaintown Station 612","lat":39.6937218,"lon":-85.779439},
  {"name":"IFD Station 55","lat":39.6962247,"lon":-85.9795233},
  {"name":"Morristown Station 651","lat":39.6760901,"lon":-85.7045637},
  {"name":"Waldron Station 641","lat":39.4537326,"lon":-85.6662435},
  {"name":"Flat Rock Station 631","lat":39.3641328,"lon":-85.8309059},
  {"name":"Sugar Creek Township Station 45","lat":39.7338448,"lon":-85.9131422},
  {"name":"Manilla Station 61","lat":39.5710743,"lon":-85.617652},
  {"name":"Shelbyville Station 692","lat":39.51627,"lon":-85.7434899},
  {"name":"Shelbyville Station 693","lat":39.5055857,"lon":-85.7945173},
  {"name":"Franklin Station 23","lat":39.523629,"lon":-86.0737878},
  {"name":"St Paul Station 41","lat":39.4282778,"lon":-85.6285885},
  {"name":"Sugar Creek Township Station 42","lat":39.7762501,"lon":-85.896068},
  {"name":"Greenwood Station 91","lat":39.6134433,"lon":-86.1040209},
]

engines = [
  {"name":"73-Fairland-E621","lat":39.5844416,"lon":-85.8572277},
  {"name":"73-Fairland-R621","lat":39.5844416,"lon":-85.8572277},
  {"name":"73-Moral-E681","lat":39.6387254,"lon":-85.9070139},
  {"name":"73-Moral-E682","lat":39.6387254,"lon":-85.9070139},
  {"name":"73-Shelbyville-E691","lat":39.5227097,"lon":-85.7786288},
  {"name":"73-Morristown-E651","lat":39.6760901,"lon":-85.7045637},
  {"name":"73-Morristown-E652","lat":39.6760901,"lon":-85.7045637},
  {"name":"73-Waldron-E641","lat":39.4537326,"lon":-85.6662435},
  {"name":"30-Sugar Creek-E445","lat":39.7338448,"lon":-85.9131422},
  {"name":"73-Shelbyville-E693","lat":39.5055857,"lon":-85.7945173},
  {"name":"41-Franklin-E23","lat":39.523629,"lon":-86.0737878},
  {"name":"16-St. Paul-E841","lat":39.4282778,"lon":-85.6285885},
  {"name":"30-Sugar Creek-E442","lat":39.7762501,"lon":-85.896068},
]

tankers = [
  {"name":"73-Fairland-T622","lat":39.5844416,"lon":-85.8572277},
  {"name":"73-Fairland-T621","lat":39.5844416,"lon":-85.8572277},
  {"name":"73-Moral-T681","lat":39.6387254,"lon":-85.9070139},
  {"name":"41-Needham-PT81","lat":39.529953,"lon":-85.9709754},
  {"name":"41-Needham-T82","lat":39.6040567,"lon":-85.9990409},
  {"name":"73-Marietta-T671","lat":39.4406702,"lon":-85.8810707},
  {"name":"41-Whiteland-T71","lat":39.5484272,"lon":-86.0747433},
  {"name":"49-IFD-T16","lat":39.6691316,"lon":-86.0065276},
  {"name":"73-Fountaintown-T612","lat":39.6937218,"lon":-85.779439},
  {"name":"73-Fountaintown-T613","lat":39.6937218,"lon":-85.779439},
  {"name":"49-IFD-T55","lat":39.6962247,"lon":-85.9795233},
  {"name":"73-Morristown-T651","lat":39.6760901,"lon":-85.7045637},
  {"name":"73-Morristown-T652","lat":39.6760901,"lon":-85.7045637},
  {"name":"73-Waldron-T641","lat":39.4537326,"lon":-85.6662435},
  {"name":"30-Sugar Creek-T442","lat":39.7762501,"lon":-85.896068},
  {"name":"73-Flatrock-T631","lat":39.3641328,"lon":-85.8309059},
]

def get_station_locations():
  return [(i["lon"], i["lat"]) for i in stations]

def get_stations():
  return stations

def get_engines():
  return engines

def get_tankers():
  return tankers
