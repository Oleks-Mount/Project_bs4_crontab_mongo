# Start 
In this project, I implemented data collection from the site using **BeautifulSoup** and writing data to the database **NoSQL(MongoDB)** .

# First step
I wrote a small parser to collect data from the site and wrote the data to a database.File **data_group.py**.
# Second step
Linux operating system. To run the file once a day, I used **crontab**.
```
1)sudo crontab -e (choose  text editor that will be convenient for you)
2)Seting the process  0 13 * * * python3 data_group.py 
3)Save and exit.
4)sudo crontab -l (this command will show which processes have been seting)
5)sudo systemctl status cron (this command checks the task)
```
# Third step
The file **main.py** will display the data in the database.

# End
This project reflects a simple automation of data collection.

 