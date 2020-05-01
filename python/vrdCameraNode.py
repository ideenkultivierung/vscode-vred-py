'''
vrdCameraNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class represents a camera in VRED.
'''

from typing import List


class vrdNode():
    pass


class vrdTurntable():
    pass


class vrdCameraCollider():
    pass


class vrdCameraTrackNode():
    pass


def activate():
    '''
    Sets the camera to active.
    '''
    pass


def getAimConstraintSources() -> List[vrdNode]:
    '''
    Returns the list of nodes set as aim constraint sources for the camera.
    '''
    return None


def getAimVisualizationScale() -> float:
    '''
    Returns the scaling value used for the aim and up vector visualization.
    '''
    return None


def getAimVisualizationVisible() -> bool:
    '''
    Queries if the aim and up vector visualization is visible in the renderer.
    '''
    return None


def getCameraCollider() -> vrdCameraCollider:
    '''
    This object gives access to the camera collision functionality.
    '''
    return None


def getCameraTrack(cameraTrackIndex: int) -> vrdCameraTrackNode:
    '''
    Gets the camera track.
    '''
    return None


def getCameraTrackCount() -> int:
    '''
    Returns the number of camera tracks in the camera.
    '''
    return None


def getCameraTracks() -> List[vrdCameraTrackNode]:
    '''
    Returns the list of all camera track nodes of the camera.
    '''
    return None


def getDefaultCameraTrack() -> vrdCameraTrackNode:
    '''
    Returns the default camera track node.
    '''
    return None


def getDollyZoom() -> bool:
    '''
    Returns the state of dolly zoom mode.
    '''
    return None


def getEvaluateNavigationMode() -> bool:
    '''
    Queries if evaluation of the navigation mode is enabled.
    '''
    return None


def getTurntable() -> vrdTurntable:
    '''
    This object gives access to the turntable.
    '''
    return None


def getUpVectorConstraintSources() -> List[vrdNode]:
    '''
    Returns the list of nodes set as up vector sources for the camera.
    '''
    return None


def getVisualizationScale() -> float:
    '''
    Returns the scaling value used for the camera visualization.
    '''
    return None


def getVisualizationVisible() -> bool:
    '''
    Queries if the visualization for the camera has been enabled.
    '''
    return None


def hasAimConstraint() -> bool:
    '''
    Queries if the camera has an aim constraint.
    '''
    return None


def hasAimConstraintSource(sourceNode: vrdNode) -> bool:
    '''
    Queries if a given node is an aim constraint source for the camera.
    '''
    return None


def isActive() -> bool:
    '''
    Determines if the camera is active.
    '''
    return None


def isDefault() -> bool:
    '''
    Determines if the camera is the default camera.
    '''
    return None


def isInitialCamera() -> bool:
    '''
    Queries if this camera is the initial camera.
    '''
    return None


def removeAimConstraintSources() -> bool:
    '''
    Removes all aim constraint sources from the camera.
    '''
    return None


def removeUpVectorConstraintSources() -> bool:
    '''
    Removes all up vector constraint sources.
    '''
    return None


def setAimConstraintSources(nodes: List[vrdNode]):
    '''
    Sets a list of nodes as aim constraint sources for the camera.
    '''
    pass


def setAimVisualizationScale(value: float):
    '''
    Sets the scaling value for the aim and up vector visualization.
    '''
    pass


def setAimVisualizationVisible(enable: bool):
    '''
    Enables / disables the aim and up vector visualizations.
    '''
    pass


def setDollyZoom(enabled: bool):
    '''
    Enables / disables dolly zoom mode.
    '''
    pass


def setEvaluateNavigationMode(enabled: bool):
    '''
    Enable / disable the evaluation of the navigation mode when playing camera animations.
    '''
    pass


def setInitialCamera():
    '''
    Sets this camera to be the initial camera.
    '''
    pass


def setUpVectorConstraintSources(nodes: List[vrdNode]):
    '''
    Sets a list of nodes as up vector constraint sources.
    '''
    pass


def setVisualizationScale(value: float):
    '''
    Sets a scaling value for the camera visualization.
    '''
    pass


def setVisualizationVisible(enable: bool):
    '''
    Enables / disables the visualization of the camera.
    '''
    pass


def updateFromPerspectiveMatch():
    '''
    Updates this camera�s focal length and rotation according to perspective match settings.
    '''
    pass

