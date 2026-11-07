"""
RECORD CHECK  -  my version
===========================

Name  :Heeresha Nawjee
Lane  :  AI 
Date  :02/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("data.csv")
df["percent"] = (df["value"] / df["limit"]) * 100
print(df)


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df = pd.read_csv("data.csv")
#Add a percent column
df["percent"] = (df["value"] / df["limit"]) * 100
#Design a function to assign status based on percentage
def get_status(p):
    """Assigns a status label based on the percentage value."""
    if p >= 100:
        return "OVER LIMIT"
    elif p >= 90:
        return "WARNING"
    else:
        return "OK"
df["status"] = df["percent"].apply(lambda x: get_status(x))




# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
import matplotlib.pyplot as plt
print(df)
filtered_df = df[df["status"] != "OK"]
print(filtered_df)
status_counts = df.groupby("status").size()
df.to_csv("full_data_output.csv", index=False)
print("\nSaved full DataFrame to 'full_data_output.csv'")
status_counts.plot(kind = "bar")
plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Count")

plt.show()

print("Saved bar chart to 'status_bar_chart.png'")
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
