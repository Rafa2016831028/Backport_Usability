import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data = {'year': [2010,  2012, 2014, 2016, 2018, 2020, 2022],
#         'unemployment_rate': [39,107,564,]
#        }
data = {'year': [2010,  2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
        'number_of_posts': [39,107,245, 327,403,478,1096, 523,997,2196,1167,1025, 1824]
       }
total =0;
for c in data['number_of_posts']:
    total += c 

# new =[]
# for  c in data['number_of_posts']:
#     varsi = (c /total)*100
#     new += varsi
    
data_domain = {'domain': ["Snapshotting",  "Branching and Merging", "Sharing and propagation", "Patching", "Inspection", "Debugging", "Workflow", "Migration"],
        'number_of_posts': [39,107,245, 327,403,478,1096, 523]} 
print(total)
  
# define data values
x = np.array([1, 2, 3, 4])  # X-axis points
y = x*2  # Y-axis points
  
plt.plot(data['year'], data['number_of_posts'])  # Plot the chart
# plt.plot(data_domain['domain'],data_domain['number_of_posts'])
plt.show()  # display