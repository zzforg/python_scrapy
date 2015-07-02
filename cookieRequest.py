import cookielib
import urllib2
 
#initiallise MozillaCookieJar
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#create request
req = urllib2.Request("http://www.baidu.com")
#use build_opener create an opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
