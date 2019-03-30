import csv

with open('isentropic_flow_table.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)  # skip header
	i_f_data = [r for r in reader]
