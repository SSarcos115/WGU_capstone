# This is a place to store the classification report. Cannot run from this file, need to copy and paste to notebook.ipynb

from sklearn.metrics import classification_report
import os

os.makedirs("graphs", exist_ok=True)

report = classification_report(y_test, predictions, target_names=["Not Compatible", "Use Caution", "Compatible"])

with open("graphs/classification_report.txt", "w") as file:
    file.write(report)