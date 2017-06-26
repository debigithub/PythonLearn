import re
f=open('Baahubali.txt','r')
final_list=list()
for line in f.readlines():
    a=re.findall('Prabhas',line)
    final_list=final_list+a
    print line

print len(final_list)
f.close()
