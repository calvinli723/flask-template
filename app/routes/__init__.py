from werkzeug.urls import url_parse

def is_safe_url(url_string):
    return url_parse(url_string).netloc == ""