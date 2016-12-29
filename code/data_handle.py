#! /usr/bin/python
#-*- encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from csv_handle import csv_readlist, csv_writelist
from xq_handle import data_get, select_data, data_get_index, select_data_index

from google_data import data_filter, gfile_check

def grab_data(ifile, file_path):
    # get online data and filter it
    is_lis_dic = csv_readlist(ifile, file_path)
    for i in is_lis_dic:
        sdict = data_get(i['SID'])
        fine_data = select_data(sdict)
        i.update(fine_data)
    #print is_lis_dic
    return is_lis_dic

def data_range(is_lis_dic):
    # find data high and low
    for i in is_lis_dic:
        #print type(i['jk'])
        cur_price = float(i['current_price'][1:])
        KL = float(i['52KL'])
        KH = float(i['52KH'])
        cal_tmp = (cur_price-KL)/(KH-KL)
        #print cal_tmp
        i['range'] = round(cal_tmp*100,2)
    basedata = csv_readlist('basedata.csv', "/srv/www/idehe.com/store/stock_data/")
    for u in is_lis_dic:
        for j in basedata:
            if u['SID'] == j['SID']:
                u.update(j)
    #print is_lis_dic
    return is_lis_dic


def data_mhandle(infile, outfile, file_path):
    grabed_data = grab_data(infile, file_path)
    data_ranged = data_range(grabed_data)
    csv_writelist(outfile, file_path, data_ranged)
    
    
if __name__ == "__main__":
    ifile = "ETF.csv"
    ofile = "ETF_data.csv"
    g_path = '/srv/www/idehe.com/store2/stock/'
    
    file_path = "/srv/www/idehe.com/store2/stock_data/"
    
    data_mhandle(ifile, ofile, file_path)
    
    