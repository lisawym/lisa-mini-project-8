## SQLite Lab

![image](https://github.com/nogibjj/mini-project5-lisa/assets/46847817/ea1edc79-ee86-4e5e-a224-b484862ae0ae)


### Lab:

* Use an AI Assistant, but use a different one than you used from a previous lab (Anthropic's Claud, Bard, Copilot, CodeWhisperer, Colab AI, etc)
* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query
For the ETL-Query lab:
## [E] Extract a dataset 
* Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats work well.
* I extracted the data from a dataset hosted on GitHub. 
* I tried to load a Kaggle database earlier, but it is protected and requires me to install Kaggle package to load the data. But there is some issue with the package. So I resorted to using a GitHub dataset.

## [T] Transform the data 
* Transform the data by cleaning, filtering, enriching, etc. to get it ready for analysis.
* In this project, I subset the data into training and test datasets randomly based on a random seed.


## [L] Load the transformed data 
*  Load the transformed data into a SQLite database table using Python's SQLite3 module.
*  Load the two tables, training and test to the dataset separately
  
## [Q] Write and execute SQL queries 
*  Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.

#### Tasks:

* Convert the main.py into a command-line tool that lets you run each step independently
* Make sure your project passes lint/tests and has a built badge
* Include an architectural diagram showing how the project works

#### Reflection Questions

* What challenges did you face when extracting, transforming, and loading the data? How did you overcome them?
* What insights or new knowledge did you gain from querying the SQLite database?
* How can SQLite and SQL help make data analysis more efficient? What are the limitations?
* What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
* If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

##### Challenge Exercises

* Add more transformations to the data before loading it into SQLite. Ideas: join with another dataset, aggregate by categories, normalize columns.
* Write a query to find correlated fields in the data. Print the query results nicely formatted.
* Create a second table in the SQLite database and write a join query with the two tables.
* Build a simple Flask web app that runs queries on demand and displays results.
* Containerize the application using Docker so the database and queries can be portable


