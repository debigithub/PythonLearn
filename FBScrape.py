import json
import urllib2

App_token="1573287812904607|7NurWwCnclV8aH-LGZHaDvXhGO8"
Page_Id="TimesofIndia"
base = "https://graph.facebook.com/v2.9"
node = "/" + Page_Id + "/feed"
parameters = "/?access_token=%s" % App_token
url = base + node + parameters
#print url
# retrieve data
req = urllib2.Request(url)
i=0
while i<=100:
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    #print json.dumps(data, indent=4, sort_keys=True)
    file_name='Outchunk' + str(i) + '.txt'
    f=open(file_name,'w')
    f.write(json.dumps(data, indent=4, sort_keys=True))
    i=i+1