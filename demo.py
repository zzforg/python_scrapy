import urllib2

request = urllib2.Request("https://esoe.qut.edu.au/qut-login/")
response = urllib2.urlopen(request)
print response.read()
