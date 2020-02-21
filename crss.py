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
    config_file = open(filePath, "r", encoding="utf-8" )
    vlf_config  = config_file.readlines()
    for linea in vlf_config:
        print (linea)

