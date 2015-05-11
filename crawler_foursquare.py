import pyquery as pyquery
import urllib

"""
Utiliza a biblioteca urllib para ler todo o codigo de uma pagina html
"""
def parse_pagina_html(url):
	return urllib.urlopen(url).read()

"""
Passa para a biblioteca pyquery o codigo de uma pagina html.
Seleciona uma estrutura onde esta a informacao desejada. Ou seja, seguindo a hierarquia da pagina, eh o caminho do CSS.
Esse caminho pode ser visto pedindo para inspecionar o elemento desejado - no Chrome, opcao Copy CSS Path.

No caso abaixo: #container > div > div.contents > div.wideColumn > div.venueInfoSection > div.venueAttributes > div.venueAttributesData > div.leftColumn > div:nth-child(2) > div.attrValue > span > span
"""
def coleta_preco(url):
	pq = pyquery.PyQuery(parse_pagina_html(url))
	span = pq('div.contents div.wideColumn div.venueInfoSection div.venueAttributes div.venueAttributesData div.leftColumn div:nth-child(2) div.attrValue span span')
	custo = span.text()#.count('$')
	return custo

def main():
	url = "https://pt.foursquare.com/v/porc%C4%81o/4b703378f964a520590b2de3"
	#parse_pagina_html(url)#aqui o codigo de toda a pagina html
	print coleta_preco(url)

if __name__ == '__main__':
	main()