
# R ... you Ready for Python?

Welcome to our Hands-On Training on the integration of R and Python into Tableau!

This sidebar contains some hopefully helpful tips and code snippets for you in addition to what we show you on stage and also to the stuff that's contained in your workbooks. Feel free to copy & paste away!

Have fun, geek out, and don't hesitate to ask us for help when needed!

Love 

// Konstantin & Lennart

===

## t-Test

### Introduction

In this part you will learn:
1. How to do a basic t-test.
2. That Trekkies are superior in R and Python to Star Wars fans.

![p-values...](https://imgs.xkcd.com/comics/p_values.png)

Here's your first tasks for this session:

1. Please start by opening this file: `R ... You Ready for Python - Starter.twbx`
2. Move to the tab **Entry** and fill out the survey. If you are done hit the button to move on.
3. Login to PostgreSQL with username `questionnaire` and password `tce2019berlin`

>[!alert] It is time to choose your profession! Please follow the outline below to connect to a RServe or TabPy! 
!IMAGE[Choose wisely!](choose-r-or-python.png)

4. Click the R or Python button on the dashboard **Entered** to proceed. 

You are now at the results page. The t-test should be evaluated here. To get started on the first exercise you can move to the sheet **R: Result Text** if you are an R user or to **Python: Result Text** if you are a Pythonista.

===

### Exercise

To put it into statistical terms: Your exercise is to find out if the difference in median values for the R or Python proficiency of the attendees of this hands-on training can be explained by them liking Star Trek or Star Wars more.

In order to find that out, we need to do a t-test and get the p-value from the result.

>[!note]#### Exercise:
1. Use the measure `[R: p value]` or `[Python: p value]` to calculate an independent t-test and return the p-value from the result of the t-test.
2. The displayed text is generated in the fields `[R: p value evaluation]` and `[Python: p value evaluation]`. You don't need to modify these fields.

>[!hint] You can `print()` out any statement from your R or Python code to the console you have open. Use this to test and troubleshoot your code!

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] Here are some references for help [R](https://www.statmethods.net/stats/ttest.html) and help [Python](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.ttest_ind.html)

>[!alert] There will be more spoilers if you proceed!

===

The following code lines could help you out.

```R
SCRIPT_REAL(
"
# do the t-test here:
t <- t.test( xxx ~ xxx )
# return the p value here:
return(t$xxx )
",
AVG([Value]), 
ATTR([Category]))
```

```Python
SCRIPT_REAL(
"
# Load packages
import pandas
from scipy import stats

# create 2 dataframes for both categories
d = {'value': _arg1, 'category': _arg2}
df = pandas.DataFrame(data=d)
startrek = df.loc[df['category']=='Star Trek']
starwars = df.loc[df['category']=='Star Wars']

# do the t-test here:
t = stats.ttest_ind(xxx['xxx'],xxx['xxx'])

# return the p-value here
return(t[xxx])
",
AVG([Value]), 
ATTR([Category]))
```

Proceed for the full solution.
===

This is how to calculate the p-value:

```R
SCRIPT_REAL(
"
# do the t-test here:
t <- t.test( .arg1 ~ .arg2 )
# return the p value here:
return(t$p.value)
",
AVG([Value]), 
ATTR([Category]))
```

```Python
SCRIPT_REAL(
"

# Load packages
import pandas
from scipy import stats

# create 2 dataframes for both categories
d = {'value': _arg1, 'category': _arg2}
df = pandas.DataFrame(data=d)
startrek = df.loc[df['category']=='Star Trek']
starwars = df.loc[df['category']=='Star Wars']

# do the t-test here:
t = stats.ttest_ind(startrek['value'],starwars['value'])

# return the p-value here
return(t[1])
",
AVG([Value]), 
ATTR([Category]))
```

The text you see is generated in the fields `[R: p value evaluation]` and `[Python: p value evaluation]` - as we said, you don't need to change these.

Head back to your repective dashboard **R: Result** or **Python: Result** to see the whole picture and find out you really are the better R or Python coder just by liking Star Trek or Star Wars more!

===

## Network Graphs

### Introduction

In this part we will show you:
1. How to generate fancy looking network graphs in Tableau.
2. How to return more than one value from External Services (R or Python) into Tableau.

First we will build a visualization of the network of German airports. Move on to the worksheet **R: Network Analysis (Flights)** or **Python: Network Analysis (Flights)**.

![Berlin Tegel Airport](https://raw.githubusercontent.com/kgreger/tce19-r-you-ready-for-python/master/img/berlin-tegel.jpg)

>[!knowledge] Note that the data is already prepared in a usable format. For that we require one file with the node information (here the airports) and one file with the edge information (here how many connection exist between two airports). The route data needs to be duplicated using a self-join and amended a column `[Path Order]`, then the airports need to be joined to the duplicated routes once for the `[To]` and `[From]` locations, respectively. Have a look at the data source tab for the `2) OpenFlights (Germany)` data source for more details.

The data was taken from the [OpenFlights database](https://openflights.org/data.html).

===

### Example: German Airport Network

This is how to create the network graph:

```R
SCRIPT_STR("
library(igraph)
library(dplyr)
set.seed(2811)

data <- data.frame(from = .arg1, 
                   to = .arg2, 
                   weight = .arg3, 
                   pathOrder = .arg4) %>% 
  filter(pathOrder == '1')
airports <- data.frame(airport = .arg5)

g <- graph_from_data_frame(data)

coords <- layout_with_fr(g) %>% 
  cbind(data.frame(airport = V(g)$name, 
                   betweenness = betweenness(g)))

ret <- left_join(airports, 
                 coords, 
                 by = 'airport')

paste(ret[, 2], ret[, 3], ret[, 4], 
      sep = '~')
", 
MAX([From]), 
MAX([To]), 
SUM([Routes]), 
MAX([Path Order]), 
MAX([Airport]))
```

```Python
SCRIPT_STR("
import pygraphviz as pgv
import pandas as pd
import re

df=pd.DataFrame(data={
	'buyer': _arg1, 
	'escort': _arg2, 
	'meetings': _arg3, 
	'pathOrder': _arg4, 
	'person': _arg5})
df=df[df.pathOrder==1]

persons=pd.DataFrame(data={
	'person': _arg5})

g=pgv.AGraph(strict=False, directed=False)

for index, row in df.iterrows():
	g.add_edge(row['buyer'], row['escort'])

g.layout(prog='neato')

coords=pd.DataFrame(columns=['person', 'x', 'y', 'degree'])

for n in g.nodes():
	new=pd.Series(data={
		'person': str(n), 
		'x': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(1), 
		'y': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(2), 
		'degree': str(g.degree()[0])})
	coords=coords.append(new, ignore_index=True)

ret=persons.set_index('person').join(coords.set_index('person'), on='person', sort=False)
ret['ret'] = ret[['x', 'y', 'degree']].apply(lambda x: '~'.join(x), axis=1)
return(ret['ret'].tolist())
", 
MAX([Buyer]), 
MAX([Escort]), 
SUM([Meetings]), 
MAX([Path Order]), 
MAX([Person]))
```

So we tricked both R and Python to return multiple pieces of information in the one and only vector/list we can send back from the External Services into Tableau. 

As a next step we need to decompose this string into the three bits of information encoded therein:
- X position, 
- Y position, 
- and betweenness centrality (R) or degree (Python).

>[!knowledge] The reason we're calculating the (rather boring) overall network degree in Python instead of each node's way more interesting betweenness centrality is that the excellent `igraph` library we're using in the R code requires Python 3 to run, while we decided to set this lab up with Python 2.7. As a result we're now bound to the inferior (in terms of functionality and performance) `pygraphviz` library, which doesn't allow for the calculation of centrality measures.

This is how to decompose and extract `X`, `Y`, and the third measure:
```X
FLOAT(LEFT([R: Graph], FIND([R: Graph], '~') - 1))
```

```Y
FLOAT(LEFT(RIGHT([R: Graph], LEN([R: Graph]) - FIND([R: Graph], '~')), 
      FIND(RIGHT([R: Graph], LEN([R: Graph]) - FIND([R: Graph], '~')), '~') - 1))
```

```Betweenness/Degree
FLOAT(RIGHT([R: Graph], LEN([R: Graph]) - FIND([R: Graph], '~', FIND([R: Graph], '~') + 1)))
```

===

### Exercise: Escort Relationships

For your exercise we're looking at another relationship network: that between customers ("buyers") and employees at an escort service. Move on to the worksheet **R: Network Analysis (Escort)** or **Python: Network Analysis (Escort)**.

![Romance!](https://raw.githubusercontent.com/kgreger/tce19-r-you-ready-for-python/master/img/romantic-date.jpg)

>[!knowledge] This data set is also already prepared for you in a usable format, similar to what we outlined above for the airport data. If you're interested, have a look at the data source tab for the `3) Escorts` data source for more details.

The data was taken from the [Koblenz Network Collection (KONECT) repository](http://konect.uni-koblenz.de/networks/escorts). If you're interested in a scientific analysis of the data, you can also read the [accompanying research paper](https://arxiv.org/ftp/arxiv/papers/1003/1003.3089.pdf).

>[!note]#### Exercise:
1. Give the end user of your network graph the option to choose between various types of network graph layouts. We already created parameters (one for R, one for Python) to allow for the selection. See if you can figure out how to embed this selection into the actual R or Python code.
2. As it's hard to distinguish which node is a buyer and which are the escorts, create a new dimension `[Type]` that will allow the end user to visually distinguish the two in the network graph.

>[!hint] You can `print()` out any statement from your R or Python code to the console you have open. Use this to test and troubleshoot your code!

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] 1. Note how the functions to generate graph layouts are being called, especially in the R code. Think of a good way of injecting whatever the parameters return into those function calls.
2. Creating the dimension shouldn't be the issue, but keep an eye out to what happens when you add it to the viz. HOw could you prevent that from happening?

>[!alert] If you're done, stuck, or want to give up, the full solutions in R and Python are shown on the next page.

===

### Solution: Escort Relationships

```R
SCRIPT_STR("
# load packages
library(igraph)
library(dplyr)
set.seed(2811)

# build data models
data <- data.frame(buyer = .arg1, 
                   escort = .arg2, 
                   meetings = .arg3, 
                   pathOrder = .arg4) %>% 
  filter(pathOrder == '1')
persons <- data.frame(person = .arg5)

# initialize & build graph
g <- graph_from_data_frame(data)

# assign layout & extract graph node coordinates
## you need to change something here!
coords <- " + [R: Please select model] + "(g) %>% 
  cbind(data.frame(person = V(g)$name, 
                   betweenness = betweenness(g)))

# build return string
ret <- left_join(persons, 
                 coords, 
                 by = 'person')

paste(ret[, 2], ret[, 3], ret[, 4], 
      sep = '~')
", 
MAX([Buyer]), 
MAX([Escort]), 
SUM([Meetings]), 
MAX([Path Order]), 
MAX([Person]))
```

```Python
SCRIPT_STR("
# load packages
import pygraphviz as pgv
import pandas as pd
import re

# build data models
df=pd.DataFrame(data={
	'buyer': _arg1, 
	'escort': _arg2, 
	'meetings': _arg3, 
	'pathOrder': _arg4, 
	'person': _arg5})
df=df[df.pathOrder==1]

persons=pd.DataFrame(data={
	'person': _arg5})

# initialize graph
g=pgv.AGraph(strict=False, directed=False)

# build graph
for index, row in df.iterrows():
	g.add_edge(row['buyer'], row['escort'])

# assign layout
## you need to change something here!
g.layout(prog='" + [Python: Please select model] + "')

# extract graph node coordinates
coords=pd.DataFrame(columns=['person', 'x', 'y', 'degree'])

for n in g.nodes():
	new=pd.Series(data={
		'person': str(n), 
		'x': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(1), 
		'y': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(2), 
		'degree': str(g.degree()[0])})
	coords=coords.append(new, ignore_index=True)

# build return string
ret=persons.set_index('person').join(coords.set_index('person'), on='person', sort=False)
ret['ret'] = ret[['x', 'y', 'degree']].apply(lambda x: '~'.join(x), axis=1)
return(ret['ret'].tolist())
", 
MAX([Buyer]), 
MAX([Escort]), 
SUM([Meetings]), 
MAX([Path Order]), 
MAX([Person]))
```

Note how the parameter is embedded into the code in a rather unusual way! Since the function call to render the graph layout in both R and Python requires different methods to be called (e.g. `layout_with_fr()` in R or `g.layout(prog='neato')`) we implanted the return string from the parameter directly into the "code" part of the `SCRIPT_*()` function, which technically is also just a string. (NB: We could have implemented it the "classic" way in Python, but decided to keep this consistent for both languages.)

The new dimension `[Type]` looks like this:

```Type
IF LEFT([Person], 1) == "b" THEN "Buyer" ELSE "Escort" END
```

Note that you can't just drag it onto the Color shelf as a dimension, as this would change the addressing and partitioning of our `SCRIPT_*()` functions - remember: they're Table Calculations! The trick is, to use them as attributes, by wrapping them in `ATTR()`.

===

## Sentiment Analysis

### Introduction

In this part you will get to know:
1. How to do a sentiment analysis and display the results.
2. How to use parameters to change the output of our code.
3. Which Top 1 Chartsongs from the UK and US have the most positive and negative sentiment.

Move on to the worksheet **R: Lyrics Sentiment** or **Python: Lyrics Sentiment**.

![Sing with me](https://www.edmsauce.com/wp-content/uploads/2018/03/Spotify-Lyrics-1068x601.jpg)

>[!knowledge] The data contains the songs and lyrics of the Top #1 Songs of the UK and US charts of the past 70 years. If you want to read up where the data is from and have a look at some other paths of analysis for it, please visit [this Tableau Public Story](https://public.tableau.com/profile/jonas5035#!/vizhome/Spottify-AnalytischeAnwendungen/MusicAnalysis).

===

### Exercise

In this exercise you need to adjust the measure `[R: Polarity]` or `[Python: Polarity]` to calculate the polarity of all lyrics in one RServe or TabPy call. The result should either be the positive or negative sentiment score, depending on the parameter `[R: Polarity Chooser]` or `[Python: Polarity Chooser]`.

>[!note]#### Exercise:
1. Use the measure `[R: Polarity]` or `[Python: Polarity]` to calculate a sentiment score / polarity.
2. Make use of the parameters `[R: Polarity Chooser]` or `[Python: Polarity Chooser]` to get only one column back, either the positive or negative sentiment score.

The outcome should look like this:
!IMAGE[result-python-sentiment.png](result-python-sentiment.png)

>[!Alert] ### Python
Please make sure to calculate the sentiment score during **one** execution of the code for all songs! You are able to execute the code for each song individually, but that will take a lot of time.

>[!hint] You can `print()` out any statement from your R or Python code to the console you have open. Use this to test and troubleshoot your code!

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] For your R-lution, lookup the function help [analyzeSentiment()](https://cran.r-project.org/web/packages/SentimentAnalysis/vignettes/SentimentAnalysis.html).  Pythonistas should lookup the function help [polarity_scores()](https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f)

>[!alert] There will be more spoilers if you proceed!

===

The following code lines could help you to out.

```R
SCRIPT_REAL("
# load in required packages
library(SentimentAnalysis)

# do the sentiment analysis on the whole vector
polarity <- analyzeSentiment(xxx)

# return NegativityGI or PositivityGI depending on parameter input
return(polarity[,xxx[x]])

",MIN([Lyrics]), [R: Polarity Chooser])
```

```Python
SCRIPT_REAL("
# load in packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initiate the analyzer
analyzer = SentimentIntensityAnalyzer()

# hand over all the lyrics to the analyzer
# cycle through all lyrics and append their values to a list
# from the polarity_scores function you only need the values for pos or neg, depending on your parameter
scores= [ ]
for lyric in xxx:
    scores.append(analyzer.polarity_scores(lyric)[xxx[0]])
   
# return the scores
return scores

",MIN([Lyrics]), [Python: Polarity Chooser])
```

>[!alert] Proceed for full solution.
===

This is how to analyze the song lyrics' sentiment:

```R
SCRIPT_REAL("
# load in required packages
library(SentimentAnalysis)

# do the sentiment analysis on the whole vector
polarity <- analyzeSentiment(.arg1)

# return NegativityGI or PositivityGI depending on parameter input
return(polarity[,.arg2[1]])

", 
MIN([Lyrics]), 
[R: Polarity Chooser])
```

```Python
SCRIPT_REAL("
# load in packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initiate the analyzer
analyzer = SentimentIntensityAnalyzer()

# hand over all the lyrics to the analyzer
# cycle through all lyrics and append their values to a list
# from the polarity_scores function you only need the values for pos or neg, depending on your parameter
scores= [ ]
for comment in _arg1:
    scores.append(analyzer.polarity_scores(comment)[_arg2[0]])
   
# return the scores
return scores

", 
MIN([Lyrics]), 
[Python: Polarity Chooser])
```

For R the solution is pretty straight forward since the function itself accepts a vector. To determine the return value, the text of a parameter can be used. For Python the implementation looks a little bit different, because the function we are using does not take a list, but an atomic string value. To accomodate that, we need a `for` loop because otherwise the Python code needs to be evaluated for each and every song, which takes long because of transfer and package load times.

===

## Done!

You're work here is done! Now it's time to sit back, relax, and take in the other nuggets of information we have prepared for you.

Live long and prosper! See you at TC19 in Las Vegas or next year at TCE20!

Love 

// Konstantin & Lennart
