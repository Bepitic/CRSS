import io
import re
import xml.etree.ElementTree as ET
import urllib.request as http

def parseRss(pathRss, regularexpresion, pd=None, dataItem="link"):
    """Get a RSS_file and exports list[title,link,pubdate]

    :pathRss: TODO
    :regularexpresion: TODO
    :pd: TODO
    :dataItem: TODO
    :returns: TODO

    """
    tree = ET.parse(pathRss)
    items = tree.findall("*/item")
    elementos_rss = []
    for item in items:
        e_title = item.find("title")
        if ( re.search( regularexpresion, e_title.text ) ):
            elemento = []
            elemento.append(e_title.text)
            elemento.append(item.find("link").text)
            elemento.append(item.find("pubDate").text)
            elementos_rss.append(elemento)

def getConfig(filePath):
    """
    Get the config file and parses it into a vector of tuples:
    each line 1 vector.
    [ http rss link ] [ Alias ] [wildcard]
    www.rss1.com/feed/rss "alias of rss1" "*car*"

    :filePath: Path to the config file
    :returns: vector of tuples with rss config parsed

    """
    rss_list = []
    config_file = open(filePath, "r", encoding="utf-8" )

    for linea in config_file:
        l=[]

        for item in linea.split('|'):
            l.append(item.strip())

        rss_list.append(l)

    return rss_list

def dl(rss_list,file_string):
        with http.urlopen(rss_list) as html_dl:
            html_dl = html_dl.read()
            f_xml = open(file_string+'.xml',"wb")
            f_xml.write(html_dl)
            f_xml.close()



            ##l[0] = xml.etree.ElementTree.fromstring(l[0])
    ##print(rss_list[0][0])
