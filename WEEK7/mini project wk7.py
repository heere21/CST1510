"""
RECORD CHECK  -  my version
===========================

Name  : Heeresha Nawjee
Lane  :  AI 
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Parses a messy line into a dictionary. """
    #Strip whitespace from the raw input line
    line = raw_line.strip()
    #split into hostname and the rest of the line
    hostname_part, rest = line.split(',', 1)
    #Remove whitespace and convert to lowercase for hostname
    hostname = hostname_part.strip().lower()
    #Initialise dictionary with hostname
    data = {'hostname': hostname}
    #Split the rest of the line by commas
    for part in rest.split(','):
        #Split each part into key and value
        key, value = part.split('=')
        #Add key-value pair to dictionary, converting value to float
        data[key.strip()] = float(value.strip())
    return data
def status_of(used, total):
    """Determines the status based on used and total values."""
    if used >= total:
        return "OVER LIMIT"
    elif used >= 0.9 * total:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []   
with open("survey_records.txt", "r") as file:
    for line in file:
        raw_records.append(line.strip())


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
#Parse and report on every record
total_records = 0
flagged_records = 0
for raw_record in raw_records:
    total_records += 1
    try:
        #Parse the raw record into a dictionary
        data = parse_line(raw_record)
        #Extract values
        rating = data.get('rating', 0)
        age = data.get('age', 0)
        #Determine status using the status_of function
        status = status_of(rating, 3)
        if status in ("OVER LIMIT", "WARNING", "FLAGGED"):
            flagged_records += 1
        #Print the cleaned dictionary and status
        print(f"{data}, Status: {status}")
    except ValueError:
        print(f"Could not parse: {raw_record}")
print(f"\nSummary: Total Records: {total_records}, Flagged Records: {flagged_records}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
