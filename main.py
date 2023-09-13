import re
import pandas as pd

# Define the regular expression pattern
pattern = r'VFUNC\s+(\d{4})\s*((\d{1,5}\s+)*\d{1,5})*'

# Open the file for reading
with open('file.txt', 'r') as file:
    data = file.read()

# Find all matches in the file
matches = re.findall(pattern, data)

# Process the matches
actual_df = pd.DataFrame(columns=["vfunc", "velocity", "position"])

for match in matches:
    vfunc_number = match[0]
    numbers = match[1].split()
    positions = numbers[::2]
    velocities = numbers[1::2]
    df = pd.DataFrame(data={"vfunc":[vfunc_number]*len(velocities), "velocity":velocities, "position":positions})
    actual_df = pd.concat((actual_df, df))

actual_df.to_csv("result.csv")
