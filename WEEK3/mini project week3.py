"""
RECORD CHECK  -  my version
===========================

Name  :Heeresha Nawjee
Lane  :  AI     
Date  :08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).

def status_of(percent):
    """Returns the status based on the given percentage value."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Clculates and returns the difference and percentage based on the given value and limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Formats and prints the complete status report based on the provided parameters."""
    print(f"  Label: {label}")
    print(f"  Value: {value}")
    print(f"  Limit: {limit}")
    print(f"  Difference: {difference}")
    print(f"  Percentage: {percent:.2f}%")
    print(f"  Status: {status}")

# ==================================================================== INPUT
# 2. Ask for your three values.


label = input("Enter label: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.

difference, percent = check(value, limit)
status = status_of(percent)

difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)

# =================================================================== OUTPUT
# 4. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Value: {value}")
print(f"  Limit: {limit}")
print(f"Status: {status}")

print(f"value: {value:>10.2f}")
print(f"limit: {limit:>10.2f}")
print(f"difference: {difference:>10.2f}")
print(f"percent: {percent:>10.2f}%")
print(f"status: {status:>10}")

print_report(label, value, limit, difference, percent, status)

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
