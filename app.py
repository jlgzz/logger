import fn

#url='https://pokeapi.co/api/v2/pokemon/ditto'
# #key='weight'

url="http://192.168.1.1/ports.jsn"
key='interface'
key2='version'

periodo= 1.0

"""Se obtine el archivo json"""
[dato,status]=fn.get_data(url,key,key2)

fn.printIt(dato,status,periodo)