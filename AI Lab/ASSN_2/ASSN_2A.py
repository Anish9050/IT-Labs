import csv

def csv_to_txt(csv_filename, txt_filename):
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            with open(txt_filename, mode='w') as txt_file:
                for row in csv_reader:
                    txt_file.write('\t'.join(row) + '\n')
        print(f"CSV data has been written to {txt_filename}")
    except Exception as e:
        print(f"Error while converting CSV to TXT: {e}")

# 009_moth.csv is takes as input and output file name:009-output1.txt
csv_to_txt("009_month.csv", "009_output1.txt")