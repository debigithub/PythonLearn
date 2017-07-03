from urllib.request import Request,urlopen

url=Request("http://www.bbc.co.uk",headers={'User-Agent': 'Mozilla/5.0'})
f=urlopen(url)
writer=open('datadump.txt','w')
writer.write(str(f.readlines()))
writer.close()