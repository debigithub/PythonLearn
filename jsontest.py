import json

json_string = '{"first_name": "Guido", "last_name":"Rossum","first_name": "Debi"}'

f=open('Outchunk0.txt','r')

dl = json.loads(f.read())


Json_level=0
global Json_level
def get_keys(dl,Json_level):
    #global Json_level
    if isinstance(dl,dict):
        for k,v in dl.iteritems():
            print  k
            print Json_level
            if isinstance(v,dict):
                get_keys(v,Json_level+1)

            elif isinstance(v,list):
                for str in v:
                    #print Json_level
                    get_keys(str,Json_level+1)



get_keys(dl,0)
