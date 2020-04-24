'''
Autogenerated Method-Stub for:
module vrVariantSets
------------------------------------------

API version: v1
Generation Date: 2020-04-24

VRED-Py: Visual Studio Code Tools for Autodesk VRED
'''

from typing import List



def beginDissection():
    '''
    Starts the dissection process.
    '''
    pass



def captureVariantSetFromRootNodes(sendMsg, roots, inclNodes, inclLights, inclView, name, inclRenderlayerStates, inclEnvs, inclMaterials):
    '''
    Captures variants to an existing variant set.
    '''
    pass



def createVariantSet(name):
    '''
    Creates a variant set.
    '''
    pass



def createVariantSetGroup(name):
    '''
    Creates a variant set group.
    '''
    pass



def deleteVariantSet(name):
    '''
    Deletes a variant set.
    '''
    pass



def deleteVariantSetGroup(name):
    '''
    Deletes a variant set group.
    '''
    pass



def dissectionSnapshot(width, ssf, filename, height):
    '''
    Creates a snapshot in dissection mode.
    '''
    pass



def endDissection():
    '''
    Ends the dissection process.
    '''
    pass



def getGroupedVariantSets():
    '''
    Gets all variant sets.
    '''
    pass



def getMaterialVariantCurrent(name):
    '''
    Returns the current state of a material variant.
    '''
    pass



def getMaterialVariantDefault(name):
    '''
    Returns the default state of a material variant.
    '''
    pass



def getMaterialVariantStates(name):
    '''
    Returns all possible states of a material variant.
    '''
    pass



def getMaterialVariants(name):
    '''
    Returns a list of all material variants of a single variant set or a list of all material variants of all variant sets if you omit the name parameter.
    '''
    pass



def getNodeVariantCurrent(name):
    '''
    Returns the current state of a node variant.
    '''
    pass



def getNodeVariantDefault(name):
    '''
    Returns the default state of a node variant.
    '''
    pass



def getNodeVariantStates(name):
    '''
    Returns all possible states of a node variant.
    '''
    pass



def getNodeVariants(name):
    '''
    Returns a list of all node variants of a single variant set or a list of all node variants of all variant sets set if you omit the name parameter.
    '''
    pass



def getVariantAnimations(name):
    '''
    Returns a list of all animations of a variant set.
    '''
    pass



def getVariantSet(name):
    '''
    Gets a variant set.
    '''
    pass



def getVariantSetPreview(name):
    '''
    Get a preview image for the variant set (if it has one).
    '''
    pass



def getVariantSets():
    '''
    Returns a list of all defined variant sets.
    '''
    pass



def getVariantViewPoints(name):
    '''
    Returns a list of all viewpoints belonging to a variant set.
    '''
    pass



def hideMaterialVariantGeometry(name):
    '''
    Disables the geometry that is switched by a material variant.
    '''
    pass



def hideNodeVariantGeometry(name):
    '''
    Disables the geometry that is switched by a node variant.
    '''
    pass



def hideVariantSetGeometry(name):
    '''
    Disables the geometry that is switched by a variant set.
    '''
    pass



def loadVariants(name):
    '''
    Loads variant definitions from an XML file.
    '''
    pass



def moveVariantSetToGroup():
    '''
    Documentation missing
    '''
    pass



def renderVariantSetPreview(name):
    '''
    Render variant set preview .
    '''
    pass



def saveSwitchedGeometry(filename):
    '''
    Saves the current switched geometry/materials into a file.
    '''
    pass



def saveVariants(name):
    '''
    Saves the variant definitions to an XML file.
    '''
    pass



def selectMaterialVariant(state, name):
    '''
    Activates a state of a material variant.
    '''
    pass



def selectNodeVariant(state, name):
    '''
    Activates a state of a node variant.
    '''
    pass



def selectVariantSetDefault(name):
    '''
    Activates the default state of a variant set.
    '''
    pass



def showMaterialVariantGeometry(name):
    '''
    Enables the geometry that is switched by a material variant.
    '''
    pass



def showNodeVariantGeometry(name):
    '''
    Enables the geometry that is switched by a node variant.
    '''
    pass



def showVariantSetGeometry(name):
    '''
    Enables the geometry that is switched by a variant set.
    '''
    pass


