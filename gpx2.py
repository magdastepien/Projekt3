# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:38:38 2019

@author: Magda
"""

import gpxpy
import datetime as dt

def wczytaj_plik(filename):
    lat = []
    lon = []
    el = []
    dates = []
    with open (filename,'r') as gpx_file:
        gpx_dane=gpxpy.parse(gpx_file)
    for track in gpx_dane.tracks:
        for seg in track.segments:
            for point in seg.points:
                lon.append(point.longitude)
                lat.append(point.latitude)
                el.append(point.elevation)
                point.time = point.time.replace(tzinfo=None)
                dates.append(point.time)
    return lon, lat, el, dates
