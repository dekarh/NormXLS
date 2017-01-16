# -*- coding: utf-8 -*-
__author__ = 'Администратор'

import csv
import xlwt
import openpyxl
from openpyxl import Workbook


def csv2xls(path_to_csv_file, separator=';', path_to_xlsx_file=''):
    if path_to_csv_file.split('.')[-1] != 'csv':
        return None
    if path_to_xlsx_file == '':
        path_to_xlsx_file = ''.join(path_to_csv_file.split('.')[0:-1]) + '.xlsx'

    rows = []
    with open(path_to_csv_file, 'r', encoding='utf-8') as file:
        newreader = csv.reader(file, delimiter=separator)
        for row in newreader:
            rows.append(row)

    wb = Workbook(write_only=True)
    ws = wb.create_sheet()
    for csv_row in rows:
        ws.append(csv_row)

    wb.save(path_to_xlsx_file)
    return path_to_xlsx_file




