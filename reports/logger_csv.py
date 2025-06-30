import csv
import os

CSV_PATH = "reports/result.csv"

def log_result(test_name, status, message):
    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Tulis header jika file baru
        if not file_exists:
            writer.writerow(["Test Case", "Status", "Message"])

        # Tulis baris data
        writer.writerow([test_name, status, message])
