
# R ... you Ready for Python?

Welcome to our Hands-On Training on the integration of R and Python into Tableau!

This sidebar contains some helpful tips and code snippets for you. It will also contain what we show you on stage and the stuff that's in your workbooks. Feel free to copy & paste away!

Have fun, geek out, and don't hesitate to ask us for help when needed!

// Madeline & Josh

===

## Startup RServe or TabPy

*  Double-click the **TC 2019 Lab Files** folder on the desktop and browse to the **19HI-120-020** folder.

Full path: `C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020`

### R Users

* [ ] Double-click the **start-rserve.bat** file

Success means you see this in the console:
```
C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020>"C:\Program Files\R\R-3.6.1\bin\Rscript.exe" "C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020\code-start-rserve.r"
Starting Rserve...
 "C:\Users\LabUser\DOCUME~1\R\WIN-LI~1\3.6\Rserve\libs\x64\Rserve.exe"

C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020>cmd /k
C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020>Rserve: Ok, ready to answer queries.
```

### Python Users

* [ ] Double-click the **start-tabpy.bat** file

Success means you see this in the console:
```
C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020>call C:\users\LabUser\Anaconda3\Scripts\activate.bat TabPy070

(TabPy070) C:\Users\LabUser\Desktop\TC 2019 Lab Files\19HI-120-020>call cd c:\users\LabUser\TabPy-0.7\

(TabPy070) c:\Users\LabUser\TabPy-0.7>call c:\users\LabUser\TabPy-0.7\startup
Checking for presence of Python in the system path variable.
Python 3.7.4
Installing any missing dependencies...
    success
    Check "c:\Users\LabUser\TabPy-0.7"\tabpy-server\install.log for details.
Parsing parameters...
Starting TabPy server...

```
===

## t-Test

### Introduction

In this part you will learn:
1. How to do a basic t-test.
2. How to make a more educated bet on a horse race derby.

