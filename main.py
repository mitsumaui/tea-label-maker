from __future__ import with_statement

import csv
import fpdf
import math

CSV_FILENAME = './addresses.csv'
LABELS_PER_ROW = 3
LABEL_HEIGHT = 24
LABEL_WIDTH = 68
LEFT_MARGIN = 12
LINE_HEIGHT = 5
PDF_FILENAME = './labels.pdf'
ROWS_PER_PAGE = 10
TOP_MARGIN = 25

LABELS_PER_PAGE = LABELS_PER_ROW * ROWS_PER_PAGE

pdf = fpdf.FPDF(orientation='P', unit='mm', format='Letter')
pdf.add_page()
pdf.set_font('Arial', '', 10)

with open(CSV_FILENAME) as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        if row['NAME'] == '':
            continue
        x = LEFT_MARGIN + (i % LABELS_PER_ROW) * LABEL_WIDTH
        page_num, page_i = divmod(i, LABELS_PER_PAGE)
        y = TOP_MARGIN + math.floor(page_i / LABELS_PER_ROW) * LABEL_HEIGHT
        pdf.text(x=x, y=y, txt=row['NAME'])
        y += LINE_HEIGHT
        pdf.text(x=x, y=y, txt=row['ADDRESS 1'])
        y += LINE_HEIGHT
        pdf.text(x=x, y=y, txt=row['ADDRESS 2'])
        if page_i + 1 == LABELS_PER_PAGE:
            pdf.add_page()
        i += 1

pdf.output(PDF_FILENAME)
