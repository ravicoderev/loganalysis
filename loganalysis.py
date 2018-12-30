#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from loganaysisdb import get_three_popular_articles

app = Flask(__name__)

# HTML template for the news reports page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
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
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Popular Articles</button></div>
      <div><button id="go" type="submit">Popular Authors</button></div>
      <div><button id="go" type="submit">Error Log Percentage</button></div>


    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''


@app.route('/', methods=['GET'])
def main():
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