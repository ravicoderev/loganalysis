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
    q1 = "select ar.title, count(l.path), 'views' "
    q2 = "from log l, articles ar "
    q3 = "where CONCAT('/article/',ar.slug) = l.path "
    q4 = "group by ar.title"
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
    q1 = "select au.name, count(l.path) as views "
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
    q1 = "select l.day, ROUND(l.day_errors/sq.total_requests * 100.0,2)|| "
    q1a = "' % errors' as percent "
    q2 = "from ( select sum(day_errors) as total_requests "
    q2a = "from log_errors_grouped ) as sq, log_errors_grouped l "
    q2b = "where ROUND(l.day_errors/sq.total_requests * 100.0,2) > 1.00 "
    q3 = "group by l.day,l.day_errors, sq.total_requests "
    q4 = "order by percent"
    select_query = q1 + q1a + q2 + q2a + q2b + q3 + q4
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
