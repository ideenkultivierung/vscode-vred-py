
# Autogenerated method stubs for 'vrVredUi.py' module
# VRED Version: 13.0
# 
# VRED-Py - Visual Studio Code Tools for Autodesk VRED
# Copyright: Christopher Gebhardt 2020



def getMainWindow():
    '''
    Returns the pointer address of vred main window. In order to use it in python you need to wrap it to a QMainWindow in python:

   from PySide2 import QtWidgets
   from shiboken import wrapInstance
   def vredMainWindow() : 
       main_window_ptr = getMainWindow() 
       return wrapInstance(long(main_window_ptr), QtWidgets.QMainWindow)

For your convenience this wrapper function is already defined when you start Vred.
@return: The main window Widget.

@rtype: long long
    '''
    pass


