import re
from collections import Counter
reader=open('datadump.txt','r')
writer=open('datadump_cleansed.txt','w')
Source='BBC.CO.UK'
Today='2017-07-04'
for x in reader.readlines():
    c=Counter(re.findall('[a-zA-Z0-9]+', x))
    for k,v in c.items():
        #print('word %s repeated %s times' % (k,v))
        if len(k) > 1:
            print('%s,%s,%s,%s' % (Today,Source,k,v))
            print('\n')
 #   writer.write(x)
  #  writer.write(' ')






