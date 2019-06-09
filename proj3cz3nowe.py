# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:49:21 2019

@author: Magda
"""

from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout  
from kivy.properties import ObjectProperty  
from kivy.garden.mapview import MapMarker, MarkerMapLayer

import matplotlib.pyplot as plt
import gpx2

class TestForm(BoxLayout):
    my_map=ObjectProperty()
    
    def analyse_file(self):
        filename='2.gpx'
        lon,lat,el,dates = gpx2.wczytaj_plik(filename)
        self.draw_route(lon,lat)
        
    def draw_route(self,lon,lat):
        data_layer = MarkerMapLayer()
        self.my_map.add_layer(data_layer)
        for point in zip(lat,lon):
            self.mark_point(*point, layer=data_layer)
            
    def mark_point(self, lat, lon,layer=None):
        if lat != None and lon != None:
            marker= MapMarker(lat=lat, lon=lon)
            self.my_map.add_marker(marker=marker, layer=layer)
    
class MapViewApp(App):
    def build(self):
        return TestForm()

if __name__ == '__main__':
    MapViewApp().run()
