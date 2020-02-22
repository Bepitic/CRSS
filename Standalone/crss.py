import time
import testxml as r

rsslist = r.getConfig('urls')

for rss_item in rsslist:
    publicDate = None
    dataItem = "link"
    if len(rss_item) > 3:
        publicDate = rss_item[3]
    if len(rss_item) > 4:
        publicDate = rss_item[4]

    r.dl(rss_item[0],rss_item[1])
    rss = r.parseRss(rss_item[1]+'.xml', rss_item[2], publicDate, dataItem)
    print(len(rss_item))

    if len(rss_item) < 4:
        rss_item.append( rss[0][2] )
    else:
        rss_item[3] = rss[0][2]


r.setConfig(rsslist,'urls')

#time.sleep(5)
