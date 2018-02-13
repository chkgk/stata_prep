import csv
import argparse

parser = argparse.ArgumentParser(description='This program renames csv column headers from otree such that they are suitable for STATA')
parser.add_argument('input_file', nargs=1)
args = parser.parse_args()

name, postfix = args.input_file[0].split('.')

input_filename = args.input_file[0]
output_filename = name+'_stata.csv'

with open(input_filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    new_header = []
    for column_name in header:
        if '.' in column_name:
            prefix, name = column_name.split('.')
            new_header.append(name)
    data = [row for row in reader]

with open(output_filename, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(new_header)
    writer.writerows(data)

