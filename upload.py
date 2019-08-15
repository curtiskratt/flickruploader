#!/usr/bin/env python

import flickrapi
import os
import requests
import configcit
import shutil


dirname = '/home/pi/Pictures/pibooth/'
uploadDst = '/home/pi/Pictures/pibooth/uploaded/'

flickr = flickrapi.FlickrAPI(configcit.API_KEY, configcit.API_SECRET, format='etree')

for filename in os.listdir(dirname):
	if filename.endswith(".jpg"):
		filepath = os.path.join(dirname,filename)
		
		upload = flickr.upload(filepath)
		if upload.attrib['stat'] == 'ok':
			print 'upload of ' + filename + ' was successful'
			shutil.move(filepath,uploadDst)
