# -*- encoding:utf-8 -*-

import flask

html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <form method = 'post'>
        <input type = 'text' name = 'name' placeholder ='enter your name' />
        <input type = 'sumbit' value = 'send post request' />
        </form>
    </body>
</html>
"""

app = flask.Flask(__name__)

@app.route('/hi', methods = ['GET', 'POST'])
def helo():
    if flask.request.method == 'GET':
        return html_txt
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)