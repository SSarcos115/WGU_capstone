# This is a place to store the confusion matrix graph. Cannot run from this file, need to copy and paste to notebook.ipynb
import os
import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay
)

os.makedirs("graphs", exist_ok=True)

plt.figure(figsize=(8, 6))

# your graph code here
cm = confusion_matrix(y_test, predictions)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Compatible", "Use Caution", "Compatible"]
)

disp.plot(cmap="Blues", values_format="d")

plt.title("Fish Compatibility Model Confusion Matrix")
plt.xlabel("Predicted Compatibility")
plt.ylabel("Actual Compatibility")


plt.savefig("graphs/confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.show()