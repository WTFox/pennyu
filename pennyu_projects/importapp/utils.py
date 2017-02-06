import csv


def handle_upload(csv_file):
    csv_file.seek(0)
    reader = csv.reader(csv_file.read().splitlines(), dialect=csv.excel)
    invalid_rows = []
    valid_rows = []
    for row in reader:
        # Skip line if it's blank.
        if not row:
            continue

        quantity, product, user, cat = row
        if int(quantity) > 13:
            valid_rows.append(row)
        else:
            invalid_rows.append(row)

    return valid_rows, invalid_rows
