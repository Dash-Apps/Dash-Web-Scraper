import re
def is_subpath(url,new_url):
    og_routes = url.split("/")
    new_routes = new_url.split("/")
    get_ids = re.search("#.*",new_url)
    print(get_ids)
    print(get_ids.span())
    match = get_ids.group()
    new_url = new_url.replace(match,"")
    print(new_url)
    if url == new_url:
        return True
    else:
        return False
