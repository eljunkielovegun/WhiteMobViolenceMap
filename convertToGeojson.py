
import json

f = open("WhiteMobViolence.json")
data = json.load(f)

title = []
location = []
date = []
fatalities = []
refugees = []
narrative = []
source = []
lat = []
lon = []

for i in range(len(data)):
    title.append(data[i]['Name'])
    location.append(data[i]['Location'])
    date.append(data[i]['Date'])
    fatalities.append(data[i]['Fatalities'])
    refugees.append(data[i]['Refugees'])
    narrative.append(data[i]['Narrative'])
    source.append(data[i]['Source'])
    lat.append(data[i]['Lat'])
    lon.append(data[i]['Long'])

# print(narrative)

file = open("WhiteMobViolence.geojson", "w")
file.write("{ " + "\"" + "type" + "\""  +": " + "\"" + "FeatureCollection" + "\"" + "," + "\n")
file.write("\"" + "features" + "\""  +": " + "[" + "\n")
for i in range(len(data)):
    file.write("\t" + "{" + "\"" + "type" + "\""+ ": " + "\"" + "Feature"+ "\"" +"," +"\n")
    file.write("\t"+ "\"" +"geometry" + "\"" + ": " + "{" + "\""+"type"+ "\""+": "+"\""+ "Point" + "\""+","  "\n")
    file.write("\t"+ "\t"+ "\"" +"coordinates" + "\"" + ": " + "[" + str(lon[i]) + "," + str(lat[i]) + "]" +"\n")
    file.write("\t"+ "\t"+  "}" +","+  "\n" )
    file.write("\t"+ "\"" +"properties" + "\"" + ": " + "{" + "\n" )
    file.write("\t"+ "\t"+ "\"" +"title" + "\"" + ": " + "\"" + str(title[i]).replace("\"", " ") + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"location" + "\"" + ": " + "\"" + str(location[i]) + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"date" + "\"" + ": " + "\"" + str(date[i]) + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"fatalities" + "\"" + ": " + "\"" + str(fatalities[i]) + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"refugees" + "\"" + ": " + "\"" + str(refugees[i]) + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"narrative" + "\"" + ": " + "\"" + str(narrative[i]).replace("\"", "'").replace("\n", " ") + "\"" + "," "\n" )
    file.write("\t"+ "\t"+ "\"" +"source" + "\"" + ": " + "\"" + str(source[i]) + "\"" +  "\n" )
    file.write("\t"+ "\t"+  "}" +  "\n" )
    file.write("\t"+  "}" +  "," + "\n" )
else:
    file.write("\t"+  "]" +  "\n" )
    file.write("\t"+  "}" +  "\n")  

    # file.write("\t"+"subjects" + " : " +str(subjects)+","+"\n")

f.close

# def convert_json(items):
#     import json
#     return json.dumps({ "type": "FeatureCollection",
#                         "features": [ 
#                                         {"type": "Feature",
#                                          "geometry": { "type": "Point",
#                                                        "coordinates": [ feature['Long'],
#                                                                         feature['Lat']]},
#                                          "properties": { key: value 
#                                                          for key, value in feature.items()
#                                                          if key not in ('Lat', 'Long') }
#                                          } 
#                                      for feature in json.loads(items)
#                                     ]
#                        })

# convert_json(f)