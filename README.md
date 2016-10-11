#H3c portal login and logout scripts
These scripts are for loging and logout of H3c routers with portal certification.
* Put the three file in the same directory.
* change the HTTPConnection ip in the files to you ip
* change the request(...,'/portal/pws?li',...) to your url
* run python3 NsINodelogin.py to login and python3 NsINodeLogout.py to logout.
* you can also change these code to python2 codes, use urllib2 and urllib instead of http.client
