# Full Stack Web Development

## Project: Log Analysis

Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

- Vagrant
- Language: Python (Python 3.5.2))
- Database: Postgres (psql (PostgreSQL) 9.5.14)

**Pre-requisites:**

1.	Vagrant is up and running if not vagrant up from the root folder where you have vagrant file and log in using vagrant ssh into vm.
2.	Download/clone repo into the vagrant folder
3.	Postgres sql is up and running and news database exist. 
4.	Verify if you can successfully log in to Postgres news database from vm prompt.
```vagrant@vagrant:/vagrant/loganalysis$psql -d news```
5.	List tables in news database by ```news#\d ```  from db prompt. Verify if you have the following 3 tables
    - articles
    - autho 
    - log
6. Execute the python script to generate simple text reports.
     - Change directory and execute the python script file at the vm prompt ```python3 loganalysisdb.py``` as below 
     
     ```
     vagrant@vagrant:/vagrant/loganalysis$python3 loganalysisdb.py
     ```

	- You should see the following reports on successfull execution
	    - popular_articles.txt
	    - popular_authors.txt
	    - percent_errors.txt
