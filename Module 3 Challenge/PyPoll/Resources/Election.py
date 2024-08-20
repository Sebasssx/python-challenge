import csv

csv_path = "election_data.csv"

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    total_votes = 0
    candidates = {}

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

winner = max(results, key=lambda x: x[2])

output = f"""

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate}: {percentage:.3f}% {votes}
-------------------------
Winner: {winner[0]}
-------------------------
"""


print(output)

with open("Election Results.txt", "w") as output_file:
    output_file.write(output)