import re
line='who misra abc mish12ra misdfsdfsdra'
m=re.findall('mi[a-z]*[\d]*ra',line)
print (m)