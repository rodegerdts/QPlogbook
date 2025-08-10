import gpxpy
import gpxpy.gpx
import lxml


gpx = gpxpy.gpx.GPX()
gpx.name = 'Logbook export'
gpx.creator = 'QPlogbook'

gpx_route = gpxpy.gpx.GPXRoute()
gpx.routes.append(gpx_route)

def gpxexp(log):
    for entry in log:
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        gpx_wps.latitude = entry['point'].latitude
        gpx_wps.longitude = entry['point'].longitude
        gpx_wps.symbol = "xmred"