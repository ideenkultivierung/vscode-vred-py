
# Autogenerated method stubs for 'vrController.py' module
# VRED Version: 13.0
# 
# VRED-Py - Visual Studio Code Tools for Autodesk VRED
# Copyright: Christopher Gebhardt 2020



def addExtProcWindow(exe_name, window_name):
    '''
    Adds a external process window on top of the render window.

@param exe_name: The name of the executable.

@type exe_name: string

@param window_name: The name of the window.

@type window_name: string
    '''
    pass



def addModule(name, menu):
    '''
    Adds custom python module plugin.

@param name: name of the module.

@type name: string

@param menu: name of the menu where the plugin is inserted.

@type menu: string
    '''
    pass



def centerMainWindow():
    '''
    Centers the main window on the screen.
    '''
    pass



def changeScenegraph():
    '''
    Emits a scenegraph changed message.
    '''
    pass



def clearUndoStack():
    '''
    Clear the undo/redo stack
    '''
    pass



def closeSocketTest():
    '''
    Closes socket test.
    '''
    pass



def closeStreams():
    '''
    Close all open vred streams.
    '''
    pass



def crashVred(type):
    '''
    Crashes vred.

@param type: The type of crash.

@type type: int
    '''
    pass



def destroyScene():
    '''
    Destroys the current scene.
    '''
    pass



def enableSimulation(state):
    '''
    Enables/disables global simulation.

@param state: Global simulation: On/Off.

@type state: bool
    '''
    pass



def getIdleTime():
    '''
    Returns the idle time.

@return: The idle time.

@rtype: int
    '''
    pass



def getPresenterMode():
    '''
    Returns true if VRED's presentation mode is currently enabeld, otherwise false.

@return: Presentation mode state.

@rtype: bool
    '''
    pass



def getSimulationTime():
    '''
    Returns the simulation time in seconds.

@return: The simulation time.

@rtype: float (64bit)
    '''
    pass



def getUnitScale():
    '''
    Returns the unit scale factor.

@return: The scale factor.

@rtype: float
    '''
    pass



def getVRender():
    '''
    Returns the state of the vrender mode.

@return: The state of the vrender mode.

@rtype: bool
    '''
    pass



def getVServerImagePath():
    '''
    Returns the vserver image path.

@return: The vserver image path.

@rtype: string
    '''
    pass



def getVServerState():
    '''
    Returns the vserver state.

@return: The vserver state.

@rtype: int
    '''
    pass



def getVredBuildDate():
    '''
    Return the vred build date.

@return: The VRED build date.

@type version: string
    '''
    pass



def getVredDisplayVersionYear():
    '''
    Return the vred display year version.

@return: year number.

@type version: string
    '''
    pass



def getVredVersion():
    '''
    Return the vred version number.

@return version: version number.

@type version: string
    '''
    pass



def getVredVersionYear():
    '''
    Return the vred year version.

@return: year number.

@type version: string
    '''
    pass



def getVredVersions():
    '''
    Return the vred version number.

@return: version number.

@type version: string
    '''
    pass



def geterrno():
    '''
    Returns the errno value.

@return: The errno value.

@rtype: int
    '''
    pass



def hideModule(name):
    '''
    Hides custom python module plugin.

@param name: name of the module.

@type name: string
    '''
    pass



def isViewer():
    '''
    Returns true when running VREDPresenter.

@return: true for viewer.

@rtype: bool
    '''
    pass



def newScene():
    '''
    Creates a new scene and destroys the current scene.
    '''
    pass



def openSocketTest():
    '''
    Opens socket test.
    '''
    pass



def reseterrno():
    '''
    Resets the errno variable.
    '''
    pass



def sendCloudMSG(message):
    '''
    Sends a message to the publish/Subscribe interface.

@param message: a name for the file (no path).

@type  message: string
    '''
    pass



def setEnvironmentVariable(name, value):
    '''
    Sets an environment variable.

@param name: The name of the variable.

@type name: string

@param value: The value of the variable.

@type value: string
    '''
    pass



def setLogEnabled(s):
    '''
    Enable or disable terminal logging.

@param s: state true or false.

@type s: bool
    '''
    pass



def setNewSceneCB(fp):
    '''
    Sets a python callback function which is called before executing newScene.

@param fp: The python function.

@type fp: function pointer
    '''
    pass



def setPresenterMode(s):
    '''
    Enable VRED's presentation mode. Only hotkeys from the Variants Sets module will work in this mode.

@param s: enable/disable.

@type s: bool
    '''
    pass



