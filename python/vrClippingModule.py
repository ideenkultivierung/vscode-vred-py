
# Autogenerated method stubs for 'vrClippingModule.py' module
# VRED Version: 13.0
# 
# VRED-Py - Visual Studio Code Tools for Autodesk VRED
# Copyright: Christopher Gebhardt 2020



def cloneClippingContour():
    '''
    Clones the contour.
    '''
    pass



def enableClippingPlane(state):
    '''
    Enables/disables clipping.

@param state: Clipping: Enable/Disable.

@type state: bool
    '''
    pass



def getClippingContourColor():
    '''
    Gets the color of the clipping contour.

@return: A vector with r, g and b values.

@rtype: Vec3f
    '''
    pass



def getClippingContourWidth():
    '''
    Gets the width of the contour.

@return: a int flag.

@rtype: int
    '''
    pass



def getClippingGridColor():
    '''
    Gets the color of the clipping grid.

@return: A vector with r, g and b values.

@rtype: Vec3f
    '''
    pass



def getClippingHideScene():
    '''
    Gets the hide scene flag of the clipping plane.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingPlaneColor():
    '''
    Gets the color of the clipping plane.

@return: A vector with r, g and b values.

@rtype: Vec3f
    '''
    pass



def getClippingPlaneInvertDirection():
    '''
    Gets the inversion flag of the clipping plane.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingPlaneNormal():
    '''
    Gets the normal of the clipping plane.

@return: A vector with x, y and z coordinates.

@rtype: Vec3f
    '''
    pass



def getClippingPlanePosition():
    '''
    Gets the position of the clipping plane.

@return: A vector with x, y and z coordinates.

@rtype: Pnt3f
    '''
    pass



def getClippingPlaneState():
    '''
    Gets the clipping plane status.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingShowContour():
    '''
    Gets the show contour flag.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingShowGrid():
    '''
    Gets the show grid flag.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingShowManipulator():
    '''
    Gets the show manipulator flag.

@return: a bool flag.

@rtype: bool
    '''
    pass



def getClippingShowPlane():
    '''
    Gets the show plane flag.

@return: a bool flag.

@rtype: bool
    '''
    pass



def setClippingContourVisualization(state, color, width):
    '''
    Sets the clipping grid visualization.

@param state: Clipping contour visualization: Enable/Disable.

@type state: bool

@param color: Sets the color of the clipping contour visualization.

@type color: Vec3f

@param width: Sets the width of the clipping contour visualization.

@type width: int
    '''
    pass



def setClippingGridVisualization(state, color):
    '''
    Sets the clipping grid visualization.

@param state: Clipping grid visualization: Enable/Disable.

@type state: bool

@param color: Sets the color of the clipping grid visualization.

@type color: Vec3f
    '''
    pass



def setClippingHideScene(state):
    '''
    Shows/hides the scene during clipping.

@param state: Show/hide the scene.

@type state: bool
    '''
    pass



def setClippingPlane(position, normal, flipped):
    '''
    Sets the clipping plane.

@param position: The position of the clipping plane.

@type position: Pnt3f

@param normal: The normal of the clipping plane.

@type normal: Vec3f

@param flipped: Sets the direction of the normal.

@type flipped: bool
    '''
    pass



def setClippingPlanePosition(position):
    '''
    Sets the position of the clipping plane.

@param position: A vector with x, y and z coordinates.

@type position: Pnt3f
    '''
    pass



def setClippingPlaneQuaternionRotation(axis, angle):
    '''
    Sets the rotation of the clipping plane with a quaternion.

@param axis: Rotation axis.

@type axis: Vec3f

@param angle: Rotation angle in degrees.

@type angle: float
    '''
    pass



def setClippingPlaneRotation(rotationX, rotationY, rotationZ):
    '''
    Sets the rotation of the clipping plane with euler rotation angles.

@param rotationX: Euler rotation angle x in degrees.

@type rotationX: float

@param rotationY: Euler rotation angle y in degrees.

@type rotationY: float

@param rotationZ: Euler rotation angle z in degrees.

@type rotationZ: float
    '''
    pass



def setClippingPlaneVisualization(state, color):
    '''
    Sets the clipping plane visualization.

@param state: Clipping plane visualization: Enable/Disable.

@type state: bool

@param color: Sets the color of the clipping plane visualization.

@type color: Vec3f
    '''
    pass



def setClippingShowManipulator(state):
    '''
    Shows/hides the clipping manipulator.

@param state: Clipping manipulator: Enable/Disable.

@type state: bool
    '''
    pass


