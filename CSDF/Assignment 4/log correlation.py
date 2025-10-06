import re
from collections import defaultdict
log_file = r"C:\Users\Akhila\Documents\system.log"  # Input log file
error_keywords = ["ERROR", "FAIL", "WARNING"]  # Keywords to watch
correlation_window = 5  # Number of lines to consider for correlation

# --------------------------
# Read log file
# --------------------------
try:
    with open(log_file, "r") as f:
        logs = f.readlines()
except FileNotFoundError:
    print(f"Log file '{log_file}' not found!")
    exit()
# --------------------------
# Capture events
# --------------------------
events = []
for i, line in enumerate(logs):
    for keyword in error_keywords:
        if keyword in line:
            events.append({"line_no": i+1, "keyword": keyword, "message": line.strip()})
# --------------------------
# Event correlation
# --------------------------
# Simple correlation: find multiple occurrences of same keyword within a window
correlated_events = defaultdict(list)

for i, event in enumerate(events):
    keyword = event["keyword"]
    line_no = event["line_no"]
    message = event["message"]
    
    # Check next few events for same keyword
    for j in range(i+1, min(i+1+correlation_window, len(events))):
        if events[j]["keyword"] == keyword:
            correlated_events[keyword].append((line_no, events[j]["line_no"]))
# --------------------------
# Output results
# --------------------------
print("\nCaptured Events:")
for event in events:
    print(f"[{event['keyword']}] Line {event['line_no']}: {event['message']}")

print("\nCorrelated Events (within window of {} lines):".format(correlation_window))
for keyword, correlations in correlated_events.items():
    if correlations:
        print(f"\nKeyword: {keyword}")
        for pair in correlations:
            print(f"  Lines {pair[0]} & {pair[1]} -> Possibly related events")
