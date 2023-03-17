import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read data
cod_data = pd.read_csv("Cod_cwl_data.csv")

#print out data point size
print(len(cod_data))

# data point labels
print(cod_data.columns)

#helper method to plot missing data
def plot_missing(df, cmap='Blues'):
    """Plot missing percentage of dataset.

    Args:
        df (pd.DataFrame): input dataset.
    """
    assert isinstance(df, pd.DataFrame)

    missing_data = pd.DataFrame({'total_missing': df.isnull().sum(), 'perc_missing': (df.isnull().sum()/82790)*100})
    missing_data = missing_data[missing_data['total_missing'] != 0]
    missing_data = missing_data.sort_values(by='total_missing')
    ax = sns.barplot(data=missing_data, y=missing_data.index, x='perc_missing', palette=cmap)
    plt.xlabel("Missing percentage (%)")
    plt.ylabel("Properties")

    return


# MISSING DATA 4
plot_missing(cod_data)
plt.gcf().canvas.manager.set_window_title('Missing Data 4')

# PLAYER KILL & DEATH COUNTS 7
sns.set(style = "whitegrid", palette = "deep")
fig_01 = plt.figure(figsize = (20,5))
subfig_1 = fig_01.add_subplot(1,2,1)
sns.histplot(cod_data['kills'], kde = True).set(title = "Player Kill Histogram")
subfig_2 = fig_01.add_subplot(1,2,2)

sns.set(style = "whitegrid", palette = "deep", rc={'figure.figsize':(10,10)})
sns.histplot(cod_data['deaths'], kde = True).set(title = "Player Death Histogram")
plt.gcf().canvas.manager.set_window_title('Player Kill & Death Counts')


# PLAYER SCORE DISTRIBUTION 8
sns.set(style = "whitegrid", palette = "deep")
fig_01 = plt.figure(figsize = (10,5))
sns.histplot(cod_data['player score'], kde = True).set(title = "Player Score Histogram")
plt.gcf().canvas.manager.set_window_title('Player Score Distributions')


# HEADSHOT KILLS vs KILL-DEATH 9
sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(9, 9)
hk = sns.scatterplot(x=cod_data['deaths'],y=cod_data['kills'],size=cod_data['headshots'], sizes=(5,160)).set(title='Kill-Death & Headshot Kill Counts')
plt.legend(title='headshots', loc='lower right')
plt.gcf().canvas.manager.set_window_title('Headshot Kills vs Kill Death')


# SCORESTREAK KILLS VS KILL-DEATH COUNTS 10
sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(9, 9)
sns.scatterplot(x=cod_data['deaths'],y=cod_data['kills'],size=cod_data['scorestreaks kills'], sizes = (20,160)).set(title='Kill-Death & Scorestreak Kills Counts')
plt.legend(title='scorestreaks kills', loc='lower right')
plt.gcf().canvas.manager.set_window_title('Scorestreak Kills vs Kill-Death Counts')


#OVERALL (K/D) DISTRIBUTION 12
plt.figure()
sns.set(style = "whitegrid", palette = "deep", rc={'figure.figsize':(10,5)})
sns.histplot(cod_data['k/d'], kde = True, bins = 60).set(title = "Player K/D Ratio Distribution")
plt.gcf().canvas.manager.set_window_title('Overall k/d Distribution')


# HEADSHOT & SCORESTREAK REVISITED 13
plt.figure()
sns.set(style="whitegrid", rc={'figure.figsize':(16,10)}, font_scale=1.75)
sns.violinplot(x=cod_data['k/d'], y=cod_data['headshots'], inner="points", orient="h", scale = "area", width=0.8, palette="pastel").set(title = "K/D Ratio vs Headshot Kills")
plt.gcf().canvas.manager.set_window_title('Headshot & Scorestreak 1')
plt.figure()
sns.set(style="whitegrid", rc={'figure.figsize':(16,10)}, font_scale=1.75)
sns.violinplot(x=cod_data['k/d'], y=cod_data['scorestreaks kills'], inner="points", orient="h", scale = "area", width=0.8, palette="pastel").set(title = "K/D Ratio vs Scorestreak Kills")
plt.gcf().canvas.manager.set_window_title('Headshot & Scorestreak 2')


# PLAYER SCORE VS K/D 14
plt.figure()
sns.set(style="whitegrid", rc={'figure.figsize':(15,10)}, font_scale=1.5)
sns.regplot(x=cod_data['k/d'],y=cod_data['player score'], marker="+", fit_reg=False).set(title = "K/D Ratio vs Player Score")
plt.gcf().canvas.manager.set_window_title('Player Score vs K/D')


# MOST COMMON WEAPONS USED 15
plt.figure()
sns.set(rc={'figure.figsize':(11.7,8.27)}, font_scale=2)
sns.countplot(x=cod_data['fave weapon'], order = cod_data['fave weapon'].value_counts().index)
plt.xticks(rotation=90)
plt.gcf().canvas.manager.set_window_title('Most Common Weapons Used')


