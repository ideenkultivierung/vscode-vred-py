'''
vrAssetsModule
------------------------------------------
API version: v1 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from typing import List


def applyMaterialAssetsByName(path):
    '''
    Each material in the scene is replaced by an equally-named material asset that can be found under the specified directory and its sub-directories.
    '''
    pass


def createEnvironmentAsset(assetManagerDirectory, environmentNode):
    '''
    Saves the given environment node as a new environment asset in the given directory.
    '''
    pass


def createGeometryAsset(assetManagerDirectory, node):
    '''
    Saves the given node as a new geometry asset in the given directory.
    '''
    pass


def createMaterialAsset(material, assetManagerDirectory):
    '''
    Saves the given material as a new material asset in the given directory.
    '''
    pass


def createSceneplateAsset(assetManagerDirectory, node):
    '''
    Saves the given node as a new sceneplate asset in the given directory.
    '''
    pass


def getSelectedAssetDirectory(assetType):
    '''
    Returns the path of the currently selected directory in the Asset Manager directory view in the tab of the given asset type.
    '''
    pass


def getSelectedMaterialAssetDirectory():
    '''
    Deprecated.
    '''
    pass


def loadEnvironmentAssetByName(assetName, assetPath):
    '''
    Load an environment asset from the Asset Manager by specifying the name of the asset and, optionally, the path where it is stored.
    '''
    pass


def loadEnvironmentAssetByUUID(assetUUID):
    '''
    Searches for an environment asset with the given UUID in the Asset Manager and loads it, if found.
    '''
    pass


def loadGeometryAssetByName(assetName, assetPath):
    '''
    Load a geometry asset from the Asset Manager by specifying the name of the asset and, optionally, the path where it is stored.
    '''
    pass


def loadGeometryAssetByUUID(assetUUID):
    '''
    Searches for a geometry asset with the given UUID in the Asset Manager and loads it, if found.
    '''
    pass


def loadMaterialAssetByName(assetName, assetPath):
    '''
    Load a material asset from the Asset Manager by specifying the name of the asset and, optionally, the path where it is stored.
    '''
    pass


def loadMaterialAssetByUUID(assetUUID):
    '''
    Searches for a material asset with the given UUID in the Asset Manager and loads it, if found.
    '''
    pass


def loadSceneplateAssetByName(assetName, assetPath):
    '''
    Load a sceneplate asset from the Asset Manager by specifying the name of the asset and, optionally, the path where it is stored.
    '''
    pass


def loadSceneplateAssetByUUID(assetUUID):
    '''
    Searches for a sceneplate asset with the given UUID in the Asset Manager and loads it, if found.
    '''
    pass


def overwriteEnvironmentAsset(environmentAsset):
    '''
    If the given environment node has a reference to an already existing environment asset in the Asset Manager, it overwrites that asset.
    '''
    pass


def overwriteGeometryAsset(assetRootNode):
    '''
    If the given node has a reference to an already existing geometry asset in the Asset Manager, it overwrites that asset.
    '''
    pass


def overwriteMaterialAsset(material):
    '''
    If the given material has a reference to an already existing material asset in the Asset Manager, it overwrites that asset.
    '''
    pass


def overwriteSceneplateAsset(assetRootNode):
    '''
    If the given node has a reference to an already existing sceneplate asset in the Asset Manager, it overwrites that asset.
    '''
    pass


def reloadAllAssetDirectories():
    '''
    Reloads all directories in the asset manager.
    '''
    pass


def reloadAssetDirectory(url):
    '''
    Reloads the directory with the specified path.
    '''
    pass

