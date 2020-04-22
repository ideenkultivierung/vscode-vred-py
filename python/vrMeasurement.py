
# Autogenerated method stubs for 'vrMeasurement.py' module
# VRED Version: 13.0
# 
# VRED-Py - Visual Studio Code Tools for Autodesk VRED
# Copyright: Christopher Gebhardt 2020



def createCircleMeasurement(node1, hitPoint1, node2, hitPoint2, node3, hitPoint3):
    '''
    Creates a circle measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test.

@param node1: The first node.

@type node1: vrNodePtr

@param hitPoint1: The intersection point on node1.

@type hitPoint1: Pnt3f

@param node2: The second node.

@type node2: vrNodePtr

@param hitPoint2: The intersection point on node2.

@type hitPoint2: Pnt3f

@param node3: The third node.

@type node3: vrNodePtr

@param hitPoint3: The intersection point on node3.

@type hitPoint3: Pnt3f
    '''
    pass



def createGapMeasurement(node1, hitPoint1, node2, hitPoint2):
    '''
    Creates a gap measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test

.(This command is only available in VRED Professional.)

@param node1: The first node.

@type node1: vrNodePtr

@param hitPoint1: The intersection point on node1.

@type hitPoint1: Pnt3f

@param node2: The second node.

@type node2: vrNodePtr

@param hitPoint2: The intersection point on node2.

@type hitPoint2: Pnt3f
    '''
    pass



def createLineObjectMeasurement(lineNode, linehitPoint, node2):
    '''
    Creates a line to object measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test.

@param lineNode: The line node.

@type node1: vrNodePtr

@param linehitPoint: The intersection point on the line node.

@type hitPoint1: Pnt3f

@param node2: The second node (no hit point needed here).

@type node2: vrNodePtr
    '''
    pass



def createObjectObjectMeasurement(node1, node2):
    '''
    Creates an object to object measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test.

@param node1: The first node.

@type node1: vrNodePtr

@param node2: The second node.

@type node2: vrNodePtr
    '''
    pass



def createPointObjectMeasurement(node1, hitPoint1, node2):
    '''
    Creates a point to object measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test.

@param node1: The first node.

@type node1: vrNodePtr

@param hitPoint1: The intersection point on node1.

@type hitPoint1: Pnt3f

@param node2: The second node (no hit point is needed here for this measurement).

@type node2: vrNodePtr
    '''
    pass



def createPointPointMeasurement(node1, hitPoint1, node2, hitPoint2):
    '''
    Creates a point to point measurement.

There are two functions:

The function can be called without parameters. The interaction mode accordingly and the picking can be done with the mouse.

The function with parameters can be used when the interaction mode can not be used (e.g. in an immersive scenario).

The parameters will have to come from a separate intersection test.

@param node1: The first node.

@type node1: vrNodePtr

@param hitPoint1: The intersection point on node1.

@type hitPoint1: Pnt3f

@param node2: The second node.

@type node2: vrNodePtr

@param hitPoint2: The intersection point on node2.

@type hitPoint2: Pnt3f
    '''
    pass



def removeAllMeasurements():
    '''
    Removes all existing measurements.
    '''
    pass



def removeSelectedMeasurement():
    '''
    Remove the currently selected measurement. The last created measurement is automatically selected.
    '''
    pass



def updateAllMeasurements():
    '''
    Update all measurements.
    '''
    pass



def updateMeasurement():
    '''
    Update the selected measurement.
    '''
    pass



def zoomOnMeasurement():
    '''
    Zoom on the selected measurement.
    '''
    pass


