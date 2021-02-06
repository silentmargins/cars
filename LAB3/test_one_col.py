#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import os

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

#sukurti pdf objecta pagal SimpleDocTemplate classe
report = SimpleDocTemplate("report.pdf")
#You can make a style all of your own, but we’ll use the default provided by the module for these examples
styles = getSampleStyleSheet()
#indidualus elementas, Flowables. Flowables are sort of like chunks of a document that reportlab can arrange to make a complete report. 
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

#surenkami duomenys lentelei, reikia list of lists (two dimesional arrays)
table_data = []
for k in fruit.keys():
    table_data.append(k)
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
#sukuriama lentele Flowables
report_table = Table(data=table_data, hAlign="LEFT")

column_of_paragraphs = []
description_directory = 'descriptions'
for file in os.listdir(description_directory):
    with open(description_directory + '/' + file, 'r') as description_file:
        description_list = []
        for line in description_file:
            description_list.append(line)
        report_name= Paragraph('name: ' + description_list[0] + '\n')
        column_of_paragraphs.append(report_name)
        report_weight = Paragraph('weight: ' + description_list[1] + '\n')
        column_of_paragraphs.append(report_weight)
        empty_line = Spacer(1,20)
        column_of_paragraphs.append(empty_line)

description_list = []
for file in os.listdir(description_directory):
    with open(description_directory + '/' + file, 'r') as description_file:
        description_files = []
        for line in description_file:
            description_files.append(line)
        description_list.append('name: ' + description_files[0].capitalize())
        description_list.append('weight: ' + description_files[1])
        description_list.append('\n')
        
paragraph = ' '.join(description_list)

#generuoti reporta
flowables = [report_title, report_table] + column_of_paragraphs
report.build(flowables)
