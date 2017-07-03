from urllib.request import Request,urlopen

url=Request("http://www.bbc.co.uk",headers={'User-Agent': 'Mozilla/5.0'})
f=urlopen(url)
print(f.readlines())