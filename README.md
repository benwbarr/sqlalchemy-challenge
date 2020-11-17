# **SQLAlchemy Homework - Surfs Up!**
> sqlalchemy-challenge

![alt text](https://github.com/benwbarr/sqlalchemy-challenge/blob/main/Images/surfs-up.png?raw=true)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

### This was done using sqlalchemy and Jupyter Notebooks. You will need to install and import the following

- sqlalchemy

- Jupyter Notebooks

- matplotlib.pyplot

- pandas 

- numpy 

- scipy.stats

- sqlalchemy 

- statistics

- automap_base

- Session

- create_engine

- func

- cm


## Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

- Design a query to retrieve the last 12 months of precipitation data.
```python
dp_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > last_year).\
            order_by(Measurement.date).all()
dp_scores
```

- Select only the date and prcp values.
```python
dp_df = pd.DataFrame(dp_scores)
dp_df.head()
```

- Load the query results into a Pandas DataFrame and set the index to the date column.
```python
dp_df_date = dp_df.set_index('date')
dp_df_date.head()
```

- Sort the DataFrame values by date.

```python
dp_df_date_sort = dp_df_date.sort_values(['date'])
dp_df_date_sort.head()
```
- Plot the results using the DataFrame plot method.
```python
dp_df.plot('date', 'prcp', color = 'teal')
plt.xlabel('Date')
plt.ylabel('Inches')
plt.title('Precipitation Analysis')
plt.xticks(rotation=90)
plt.legend(["precipitation"])
plt.show()
```
![alt text](https://github.com/benwbarr/sqlalchemy-challenge/blob/main/Images/plot.PNG?raw=true)

- Use Pandas to print the summary statistics for the precipitation data.
```python
dp_df.describe()
```
## Station Analysis

- Design a query to calculate the total number of stations.
```python
station_count = session.query(Station).count()
```
- Design a query to find the most active stations.
```python
active_station = session.query(Measurement.station, func.count(Measurement.station)).\
                 group_by(Measurement.station).\
                 order_by(func.count(Measurement.station).desc()).\
                 all()
```
- Design a query to retrieve the last 12 months of temperature observation data (TOBS).
```python
highest_temp = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
               filter(Measurement.station == highest_active_station).\
               filter(Measurement.date > last_year).order_by(Measurement.date).all()
```
- Plot the results as a histogram with bins=12.
```python
highest_temp_q.plot.hist(bins = 12)
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Most Active Station: ' + highest_active_station)

plt.show()
```
![alt text](https://github.com/benwbarr/sqlalchemy-challenge/blob/main/Images/histogram.PNG?raw=true)







