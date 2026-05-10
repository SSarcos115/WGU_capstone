# This is a place to store the fish pair distribution graph. Cannot run from this file, need to copy and paste to notebook.ipynb

import os
import matplotlib.pyplot as plt

# create graphs folder if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# create figure
plt.figure(figsize=(8, 5))

# create histogram
plt.hist(
    pair_df["Overall Compatibility Score 0-100"],
    bins=10,
    edgecolor="black"
)

# labels and title
plt.title("Distribution of Fish Pair Compatibility Scores")
plt.xlabel("Compatibility Score")
plt.ylabel("Number of Fish Pairs")

# save graph into graphs folder
plt.savefig(
    "graphs/compatibility_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

# display graph
plt.show()