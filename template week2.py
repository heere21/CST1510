"""
RECORD CHECK  -  my version
===========================

Name  :Heeresha Nawjee
Lane  :  AI / Cyber / IT      (delete two)
Date  :02/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
label = input("Enter a label: ")
value = float(input("Enter a value: "))
limit = float(input("Enter a limit: "))

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
difference = value - limit
percent = (value / limit) * 100

# 3. Decide a status and store it in a variable called status.
if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here
print(f"  Value     : {value:>10.2f}")
print(f"  Limit     : {limit:>10.2f}")
print(f"  Difference: {difference:>10.2f}")
print(f"  Percent   : {percent:>10.2f}%")
print(f"  Status    : {status:>10}")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
