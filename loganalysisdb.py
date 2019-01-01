#! Python 3.5.2
# "Log Analysis database code" for news reports.

import datetime
import psycopg2
import bleach
import csv

DBNAME = "news"


def ready_to_view_reports():
    POSTS = [("This is the first post.", datetime.datetime.now())]

# PROBLEM - 1. What are the most popular three articles of all time? 


def get_three_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q1 = "select ar.title, count(l.path) as views, ' - views' "
    q2 = "from log l, articles ar "
    q3 = "where CONCAT('/article/',ar.slug) = l.path "
    q4 = "group by ar.title order by views desc LIMIT 3"
    select_query = q1 + q2 + q3 + q4
    c.execute(select_query)
    results = c.fetchall()
    print(results)
    #  return reversed(results) # write into text file
    with open('popular_articles.txt', 'w') as f:
        #  writer = csv.writer(f, delimiter=',')
        for row in results:
            # writer.writerow(row)
            f.write("%s\n" % str(row))
    print("Done Writing")
    db.close()


# PROBLEM - 2. Who are the most popular article authors of all time?


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q1 = "select au.name, count(l.path) as views, ' - views' "
    q2 = "from authors au, log l, articles ar "
    q3 = "where CONCAT('/article/',ar.slug) = l.path "
    q4 = "and ar.author = au.id "
    q5 = "group by au.name order by views desc"
    select_query = q1 + q2 + q3 + q4 + q5
    c.execute(select_query)
    results = c.fetchall()
    print(results)
    #  return reversed(results) # write into text file
    with open('popular_authors.txt', 'w') as f:
        #  writer = csv.writer(f, delimiter=',')
        for row in results:
            # writer.writerow(row)
            f.write("%s\n" % str(row))
    print("Done Writing")
    db.close()


# PROBLEM - 3. On which days did more than 1% of requests lead to errors?


def get_percent_error_requests():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    q1 = "select time::timestamp::date as day, "
    q1a = "ROUND(100.00 * SUM(CASE WHEN log.status='404 NOT FOUND' "
    q1b = "THEN 1 ELSE 0 END) / count(status),2) || ' % errors'"
    q2 = "from log group by day "
    q3 = "having ROUND(100.00 * SUM(CASE WHEN log.status='404 NOT FOUND' "
    q3a = "THEN 1 ELSE 0 END) / count(status),2) > 1.00"
    select_query = q1 + q1a + q1b + q2 + q3 + q3a
    c.execute(select_query)
    results = c.fetchall()
    print(results)
    #  return reversed(results) # write into text file
    with open('percent_errors.txt', 'w') as f:
        #  writer = csv.writer(f, delimiter=',')
        for row in results:
            # writer.writerow(row)
            f.write("%s\n" % str(row))
    print("Done Writing")
    db.close()


get_three_popular_articles()
get_popular_authors()
get_percent_error_requests()
