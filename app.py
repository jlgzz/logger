import fn

#url="http://192.168.1.1/ports.jsn"
url='https://pokeapi.co/api/v2/pokemon/ditto'
key='weight'

"""Se obtine el archivo json"""
[dato,status]=fn.get_data(url,key)

fn.printIt(dato,status)