# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:17:58 2023

@author: Lenovo
"""

#Python for datascience : Matplotlib
#Used to plot the graphs
#imp for machine learning vitualisation

#ploting a single line
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()
plt.legend()

###########################################################################3

#multiline plots
import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x,[xi*1.5 for xi in x]) #used list comprehension
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()
#matplotlib atomatically chooses different colors fir different lines
#########################################################################

#Grid,axes, and labels

#grid
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0) #(x,y,x,y,x,y)
plt.grid(True) 
plt.show

################

#Handling axes (Adjusting axes)
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis() #show the current axis limits values
plt.axis([0,5,-1,13]) #([x-min ,x-max,y-min,y-max])
plt.show()

###############

#adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel('This is x-axis')
plt.ylabel('This is a y-axis')
plt.show()

#########################################################################

#adding titles
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple title') #gives a title above the graph
plt.show()
#matplotlib provides simple function plt.title to add title to the graph

##########################################################################

#Adding legends
#information of the graph or which line provides which information is given by the legend
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5 , label = 'Normal' ) #used list comprehension
plt.plot(x,x*3.0 ,label = 'Fast')
plt.plot(x,x/3.0 ,label = 'slow' )
plt.legend()
plt.show()

########################################################################

#control colors
'''
color   name
b       blue
c       cyan
g       green
k       black
m       magenta
r       red
w       white
y       yellow
'''
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

###################################################################

#specifying styles in multiline plot
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show
#style abbrevation
'''
-   solid line
--  dotted line
'''
############################

#Control markers in the graph
'''
.  point marker

'''






######################################################################

import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()

###################################################################

#Histogram charts

#when mean == median then it is known as normal distribution : equal distribution
import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.show()

#######################################################################
#EDA: Exploratory data analysis
#Bar plots
#Bar function is used to plot bar graphs
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])        #([x-coordinates],[y-coordinates])
plt.show()

#######################################################################

#scatter plots :imp when studing regression
#Display values for two set of data
#usually diplayed in the form of points
#each of them have coordinates 
#one variable ditermeines X- position and othe variable determines Y- position
import matplotlib.pyplot as plt
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y)
plt.show

######Changing size and colors of the scatter plot graph
import matplotlib.pyplot as plt
size = 50*np.random.randn(1000)
color = np.random.randn(1000)
plt.scatter(x,y,s=size,c=color)
plt.show

#################################

#Adding text
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4, 4,1024)
y = .25*(x+4.)*(x+1.)*(x+2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(x,y,c='k')
plt.show()

############################################################################













