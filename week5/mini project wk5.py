"""
RECORD CHECK  -  my version
===========================

Name  : HEERESHA NAWJEE
Lane  :  AI 
Date  :22/10/26  

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    """A class to monitor and track record values against a specific limit."""
    #Class-level running total for records that exceed the limit
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """Initialise the Record with a label, value and limit and update the over_limit_count if the value exceeds the limit."""
        self.label = label
        self.value = value
        self.limit = limit
        #Check if the initial valueis over the limit and update the class-level counter
        if self.value >= self.limit:
            Record.over_limit_count += 1

    def status(self):
        """Return the status based on value and limit"""
        #Calculate percentage of he limit reached
        percentage = (self.value/self.limit)*100 if self.limit > 0 else 0

        if self.value >= self.limit:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

        


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

 
def load_records(path):
    """Read records from file and return a list of Record object."""
    records = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                label = parts[0]
                #Convert value and limit to appropriate numeric types
                value = float(parts[1])
                limit = float(parts[2])
                #Create and append  Record instance
                records.append(Record(label, value, limit))
    return records
#Load records from data file
records = load_records("records.txt")
for r in records:
       print(f"{r.label} {r.status()}")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

   #Print the record's value, limit and status
print(f"Value : {record.value}")
print(f"Limit : {record.limit}")
print(f"Status : {record.status()}")

print("=" * 34)
print(f"\nTotal Over Limit Records: {Record.over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
