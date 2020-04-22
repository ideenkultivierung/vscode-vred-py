"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const path = require("path");
function activate(context) {
    let pythonConfig = vscode.workspace.getConfiguration("python");
    let extraPaths = pythonConfig.get("autoComplete.extraPaths") || [];
    let autoCompletionPath = path.join(path.dirname(__dirname), "python");
    if (!extraPaths.includes(autoCompletionPath)) {
        extraPaths.splice(0, 0, autoCompletionPath);
        pythonConfig.update("autoComplete.extraPaths", extraPaths, true);
    }
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map