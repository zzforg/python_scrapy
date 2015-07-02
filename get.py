import urllib2
import urllib

values={}
values['username'] = "zzforg@hotmail.com"
values['password'] = "surewinZ1"
data = urllib.urlencode(valuse)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
