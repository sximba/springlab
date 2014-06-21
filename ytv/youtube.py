import mechanize as me
from bs4 import BeautifulSoup as bs

def text_with_newlines(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += '\n'
    return text

def get_ytid(_url):
    ytid_len = 11
    
    id_start = _url.find('?v=')
    
    if id_start == -1:
        id_start = _url.find('&v=')
    
    if id_start == -1:
        return None
    
    id_start += 3
    ytid = _url[id_start:id_start + ytid_len]
    return ytid

yturl = "http://www.youtube.com/watch?v=QpkHt1hDYTo&list=WL6DF303C9A056101C"

def get_details(yturl):
    mech = me.Browser()
    mech.set_handle_robots(False)
    mech.set_handle_refresh(False)
    mech.set_handle_gzip(True)
    
    try:
        response = mech.open(yturl)
        if response.code == 200:
            content = response.read()
            tb = bs(content)

            description_tag = tb.find(attrs={"id":"eow-description"})
            if description_tag:
                description = text_with_newlines(description_tag)
                #description = unicode(description_tag.string)
            else:
                description = None

            title_tag = tb.find(attrs={"id":"eow-title"})
            if title_tag:
                title = title_tag.get('title')
            else:
                title = None

            ytid = get_ytid(yturl)
            
            # Maybe not the best way?
            return [ytid, title, description]
        else:
            return None
    except Exception as e:
        # Video does not exist or some connections error
        # do not re-raise exception
        return None