![p-values...](https://imgs.xkcd.com/comics/p_values.png)

Your first tasks for this session:

1. Please start by opening this file: `R ... You Ready for Python - Starter.twbx`
2. If a pop-up window appears with some confusing looking code, press the **enter** key.

>[!alert] It is time to choose your profession! Please follow the outline below to connect to a RServe or TabPy!

Connect To External Services (click to enlarge)
![connection_info](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/external_service_connection.gif)



3. Click on the **R: Results Text** or the **Python: Results Text** sheet. You will start the exercise here. You are now at the results page. The t-test should be evaluated here. 

===

### Exercise

To put it into statistical terms: Your exercise is to find out if the difference in mean values for the winners and losers of the horses that raced at Happy Valley Racecourse in Hong Kong can be explained by their declared weight, which is the total weight of the horse and the jockey.

![horse_racing_gif](https://media.tenor.com/images/40924e628ce0ed83b55524c0c04179c9/tenor.gif)

In order to find that out, we need to do a t-test and get the p-value from the result.

>[!note]#### Exercise:
1. Use the measure `[R: p value]` or `[Python: p value]` to calculate an independent t-test and return the p-value from the result of the t-test.
2. The displayed text is generated in the fields `[R: p value evaluation]` and `[Python: p value evaluation]`. You don't need to modify these fields.

>[!hint] You can `print()` out any statement from your Python or R code to the console you have open. Use this to test and troubleshoot your code! 

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] Here are some references for help [R](https://www.statmethods.net/stats/ttest.html) and help [Python](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.ttest_ind.html)

>[!alert] There will be more spoilers if you proceed!

===

The following lines of code may help you out. The xxx represents code you must fill in yourself!

### R
```R
SCRIPT_REAL(
"
# do the t-test here:
t <- t.test( xxx ~ xxx )
# return the p value here:
return(t$xxx)
",
AVG([Declared Weight]), 
ATTR([Won]))
```

### Python
```Python
SCRIPT_REAL(
"
#load packages
import pandas as pd
import numpy as np
from scipy import stats

#create temp data frame with 2 args
d = {'declared_weight': xxx, 'won': xxx}
#subset the data based on d
df = pd.DataFrame(data=d)
print( df.head() )

#subset the data into winning horses and losing horses
winners = df.loc[df['won'] == 1]
losers = df.loc[df['won'] == 0]

#run the t test to return the vector with list of values
t = stats.ttest_ind(xxx['xxx'], xxx['xxx'])
print(t)

#grab the second item in the vector t
return t[xxx]

",
AVG([Declared Weight]), ATTR([Won])

)
```

### Proceed for the full solution.
===

This is how to calculate the p-value:

### R

R Code Solution (click to enlarge)
![t_test_R_Solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/t_test_R_solution.gif)

```R

SCRIPT_REAL(
"
# do the t-test here:
t <- t.test( .arg1 ~ .arg2 )
# return the p value here:
return(t$p.value)
",

AVG([Declared Weight]), 

ATTR([Won]))
```


### Python

Pyhton Code Solution (click to enlarge)
![t_test_R_Solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/t_test_python_solution.gif)

```Python

#p values come in the form of decimals, so use script_real

SCRIPT_REAL(
"
#load packages
import pandas as pd
import numpy as np
from scipy import stats

#create dictionary that you will use to subset the data frame, assigning the correct vectors
d = {'declared_weight': _arg1, 'won': _arg2}
#subset the data frame
df = pd.DataFrame(data=d)
#subset the data frame to create winners and losers data sets
winners = df.loc[df['won'] == 1]
losers = df.loc[df['won'] == 0]

#run the t test
t = stats.ttest_ind(winners['declared_weight'], losers['declared_weight'])

#return the second item from the vector 't'
return t[1]

",

#use the [Declared Weight] and [Won] attributes to read into the dictionary
AVG([Declared Weight]), ATTR([Won])

)
```




The text you see is generated in the fields `[R: p value evaluation]` and `[Python: p value evaluation]` - as we said, you don't need to change these.

Head back to your respective dashboard **R: Result** or **Python: Result** to see the whole picture and find out if you can use declared weight to make a better informed bet on horses at Happy Valley!

Final Dashboard (click to enlarge)
![Python Solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/python_T_Test_solution.PNG)


===

## Addressing & Partitioning

  

Partioning plays a pivotal component in your interactions with External Services in Tableau. Now is your chance to get hands-on and experiment to see exactly what that looks like from within Tableau Desktop.

  

Here we will cover:

1. Creating a new field to use in R or Python

2. The effects of partitioning on the R and Python results

3. How to leverage the console to help debug your code

  

### Exercise: Partitioning

  

>[!note]#### Exercise: Partitioning

1. Open the **R: Partitioning** or **Python: Partitioning** worksheet

2. Drag **index_x_10** to the columns shelf

3. Edit the **index_x_10** field to return 10 times the `index()` value for the given row. The count should display from 10 to 150 across all the rows.

  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4mcImaaXg1VAy4rspAzwWuG9pYVtz9umvdfHe80x-dGAqr1oXNssFpJa5GAUTcekz03RZNyo9iPNDUSSQ8IJxyJRzBv7c0HcplC4HnpaSMVxZrfKseafC6g9klMLvzYWbrDm-8R05OX5-C6k0OOyNDw46kc7u65A8fDL0KnZ070-Di56uhbphgAE7vcEd4JIBtdi4Wsxf_23mj4j1Av1H04A/02a-Table-Down.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mcImaaXg1VAy4rspAzwWuG9pYVtz9umvdfHe80x-dGAqr1oXNssFpJa5GAUTcekz03RZNyo9iPNDUSSQ8IJxyJRzBv7c0HcplC4HnpaSMVxZrfKseafC6g9klMLvzYWbrDm-8R05OX5-C6k0OOyNDw46kc7u65A8fDL0KnZ070-Di56uhbphgAE7vcEd4JIBtdi4Wsxf_23mj4j1Av1H04A/02a-Table-Down.png?psid=1)


>[!alert] Proceed for the full solution.

===

### Solution: Partitioning Table Down

  

The following code will return 10 times the value of **index()** for each row

  

#### R

```R

SCRIPT_INT("

result = .arg1 * 10

",

INDEX()

)

```

#### Python

```Python

SCRIPT_INT("

result = [x * 10 for x in _arg1]

return result

",

INDEX())

```
 

#### Modifying the partitions

1. On the column shelf, click the green pill for **index_x_10**

1. In the menu, select: Compute Using > Table Down

1. Click the Text Label icon above the Columns shelf, or Drag **index_x_10** to the Label card to display the value.

  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4mcImaaXg1VAy4rspAzwWuG9pYVtz9umvdfHe80x-dGAqr1oXNssFpJa5GAUTcekz03RZNyo9iPNDUSSQ8IJxyJRzBv7c0HcplC4HnpaSMVxZrfKseafC6g9klMLvzYWbrDm-8R05OX5-C6k0OOyNDw46kc7u65A8fDL0KnZ070-Di56uhbphgAE7vcEd4JIBtdi4Wsxf_23mj4j1Av1H04A/02a-Table-Down.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mcImaaXg1VAy4rspAzwWuG9pYVtz9umvdfHe80x-dGAqr1oXNssFpJa5GAUTcekz03RZNyo9iPNDUSSQ8IJxyJRzBv7c0HcplC4HnpaSMVxZrfKseafC6g9klMLvzYWbrDm-8R05OX5-C6k0OOyNDw46kc7u65A8fDL0KnZ070-Di56uhbphgAE7vcEd4JIBtdi4Wsxf_23mj4j1Av1H04A/02a-Table-Down.png?psid=1)

  
  

===

### Exercise: Partitioning by Ship Mode

>[!note]#### Exercise: Partitioning by Ship Mode

1. Duplicate the **Partitioning** worksheet you just completed.

