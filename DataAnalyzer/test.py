import pandas as pd
import matplotlib.pyplot as plot
# Create DataFrame
df = pd.DataFrame({"Upvote":[58, 41, 67, 41, 68, 39, 30, 39 ],
                   "Downvote":[41.5, 30, 29, 58, 43, 28, 68, 56],
                }, 
                  index = ["A", "B", "C", "D", "E", "F", "G", "H"])
print(df)

# Create unstacked multiple columns bar
df.plot(kind="bar", figsize = (2, 4))
plot.ylabel("Proportion distribution of upvote and downvote (%)")
plot.show()