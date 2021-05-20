import csv,json

data = {}
with open('main.csv', 'r') as csv_reader_file:
	csv_reader = csv.reader(csv_reader_file)
	status = True
	for row in csv_reader:
		if(len(row)) != 0:
			if status == True:
				status = False
			else:
				question_user_id = row[len(row)-2]
				answer_user_id = row[len(row)-1]
				
				intermediate_data = [answer_user_id]

				if question_user_id not in data.keys():
					data[question_user_id] = intermediate_data
				else:
					#if answer_user_id not in data[question_user_id]:
					data[question_user_id] = data[question_user_id] + intermediate_data
					
with open("data.json",'w') as json_write_file:
	json.dump(data, json_write_file, indent=4 )
