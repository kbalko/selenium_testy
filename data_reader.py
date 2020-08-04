# -*- coding: utf8 -*-
import csv


def read_data(path):

    rows = []
    data = open(str(path), "rt")
    content = csv.reader(data)

    next(content, None)

    for row in content:
        rows.append(row)

    return rows
