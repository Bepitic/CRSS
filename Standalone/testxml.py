import io
import re
import xml.etree.ElementTree as ET
import urllib.request as dl


tree = ET.parse("xml.txt")
items = tree.findall("*/item")
elementos_rss = []
for item in items:
    e_title = item.find("title")
    if ( re.search( "manual intervention", e_title.text ) ):
        elemento = []
        elemento.append(e_title.text)
        elemento.append(item.find("link").text)
        elemento.append(item.find("pubDate").text)
        elementos_rss.append(elemento)

print(elementos_rss[1])



