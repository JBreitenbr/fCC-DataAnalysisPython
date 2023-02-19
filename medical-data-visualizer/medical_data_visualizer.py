import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["BMI"]=df["weight"]/((df["height"]/100)**2)
df['overweight'] = np.where(df["BMI"]>25.0,1,0)
del df["BMI"]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df["cholesterol"].replace([1, 2, 3], [0, 1, 1])
df["gluc"] = df["gluc"].replace([1, 2, 3], [0, 1, 1])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=["cardio"], value_vars=["active","alco","cholesterol","gluc","overweight","smoke"])
    

    # Draw the catplot with 'sns.catplot'
    
    fig = sns.catplot(data=df_cat, kind="count",x="variable",hue="value",col="cardio")
    fig.set_axis_labels("variable","total")
    fig=fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_lo"]<=df["ap_hi"]) & (df["weight"]>=df["weight"].quantile(0.025)) & (df["weight"]<=df["weight"].quantile(0.975)) & (df["height"]>=df["height"].quantile(0.025)) & (df["height"]<=df["height"].quantile(0.975))]

  

    # Calculate the correlation matrix
    corr = round(df_heat.corr(),1)

    # Generate a mask for the upper triangle
    mask = np.full(corr.shape,True)

    for i in range(corr.shape[0]):
      for j in range(corr.shape[1]):
        if i>j:
          mask[i][j]=False


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, square=True) 


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