def setRenderUpdateEnabled(state):
    '''
    Enables or disables the main render window update.

@param state: Main render window update: On/Off.

@type state: bool
    '''
    pass



def setShowQuickActionBars(state):
    '''
    Show/hide all quick action bars.

@param state: visible state.

@type state: bool
    '''
    pass



def setShowSurfaceAnalysisModule(show):
    '''
    Show/hide Surface Analysis module in VREDPresenter.

@param show: show/hide Surface Analysis module.

@type show: bool
    '''
    pass



def setStyleSheet(filename):
    '''
    Loads a qt style sheet.

@param filename: The absolute path of .qss style sheet file.

@type filename: string
    '''
    pass



def setUnitScale(scale):
    '''
    Sets the unit scale factor.

@param scale: The scale factor. 1.0 for mm, 10.0 for cm and 1000.0 for m.

@type scale: float
    '''
    pass



def setVREDPresenterWebViewFixedHeight(height):
    '''
    Changes the height of the VREDPresenter webview widget and disables vertical resizing.

@param height: The height in pixels.

@type height: int (32bit)
    '''
    pass



def setVREDPresenterWebViewFixedWidth(width):
    '''
    Changes the width of the VREDPresenter webview widget and disables horizontal resizing.

@param width: The width in pixels.

@type width: int (32bit)
    '''
    pass



def setVREDPresenterWebViewWidth(width):
    '''
    Changes the width of the VREDPresenter webview widget.

@param width: The width in pixels.

@type width: int (32bit)
    '''
    pass



def setVRender(state):
    '''
    Enables vrender mode.

@param state: The vrender mode: On/Off.

@type state: bool
    '''
    pass



def setVServerImagePath(path):
    '''
    Sets vserver image path.

@param path: The image path.

@type path: string
    '''
    pass



def setVServerState(state):
    '''
    Sets vserver state.

@param state: The vserver state.

@type state: int
    '''
    pass



def setWIMergeCommands():
    '''
    Merge duplicated python commands.
    '''
    pass



def showLicenseDialog():
    '''
    Show license dialog.
    '''
    pass



def showModule(name):
    '''
    Shows custom python module plugin.

@param name: name of the module.

@type name: string
    '''
    pass



def showToolBars(state):
    '''
    Shows or hides the main window toolbars.

@param state: Main window toolbars: -1 = Toggle, 0 = Off, 1 = On.

@type state: integer
    '''
    pass



def subModule(name):
    '''
    Subs custom python module plugin.

@param name: name of the module.

@type name: string
    '''
    pass



def terminateVred():
    '''
    Terminates vred.
    '''
    pass



def togglePresenterMode():
    '''
    Toggles VRED's presentation mode state.
    '''
    pass



def updateRender(force):
    '''
    Redraws the render widget.

@param force: Set true to update the render widget immediately, false otherwise (Optional). Default is false.

@type force: bool
    '''
    pass



def updateRenderNoOCC(force):
    '''
    Redraws the render widget. This function is obsolete, use updateRender instead.

@param force: Set true to update the render widget immediately, false otherwise (Optional). Default is false.

@type force: bool
    '''
    pass



def updateScene():
    '''
    Calculates new near/far clipping plane and new camera position.
    '''
    pass



def updateTouchSensors():
    '''
    Update touch sensor user interface.
    '''
    pass



def vredLoop(count):
    '''
    Calls the internal timer loop n times.

@param count: The number of calls.

@type count: unsigned int (32bit)
    '''
    pass



def vred_click():
    '''
    Deprecated.
    '''
    pass



def vred_mousedown(x, y):
    '''
    Simulates a mouse button-down event for the left mouse button.

The coordinates are in pixels and relative to the VRED main window, origin is upper-left corner.

@param x: x coordinate.

@type x: int

@param y: y coordinate.

@type y: int
    '''
    pass



def vred_mouseup(x, y):
    '''
    Simulates a mouse button-up event for the left mouse button.

The coordinates are in pixels and relative to the VRED main window, origin is upper-left corner.

@param x: x coordinate.

@type x: int

@param y: y coordinate.

@type y: int
    '''
    pass



def vred_swipemove(x, y):
    '''
    Simulates a mouse button move event for the left mouse button

The coordinates are in pixels and relative to the VRED main window, origin is upper-left corner.

@param x: x coordinate.

@type x: int

@param y: y coordinate.

@type y: int
    '''
    pass



def writeTerminalOutput(filename):
    '''
    Writes the terminal output as html out.

@param filename: The absolute path of the .html file.

@type filename: string
    '''
    pass


