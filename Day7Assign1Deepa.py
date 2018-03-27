import scipy.stats
import math
from scipy.stats import distributions as dists


#given values
Sx=809
Sy=68.3
Sxx=3630.95
Sxy=201.665
Syy=12.9455
n=20
# specifying degrees of freedom for numerator and denominator
df1=1
df2=n-df1-1

#calculating Xbar and Ybar for the given sample
xbar=Sx/n
ybar=Sy/n
#calculating Beta0 the intercept and Beta1 the slope

slope=Sxy/Sxx
intercept=ybar-(slope*xbar)
print("The equation is : y= %0.2f + %0.2fx" %(intercept,slope))
print("---------------------------------------------------------")
print("---------------------------------------------------------")

#Calculating the Anova Table statistics
SSR=(slope**2)*Sxx
SSE=(Syy-(slope*Sxy))
MSreg=SSR/1
MSerror=SSE/(n-2)
Fstat=MSreg/MSerror
print("The F statistic is %0.2f" %(Fstat))

#Reference for .ppf function inputs for this problem f.ppf(q=1-0.05, dfn=1, dfd=20-2)
Fcrit = dists.f.ppf(1-0.05,1,18)  # F statistics with DF regression = 5, Resiductaion =10
print("F critical value is : %0.2f" %(Fcrit))
print("---------------------------------------------------------")
alpha=0.05
if Fstat>Fcrit:
    print("Reject Null Hypothesis that all Betas are Zero, Regression Model is ok")

#Tstatistic=Beta1 divided by (sigmaHat/Sqrt(Sxx))
tstat=slope/(math.sqrt(MSerror)/math.sqrt(Sxx))
tcrit=dists.t.ppf(1-0.05/2,18)
print("The t-statistic is %0.2f" %(tstat))
print("The tcritical value is %.02f" %(tcrit))
if tstat>tcrit:
    print("The test statistic is greater than Tcritical, hence we reject Null that Beta1 is zero")
