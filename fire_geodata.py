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
  {"name":"Greenwood Station 91","lat":39.6134433,"lon":-86.1040209},
  {"name":"St Paul Fire","lat":39.4282778,"lon":-85.6285885},
]
def get_stations() -> list:
  return [(i["lon"], i["lat"]) for i in stations]
