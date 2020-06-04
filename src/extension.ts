import * as vscode from "vscode";
import * as path from "path";
import { Uri } from "vscode";
import { ModuleManager } from "./module-manager";
import { VredCodeActionProvider } from "./vred-code-action-provider";
import { ImportManager } from "./import-manager";

export async function activate(context: vscode.ExtensionContext) {
  let pythonConfig = vscode.workspace.getConfiguration("python");
  let extraPaths: string[] = pythonConfig.get("autoComplete.extraPaths") || [];
  let pythonPath: string = path.join(path.dirname(__dirname), "python");

  if (!extraPaths.includes(pythonPath)) {
    extraPaths.splice(0, 0, pythonPath);
  }
  pythonConfig.update("autoComplete.extraPaths", extraPaths, true);

  let moduleManager = new ModuleManager();
  let importManager = new ImportManager(moduleManager);

  await moduleManager.init(Uri.file(pythonPath));

  context.subscriptions.push(
    vscode.languages.registerCodeActionsProvider(
      "python",
      new VredCodeActionProvider(moduleManager),
      {
        providedCodeActionKinds: [vscode.CodeActionKind.QuickFix],
      }
    )
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("vred-py.add-to-import", async () => {
      if (activeEditor) {
        importManager.addImportToDocument(activeEditor);
      }
    })
  );

  let activeEditor = vscode.window.activeTextEditor;

  if (activeEditor) {
    importManager.updateImports(activeEditor.document);
  }

  vscode.window.onDidChangeActiveTextEditor(
    async (editor) => {
      activeEditor = editor;
      if (activeEditor) {
        importManager.updateImports(activeEditor.document);
      }
    },
    null,
    context.subscriptions
  );

  vscode.workspace.onDidChangeTextDocument(
    async (event) => {
      if (activeEditor) {
        importManager.updateImports(activeEditor.document);
      }
    },
    null,
    context.subscriptions
  );
}

export function deactivate() {}
