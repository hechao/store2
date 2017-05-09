#! /usr/bin/python
#-*- encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from csv_handle import csv_readlist, csv_writelist
from xq_handle import xq_data_A, xq_data_A_filter, xq_data_index_bond, xq_data_index_filter, xq_data_bond_filter

#from google_data import data_filter, gfile_check

def grab_data(ifile, file_path):
    # read csv SID list, get data, filter, update list
    update_data = csv_readlist(ifile, file_path)
    for i in update_data:
        xdA = xq_data_A(i['SID'])
        data_filtered = xq_data_A_filter(xdA)
        i.update(data_filtered)
    #print stock_data
    return update_data

def data_add_range(updated_data):
    # find data high and low
    for i in updated_data:
        #print type(i['jk'])
        cur_price = float(i['current_price'][1:])
        KL = float(i['52KL'])
        KH = float(i['52KH'])
        cal_tmp = (cur_price-KL)/(KH-KL)
        #print cal_tmp
        i['range'] = round(cal_tmp*100,2)
    ## 手动替换显示一些不靠谱数据
    basedata = csv_readlist('basedata.csv', "/srv/www/idehe.com/store2/data/")
    for u in updated_data:
        for j in basedata:
            if u['SID'] == j['SID']:
                u.update(j)
    #print updated_data
    return updated_data


def data_sort(infile, outfile, ifile_path, ofile_path):
    #grab data
    grabed_data = grab_data(infile, ifile_path)
    # update range 
    data_ranged = data_add_range(grabed_data)
    # write back
    csv_writelist(outfile, ofile_path, data_ranged)
    
    
if __name__ == "__main__":
    ifile = "ETF.csv"
    ofile = "ETF_data.csv"
    #g_path = '/srv/www/idehe.com/store2/stock/'
    
    #file_path = "/srv/www/idehe.com/store2/stock_data/"
    
    data_sort(ifile, ofile, ifile_path, ofile_path)
    
    