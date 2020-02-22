import xml
import time
import io
import urllib.request as dl

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

def getRss(rss_list):
    for l in rss_list:
        print(l[0])
        with dl.urlopen(l[0]) as l[0]:
            l[0] = l[0].read()
            ##l[0] = xml.etree.ElementTree.fromstring(l[0])
    ##print(rss_list[0][0])


getRss(getConfig('urls'))
time.sleep(5)
