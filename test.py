#!/usr/bin/env python

import flickrapi

#print "test"

api_key = os.environ['api_key']
api_secret = os.environ['api_secret']


flickr = flickrapi.FlickrAPI(api_key, api_secret)
photos = flickr.photos.search(user_id='145863987@N04', per_page='10')
sets = flickr.photosets.getList(user_id='145863987@N04')

print sets


