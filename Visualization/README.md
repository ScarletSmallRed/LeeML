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