# -*- coding: utf8 -*-
import csv


def read_data(file_name):

    rows = []
    data = open(str(file_name), "rt")
    content = csv.reader(data)

    next(content, None)

    for row in content:
        rows.append(row)

    return rows
