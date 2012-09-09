#/usr/bin/python
#coding=utf-8


import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import urllib
import urllib2
import json

def dwz(website):
    def post(url,data):
        request = urllib2.Request(url)
        data = urllib.urlencode(data)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(request,data)
        return response.read()
    url = "http://dwz.cn/create.php"
    data = {'url' : str(website)}
    result = json.loads(post(url,data))['tinyurl']
    return result

def search(request):
    error = False
    search = False
    if 'wd' in request.GET:
        keyword = request.GET['wd']
        if not keyword:
            error = True
        else:
            a = 'http://127.0.0.1:8000/visited/'
            b = urllib.urlencode({'wd':keyword})
            url = ''.join([a,b])
            tinyurl = dwz(url)
            search = True
            return render_to_response('search_form.html',{'keyword':keyword,'tinyurl':tinyurl,'search':search})
    return render_to_response('search_form.html',{'error':error})

def visited(request):
    text = str(request.path[12:])
    redirect = ''.join(['http://www.baidu.com/s?wd=',text])
    return render_to_response('visited.html',{'text':text,'redirect':redirect})     
