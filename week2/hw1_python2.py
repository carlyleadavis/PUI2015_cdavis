import json
import sys
from  urllib.request import urlopen

#for a static file of the B52 data run:
# curl http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=2d5f28e3-c82f-4034-a536-60f46cdb8b9a&VehicleMonitoringDetailLevel=calls&LineRef=B52 > homework.json
#at command line be able to input:
#python3 show_bus_locations.py <mta_key> <bus_line>
#MTA KEY: 2d5f28e3-c82f-4034-a536-60f46cdb8b9a

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_line = sys.argv[2]
    
    url = 'http://api.prod.obanyc.com/api/siri/vehiclemonitoring.json?key={0}&VehicleMonitoringDetailLevel=calls&LineRef={1}'.format(mta_key, bus_line)
    response = urlopen(url)
    str_response = response.readall().decode('utf-8')
    
    #error is coming in on the below line
    data = json.loads(str_response)

    print ('Bus Line : ', bus_line)

    get = (len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))

    print ('Number of Active Buses : ', get)

    for bus in range(get):
        lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus {0} is at latitude {1} and longtidue {2}".format(bus, lat, long))
        print("Bus ", bus," is at latitude ", lat," and longitude ", long)
