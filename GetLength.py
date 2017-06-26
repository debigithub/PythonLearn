def getLength(element):

    count = 0
    if isinstance(element,list):
        for i in element:
            print (i)
            c=getLength(i)
            count+=c
        return count
    else:
        return 1