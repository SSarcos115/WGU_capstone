# This is a place to store the compatibility model. Cannot run from this file, need to copy and paste to notebook.ipynb

import os
import matplotlib.pyplot as plt
import pandas as pd

# create visuals folder if it doesn't exist
os.makedirs("graphs", exist_ok=True)

# create feature importance series
feature_importance = pd.Series(
    compatibility_model.feature_importances_,
    index=X.columns
).sort_values(ascending=True)

# create plot
plt.figure(figsize=(8, 6))

feature_importance.plot(kind="barh")

plt.title("Feature Importance for Fish Compatibility Model")
plt.xlabel("Importance Score")
plt.ylabel("Model Feature")

# save image to visuals folder
plt.savefig(
    "graphs/feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

# show plot
plt.show()