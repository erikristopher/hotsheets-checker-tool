#!/usr/bin/python

import glob
import csv
import re

rows = []

# replace hotsheets order csv file name below
main_file = "Charges-HS Orders - Wk 2 (1).csv"
# path to the hotsheets files
your_path = "D:/UPWORK/MyTools/hotsheets-checker-tool/sheets/*.csv"


def read_hot_sheets(path):
    for record in rows:
        for file_name in glob.glob(path):
            if record[4] != "" and record[4] in file_name:
                row_count = 0
                with open(file_name, 'r') as file:
                    csvreader = csv.reader(file)
                    _ = next(csvreader)
                    for row in csvreader:
                        row_count += 1
                        formatted_row = "~".join(row).lower()
                        if record[3] not in formatted_row:
                            print("Expected Property State is not seen for {}, row # {}".format(record, str(row_count)))
                        if record[2] not in formatted_row:
                            print("Expected County is not seen {}, row # {}".format(record, str(row_count)))
                    print("Name: {} {}, State: {}, County: {}, Row Count: {}".format(record[0], record[1], record[3],
                                                                                     record[2], str(row_count)))


def read_charges_hs_orders(args):
    with open(args, 'r') as file:
        csvreader = csv.reader(file)
        _ = next(csvreader)
        for row in csvreader:
            name = re.findall(r"([\w\s\.]+),([\w\s\-]+)", row[0])
            loc = re.findall(r"([\w\s\.]+):([\w\s\-]+)", row[1])
            file_name = re.findall(r"([\w\s\.\-\d\,]+)\(https", row[11])
            rows.append([name[0][1].strip().lower(),
                         name[0][0].strip().lower(),
                         loc[0][1].strip().lower(),  # county
                         loc[0][0].strip().lower(),  # state
                         "".join(file_name).strip()
                         ])


if __name__ == '__main__':
    read_charges_hs_orders(main_file)
    read_hot_sheets(your_path)
