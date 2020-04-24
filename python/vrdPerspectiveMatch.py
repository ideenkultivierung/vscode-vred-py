'''
Autogenerated Method-Stub for:
module vrdPerspectiveMatch
------------------------------------------

API version: v2
Generation Date: 2020-04-24

VRED-Py: Visual Studio Code Tools for Autodesk VRED
'''

from typing import List



def doRotateLeft():
    '''
    Rotates the camera clockwise around the pivot by the amount of degrees set with         vrdPerspectiveMatch.setRotationStepSize(deg)
    '''
    pass



def doRotateRight():
    '''
    Rotates the camera counterclockwise around the pivot by the amount of degrees set with         vrdPerspectiveMatch.setRotationStepSize(deg)
    '''
    pass



def getEnabled():
    '''
    Returns if perspective matching tool is currently enabled.
    '''
    pass



def getMagnifyFactor():
    '''
    Returns the scale factor used for the magnifier.
    '''
    pass



def getPivot():
    '''
    Returns the pivot used for rotations with         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass



def getRotationStepSize():
    '''
    Returns the rotation step size used by         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass



def getVanishingLinesType():
    '''
    Returns the vanishing lines type.
    '''
    pass



def setDefaultLines():
    '''
    Resets the vanishing lines to default values.
    '''
    pass



def setEnabled(enabled):
    '''
    Enables or disables the perspective match tool.
    '''
    pass



def setMagnifyFactor(factor):
    '''
    Sets the magnify factor used for the magnifier shown at the manipulator handles. This does not have an effect on the calculation.
    '''
    pass



def setPivot(pivot):
    '''
    Sets the pivot used for rotations with         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass



def setPivotFromNavigator():
    '''
    Applies the currently used navigation pivot as perspective match pivot.
    '''
    pass



def setRotationStepSize(deg):
    '''
    Sets the rotation step size used by         vrdPerspectiveMatch.doRotateLeft() and vrdPerspectiveMatch.doRotateRight()
    '''
    pass



def setVanishingLinesType(type):
    '''
    Sets the vanishing lines type defining which vanishing lines should be used (and shown) for perspective matching.
    '''
    pass


