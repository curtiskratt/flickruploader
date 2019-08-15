#!/usr/bin/env python

import flickrapi
import configcit

flickr = flickrapi.FlickrAPI(configcit.API_KEY, configcit.API_SECRET)
flickr.authenticate_via_browser(perms='write')
