import pandas as pd
from matplotlib import pyplot as plt
 
# https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
# Read CSV into pandas
data = {'feature': ["Branching and Merging", "Tree Structure","Workflow","Hosting "], 'count': [11080, 1749, 637, 1192]}
data_Branch = {'feature': ["commit", "cherry-pick","hooks","remote","stash",
                           "ignore","checkout","show","log","fetch",
                           "clone","pull","branch","lfs","reset", 
                           "amend"], 
               'count': [2180, 691, 1755, 416,362,
                         2015,507,53,530,228,
                         666,609,1184,495,283, 57]}

data_domain = {'feature': ["Snapshotting",  "Branching and Merging", "Sharing and propagation", "Patching", "Inspection", "Debugging", "Workflow", "Migration"],
        'count': [39,107,245, 327,403,478,1096, 523]} 
# data.head()
df = pd.DataFrame(data_domain)
 
name = df['feature'].head(16)
price = df['count'].head(16)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(name, price)
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='gray')
 
# Add Plot Title
ax.set_title('The number of Conceptual question over git core branching and merging feature',
             loc ='left', )
 
# # Add Text watermark
# fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
#          color ='grey', ha ='right', va ='bottom',
#          alpha = 0.7)
 
# Show Plot
plt.show()