#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import json

# need: pip install httplib2
import httplib2

class Rest(object):
    uri = ""

    def __init__(self, uri):
        self.uri = uri

    def request(self, uri = "", body = {} ):
        hcQuery = httplib2.Http(".cache")
        response, content = hcQuery.request(uri, "POST", json.dumps(body) )
        self.is_ok(response)
        diContent =  self.deserialize(content)
        return(diContent)
        
    def deserialize(self, content):
        return json.loads(content)

    def is_ok(self, reResponse, f_exit = True):
        if reResponse.status == 200:
            return True
        return False

def api_add(val1, val2):
    Re = Rest("")
    liRes = Re.request("http://www.hogetan.net/add/add",
                       {"val1": val1, "val2": val2} )
    return(int(liRes["res"]))


if __name__ == "__main__":
    print(api_add(1,2) )
    print(api_add(1,3) )
