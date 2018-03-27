#Exercise 4
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

xbar=1985
Sxx=1500
Sy=1107

year = [1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005]
speed = [109, 114, 116, 117, 114, 127, 131, 138, 141]

#plt.scatter(year,speed)
#plt.show()
df=pd.DataFrame({ 'year':year, 'speed':speed})
#result = smf.ols('speed~year',data = df).fit()
#print(result.summary())
#equation is y=-1465+0.8year
#table = sm.stats.anova_lm(result)
#print(table)

#dropping the value for 1985
df = df[df.year != 1985]

print(df)
result = smf.ols('speed~year',data = df).fit()
#print(result.summary())
#equation is y=-1465+0.8year
table = sm.stats.anova_lm(result)
print(table)

#predict new record
newrecord=pd.DataFrame({'year':[1985]}) #0    124.125
newrecord=pd.DataFrame({'year':[2010]}) #0    144.125
#newrecord=pd.DataFrame({'speed':[160]})
#f=result.predict((newrecord))
year1=(160+1465)/0.8
print(year1)