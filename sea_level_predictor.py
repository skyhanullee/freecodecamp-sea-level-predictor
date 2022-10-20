import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Sky Lee
# 10/6/2022

def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv", delimiter=',')
  
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  # Create scatter plot
  plt.figure(figsize=(12, 6))
  plt.xlim(1850, 2060) # extends the graph to show year 2050
  
  plt.scatter(x, y, color='red')

  # Create first line of best fit
  extendedX = range(min(x), 2051)
  res1 = linregress(x, y)
  
  plt.plot(
    extendedX, 
    res1.intercept + res1.slope*extendedX, 
    label='linregress from start to 2050', 
    color='blue'
  )

  # Create second line of best fit
  altX = df.loc[df['Year'] >= 2000, 'Year']
  altY = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']
  altYearRange = range(2000, 2051)
  res2 = linregress(altX, altY)
  
  plt.plot(
    altYearRange, 
    res2.intercept + res2.slope*altYearRange, 
    label='linregress from 2000 to 2050', 
    color='green', 
    linestyle='--'
  )
  
  # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.legend()
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()