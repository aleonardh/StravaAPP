import gpxpy
import os

gpx_file = open('test_files/luintra.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
os.system("dir")