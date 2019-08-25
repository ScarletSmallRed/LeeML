# Visualization
Use Python library `Matplotlib` to implement some data visualization.
## Temperature Trend
`y1` and `y2` represent the temperature of room1 and room2 from 10:00 to 12:00, respectively, and draw a line chart to observe the change of temperature.

Relevant code [here](./TemperatureChange/Plot.py).
```
y1 = [random.randint(20, 35) for i in range(0, 120, 3)]
y2 = [random.randint(20, 35) for i in range(0, 120, 3)]
```
![Line Chart](./TemperatureChange/tempearture.png)
## Weather Scatter
Draw a scatter plot of the temperature distribution in March and October.

Relevant code [here](./Weather/Scatter.py).
![Scatter](./Weather/Scatter.png)
## 2019 Movie Box Office
Use `Matplotlib` to draw bar charts to visualize 2019 movie box office data.

Relevant code [here](./Movies/Bar1.py).
![Bar](./Movies/Movie.png)
## Three Days Movies Box Office
Draw multiple bar charts to show box office information for several movies in three days.

Relevant code [here](./Movies2/Bar.py).
![Bar](./Movies2/Movies.png)
## Movies Duration Distribution 
Draw a histogram to analyze the distribution of the duration of 1000 movies.

Relevant code [here](./MovieDuration/Hist.py).
![Hist](./MovieDuration/MovieDuration.png)
## IMDB
Use the two Python libraries `numpy` and `pandas` to analyze the distribution of movie types in the 1,000 movies of IMDB.

Relevant code [here](./IMDB/IMDB.py).
![IMDB](./IMDB/IMDB1.png)
## Starbucks
Use the method `groupby` in the `pandas` library to count the number of Starbucks in each country.

Relevant code [here](./Starbucks/chart1.py).
![chart1](./Starbucks/chart1.png)

Count the number of Starbucks in the major cities of the United States.

Relevant code [here](./Starbucks/chart2.py).
![chart2](./Starbucks/chart2.png)
## Books
The annual average rating change trend of books.

Relevant code [here](./Books/chart.py).
![chart](./Books/chart.png)
## Emergency (911) Calls
Csv [file](./911/911.csv) description: Fire, Traffic, EMS for Montgomery County, PA 

Analyze the total number of calls for three types of emergency calls.

Relevant code [here](./911/chart.py).

![chart](./911/chart.png)

Analyze the changes in the number of calls for emergency calls per month.

Relevant code [here](./911/chart2.py).

![chart2](./911/chart2.png)

Analyze the changes in the number of calls for three types of emergency calls per month.

Relevant code [here](./911/chart3.py).

![chart3](./911/chart3.png).