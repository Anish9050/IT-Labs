import csv
def txt_to_csv(txt_filename, csv_filename):
    try:
        with open(txt_filename, mode='r') as txt_file:
            lines = txt_file.readlines()
            with open(csv_filename, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for line in lines:
                    row = line.strip().split('\t')
                    csv_writer.writerow(row)
        print(f"TXT data has been written to {csv_filename}")
    except Exception as e:
        print(f"Error while converting TXT to CSV: {e}")
#inputfile used 009_anish.txt,output file:009_output2.csv
txt_to_csv('009_anish.txt', '009_output2.csv')