2. Modify the partitioning to reset the count for each new **Ship Mode** value. The count should display from 10 to 50, resetting for each Ship Mode.

  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4m9t-jxnWUaka8ktBghesEMirGjdFMjr2oM6S2korfSVvbOT2I8U1k66pNuBx5HN4ZVVnzKhw1fAexbwQKVKBITNNbvt_qa31GUChVrN2RUMveGR9PaOuYMu-uevzccTvqM4r7k61MgixB_njs_E4C4sD_GQZCrzZj4wrxII01qJhQQpGyu_Y3wjph2dbGC4zy47VsnqkifcIugZKdFFyFCg/02b-Pane-Down.png?psid=1&width=598&height=177](https://ch3302files.storage.live.com/y4m9t-jxnWUaka8ktBghesEMirGjdFMjr2oM6S2korfSVvbOT2I8U1k66pNuBx5HN4ZVVnzKhw1fAexbwQKVKBITNNbvt_qa31GUChVrN2RUMveGR9PaOuYMu-uevzccTvqM4r7k61MgixB_njs_E4C4sD_GQZCrzZj4wrxII01qJhQQpGyu_Y3wjph2dbGC4zy47VsnqkifcIugZKdFFyFCg/02b-Pane-Down.png?psid=1&width=598&height=177)

>[!alert] Proceed for the full solution.

===

### Solution: Partitioning Pane Down

  

#### Modifying the partitions

1. On the column shelf, click the green pill for **index_x_10**

1. In the menu, select: Compute Using > Pane Down

1. (Optional): Drag **Ship Mode** to the Color Card

  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4m9t-jxnWUaka8ktBghesEMirGjdFMjr2oM6S2korfSVvbOT2I8U1k66pNuBx5HN4ZVVnzKhw1fAexbwQKVKBITNNbvt_qa31GUChVrN2RUMveGR9PaOuYMu-uevzccTvqM4r7k61MgixB_njs_E4C4sD_GQZCrzZj4wrxII01qJhQQpGyu_Y3wjph2dbGC4zy47VsnqkifcIugZKdFFyFCg/02b-Pane-Down.png?psid=1&width=598&height=177](https://ch3302files.storage.live.com/y4m9t-jxnWUaka8ktBghesEMirGjdFMjr2oM6S2korfSVvbOT2I8U1k66pNuBx5HN4ZVVnzKhw1fAexbwQKVKBITNNbvt_qa31GUChVrN2RUMveGR9PaOuYMu-uevzccTvqM4r7k61MgixB_njs_E4C4sD_GQZCrzZj4wrxII01qJhQQpGyu_Y3wjph2dbGC4zy47VsnqkifcIugZKdFFyFCg/02b-Pane-Down.png?psid=1&width=598&height=177)

  
  

===

### Exercise: Partitioning by Order Priority

>[!note]#### Exercise: Partitioning by Order Priority

1. Duplicate the **Partitioning** worksheet you just completed.

1. Modify the partitioning to reset the count for each new **Order Priority** value. The count should display from 10 to 30, resetting for each Order Priority.

  

>[!hint] With the current visualization, you might have to edit the partition for Specific Dimensions

  

>[!Knowledge] Reading Table Calculations in an English Sentence:

For Each _[unchecked dimension]_ Compute _[script]_ By _[checked dimensions]_

  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4mTKXDcOkxJOP_YYpaAEllfgeyzLxYA5f9SBd2ONS2svxta_3kq6GrMNUrCxdkF2x90SKLryicqZ4seQZ07Lb1AMyT2tOm-msVW4i74Aj0F8pcFe0CijxcAZzLHziQkwHDdm7fceZgBF5omcasW-dpsoe3mmIaIjtjyFpHIX23WhqHWUvQK7pfbWnvvYDopBWikVGyxYNBmm3iOgtN9_xszA/02c-Order-Priority-partition.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mTKXDcOkxJOP_YYpaAEllfgeyzLxYA5f9SBd2ONS2svxta_3kq6GrMNUrCxdkF2x90SKLryicqZ4seQZ07Lb1AMyT2tOm-msVW4i74Aj0F8pcFe0CijxcAZzLHziQkwHDdm7fceZgBF5omcasW-dpsoe3mmIaIjtjyFpHIX23WhqHWUvQK7pfbWnvvYDopBWikVGyxYNBmm3iOgtN9_xszA/02c-Order-Priority-partition.png?psid=1)

  

>[!alert] Proceed for the full solution.

===

### Solution: Partitioning Order Priority

  

#### Modifying the partitions

1. On the column shelf, click the green pill for **index_x_10**

1. In the menu, select: **Edit Table Calculation**

1. Change **Compute Using** to: **Specific Dimensions**

1. Uncheck **Order Priority** and close that window

1. (Optional): Drag **Order Priority** to the Color Card

  
  

**Final Visualization**  _(click to enlarge)_

