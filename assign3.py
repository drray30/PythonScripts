#Exercise 3
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

y=[14,20,37,36,31,42,54,64,38,66,64,77,79,93,119,135]
x1=[120,120,120,120,150,150,150,150,180,180,180,180,240,240,240,240]
x2=[60,80,100,120,75,100,125,150,90,120,150,180,120,160,200,240]
df=pd.DataFrame({ 'length':x1, 'width':x2,'Price':y})
#Plots
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
f.suptitle('Sharing Y axis')
ax1.scatter(x1, y)
ax1.set_title('Price vs Length')
ax2.scatter(x2, y)
ax2.set_title('Price vs Width')
#plt.show()
result = smf.ols('Price~length+width',data = df).fit()
print(result.summary())
#fitted equation is price=-52.6714 + 0.3236xlength + 0.4438xwidth

table = sm.stats.anova_lm(result)
print(table)

#predict new record
newrecord=pd.DataFrame({'length':[200], 'width':[150]})
f=result.predict((newrecord))
print(f)