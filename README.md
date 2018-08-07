# Get User Stats
Get the votes of a user and displays the results as a graph, for example

![My stats](https://github.com/thepolm3/Get-user-stats/blob/master/plot.png)

# Requirements
* [python 3.6](https://python.org)
* [praw](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org)

# Usage
* set up secret.py containg your reddit [client_id and client_secret](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) like this

```
client_id = 'my_id'
client_secret = 'my_secret'
```
Then to generate the table of votes use

>python getUserStats.py user_name

on the commandline, and

>python createGraph.py

to create a graph of the data
