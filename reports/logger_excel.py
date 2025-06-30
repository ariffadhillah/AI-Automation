# from openpyxl import Workbook, load_workbook
# import os

# EXCEL_PATH = "reports/result.xlsx"

# def log_result(test_name, status, message):
#     if os.path.exists(EXCEL_PATH):
#         wb = load_workbook(EXCEL_PATH)
#         ws = wb.active
#     else:
#         wb = Workbook()
#         ws = wb.active
#         ws.append(["Test Case", "Status", "Message"])

#     ws.append([test_name, status, message])
#     wb.save(EXCEL_PATH)