![https://4h5wnw.ch.files.1drv.com/y4mTKXDcOkxJOP_YYpaAEllfgeyzLxYA5f9SBd2ONS2svxta_3kq6GrMNUrCxdkF2x90SKLryicqZ4seQZ07Lb1AMyT2tOm-msVW4i74Aj0F8pcFe0CijxcAZzLHziQkwHDdm7fceZgBF5omcasW-dpsoe3mmIaIjtjyFpHIX23WhqHWUvQK7pfbWnvvYDopBWikVGyxYNBmm3iOgtN9_xszA/02c-Order-Priority-partition.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mTKXDcOkxJOP_YYpaAEllfgeyzLxYA5f9SBd2ONS2svxta_3kq6GrMNUrCxdkF2x90SKLryicqZ4seQZ07Lb1AMyT2tOm-msVW4i74Aj0F8pcFe0CijxcAZzLHziQkwHDdm7fceZgBF5omcasW-dpsoe3mmIaIjtjyFpHIX23WhqHWUvQK7pfbWnvvYDopBWikVGyxYNBmm3iOgtN9_xszA/02c-Order-Priority-partition.png?psid=1)

  

===

  

### Exercise: Output to Console

>[!note]#### BONUS: Output to Console

### R and Python

1. Add a print line in your code, e.g. ***print('test')***

1. Navigate the command window to observe the output


===

## Network Graphs

### Introduction

In this part we will show you:
1. How to generate fancy looking network graphs in Tableau.
1. How to return more than one value from External Services (R or Python) into Tableau.
1. How to send commands to R or Python only when you're ready to do so.
1. How to add interactivity.
1. Practice partitioning again, combined with the use of dual-axis

First we will build a visualization of the network of airports related to Las Vegas. Move on to the worksheet **R: LAS Flights Origin** or **Python: LAS Flights Origin**.

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/kenlund/15517242227/" title="McCarran International Airport, Las Vegas, Nevada"><img src="https://live.staticflickr.com/3939/15517242227_48c9d4c817_k.jpg" width="1024" alt="McCarran International Airport, Las Vegas, Nevada"></a>

>[!knowledge] Note that the data is already prepared in a usable format. For that we require one file with edge information (here how many connections exist between two airports). The file also contains the number of flights that have occurred for that Origin to Destination route. For Tableau to know how to draw the path the route will take, the route data needs to be duplicated using a self-join and amended a column **`[Path Order]`**.  Have a look at the data source tab for the `2) Flights All Summarized` data source for more details.

The data was taken from an internal reference data source at Tableau, but the data seems consistent with flight data shown on [Stat Computing](http://stat-computing.org/dataexpo/2009/the-data.html).

===

### Example: Airport Network Originating from LAS

This is how to create the network graph:

### R
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

### Python
```Python
# load packages
import pygraphviz as pgv
import pandas as pd
import re

# build data models
df=pd.DataFrame(data={
	'from': _arg1, 
	'to': _arg2, 
	'weight': _arg3, 
	'pathOrder': _arg4, 
	'airport': _arg5})

# Keep only the Origin data for network analysis
df=df[df.pathOrder==1]

airports=pd.DataFrame(data={'airport': _arg5})

# initialize graph
g=pgv.AGraph(strict=False, directed=False, overlap=False, splines=True)

# build graph
for index, row in df.iterrows():
	g.add_edge(row['from'], row['to'])

# assign layout
g.layout(prog='neato')

# extract graph node coordinates
coords=pd.DataFrame(columns=['airport', 'x', 'y', 'degree'])

for n in g.nodes():
	print(str(n) + ': ' + str(g.get_node(n).attr['pos']) )
	new=pd.Series(data={
		'airport': str(n), 
		'x': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(1), 
		'y': re.search(r'(.*),(.*)', str(g.get_node(n).attr['pos'])).group(2), 
		'degree': str(g.degree()[0])})
	coords=coords.append(new, ignore_index=True)

# build return string
ret=airports.set_index('airport').join(coords.set_index('airport'), on='airport', sort=False)

# build return string
ret['ret'] = ret[['x', 'y', 'degree']].apply(lambda x: '~'.join(x), axis=1)

return(ret['ret'].tolist())
", 
MAX([Origin]), 
MAX([Dest]), 
SUM([Flights]), 
MAX([Path Order]), 
MAX([Airport]),
MAX(FALSE)
)
```

We just tricked both R and Python to return multiple pieces of information in the one and only vector/list we can send back from the External Services into Tableau. 

As a next step we need to decompose this string into the three bits of information encoded therein:
- X position, 
- Y position, 
- and betweenness centrality (R) or degree (Python).

===
### Decompose the String into Tokens
>>[!knowledge]Tokenizing strings is simply the process of splitting a string up into sub-strings that contain values which we want to use.

This is how to decompose and extract **X**, **Y**, and the third measure:
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

### Exercise: Flights

>[!note]#### Exercise: Refresh on Demand

The worksheet isn't refreshing. Why? Can you fix it?​

1. Open the **LAS+Others (Flights All Summarized)** worksheet.

2. Figure out why the visualization isn't refreshing.

>[!hint] The reason might have nothing directly to do with the code or external services

  

>[!alert] Proceed for the full solution.

===

### Solution: Refresh on Demand

In this case, the code isn't running because we have disabled Auto-update for the worksheet.

This is a useful feature to know about as you develop your custom scripts *-- though certainly not a requirement*. If you don't turn off **Auto-update** Tableau will just pass the **Script_** code to the external service for each interaction you make with the worksheet _(just as it would update for interactions with your data sources)_.

1. In the icon menu at the top of Tableau Desktop, click the Run-Update Icon ![https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png](https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png)
 (or press F9)

1. Observe the data is now showing in the viz

#### R Initial View
 ![https://4h5wnw.ch.files.1drv.com/y4mzl_QTqdToo3_IN3WqNJGIz4EVLDo5LnOL9kg-KUaPWNfrvpC57TBes5pVNf-Te-qtRoURDiQQ5o8QI_6D5MhrRwakc2IQsT5Hi3tnGZZE80klKC9adfS_9VZDrr5EZ3WMrJ-LcB5nLsnscpVkzFWT4xorg_jMYFQ9nbyJaHLpx9vHvENpiNxZpb8eGY6hLFpPrLj4MNvAd2rEVsXgXYxuA/03r-10-Airports-initial.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mzl_QTqdToo3_IN3WqNJGIz4EVLDo5LnOL9kg-KUaPWNfrvpC57TBes5pVNf-Te-qtRoURDiQQ5o8QI_6D5MhrRwakc2IQsT5Hi3tnGZZE80klKC9adfS_9VZDrr5EZ3WMrJ-LcB5nLsnscpVkzFWT4xorg_jMYFQ9nbyJaHLpx9vHvENpiNxZpb8eGY6hLFpPrLj4MNvAd2rEVsXgXYxuA/03r-10-Airports-initial.png?psid=1)

#### Python Initial View
![https://4h5wnw.ch.files.1drv.com/y4mTIh5clIoQxLKN3spzw2goB3yWIBk6BvmChz4U8c6VAgEAHdTE3xXYWCEhD1Yg69990wukCxmof9uzNS_1A-zfQ2TRP8auCCk4i35icx_zByM5dhM41-qbGtQZCdOBLJnQhYho304VL8SgIZo9Brxl7WxiALUqYFV_lajV2JvipzKB2HSxy3UaTSPvpiLn7Y6JVfWkzIQGy8hsIje8OPkKQ/03p-10-Airports-initial.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mTIh5clIoQxLKN3spzw2goB3yWIBk6BvmChz4U8c6VAgEAHdTE3xXYWCEhD1Yg69990wukCxmof9uzNS_1A-zfQ2TRP8auCCk4i35icx_zByM5dhM41-qbGtQZCdOBLJnQhYho304VL8SgIZo9Brxl7WxiALUqYFV_lajV2JvipzKB2HSxy3UaTSPvpiLn7Y6JVfWkzIQGy8hsIje8OPkKQ/03p-10-Airports-initial.png?psid=1)


===
### Exercise: Flights Partitions and Paths

We have nodes on screen now, but we still need to make some adjustments to see the edges.

>[!note]#### Exercise: Creating the Network Visualization

1. Continue working with **LAS+Others (Flights All Summarized)** worksheet.

1. Adjust the Partitioning to a setting that will allow you to send all the rows to the external service (R/Python) in one call

1. Adjust the visualization to show a secondary axis for the **Y** field.  Make adjustments so one axis is represented as a circle.  The other should be represented by a line, with **Path Order** used as the path.  


>[!alert] Proceed for some hints

===
### Hints: Flights Partitions and Paths
>[!hint]
* To send the data all at once, all of the dimensions should be checked, i.e. **Path Order**, **Dest**, and **Origin**
* Duplicate the **Y** field that is on the row shelf _(CTRL + Click and Drag to the right)_.  Be sure to set this field as a secondary axis
* Adjust the **Y** measure in the marks card area to have the first entry _(right below "All")_ represented as a line.  

>[!alert] Proceed for the full solution
===
### Solution: Partitions and Paths

We started with the partitioning setup not quite correct, and only a singular axis.  To solve this exercise, we needed to create another axis and leverage **Path Order** to define our path.

1. Edit the Table Calculations for both the **X** and **Y** fields, using specific dimensions.  All of the dimensions should be checked, i.e. **Path Order**, **Dest**, and **Origin**
1. Duplicate the **Y** field that is on the row shelf _(CTRL + Click and Drag to the right)_.  
1. Press F9 or Update the worksheet with the icon in the menu bar. ![https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png](https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png)

1. Set the secondary **Y** field you just added as a dual axis.  
1. Within the Marks card area, adjust the first **Y** measure's mark card.  Change the drop-down from circle to Line.
1. Change the **Path Order** blue pill on Color to continuous.
1. Duplicate the _(now green)_ **Path Order** pill that we just worked on and drop it onto the Path card.
1. Press F9 or Update the worksheet with the icon in the menu bar. ![https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png](https://help.tableau.com/v2019.3/pro/desktop/en-us/Img/runquery.png)

#### R Final Visualization
![https://4h5wnw.ch.files.1drv.com/y4mJihvNp2KW3eQbXbcNeKLYqTM8INUFWHjndDtcLR1xeeY8VIL51ylOoUrz0Pb8wOW1ATcg-ZnnX0cglOrwKZTfbYT3dsNf_OOxR_rwsAXOVW8dRTUGvdhmtxbQxzTPWmlBlr3KDLeb5knS1qRkQ2slbRUiOUiOetfsicnl4rCMlpFgiEKLUDtYy4lfu9tNgcn5fRHQ8t5KMpP_9-knAR1PQ/03r-20-Airports-Final.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mJihvNp2KW3eQbXbcNeKLYqTM8INUFWHjndDtcLR1xeeY8VIL51ylOoUrz0Pb8wOW1ATcg-ZnnX0cglOrwKZTfbYT3dsNf_OOxR_rwsAXOVW8dRTUGvdhmtxbQxzTPWmlBlr3KDLeb5knS1qRkQ2slbRUiOUiOetfsicnl4rCMlpFgiEKLUDtYy4lfu9tNgcn5fRHQ8t5KMpP_9-knAR1PQ/03r-20-Airports-Final.png?psid=1)

#### Python Final Visualization
![https://4h5wnw.ch.files.1drv.com/y4mqXAIbl8hwvczDfEfiMl09NyyfMjLLDwA3FPNIu2M_ISLu7qV11HW4FnqI7F4NQhW2S8lNLWsHRvOPZqG33adtWBWdALfX54lIGhx4yM_vBWVHJkCYTWeWnUli7IZrRJGlIbSLrvWP9rNA426dvkq0cp7491dROuqmIMLvqaiwUsLM4tin3z-pgFBkyJ9Isl591R302z8iVo8OKvs0pMmPw/03p-20-Airports-Final.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mqXAIbl8hwvczDfEfiMl09NyyfMjLLDwA3FPNIu2M_ISLu7qV11HW4FnqI7F4NQhW2S8lNLWsHRvOPZqG33adtWBWdALfX54lIGhx4yM_vBWVHJkCYTWeWnUli7IZrRJGlIbSLrvWP9rNA426dvkq0cp7491dROuqmIMLvqaiwUsLM4tin3z-pgFBkyJ9Isl591R302z8iVo8OKvs0pMmPw/03p-20-Airports-Final.png?psid=1)

===
### Exercise: Adding Interactivity

>[!note]#### Exercise: Adding Interactivity
Now that we have a Network Graph, we can start to leverage the power of External Services + Tableau. We'll add a simple example -- the ability to highlight the origin airport.  Add a highlighter for the origin airport to the visualization.

>[!alert] Proceed for the full solution
===
### Solution: Interactivity

1. Navigate to the **Analysis** menu.
1. Select: _Analysis_ > _Highlighters_ > _Origin_
1. Make some changes to the Highlight card to see your selected airport highlighted on the visualization.

#### Python Example (LAS Highlighted)
![https://4h5wnw.ch.files.1drv.com/y4mbbiQno3eom6P9uiBOftSDWD3HIekIV6RqmZTxWLQZXJz0bbvKISkjd40MqD8H3TrnWNrM-8dT_cd0813do3Ti8vWZZNc0DUs1H3I7-1tpD6dDMZmpKNnCLKk49SCg-gKVr7wnNX_mS5e32mH7BKTi_DLIVXep3lCUrWuxpuLWuRaFzI-IEH6KKbMo_9YZpkb28P2LqsQhk9no7fnrha3Rg/03p-30-Airports-Highlights.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4mbbiQno3eom6P9uiBOftSDWD3HIekIV6RqmZTxWLQZXJz0bbvKISkjd40MqD8H3TrnWNrM-8dT_cd0813do3Ti8vWZZNc0DUs1H3I7-1tpD6dDMZmpKNnCLKk49SCg-gKVr7wnNX_mS5e32mH7BKTi_DLIVXep3lCUrWuxpuLWuRaFzI-IEH6KKbMo_9YZpkb28P2LqsQhk9no7fnrha3Rg/03p-30-Airports-Highlights.png?psid=1)

#### R Example (LAS Highlighted)
![https://4h5wnw.ch.files.1drv.com/y4m43iYd_IRjejQ9y-VASMxLjalqGsyCIv5khA3DM8LavWhqdqbtRpSXfdqE5HWepBeMH438MYZHgXBZtbApOfY2SCF4muF9dj1YKrJNwwkF-KTYb-xtJ0gsKI9X821fldnSeigZRgwaFVD7J6B62KImBgb02raEodEVtqa_7AA4_2q7wEs8eRkwMOOLQC7k9k-FC7tn6MqvSKfD-b1OB6phw/03r-30-Airports-Highlights.png?psid=1](https://4h5wnw.ch.files.1drv.com/y4m43iYd_IRjejQ9y-VASMxLjalqGsyCIv5khA3DM8LavWhqdqbtRpSXfdqE5HWepBeMH438MYZHgXBZtbApOfY2SCF4muF9dj1YKrJNwwkF-KTYb-xtJ0gsKI9X821fldnSeigZRgwaFVD7J6B62KImBgb02raEodEVtqa_7AA4_2q7wEs8eRkwMOOLQC7k9k-FC7tn6MqvSKfD-b1OB6phw/03r-30-Airports-Highlights.png?psid=1)
===

### Exercise: Buyer and Seller Relationships

For your exercise we're looking at another relationship network: that between customers ("buyers") and sellers on ebay. Move on to the worksheet **R: Network Analysis (Buyer-Seller)** or **Python: Network Analysis (Buyer-Seller)**.

![Buyer-Seller!](https://c.pxhere.com/images/fc/44/d7ee5cfc2f73f2c97297e7f3d010-1452877.jpg!d)

>[!knowledge] This data set is also already prepared for you in a usable format, similar to what we outlined above for the airport data. If you're interested, have a look at the data source tab for the `3) Buyer-Seller` data source for more details.

>[!note]#### Exercise:
1. Give the end user of your network graph the option to choose between various types of network graph layouts. We already created parameters (one for R, one for Python) to allow for the selection. See if you can figure out how to embed this selection into the actual R or Python code.
2. As it's hard to distinguish which node is a buyer and which are the sellers, create a new dimension `[Type]` that will allow the end user to visually distinguish the two in the network graph.

>[!hint] You can `print()` out any statement from your R or Python code to the console you have open. Use this to test and troubleshoot your code!

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] 1. Note how the functions to generate graph layouts are being called, especially in the R code. Think of a good way of injecting whatever the parameters return into those function calls.
2. Creating the dimension shouldn't be the issue, but keep an eye out to what happens when you add it to the viz. HOw could you prevent that from happening?

>[!alert] If you're done, stuck, or want to give up, the full solutions in R and Python are shown on the next page.

===

### Solution: Buyer and Seller Relationships

### R
```R
SCRIPT_STR("
# load packages
library(igraph)
library(dplyr)
set.seed(2811)

# build data models
data <- data.frame(buyer = .arg1, 
                   seller = .arg2, 
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
MAX([Seller]), 
SUM([Meetings]), 
MAX([Path Order]), 
MAX([Person]))
```

### Python
```Python
SCRIPT_STR("
# load packages
import pygraphviz as pgv
import pandas as pd
import re

# build data models
df=pd.DataFrame(data={
	'buyer': _arg1, 
	'seller': _arg2, 
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
	g.add_edge(row['buyer'], row['seller'])

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
MAX([Seller]), 
SUM([Meetings]), 
MAX([Path Order]), 
MAX([Person]))
```

Note how the parameter is embedded into the code in a rather unusual way! Since the function call to render the graph layout in both R and Python requires different methods to be called (e.g. `layout_with_fr()` in R or `g.layout(prog='neato')`) we implanted the return string from the parameter directly into the "code" part of the `SCRIPT_*()` function, which technically is also just a string. (NB: We could have implemented it the "classic" way in Python, but decided to keep this consistent for both languages.)

The new dimension `[Type]` looks like this:

```Type
IF LEFT([Person], 1) == "b" THEN "Buyer" ELSE "Seller" END
```

Note that you can't just drag it onto the Color shelf as a dimension, as this would change the addressing and partitioning of our `SCRIPT_*()` functions - remember: they're Table Calculations! The trick is, to use them as attributes, by wrapping them in `ATTR()`.

===

## Sentiment Analysis

### Introduction

In this part you will learn:
1. How to do a sentiment analysis and display the results.
2. How to use parameters to change the output of your code.
3. Which Top 1 Chart songs from the UK and US have the most positive or negative sentiment.


Please move to the worksheet **R: Lyrics Sentiment** or **Python: Lyrics Sentiment**.

![Sing with me](https://www.edmsauce.com/wp-content/uploads/2018/03/Spotify-Lyrics-1068x601.jpg)

>[!knowledge] The data contains the songs and lyrics of the Top #1 Songs of the UK and US charts of the past 70 years. If you want to read up where the data is from and have a look at some other paths of analysis for it, please visit [this Tableau Public Story](https://public.tableau.com/profile/jonas5035#!/vizhome/Spottify-AnalytischeAnwendungen/MusicAnalysis).

===
### Exercise

In this exercise you need to adjust the measure `[R: Polarity]` or `[Python: Polarity]` to calculate the polarity of all lyrics in one RServe or TabPy call. The result should either be the positive or negative sentiment score, depending on the parameter `[R: Polarity Chooser]` or `[Python: Polarity Chooser]`.

>[!note]#### Exercise:
1. Use the measure `[R: Polarity]` or `[Python: Polarity]` to calculate a sentiment score / polarity.

2. Make use of the parameters `[R: Polarity Chooser]` or `[Python: Polarity Chooser]` to get only one column back, either the positive or negative sentiment score.

3. Add the `[R: Polarity]` or `[Python Polarity]` field to the view and create a boxplot (either use show me, or from scratch).

Optional Bonus: Create a dashboard with your boxplot worksheet that also has a URL action to listen to the song on Spotify Web Player.
Hint: use https://open.spotify.com/track/<ATTR(Song Id)>

The outcome should look like this (click to enlarge):
![result-python-sentiment.png](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/sentiment_analysis_solution.PNG)

>[!Alert] ### Python
Please make sure to calculate the sentiment score during **one** execution of the code for all songs! You are able to execute the code for each song individually, but that will take a lot of time.

>[!hint] You can `print()` out any statement from your R or Python code to the console you have open. Use this to test and troubleshoot your code!

The following pages contains help on various levels. If you need a little jumpstart to the solution: proceed.

===

>[!hint] For your R solution, lookup the function help [analyzeSentiment()](https://cran.r-project.org/web/packages/SentimentAnalysis/vignettes/SentimentAnalysis.html).  Python users should lookup the function help [polarity_scores()](https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f)

>[!alert] There will be more spoilers if you proceed!

===
### Starter Solution
The following lines of code may help you out. The xxx represents code you must fill in yourself!

### R
```R

SCRIPT_REAL("

# load in required packages
library(SentimentAnalysis)

# do the sentiment analysis on the whole vector
polarity <- analyzeSentiment(xxx)

# return NegativityGI or PositivityGI depending on parameter input
return(polarity[,xxx[xxx]])

",MIN([Lyrics]), [R: Polarity Chooser])
```

### Python
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

## Proceed for Full Solution

This is how to analyze the song lyrics' sentiment:

### R

R Code Solution (click to enlarge):
![result-r-sentiment.gif](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/r_sentiment_solution.gif)


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

### Python

Python Code Solution (click to enlarge):
![result-python-sentiment](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/python_sentiment_solution.gif)

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

Boxplot Building (click to enlarge):
![boxplot_gif](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/python_sentiment_boxplot.gif)

1. Once you have completed the Polarity variable, drag `[R: Polarity]` or `[Python: Polarity]` to rows. 

2. Then, create the boxplot using show me. Fit the display to 'Entire View', and format the size of the marks to be larger.

3. Drag `[R: Polarity]` or `[Python: Polarity]` to color on the marks card.

4. Interact with the parameter to see how the boxplot changes.

5. Optional Challenge: To create the clickable link to listen to the song, add your worksheet to a dashboard. Then, add a URL action using 'Menu' and the link https://open.spotify.com/track/<ATTR(Song Id)>.

Optional Challenge Solution (click to enlarge)
![URL_action](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/python_sentiment_dashboard.gif)

The R solution is pretty straight forward since the function itself accepts a vector. To determine the return value, the text of a parameter can be used. For Python the implementation looks a little bit different, because the function we are using does not take a list, but an atomic string value. To accomodate that, we need a `for` loop. Otherwise the Python code would need to be evaluated for each and every song, which takes longer than the `for` loop because of transfer and package load times.

===

### Exercise: NEW in 2019.3 - Pre-processing with Prep Builder

In this exercise, we will move to Tableau Prep Builder to conduct an exercise using our new external services feature, recently released in 2019.3! We will conduct sentiment analysis on yelp reviews of buffets in Vegas to determine each review's compound sentiment score.

![buffet-image](https://cdn.citynomads.com/wp-content/uploads/2019/09/09170827/Coffee-Lounge-Dessert-Buffet-With-Mao-Shan-Wang-and-D24-Durian-Delights.jpg)

For now, you can just listen to how Prep Builder interacts with R and Python.

===

Move to the Tableau Prep Shortcut on the Desktop and open the flow titled **yelp_starter_flow.tflx**.
If a security warning comes up, click 'Load'.

![data_security_warning](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/data_security_warning.PNG)

1. Create a dummy variable (null column) for the script to populate once it runs.
2. Edit the .py file or .R file in the Lab Files Folder to write a function 'classify_sentiment' that takes a dataframe as its input and outputs a 'compound' sentiment score into the dummy variable column.
3. Save the file!
4. Go to the 'Script' step and connect to the correct server and file, then add the function name 'classify_sentiment' to the 'function name' field.
5. Run the flow to see the null column populate!

Optional bonus challenge: First filter to ~1K rows, then edit the function to output another column with positive or negative sentiment.


The outcome should look like this (click to enlarge):
![prep_solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/prep_solution.PNG)

>[!alert] There will be more spoilers if you proceed!
==


The following lines of code may help you out. The xxx represents code you must fill in yourself!

### Creating a dummy variable

Create your dummy variable like this (click to enlarge):
![dummy_variable_gif](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/dummy_variable_gif.gif)

### R
```R
library(SentimentAnalysis)
library(SnowballC)
library(Rserve)

#create a function that takes 1 input, a datafrme
classify_sentiment <- function(prep_data_frame) {
  
  #grab the column with review text
  df_text <- prep_data_frame[,'xxx']
  #create a vector and assign it the sentiment analysis results
  sentiment_vector <- analyzeSentiment(xxx);
  #grab the right score to return
  compound <- xxx[, 'SentimentQDAP'];
  #assign score to the sentiment column in the dataframe
  prep_data_frame$sentiment <- xxx
  #return the dataframe 
  return(prep_data_frame)
}
```

### Python
```Python

#import packages
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def classify_sentiment(prep_data_frame):
    print('creating list to append to...')
    #use lambda function to grab the 'compound' sentiment score from the polarity score vector
    scores = prep_data_frame['xxx'].apply(lambda x:
                                      SentimentIntensityAnalyzer().polarity_scores(x)['xxx'])
    

    #add back to dataframe
    prep_data_frame['xxx'] = xxx
    print('added sentiment to dataframe... now returning dataframe')
    #return data frame
    return(prep_data_frame)
```

### Proceed for the full solution.
===

### R

R Code Solution (click to enlarge):
![r-sentiment-prep-solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/r_sentiment_prep_solution.gif)

```R

library(SentimentAnalysis)
library(SnowballC)
library(Rserve)

classify_sentiment_<- function(prep_data_frame){
  df_text <- data_frame[,'text']
  sentiment_vector <- analyzeSentiment(df_text);
  compound <- sentiment_vector[, 'SentimentQDAP'];
  prep_data_frame$sentiment <- compound
  return(prep_data_frame)
}
```

### Python

Python Code Solution (click to enlarge):
![edit_python_script](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/python_prep_sentiment_solution.gif)

```Python
#import packages
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def classify_sentiment(prep_data_frame):
    print('creating list to append to...')
    #use lambda function to grab the 'compound' sentiment score from the polarity score vector
    scores = prep_data_frame['text'].apply(lambda x:
                                      SentimentIntensityAnalyzer().polarity_scores(x)['compound'])
    

    #populate sentiment column with the scores vector
    prep_data_frame['sentiment'] = scores
    print('added sentiment to dataframe... now returning dataframe')
    #return data frame
    return(prep_data_frame)
    
```


### Final Result
![prep_solution](https://raw.githubusercontent.com/madelinefromtableau/TC2019/master/prep_solution.PNG)



## Done!

You're work here is done! Now it's time to sit back, relax, and take in the other nuggets of information we have prepared for you.

Awesome job data rockstars! See you at next year at TC2020!

//Madeline and Josh
