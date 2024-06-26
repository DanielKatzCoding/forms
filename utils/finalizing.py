import json

import pandas as pd

import os

import pathlib


def get_desktop_path():
    if os.name == 'nt':  # Windows
        desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:  # Linux and other Unix-like systems
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

    return desktop


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


def export_data(quest):
    rows = build_obj()
    df = pd.DataFrame(rows)
    postfix = "-"
    if rows.get("שם המועמד"):
        postfix += rows.get("שם המועמד")[0]
    elif rows.get("תעודת זהות"):
        postfix += rows.get("תעודת זהות")[0]
    # Export to Excel with RTL support
    excel_writer = pd.ExcelWriter(f"{get_desktop_path()}/{quest+postfix}.xlsx", engine='openpyxl')
    df.to_excel(excel_writer, index=False, sheet_name='Sheet1')
    # Adjust Excel settings for RTL format
    worksheet = excel_writer.sheets['Sheet1']
    worksheet.sheet_view.rightToLeft = True

    excel_writer._save()
    reset_database()
