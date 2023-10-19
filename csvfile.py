import csv

def is_valid(row, header):
    # Check if row has same number of columns as header
    if len(row) != len(header):
        return False
    # Check if row has any missing values
    for value in row:
        if not value:
            return False
    return True

with open('employees_data.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        if is_valid(row, header):
            writer.writerow(row)

with open('output.csv', 'r') as outfile:
    print(outfile.read())
