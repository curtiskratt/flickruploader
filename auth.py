#!/usr/bin/env python

import flickrapi

api_key = os.environ['api_key']
api_secret = os.environ['api_secret']

flickr = flickrapi.FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms='write')
