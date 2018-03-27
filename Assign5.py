#Exercise 5
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from statsmodels.graphics.regressionplots import abline_plot

x=[1.8,3.0,4.0,5.7,7.2,8.4,10.3]
t=[3.4,5.9,7.0,8.7,9.5,10.4,11.1]
df=pd.DataFrame({"thickness":x,"time":t})

results=smf.ols('time~thickness',data = df).fit()
print(results.summary())
#3.02+0.86thickness

plt.scatter(x,t)

#fit function
f = lambda x: 0.8617*x - 3.027
# x values of line to plot
x = np.array([0,100])
# plot fit
plt.plot(x,f(x),label="fit line ")
plt.show()



"""#transform x
xlog=np.log(x)
df1=pd.DataFrame({"logx":xlog,"time":t})
results=smf.ols('time~logx',data = df1).fit()
print(results.summary())"""