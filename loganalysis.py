#!/usr/bin/env python3
#

from flask import Flask, request, redirect, url_for

from loganalysisdb import ready_to_view_reports, get_three_popular_articles

app = Flask(__name__)

# HTML template for the news reports page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log Analysis Reports</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>Log Analysis Reports</h1>
    <form method=get>
     <!-- <div><textarea id="content" name="content"></textarea></div> -->
      <div>
      <button id="btn1" type="submit">Popular Articles</button>
      <button id="btn2" type="submit">Popular Authors</button>
      <button id="btn3" type="submit">Error Log Percentage</button>
      </div>
      <br>
      <input type="submit" name="Popular Articles" value="popular_articles">
      <input type="submit" name="Popular Authors" value="popular_authors">
      <input type="submit" name="Error Log Percentage" value="error_log">
      <div>

    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the news report.'''
    posts = ready_to_view_reports()
    # posts = "".join(
    #                 POST % (date, text)
    #                 for text, date in
    #                 ready_to_view_reports()
    #                 )
    # html = HTML_WRAP % posts
    # return html
    return redirect('LogAnalysis.html')


@app.route('/popular_articles', methods=['GET'])
def popular_articles():
    '''Main page of the news report.'''
#   posts = "".join(POST % (date, text) for text, date in get_posts())
    posts = "".join(
                    POST % (date, text)
                    for text, date in
                    get_three_popular_articles()
                    )
    html = HTML_WRAP % posts
    return html


@app.route('/', methods=['POST'])
def post():
    '''New post submission.'''
    message = request.form['content']
    add_post(message)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
