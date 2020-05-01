'''
vrdRayFile
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Interface to ray files.
'''

from typing import List


class vrdRayFile():
    pass


class vrdRayFileInfo():
    pass


def clear():
    '''
    Clears the loaded file.
    '''
    pass


def getDirectEvaluationConeAngle() -> float:
    '''
    Returns the cone of valid directions used when directly looking into a ray file.
    '''
    return None


def getDirectEvaluationOffset() -> float:
    '''
    Returns the offset along the surface normal to be used when directly looking into a ray file. Use this to fix lookup surfaces that are not exactly where the ray origins are.
    '''
    return None


def getDirectEvaluationRadius() -> float:
    '''
    Returns the radius to be used for lookup when directly looking into a ray file.
    '''
    return None


def getFileName() -> str:
    '''
    Returns the file name of the ray file.
    '''
    return None


def getRayFileInfo() -> vrdRayFileInfo:
    '''
    Returns ray file information.
    '''
    return None


def getUsePhotonsForDirectLighting() -> bool:
    '''
    Returns whether photon mapping for direct lighting is used or not. If disabled, ray lights can be used without photon mapping but it is necessary to define surface with ray light evaluation turned on. These surfaces will then act as light sources using all the ray files that are within the given radius.
    '''
    return None


def getUseRandomSampling() -> bool:
    '''
    Returns if random sampling of the rays is used.
    '''
    return None


def getVisualizationRayCount() -> int:
    '''
    Returns the number of rays used for the viewport visualization.
    '''
    return None


def getVisualizationRayLength() -> float:
    '''
    Returns the length used for the viewport visualization of rays.
    '''
    return None


def load(filename: str):
    '''
    Loads the given file.
    '''
    pass


def reload():
    '''
    Reloads the current file.
    '''
    pass


def setDirectEvaluationConeAngle(angle: float):
    '''
    Sets the cone of valid directions to be used when directly looking into a ray file.
    '''
    pass


def setDirectEvaluationOffset(offset: float):
    '''
    Sets the offset along the surface normal to be used when directly looking into a ray file. Use this to fix lookup surfaces that are not exactly where the ray origins are.
    '''
    pass


def setDirectEvaluationRadius(radius: float):
    '''
    Sets the radius to be used for lookup when directly looking into a ray file.
    '''
    pass


def setFileName(fileName: str):
    '''
    Loads the given ray file and sets the file name.
    '''
    pass


def setTo(other: vrdRayFile):
    '''
    Shares data of ray file in order to reduce memory consumption. Note that when a ray file is no longer used by any light it will be removed and needs to be reloaded from disk again.
    '''
    pass


def setUsePhotonsForDirectLighting(use: bool):
    '''
    Toggles whether to use photon mapping for direct lighting or not. If disabled, ray lights can be used without photon mapping but it is necessary to define surface with ray light evaluation turned on. These surfaces will then act as light sources using all the ray files that are within the given radius.
    '''
    pass


def setUseRandomSampling(use: bool):
    '''
    Uses random sampling of the rays. Use this if you have more than one luminaire in your ray file.
    '''
    pass


def setVisualizationRayCount(count: int):
    '''
    Sets the number of rays used for the viewport visualization.
    '''
    pass


def setVisualizationRayLength(length: float):
    '''
    Sets the length of used for the viewport visualization of rays.
    '''
    pass

