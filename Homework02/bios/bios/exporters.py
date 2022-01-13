# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:44:45 2021

@author: Jimi
"""

from scrapy.exporters import CsvItemExporter


class HeadlessCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['include_headers_line'] = False
        super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)