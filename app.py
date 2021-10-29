import fn

#url="http://192.168.1.1/ports.jsn"
url='https://pokeapi.co/api/v2/pokemon/ditto'
parametro='weight'

dato=fn.get_data(url,parametro)
fn.printIt(dato)