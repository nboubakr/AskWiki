#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
import re


class AskWiki:
    """
    AskWiki is a python package for querying wikipedia in any language from your python application.

    Example usage:

    >>> from AskWiki import AskWiki
    >>> wiki = AskWiki('en')
    >>> wiki_info = wiki.ask('wikipedia')
    >>> wiki_info[1070:1260]
    u'Wikipedia (i/\u02ccw\u026ak\u0268\u02c8pi\u02d0di\u0259/ or i/\u02ccw\u026aki\u02c8pi\u02d0di\u0259/ WIK-i-PEE-dee-\u0259) is a collaboratively edited, multilingual, free Internet encyclopedia that is supported by the non-profit Wikimedia Foundation.'
    """

    def __init__(self, lang='en'):
        self.language = lang

    def ask(self, query):
        request_url = "http://" + self.language + ".wikipedia.org/w/api.php?action=parse&page=" + query + "&format=json&prop=text&section=0&redirects"

        text = urllib.urlopen(request_url).read()
        text = re.sub("<[^<]+?>", '', text)    # Strip tags
        text = re.sub("(?m)^\s+", '', text)    # Strip whitespace
        text = re.sub("&#[0-9]+;", '', text)   # Strip encoded
        text = re.sub("\[[0-9]+\]", '', text)  # Strip referencing

        result = json.loads(text)['parse']['text']['*']
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
