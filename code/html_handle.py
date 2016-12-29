# -*- coding: utf-8 -*- 
from html import HTML

from csv_handle import csv_readlist


def html(html_body):
    html_header ="""
    <!DOCTYPE html>
    <html>
    <head>
    <title>This is my stock manager!</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    </head>
    <body>
    %s
    </body>
    </html>""" % (html_body)
    return html_header

def h_content(desc, t1, t2):
    layout = """
    <div class="container">
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	
        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>

        <div class="row clearfix">
    		<div class="col-md-12 column">
    		%s
    		</div>
    	</div>
    	

	</div>
    """ % (desc, t1, t2)
    
    return layout


def page_desciption():
    page_desc = HTML()
    page_desc.h2("Welcome!")
    l = page_desc.ol
    l.li('This is the store of all my stocks! thanks for visiting!')

    return str(page_desc)

def table_index(data, title, tdesc):
    dtable = HTML()
    dtable.h3(title)
    
    desc = []
    if tdesc !="":
        desc = tdesc.split("/")
    l = dtable.ol
    for k in desc:
        l.li(k)

    t = dtable.table(border='2px', width ='60%', klass ='table table-bordered')
    t.th('SID')
    t.th('名称')
    t.th('52W区间')
    t.th('52W最高 / 2015-2016')
    t.th('52W最低 / 2015-2016')
    t.th('价格')
    t.th('90日均价')
    t.th('均价比较')
    t.th('市值')
    t.th('30日均量')

    
    for i in data:
        #print i
        r = t.tr
        r.td(str(i['SID']))
        r.td(str(i['cname']))
        r.td(str(i['range'])+"%" + " | " + str(i['hist_range'])+"%")
        r.td(str(i['52KH']) + " | " + str(i['hist_H']))
        r.td(str(i['52KL']) + " | " + str(i['hist_L']))
        r.td(str(i['current_price']))
        r.td(str(i['90_avg']))
        r.td(str(i['avg_compr']))
        r.td(str(i['volumn']))
        r.td(str(i['30avg']))
    return str(dtable)
    
def table(data, title, tdesc):
    dtable = HTML()
    dtable.h3(title)
    
    desc = []
    if tdesc !="":
        desc = tdesc.split("/")
    l = dtable.ol
    for k in desc:
        l.li(k)

    t = dtable.table(border='2px', width ='60%', klass ='table table-bordered')
    t.th('SID')
    t.th('名称')
    t.th('52W区间')
    t.th('52W最高')
    t.th('52W最低')
    t.th('价格')
    t.th('市值')
    t.th('30日均量(总市值)')
    t.th('折溢价')
    t.th('组别')
    t.th('X?')
    
    for i in data:
        #print i
        r = t.tr
        r.td(str(i['SID']))
        r.td(str(i['cname']))
        r.td(str(i['range'])+"%")
        r.td(str(i['52KH']))
        r.td(str(i['52KL']))
        r.td(str(i['current_price']))
        r.td(str(i['volumn']))
        r.td(str(i['30avg']))
        r.td(str(i['premium']))
        r.td(str(i['category']))   
        r.td(str(i['disct']))
    return str(dtable)

    
