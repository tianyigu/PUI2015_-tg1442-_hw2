# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:37:30 2015

@author: tianyigu
"""
import json
import sys
import csv
import urllib2
    
if __name__=='__main__': 
    #key = 'b59dc318-ccb0-41e0-b02c-3f6f46977018'
    #bus = 'M42'

    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    #url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key,bus)
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    busline = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    
with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
        
        for i in busline:
            Latitude  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude  = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopName = 'N/A'
                StopStatus = 'N/A'
            else:
                StopName = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StopStatus = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            writer.writerow([Latitude,Longitude,StopName,StopStatus])
