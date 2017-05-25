# -*- encoding:utf-8 -*-
import flask
from flask import Flask, render_template, request, redirect
from csv_handle import csv_readlist, csv_writelist


stock_txt = """
<!DOCTYPE html>
<html>
    <head>
        <title>Update stock info!</title>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
        <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
        <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    </head>
    <body>
    <div class="container">
    	<div class="row clearfix">
    		<div class="col-md-12 column">
    			<div class="jumbotron">
    				<h1>
    					修改持仓信息！
    				</h1>
    				<p>
    					This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.
    				</p>
                    <form class="form-inline", method = 'post', role="form">
                            <div class="form-group">
                                    <div class="form-group">
                                        <label for="name">SID</label>
                                        <input type="text" name='sid' class="form-control" placeholder="输入股票代码">
                                    </div>
                                    <div class="form-group">
                                        <label for="name">average</label>
                                        <input type="text" name='avg' class="form-control" placeholder="输入平均持仓价">
                                    </div>
                                    <div class="form-group">
                                        <label for="name">last</label>
                                        <input type="text" name='last' class="form-control" placeholder="输入上次调仓价">
                                    </div>
                                    <div class="form-group">
                                        <label for="name">share</label>
                                        <input type="text" name='share' class="form-control" placeholder="仓位">
                                    </div> 
                                
                                    <div class="form-group">
                                        <label for="name">setlow</label>
                                        <input type="text" name='setlow' class="form-control" placeholder="输入估算最低价">
                                    </div>  
                                    
                                <div>
                                  <label class="checkbox-inline">
                                    <input type="radio" name="file" value="ETF.csv" checked>ETF.csv
                                  </label>
                                  <label class="checkbox-inline">
                                    <input type="radio" name="file" value="rest.csv">rest.csv
                                  </label>
                                  <label class="checkbox-inline">
                                    <input type="radio" name="file" value="rest2.csv">rest2.csv
                                  </label>
                                </div>
                                <button type="submit" class="btn btn-default">提交</button>
                            </div>
                    </form>
    				</p>
    			</div>
    		</div>
    	</div>
    </div>
    </body>
</html>
"""

cash_txt = """
<!DOCTYPE html>
<html>
    <head>
        <title>Update stock info!</title>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
        <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
        <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    </head>
    <body>
    <div class="container">
    	<div class="row clearfix">
    		<div class="col-md-12 column">
    			<div class="jumbotron">
    				<h1>
    					修改现金！
    				</h1>
    				<p>
    					This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.
    				</p>
                    <form class="form-inline", method = 'post', role="form">
                            <div class="form-group">
                                    <div class="form-group">
                                        <label for="name">SID</label>
                                        <input type="text" name='cash' class="form-control" placeholder="输入现金变更">
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="name">average</label>
                                        <input type="text" name='bond' class="form-control" placeholder="输入债券">
                                    
                                    </div>
                            </p>
                            <button type="submit" class="btn btn-default">提交</button>
                            </div>        
                    </form>
    				</p>
    			</div>
    		</div>
    	</div>
    </div>
    </body>
</html>
"""


app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

#

def stock():
    if flask.request.method == 'GET':
        return stock_txt
    else:
        sid = 'sid' in flask.request.form and flask.request.form['sid']
        myp = 'avg' in flask.request.form and flask.request.form['avg']
        lastp = 'last' in flask.request.form and flask.request.form['last']
        share = 'share' in flask.request.form and flask.request.form['share']
        
        setlow = 'setlow' in flask.request.form and flask.request.form['setlow']
        
        file = 'file' in flask.request.form and flask.request.form['file']
        #print (myp + lastp)
        
        if file:
            print (file)
            data_get = {}
            if sid:
                data_get['SID'] = sid
            if myp:
                data_get['myprice'] = myp
            if lastp:
                data_get['last_price'] = lastp
            if share:
                data_get['share'] = share
                
            if setlow:
                data_get['setlow'] = setlow
                
            ## what data got in list
            print (data_get) 
            
            # read data file
            data_read = csv_readlist(file, "/srv/www/idehe.com/store2/data/")
            
            ## update 
            for i in data_read:
                if i['SID'] == data_get['SID']:
                    i.update(data_get)
                    
            #save into file
            csv_writelist(file, "/srv/www/idehe.com/store2/data/", data_read)
            return redirect('/')
        else:
            return "not good"
        
@app.route('/cash', methods = ['GET', 'POST'])
def cash():
    if flask.request.method == 'GET':
        return cash_txt

    else:
        cash = 'cash' in flask.request.form and flask.request.form['cash']
        bond = 'bond' in flask.request.form and flask.request.form['bond']

        data_read = csv_readlist("cash_data.csv", "/srv/www/idehe.com/store2/data_output/")        
        if cash:
            data_read[0]['share'] = float(data_read[0]['share']) + float(cash)
        if bond:
            data_read[1]['share'] = float(data_read[1]['share']) + float(bond)
            
        print data_read
        csv_writelist("cash_data.csv", "/srv/www/idehe.com/store2/data_output/", data_read)
        
        return redirect('/cash')
        

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=8080)
    app.run(debug=True, host='0.0.0.0', port=18080)
    
    
    