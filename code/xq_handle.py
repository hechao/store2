#! /usr/bin/python
#-*- encoding: utf-8 -*-

import cookielib, urllib2
from bs4 import BeautifulSoup
from urllib2 import urlopen
import string

def xq_raw_data(sid, url_prefix):
    url = url_prefix+sid
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # default User-Agent ('Python-urllib/2.6') will *not* work
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
        ]
    #open homepage first to get cookie, and then open target URL again to get the target content
    home = opener.open('http://xueqiu.com')
    quote = opener.open(url)
    content = quote.read()
    return content

def xq_data_A(sid):
    url_prefix = "https://xueqiu.com/S/"
    # filter table td data from raw by soup
    rawdata = xq_raw_data(sid, url_prefix)
    soup = BeautifulSoup(rawdata, 'lxml')
    #toptable all td
    toptable = soup.find('table', class_="topTable")
    c_price = soup.find('strong',{"data-current":True})
    cu_price = c_price.text
    #table_body = toptable.find('tbody')
    #print type(toptable)
    td_list = toptable.find_all("td")
    sid_dict = {}
    #sid_dict['name'] = sid
    #print len(td_list)
    for i in range(len(td_list)):
        #print i
        head = td_list[i].find(text=True)
        head_num = td_list[i].find('span').text
        sid_dict[head] = head_num
    sid_dict['current_price'] = cu_price
    return sid_dict
    
def xq_data_A_filter(sdict):
    # 52KH, 52KL, current price, volumn, today_open
    e_data = {}
    e_data['52KH'] = sdict[u'52\u5468\u6700\u9ad8\uff1a'].encode()
    e_data['52KL'] = sdict[u'52\u5468\u6700\u4f4e\uff1a'].encode()
    e_data['current_price'] = sdict['current_price']
    e_data['volumn'] = sdict[u'\u8d44\u4ea7\u51c0\u503c\uff1a']
    e_data['jk'] = sdict[u'\u4eca\u5f00\uff1a'].encode()
    
    premium_tmp = sdict[u'\u6ea2\u4ef7\u7387\uff1a'].encode()
    #print premium_tmp
    if str(premium_tmp) == '-':
        e_data['premium'] = '0%'
        #print 'find -'
    else:
        e_data['premium'] = premium_tmp
    e_data['30avg'] = sdict[u'30\u65e5\u5747\u91cf\uff1a']
    return e_data

def xq_data_index_bond(sid):
    # Data get for index
    url_prefix = "https://xueqiu.com/S/"
    # filter table td data from raw by soup
    rawdata = xq_raw_data(sid, url_prefix)
    soup = BeautifulSoup(rawdata, 'lxml')
    #toptable all td
    toptable = soup.find_all('div', class_="wrapper")
    table = toptable[1].find_all('table')[0]
    td_list = table.find_all("td")
    #print td_list
    c_price = soup.find('strong',{"data-current":True})
    cu_price = c_price.text
    
    sid_dict = {}
    for i in range(len(td_list)):
        #print i
        head = td_list[i].find(text=True)
        
        if td_list[i].find('span') == None:
            #print "none find"
            sid_dict[head] = ''
        else: 
            head_num = td_list[i].find('span').text
            sid_dict[head] = head_num
    sid_dict['current_price'] = cu_price
    #print sid_dict
    return sid_dict
    
def xq_data_bond_filter(sdict):
    # english data and select data
    bond_data = {}
    bond_data['current_price'] = sdict['current_price']
    bond_data['full_price'] = sdict[u'\u5168\u4ef7(\u5143)\uff1a'].encode()
    return bond_data    

def xq_data_index_filter(sdict):
    # english data and select data
    e_data = {}
    e_data['52KH'] = sdict[u'52\u5468\u6700\u9ad8\uff1a'].encode()
    e_data['52KL'] = sdict[u'52\u5468\u6700\u4f4e\uff1a'].encode()
    e_data['current_price'] = sdict['current_price']
    if sdict.has_key(u'\u603b\u5e02\u503c\uff1a') :
        e_data['volumn'] = sdict[u'\u603b\u5e02\u503c\uff1a']
    else:
        e_data['volumn'] = ''
    if sdict.has_key(u'\u4eca\u5f00\uff1a') :
        e_data['jk'] = sdict[u'\u4eca\u5f00\uff1a'].encode()
    else:
        e_data['jk'] = ''
    e_data['premium'] = ''
    if sdict.has_key(u'30\u65e5\u5747\u91cf\uff1a') :
        e_data['30avg'] = sdict[u'30\u65e5\u5747\u91cf\uff1a']
    else:
        e_data['30avg'] = '0%'
    return e_data


    
    
if __name__ == "__main__":
    
    #bond
    sid_bond = "SH124161" # 13瑞水泥 bond
    #sid_dict_bond = xq_data_index_bond(sid_bond)
    #print xq_data_bond_filter(sid_dict_bond)
    
    
    #A
    sid_A = "SZ164105" # 华富强债 A
    sid_dict = xq_data_A(sid_A)
    print xq_data_A_filter(sid_dict)
    
    #index
    sid_index = "SZ399001" # 深圳成指 index
    #sid_dict_index = xq_data_index(sid_index)
    #print xq_data_index_filter(sid_dict_index)
    
    
    