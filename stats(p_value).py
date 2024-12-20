# -*- coding: utf-8 -*-
"""stats(p -value)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nx1XZ3CzGw4yPHww2gnTjEN6uKF9UgVZ

**A researcher wants to know if a new drug affects IQ levels, so he recruits 20 patients to try it and records their IQ levels.The following code shows how to perform a one smaple z-test in python to determone if the new frug causes a significant difference in IQ levels:**
"""

from statsmodels.stats.weightstats import ztest as ztest

#enter IQ levels for 20 patients
data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 110, 112, 112, 113, 114, 115]
ztest(data,value=110)

# t-test

ages=[10, 20, 35, 50, 28, 40, 55, 18, 16, 55, 30, 25, 43, 18, 30, 28, 14, 24, 16, 17, 32, 35, 26, 27, 65, 18, 43, 23, 21, 20, 19, 70]

import numpy as np
ages_mean=np.mean(ages)
ages_mean

sample_size=10
ages_sample=np.random.choice(ages,sample_size)
ages_sample

np.mean(ages_sample)

from scipy.stats import ttest_1samp
ttest_1samp(ages_sample,30)

"""**Consider another example ages of the college students(population) 1 class student mean of all the ages.**"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)
school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500)
classA_ages=stats.poisson.rvs(loc=18,mu=30,size=60)
school_ages

classA_ages

classA_ages.mean()

_,p_value=ttest_1samp(classA_ages,popmean=school_ages.mean())
school_ages.mean()

if p_value<=0.05:
  print("Reject H0")
else:
  print("Accept H0")

import seaborn as sns
df=sns.load_dataset('iris')
df.head()

sns.pairplot(df)

