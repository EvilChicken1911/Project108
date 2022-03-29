import pandas as pd
import csv
import plotly.figure_factory as pf
import scipy

df = pd.read_csv("C:/Users/Jonathan Wu/Downloads/White Hat/Class108/projectdata.csv")
fig = pf.create_distplot([df["Avg_Rating"].tolist()], ["rating"], show_hist = False)
fig.show()