# TOP 8 MOST USED WEAPONS COMPARED 16
plt.figure()
sns.set(style = "whitegrid", font_scale=1.25, rc={'figure.figsize':(12,6)})
sns.distplot(cod_data[cod_data['fave weapon']=='Maddox RFB']['kills per 10min'],hist=False, label='Maddox RFB')
sns.distplot(cod_data[cod_data['fave weapon']=='Saug 9mm']['kills per 10min'],hist=False, label='Saug 9mm')
sns.distplot(cod_data[cod_data['fave weapon']=='ICR-7']['kills per 10min'],hist=False, label='ICR-7')
sns.distplot(cod_data[cod_data['fave weapon']=='PPSh-41']['kills per 10min'],hist=False, label='PPsh-41')
sns.distplot(cod_data[cod_data['fave weapon']=='FG 42']['kills per 10min'],hist=False, label='FG 42')
sns.distplot(cod_data[cod_data['fave weapon']=='Paladin HB50']['kills per 10min'],hist=False, label='Paladian HB50')
sns.distplot(cod_data[cod_data['fave weapon']=='KN-57']['kills per 10min'],hist=False, label='KN-57')
sns.distplot(cod_data[cod_data['fave weapon']=='Kar98k']['kills per 10min'],hist=False, label='Kar98k')
plt.legend()
plt.gcf().canvas.manager.set_window_title('Top 8 Most Used Weapons Compared')


# WEAPONS EXHIBITING SIMILAR DISTRIBUTIONS 17
plt.figure()
sns.set(style = "whitegrid", font_scale=1.25, rc={'figure.figsize':(12,6)})
sns.distplot(cod_data[cod_data['fave weapon']=='Maddox RFB']['kills per 10min'],hist=False, label='Maddox RFB')
sns.distplot(cod_data[cod_data['fave weapon']=='Saug 9mm']['kills per 10min'],hist=False, label='Saug 9mm')
sns.distplot(cod_data[cod_data['fave weapon']=='PPSh-41']['kills per 10min'],hist=False, label='PPsh-41')
sns.distplot(cod_data[cod_data['fave weapon']=='FG 42']['kills per 10min'],hist=False, label='FG 42')
plt.legend()
plt.gcf().canvas.manager.set_window_title('Weapons Exhibiting Similar Distributions')


# WEAPONS DISPLAYING DIFFERENT TRENDS 18
plt.figure()
sns.set(style = "whitegrid", font_scale=1.25, rc={'figure.figsize':(12,6)})
sns.distplot(cod_data[cod_data['fave weapon']=='ICR-7']['kills per 10min'],hist=False, label='ICR-7')
sns.distplot(cod_data[cod_data['fave weapon']=='Paladin HB50']['kills per 10min'],hist=False, label='Paladian HB50')
sns.distplot(cod_data[cod_data['fave weapon']=='KN-57']['kills per 10min'],hist=False, label='KN-57')
sns.distplot(cod_data[cod_data['fave weapon']=='Kar98k']['kills per 10min'],hist=False, label='Kar98k')
plt.legend()
plt.gcf().canvas.manager.set_window_title('Weapons Displaying Different Trends')


# helper method to plot heatmaps to display relationships between labels
def plot_heatmap(df, x, y, norm='columns', annot=True, cmap='Blues'):
    """Plot heatmap of two properties.

    Args:
        df (pd.DataFrame): input dataset.
        x (str): property on x axis.
        y (str): property on y axis.
        norm (str, optional): normalization mode for pd.crosstab (‘all’, ‘index’, ‘columns’). Defaults to 'columns'.
        annot (bool, optional): Annotating values or not. Defaults to True.
        cmap (str, optional): colormap for sns.heatmap. Defaults to 'Blues'.
    """
    assert isinstance(df, pd.DataFrame)
    assert isinstance(x, str)
    assert isinstance(y, str)
    assert isinstance(norm, str) and (norm=='all' or norm=='index' or norm=='columns')
    assert isinstance(annot, bool)
    assert isinstance(cmap, str)
    plt.figure()
    sns.heatmap(pd.crosstab(df[y], df[x], normalize=norm), annot=annot, cmap=cmap)

    return


# WEAPON POPULARITY VS GAME MODE 19
plot_heatmap(cod_data, 'mode', 'fave weapon')
plt.gcf().canvas.manager.set_window_title('Weapon Popularity vs Game Mode')


# WEAPON POPULARITY VS SPECIALISTS 20
plot_heatmap(cod_data, 'fave specialist', 'fave weapon')
plt.gcf().canvas.manager.set_window_title('Weapon Popularity Vs Specialists')

plt.show()