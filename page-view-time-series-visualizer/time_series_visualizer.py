import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col="date",parse_dates=True)

# Clean data
df = df[(df["value"]>df["value"].quantile(0.025)) & (df["value"]<df["value"].quantile(0.975))]


def draw_line_plot():
    fig=plt.figure(figsize=(12,12))
    plt.plot(df.index,df["value"],color="firebrick")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"]=df_bar.index.year
    df_bar["month"]=df_bar.index.month

    means=df_bar.groupby(["year", "month"]).mean()
    means.columns=["mean"]
    means.reset_index(inplace=True)

    lst16=(means.loc[0:7,"mean"]).tolist()
    lst16=["2016",0,0,0,0]+lst16
    lst17=(means.loc[8:19,"mean"]).tolist()
    lst17=["2017"]+lst17
    lst18=(means.loc[20:31,"mean"]).tolist()
    lst18=["2018"]+lst18
    lst19=(means.loc[32:44,"mean"]).tolist()
    lst19=["2019"]+lst19
    df_bar=pd.DataFrame([lst16,lst17,lst18,lst19],columns=["Year","January","February","March","April","May","June","July","August","September","October","November","December"])
    # Draw bar plot  
    fig=df_bar.plot(x="Year",kind="bar",stacked=False).get_figure()
    fig.set_figheight(6)
    fig.set_figwidth(8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'],   y=df_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y=df_box['value'],order=months).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
