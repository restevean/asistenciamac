import datetime as datetime
from datetime import datetime


def parse_row(row: list):
    # time = datetime.strptime(row[2], '%m/%d/%Y, %I:%M:%S %p')
    # row[2] = time.strftime('%d/%m/%Y, %H:%M:%S')
    # row[2] = datetime.strptime(row[2], '%m/%d/%Y, %I:%M:%S %p').strftime('%d/%m/%Y, %H:%M:%S')
    # new_row = row[0], row[1], row[2]
    # new_row = row[0], row[1], datetime.strptime(row[2], '%m/%d/%Y, %I:%M:%S %p').strftime('%d/%m/%Y, %H:%M:%S')

    # return new_row
    return row[0], row[1], datetime.strptime(row[2], '%m/%d/%Y, %I:%M:%S %p').strftime('%d/%m/%Y, %H:%M:%S')


def parse_file_name(file: str):
    if file[len(file) - 4: len(file) - 3: 1] == ".":
        if file[len(file) - 3: len(file): 1] != "csv":
            file = file[0: len(file) - 3: 1] + "csv"
    else:
        file = file + ".csv"

    return file
