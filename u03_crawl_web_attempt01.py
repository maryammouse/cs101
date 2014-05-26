def get_all_links(page):
        links = []
        while True:
            url, endpos = get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break



def union(list01, list02):
    for element in list02:
        if element not in list01:
            list01.append(element)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    i = 0
    while tocrawl != []:  # this means it will run until the list tocrawl is empty
        current_page = tocrawl[i]  # marks the page in the front of the queue (position 0 in the list)to be crawled
        page_links = get_all_links(current_page)  # crawls the page for links
        tocrawl = union(tocrawl, page_links)  # updates list tocrawl with new links, ignoring duplicates already in tocrawl
        crawled = crawled.append(tocrawl.pop(i))  # updates crawled with the page that was just crawled
