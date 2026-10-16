"""
RECORD CHECK  -  my version
===========================

Name  :HEERESHA NAWJEE
Lane  :  AI 
Date  :15/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


def check_record(value, limit):
    """Calculate the difference, percentage"""
    #Calculate difference between value and limit
    difference = value - limit

    #Calculate the percentage of limit used
    percent = (value/limit)*100 if limit != 0 else 0

    #Determine if it is within limits or over
    if value <= limit:
        status = "OK"
    else:
        status = "OVER LIMIT"
    return difference, percent, status

def print_report(label, value, limit, difference, perecent, status):
    print(f"Record:{label}")
    print(f"Value:{value} | Limit: {limit}")
    print(f"Difference: {difference:.2f} | Percent: {perecent:.2f}% | Status: {status}")
    print("-"*30)



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "server", "value": 21, "limit": 15},
    {"label": "client", "value": 453.2, "limit": 25.3},
    {"label": "record",  "value": 152.11, "limit": 70.11}
]





# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
count = 0

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

    if status == "OVER_LIMIT":
        count += 1

print(f"Total OVER_LIMIT records: {count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