def my_table (file, file_path, title, tdesc):
    data = csv_readlist(file, file_path)
    dtable = HTML()
    dtable.h3(title)
    
    desc = []
    if tdesc !="":
        desc = tdesc.split("/")
    l = dtable.ol
    for k in desc:
        l.li(k)

    t = dtable.table(border="0", width ="60%", klass ='table table-bordered')
    
    t.th('SID')
    t.th('名称')
    t.th('变动')
    t.th('上次价')
    t.th('盈亏')
    t.th('持仓价')
    t.th('现价')
    t.th('100建仓价/0.5')
    t.th('98/1')
    t.th('96/1')
    t.th('94/1.5')
    t.th('92/1.5')
    t.th('90/2')
    t.th('88/2')
    t.th('86最低/3')
    
    for i in data:
        
        cp = i['current_price']
        cpf = float(filter(lambda ch: ch in '0123456789.', i['current_price']))
        #print cpf
        if i['myprice'] == "":
            mp = 1000
        else:
            mp = float(i['myprice'])

        if i['setlow'] == "":
            sl = 1000
        else:
            sl = float(i['setlow'])

        if i['last_price'] == "":
            lp = 1000
        else:
            lp = float(i['last_price'])
            
        if lp == 1000:
            lp_change = "NA"
        else:            
            lp_change = round(((cpf-lp)/lp)*100,2)
        
        if mp == 1000:
            mp_change = "NA"
        else:
            mp_change = round(((cpf-mp)/mp)*100,2)
        #print lp_change
        #print i
        r = t.tr
        r.td( str(i['SID']))
        r.td( str(i['cname']))
        if lp_change == "NA":
            r.td( str( lp_change ) +"%")
        elif lp_change <= -1:
            r.td( str( lp_change ) +"%", bgcolor="#90EE90")
        elif lp_change >= 0.5:
            r.td( str( lp_change ) +"%", bgcolor="#DDA0DD")
        else:
            r.td( str( lp_change ) +"%")
            
        r.td( str( lp ))
        r.td( str(mp_change) +"%" )
        r.td( str( mp ) )
        r.td.b( str( cp ) )
        if sl == 1000:
            r.td("NA")
            r.td("NA")
            r.td("NA")
            r.td("NA")
            r.td("NA")
            r.td("NA")
            r.td("NA")
            r.td("NA")
        else:
            sl_ary = [sl*100/86, sl*98/86, sl*96/86, sl*94/86, sl*92/86, sl*90/86, sl*88/86, sl]
            for i in sl_ary:
                if cpf <= i :
                    r.td(str(round(i,2)), bgcolor="#ADD8E6") 
                    
                else:
                    r.td(str(round(i,2)), bgcolor="#FAFAD2") 
    return str(dtable)
    

def sort_range(file, file_path):
    read_dt = csv_readlist(file, file_path)
    range_ls_tmp =[]
    sorted_dt = []
    range_ls = []
    for j in read_dt:
            range_ls_tmp.append(float(j['range']))
            
    range_ls = sorted(range_ls_tmp)
    #print range_ls
    for k in range_ls:
        for i in read_dt:
            if float(i['range']) == k:
                #print i['range']
                sorted_dt.append(i)
                
    #print sorted_dt
    return sorted_dt
    
def sort_premium(file, file_path):
    read_dt = csv_readlist(file, file_path)
    range_ls_tmp =[]
    sorted_dt = []
    range_ls = []
    
    for j in read_dt:
        range_ls_tmp.append(float(j['premium'][:-1]))
        
    range_ls = sorted(range_ls_tmp)
    #print range_ls
    for k in range_ls:
        for i in read_dt:
            if float(i['premium'][:-1]) == k:
                sorted_dt.append(i)
                
    #print sorted_dt
    return sorted_dt

def sort_range_f5(lsdt):
    lsdt5 = []
    for i in lsdt[:11]:
        lsdt5.append(i)
    #lsdt.remove([5:-1])
    return lsdt5

def index_write():
    f = open('/srv/www/idehe.com/store2/index.html','w')
    
    file_etf = "ETF_data.csv"
    file_path = '/srv/www/idehe.com/store2/stock_data/'
    
    etf_data = sort_range(file_etf, file_path)
    table_e = table(etf_data, '主要市场ETF', '1年价格排序/')
    table_set = my_table(file_etf, file_path, '数据处理ETF', '数据处理/下跌1%上涨2%进行仓位操作')
    #print table_etable(etf_data, '主要市场ETF', '1年价格排序/')
    #table_t = table(topic_data, '主题ETF', '1年价格排序/')
    #table_fa = table(f5_funda, '分级A', "选取隐含收益5%以上，成交量100W以上，1年价格排序/52K不准确：环保，军工股A，网金融/X=分级A合并溢价, 正的高价，深圳区申购")
    #table_zj = table(zhaij_data, '场内债基', '按照折溢价排序/主要看折溢价，成交量/年化折价')
    #table_un = table(uncategory_data, '其他未分类', 'X=封基年化折价')

    
    desc = page_desciption()
    content = h_content(desc, table_e, table_set)
    
    h = html(content)
    
    f.writelines(h)
    
        
if __name__ == "__main__":
    index_write()
 
 
 
    