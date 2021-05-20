import os,csv

names = os.listdir('data/')

with open("main.csv", 'w') as csv_write_file:
	csv_writer = csv.writer(csv_write_file, delimiter=',')
	csv_writer.writerow(["Question Title","Question","Tags","Question_User_Id","Answer_User_Id"])

	for file_name in names:
		print(f"Copying {file_name} to main file")
		with open(f"data/{file_name}", 'r') as csv_read_file:
			csv_reader = csv.reader(csv_read_file)
			status = False
			for row in csv_reader:
				if status == False:
					status = True
					pass
				else:
					csv_writer.writerow(row)
	print("Successfully copied all files to a single main file")


