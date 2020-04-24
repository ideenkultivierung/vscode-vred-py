import * as vscode from "vscode";
import * as path from "path";

export function activate(context: vscode.ExtensionContext) {
  let pythonConfig = vscode.workspace.getConfiguration("python");

  let extraPaths: string[] = pythonConfig.get("autoComplete.extraPaths") || [];
  let pythonPath: string = path.join(path.dirname(__dirname), "python");

  if (!extraPaths.includes(pythonPath)) {
    extraPaths.splice(0, 0, pythonPath);
  }
  pythonConfig.update("autoComplete.extraPaths", extraPaths, true);
}

export function deactivate() {}
