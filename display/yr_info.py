
import os
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
#from aifc import data


class YrParser(HTMLParser):
    
    
    def init(self):
        self._in_table = 0
        self._in_today_body = False
        self._weather_col_index = 0
        self._today = False
        self._weather_info = [] #list of tuples, where 0:timestring, 1:temperature, 2:url to precip graphic
        self._current_time = ""
        self._current_temp = ""
        self._current_pic_url = ""
         
    def get_weather_info(self):
        
        return self._weather_info
        
    
    def handle_starttag(self, tag, attrs):
        
        if tag == "table":
            self._in_table += 1
        
        if tag == "tbody" and self._today:
            self._in_today_body = True
            
        if tag == "tr" and self._in_today_body:
            self._weather_col_index = 0
            self._current_tuple = ()
        
        if tag == "td" and self._in_today_body:
            self._weather_col_index += 1
            if self._weather_col_index == 3:
                if attrs[0][1].count("plus"):
                    self._current_temp = "+"
                else:
                    self._current_temp = ""
        
        if tag == "img" and self._weather_col_index == 2:
            for attr in attrs:
                if attr[0] == "src":
                    self._current_pic_url = attr[1] 
                
    def handle_endtag(self, tag):
        
        if tag == "table":
            self._in_table -= 1
            if self._today:
                self._today = False
        if tag == "tr":
            if self._in_today_body:
                self._weather_info.append([self._current_time, self._current_temp, self._current_pic_url])
        if tag == "tbody":
            self._in_today_body = False
        
    def handle_data(self, data):
        
        if self._in_today_body:
            if self._weather_col_index == 1:
                if data.strip():
                    self._current_time = data
            elif self._weather_col_index == 3:
                if data.strip():
                    self._current_temp += data
        elif self._in_table and (data.count("Today,") or data.count("Tomorrow,")):
            self._today = True

    
    def handle_comment(self, data):
        pass
    
#     def handle_entityref(self, name):
#         c = unichr(name2codepoint[name])
#         print "Named ent:", c
#     
#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = unichr(int(name[1:], 16))
#         else:
#             c = unichr(int(name))
#         print "Num ent  :", c
#     def handle_decl(self, data):
#         print "Decl     :", data

class YrWeatherFetcher(object):
    
    def __init__(self):
        
        self._parser = YrParser()
        self._parser.init()
        pass
    
    def open(self, url):
        
        opener = urllib2.urlopen(url)
        self._parser.feed(opener.read())
        
    def get_result(self, cache_dir):
        
        result = self._parser.get_weather_info()
        for i in range(len(result)):
            opener = urllib2.urlopen(result[i][2])
            target_path = os.path.join(cache_dir, os.path.basename(result[i][2]))
            with open(target_path, "w") as _f:
                _f.write(opener.read())
            result[i][2] = target_path
        return result[:4]
         
if __name__ == '''__main__''':
    ywf = YrWeatherFetcher()
    ywf.open("http://www.yr.no/place/Norway/Buskerud/Kongsberg/Kongsberg/")
    for el in  ywf.get_result():
        for l in el:
            print l
