import time
import testxml as r

rsslist = r.getConfig('urls')

for rss_item in rsslist:
    r.dl(rss_item[0],rss_item[1])

time.sleep(5)
