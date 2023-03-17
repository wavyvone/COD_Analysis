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


# Helper Method for scatter
def scatter_helper(a, b, c, d):
    '''
    Helps plot scatter plots of a vs b vs c
    a: first label
    b: second label
    c: third label
    d: title
    '''
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(c, str)
    assert isinstance(d, str)
    sns.set_style('ticks')
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 9)
    hk = sns.scatterplot(x=cod_data[a],y=cod_data[b],size=cod_data[c], sizes=(5,160)).set(title= d)
    plt.legend(title=c, loc='lower right')
    plt.gcf().canvas.manager.set_window_title(d +' vs ' + b + '-' + a + ' counts')
    return


# HEADSHOT KILLS vs KILL-DEATH 9
scatter_helper('deaths', 'kills', 'headshots', 'Kill-Death & Headshot Kill Counts')

# SCORESTREAK KILLS VS KILL-DEATH COUNTS 10
scatter_helper('deaths', 'kills', 'scorestreaks kills', 'Kill-Death & Scorestreak Kills Counts')


#OVERALL (K/D) DISTRIBUTION 12
plt.figure()
sns.set(style = "whitegrid", palette = "deep", rc={'figure.figsize':(10,5)})
sns.histplot(cod_data['k/d'], kde = True, bins = 60).set(title = "Player K/D Ratio Distribution")
plt.gcf().canvas.manager.set_window_title('Overall k/d Distribution')

#Violinplot helper method
def violin_helper(a,b, title, w_title):
    '''
    helps plot violinplots between data labels in cod_data
    a: first label (string)
    b: second label (string)
    title: title (string)
    w_title: window title (string)
    '''
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(title, str)
    assert isinstance(w_title, str)
    plt.figure()
    sns.set(style="whitegrid", rc={'figure.figsize':(16,10)}, font_scale=1.75)
    sns.violinplot(x=cod_data[a], y=cod_data[b], inner="points", orient="h", scale = "area", width=0.8, palette="pastel").set(title = title)
    plt.gcf().canvas.manager.set_window_title(w_title)
    return
    
# HEADSHOT & SCORESTREAK REVISITED 13
violin_helper('k/d', 'headshots', "K/D Ratio vs Headshot Kills", 'Headshot & Scorestreak 1')

violin_helper('k/d','scorestreaks kills', 'K/D Ratio vs Scorestreak Kills', 'Headshot & Scorestreak 2')


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

# helper method for comparing most used weapons trends
def distplot_helper(a, title):
    '''
    Plot the distribution usage between weapons
    a: list of weapons to compare with (string)
    title: the title of the graph (string)
    '''
    assert isinstance(a, list)
    assert isinstance(title, str)
    for i in a:
        assert isinstance(i, str)
    plt.figure()
    sns.set(style = "whitegrid", font_scale=1.25, rc={'figure.figsize':(12,6)})
    for i in a:
        sns.distplot(cod_data[cod_data['fave weapon']==i]['kills per 10min'],hist=False, label=i)
    plt.legend()
    plt.gcf().canvas.manager.set_window_title(title)
    return

# TOP 8 MOST USED WEAPONS COMPARED 16
top_8_weapons = ['Maddox RFB','Saug 9mm','ICR-7','PPSh-41','FG 42','Paladin HB50','KN-57','Kar98k']
top_8_title = 'Top 8 Most Used Weapons Compared'
distplot_helper(top_8_weapons, top_8_title)


# WEAPONS EXHIBITING SIMILAR DISTRIBUTIONS 17
similar_weapons = ['Maddox RFB','Saug 9mm','PPSh-41','FG 42']
similar_title = 'Weapons Exhibiting Similar Distributions'
distplot_helper(similar_weapons, similar_title)


# WEAPONS DISPLAYING DIFFERENT TRENDS 18
diff_weapons = ['ICR-7','Paladin HB50','KN-57','Kar98k']
diff_title = 'Weapons Displaying Different Trends'
distplot_helper(diff_weapons, diff_title)


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