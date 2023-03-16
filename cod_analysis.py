#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data
cod_data = pd.read_csv("Cod_cwl_data.csv")

#Plot missing Data
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

#Plot heatmap
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

    sns.heatmap(pd.crosstab(df[y], df[x], normalize=norm), annot=annot, cmap=cmap)

    return




# ### Observe Player Kills and Death Counts

# In[10]:


#player kills (counts of number of kills from data)
sns.set_style("whitegrid")
kills_plot = sns.histplot(data= cod_data, x = 'kills', kde = True)
kills_plot.set_title("Player Kill Histogram")
kills_plot.set_ylabel("Count")
kills_plot.set_xlabel("Kills")


# In[11]:


#player deaths (counts of number of deaths from data)
sns.set_style("whitegrid")
death_plot = sns.histplot(data= cod_data, x = 'deaths', kde = True)
death_plot.set_title("Player Death Histogram")
death_plot.set_ylabel("Count")
death_plot.set_xlabel("Deaths")


# ## Player Score Distribution

# In[12]:


#player deaths (counts of number of deaths from data)
sns.set_style("whitegrid")
p_score_plot = sns.histplot(data= cod_data, x = 'player score', kde = True)
p_score_plot.set_title("Player Score Histogram")
p_score_plot.set_ylabel("Count")
p_score_plot.set_xlabel("Player Score")


# ## Headshot Kills vs Kill-Death Count

# In[13]:


sns.set(rc={"figure.figsize":(6.5, 6.5)})
sns.set_style("ticks")
hvk_plot = sns.scatterplot(x=cod_data['deaths'],y=cod_data['kills'], size =cod_data['headshots'])
hvk_plot.set_title("Kill-Death & Headshot Kills Count")
hvk_plot.set_ylabel("Kills")
hvk_plot.set_xlabel("Deaths")
sns.move_legend(hvk_plot,"lower right")


# ## Scorestreak Kills vs Kill-Death Counts

# In[14]:


sns.set(rc={"figure.figsize":(6.5, 6.5)})
sns.set_style("ticks")
svk_plot = sns.scatterplot(x=cod_data['deaths'],y=cod_data['kills'], size =cod_data['scorestreaks kills'])
svk_plot.set_title("Kill-Death & Scorestreak Kills Count")
svk_plot.set_ylabel("Kills")
svk_plot.set_xlabel("Deaths")
sns.move_legend(svk_plot,"lower right")


# ## Overall K/D Distribution

# In[15]:


sns.set(rc={"figure.figsize":(9.5, 6.5)})
sns.set_style("whitegrid")
kd_plot = sns.histplot(data= cod_data, x = 'k/d', kde = True, bins=60)
kd_plot.set_title("Player K/D Distribution")
kd_plot.set_ylabel("Count")
kd_plot.set_xlabel("K/D")


# ## Headshot vs Scorestreak

# In[ ]:





# ## Player Score vs K/D Ratio

# In[16]:


sns.set(rc={"figure.figsize":(10.5, 6.5)})
sns.set_style("whitegrid")
sns.regplot(x=cod_data['k/d'],y=cod_data['player score'], marker="+", fit_reg=False).set_title("K/D Ratio vs Player Score")


# ## Most Common Weapons Used

# In[17]:


sns.set(rc={'figure.figsize':(11.7,8.27)}, font_scale=2)
sns.countplot(x=cod_data['fave weapon'], order = cod_data['fave weapon'].value_counts().index)
plt.xticks(rotation=90)


# ## Top 8 Most Used Weapons Compared

# In[18]:


sns.set(rc={'figure.figsize':(11.7,6.27)}, font_scale=2)
sns.set_style("whitegrid")
sns.distplot(cod_data[cod_data['fave weapon']=='Maddox RFB']['kills'],hist=False, label='Maddox RFB')
sns.distplot(cod_data[cod_data['fave weapon']=='Saug 9mm']['kills'],hist=False, label='Saug 9mm')
sns.distplot(cod_data[cod_data['fave weapon']=='ICR-7']['kills'],hist=False, label='ICR-7')
sns.distplot(cod_data[cod_data['fave weapon']=='PPSh-41']['kills'],hist=False, label='PPsh-41')
sns.distplot(cod_data[cod_data['fave weapon']=='FG 42']['kills'],hist=False, label='FG 42')
sns.distplot(cod_data[cod_data['fave weapon']=='Paladin HB50']['kills'],hist=False, label='Paladian HB50')
sns.distplot(cod_data[cod_data['fave weapon']=='KN-57']['kills'],hist=False, label='KN-57')
sns.distplot(cod_data[cod_data['fave weapon']=='Kar98k']['kills'],hist=False, label='Kar98k')

plt.legend()


# ## Weapons Exhibiting Similar Distributions

# In[19]:


sns.set(rc={'figure.figsize':(11.7,6.27)}, font_scale=2)
sns.set_style("whitegrid")
sns.distplot(cod_data[cod_data['fave weapon']=='Maddox RFB']['kills'],hist=False, label='Maddox RFB')
sns.distplot(cod_data[cod_data['fave weapon']=='Saug 9mm']['kills'],hist=False, label='Saug 9mm')
sns.distplot(cod_data[cod_data['fave weapon']=='PPSh-41']['kills'],hist=False, label='PPsh-41')
sns.distplot(cod_data[cod_data['fave weapon']=='FG 42']['kills'],hist=False, label='FG 42')

plt.legend()


# ## Weapons Displaying Different Trends

# In[20]:


sns.set(rc={'figure.figsize':(11.7,6.27)}, font_scale=2)
sns.set_style("whitegrid")
sns.distplot(cod_data[cod_data['fave weapon']=='ICR-7']['kills'],hist=False, label='ICR-7')
sns.distplot(cod_data[cod_data['fave weapon']=='Paladin HB50']['kills'],hist=False, label='Paladian HB50')
sns.distplot(cod_data[cod_data['fave weapon']=='KN-57']['kills'],hist=False, label='KN-57')
sns.distplot(cod_data[cod_data['fave weapon']=='Kar98k']['kills'],hist=False, label='Kar98k')

plt.legend()





#Plot missing data percentages
plot_missing(cod_data)




# ## Weapon Popularity vs Game Modes
plot_heatmap(cod_data, 'mode', 'fave weapon')


# ## Weapon Popularity vs Specialists
plot_heatmap(cod_data, 'fave specialist', 'fave weapon')





