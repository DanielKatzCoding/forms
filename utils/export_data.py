import json

import pandas as pd


def export_data(prefix):
    rows = {}
    with open("data/data.json", 'r') as f:
        data: dict = json.load(f)[prefix]
        data.pop("navs")

    for quests in data.values():
        rows.update({k: [v] for k, v in quests.items()})

    rows.pop("title")
    df = pd.DataFrame(rows)
    # Export to Excel with RTL support
    excel_writer = pd.ExcelWriter("output.xlsx", engine='openpyxl')
    df.to_excel(excel_writer, index=False, sheet_name='Sheet1')

    # Adjust Excel settings for RTL format
    workbook = excel_writer.book
    worksheet = excel_writer.sheets['Sheet1']
    worksheet.sheet_view.rightToLeft = True

    excel_writer._save()

