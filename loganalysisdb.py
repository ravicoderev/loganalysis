# "Log Analysis database code" for the DB news.

import datetime
import psycopg2
import bleach

DBNAME = "news"

POSTS = [("This is the first post.", datetime.datetime.now())]

# PROBLEM - 1. What are the most popular three articles of all time? 


def get_three_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    select_query =
    '''
    select ar.title, count(l.path) as views
    from "log" l, articles ar
    where CONCAT('/article/',ar.slug) = l.path
    group by ar.title
    order by views desc
    '''
    c.execute(select_query)
    POSTS = c.fetchall()
    return reversed(POSTS)
    db.close()


# PROBLEM - 2. Who are the most popular article authors of all time?


def get_popular_article_authors():
