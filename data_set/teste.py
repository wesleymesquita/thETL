def isNumeric(input_str):
	try:
		a = float(input_str)
	except:
		return False
	return True

def printSummary(col_names, col_types):
	summary = dict(zip(col_names, col_types))
	for key, value in summary.iteritems():
		print "{} , {}".format(key, value)

def guessTypes(field_vals):
	col_types = []	
	
	for field_val in field_vals:	
		if isNumeric(field_val):
			col_types.append('N') #numeric
		else:
			col_types.append('T') #text
	return col_types	

def selectColumns(data_file, col_names, select_cols, nreg=100):
	sel_data = []
	
	index_list = [ col_names.index(selected_col) for selected_col in select_cols] 
	
	print "index_list == " + str(index_list) 
	
	for i in range(1, nreg):
		data_cols = data_file.readline().split(',')
		selected_data = [data_cols[i] for i in index_list]
		sel_data.append(selected_data)
		
	return sel_data
	
f_data = open('1987.csv')

col_names = f_data.readline().split(',');

field_values = f_data.readline().split(',');
col_types = guessTypes(field_values)
printSummary(col_names, col_types)	

sel_data = selectColumns(f_data, col_names, ["DepTime", "Distance", "ArrDelay"])

for d in sel_data:
	print d

f_data.close()