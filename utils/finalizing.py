import json

import pandas as pd


def build_obj() -> dict:
    rows = {}
    with open("data/data.json", 'r') as f:
        data: dict = json.load(f)

    for quests in data.values():
        rows.update({k: [v] for k, v in quests.items()})

    rows.pop("title")

    return rows


def reset_database():
    with open("data/data.json", 'w') as f:
        json.dump({}, f, indent=4, ensure_ascii=False)


def export_data():
    rows = build_obj()
    df = pd.DataFrame(rows)
    # Export to Excel with RTL support
    excel_writer = pd.ExcelWriter("output.xlsx", engine='openpyxl')
    df.to_excel(excel_writer, index=False, sheet_name='Sheet1')

    # Adjust Excel settings for RTL format
    worksheet = excel_writer.sheets['Sheet1']
    worksheet.sheet_view.rightToLeft = True

    excel_writer._save()
    reset_database()
