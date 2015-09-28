# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import urllib2
import sys

if __name__ =='__main__':
    #key = 'b59dc318-ccb0-41e0-b02c-3f6f46977018'
    #bus = 'M42'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.load(request)

    busline = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
   
    
    
    print "Bus Line: %s" % (sys.argv[2])
    print "Number of Active Buses: %s" %(len(busline))
    
    num = 0
    for i in busline:
         Latitude  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
         Longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
         print "Bus %s is at latitude %s and longitude %s" % (num, Latitude, Longitude)
         
         num +=1
         
