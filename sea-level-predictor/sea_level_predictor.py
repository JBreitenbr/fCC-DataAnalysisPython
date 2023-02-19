import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig=plt.figure(figsize=(12,9))
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])


    # Create first line of best fit
    res1=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    x1=[]
    y1=[]
    for i in range(1880,2051):
       x1.append(i)
       y1.append(res1.intercept + i*res1.slope)
    plt.plot(x1,y1,color="blue")

    # Create second line of best fit
    df_2000=df[df["Year"]>=2000]
    res2=linregress(df_2000["Year"],df_2000["CSIRO Adjusted Sea Level"])
    x2=[]
    y2=[]
    for i in range(2000,2051):
       x2.append(i)
       y2.append(res2.intercept + i*res2.slope)
    plt.plot(x2,y2,color="magenta")
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
