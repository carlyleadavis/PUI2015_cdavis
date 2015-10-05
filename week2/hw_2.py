import json
import csv
import sys
from  urllib.request import urlopen

#for a static file of the B52 data run:
# curl http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=2d5f28e3-c82f-4034-a536-60f46cdb8b9a&VehicleMonitoringDetailLevel=calls&LineRef=B52 > homework.json
#at command line be able to input:
#python3 get_bus_info.py <mta_key> <bus_line> <bus_line.csv>
#MTA KEY: 2d5f28e3-c82f-4034-a536-60f46cdb8b9a

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_line = sys.argv[2]

    url = 'http://api.prod.obanyc.com/api/siri/vehiclemonitoring.json?key={0}&VehicleMonitoringDetailLevel=calls&LineRef={1}'.format(mta_key, bus_line)
    response = urlopen(url)
    str_response = response.readall().decode('utf-8')
    
    #error is coming in on the below line
    data = json.loads(str_response)

#       with open('homework.json') as data_file:
#       data = json.load(data_file)

#number of active buses on a bus line
    get = (len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))

    with open(sys.argv[3], 'w') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitutde', 'Longtitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)


        for bus in range(get):
            lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            #the next approaching stop for the bus, includes replacing error with Try/Except to see if there is a null value
            try:
                stopName = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            except (RuntimeError, TypeError, NameError, ValueError):
                stopName = 'NA'
            try:
                stopStatus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            except (RuntimeError, TypeError, NameError, ValueError):
                stopStatus = 'NA'
            writer.writerow([lat, long, stopName, stopStatus])

#            print("Bus: ", bus,", lat: ", lat,", long: ", long, ", stop name: ", stopName, ", stop status: ", stopStatus)
