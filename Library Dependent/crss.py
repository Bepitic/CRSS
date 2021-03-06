import io

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

print (getConfig("urls"))
