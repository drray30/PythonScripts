
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

heat=[1.64,1.60,1.63,1.65,1.67,1.67,1.72,1.70,1.71,1.72,1.71,1.74]
temp=[50,50,60,60,70,70,80,80,90,90,100,100]
n=len(heat)
df=pd.DataFrame({'t': temp, 'h': heat})
result = smf.ols('heat~temp',data = df).fit()
print(result.summary())
X_new = pd.DataFrame({'temp': [85]})
X_new.head()
preds = result.predict(X_new)
print(preds)