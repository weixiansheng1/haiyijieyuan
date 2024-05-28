# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:27:03 2024

@author: Microsoft
"""
import win32print


printers =[printer[2] for printer in win32print.EnumPrinters(2)]
#选择一个打印机
printer_name = printers[1]

printer_props  = win32print.GetPrinter(printer_name,3) #获取打印机属性
duplex = win32print.Duplex.DUPLEX_HORIZONTAL
#获取双面打印属性

if win32print.DEVICEMODE_DUPLEX in printer_props['pDevMode'].keys():
    #如果打印机已经设置了双面打印，则使用该设置
    duplex = printer_props['pDevMode'][win32print.DEVICEMODE_DUPLEX]
    #打印双面
    
    job = win32print.StartDocPrinter(printer_name, 1,("testjob",None,"RAW"))
    win32print.SetJob(printer_name, job, 2,{"pagesPerside": win32print.PAGES_PER_SIDE_TW0})
    win32print.startPagePrinter(job)
    win32print.WritePrinter(job,"hello，world!".encode())
    win32print.EndPagePrinter(job)
    win32print.SetJob(printer_name, job, 2,{"pagesPerside": win32print.PAGES_PER_SIDE_ONE})
    win32print.startPagePrinter(job)
    win32print.writePrinter(job,"hello again!".encode())
    
    win32print.EndPagePrinter(job)
    win32print.EndDocPrinter(job)