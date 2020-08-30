# 2019 Nov
# Author: Sherwin Massoudian

# Usage: Traffic.getTraffic()

# Output is seconds in traffic betweem 2 locations
# 410


import requests, json

class Traffic: 
    backupResponse = { "destination_addresses" : [ "San Marcos, TX, USA" ], "origin_addresses" : [ "Austin, TX, USA" ], "rows" : [ { "elements" : [ { "distance" : { "text" : "40 mi", "value" : 64373.8 }, "duration" : { "text" : "0 hours 45 mins", "value" : 2700 }, "status" : "OK" } ] } ], "status" : "OK" }
    # This method returns traffic time in seconds
    def getTraffic(self, source, destination):
        api_key = 'AIzaSyAyDDKXONfTxf1Cj4I-oB1b3bE4ZIictgE'
        url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        # Get travel time from payload
        payload = requests.get(url + 'origins = ' + source + '&destinations = ' + destination + '&key = ' + api_key)	
        response = payload.json()
        response = self.backupResponse
        rowArr = response['rows']
        rows = rowArr[0]
        elementArr = rows['elements']
        elements = elementArr[0]
        duration = elements['duration']
        currentTravelTime = duration['value'] 
        return currentTravelTime - self.getAvg()
    
	# This method returns the average traffic time
    def getAvg(self): 
        SanMarcos2Austin = 2420
        return SanMarcos2Austin
	
	# Prints the traffic time to file
	# def printTime(self):
        # Output to a text file
        # file = open("trafficTime.txt","w")
        # file.write(str(Austin.getTime()))
        # file.close()

# Sample usage
Austin = Traffic()
print ("Expected time in traffic:", Austin.getTraffic('Austin', 'Texas State University'),"seconds")
