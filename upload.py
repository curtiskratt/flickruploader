#!/usr/bin/env python

import flickrapi
import os
import requests

api_key = os.environ.get['api_key']
api_secret = os.environ.get['api_secret']
dirname = '/home/pi/Pictures/pibooth/'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='etree')

#results = flickr.upload('image.jpg')


for filename in os.listdir(dirname):
	if filename.endswith(".jpg"):
		upload = flickr.upload(os.path.join(dirname,filename))
