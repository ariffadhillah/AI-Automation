import csv
from datetime import datetime
import os

# Baca hasil dari logs/result.csv
with open("logs/result.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Siapkan HTML dasar
html = """
<html>
<head>
    <title>AI Test Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .Passed { background-color: #d4edda; color: #155724; font-weight: bold; }
        .Failed { background-color: #f8d7da; color: #721c24; font-weight: bold; }
    </style>
</head>
<body>
    <h2>AI Test Report</h2>
    <p>Generated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    <table>
        <tr><th>Step</th><th>Prompt</th><th>Status</th><th>Message</th></tr>
"""

# Tambahkan isi tabel
for row in rows:
    status_class = row["Status"]
    html += f"<tr>"
    html += f"<td>{row['Step']}</td>"
    html += f"<td>{row['Prompt']}</td>"
    html += f"<td class='{status_class}'>{row['Status']}</td>"
    html += f"<td>{row['Message']}</td>"
    html += f"</tr>"

html += """
    </table>
</body>
</html>
"""

# Simpan ke file HTML
os.makedirs("reports", exist_ok=True)
with open("reports/report.html", mode="w", encoding="utf-8") as f:
    f.write(html)

print("✅ Laporan HTML berhasil disimpan di reports/report.html")
