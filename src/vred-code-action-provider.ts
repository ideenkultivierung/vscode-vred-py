import {
  CodeActionProvider,
  TextDocument,
  CodeActionContext,
  CancellationToken,
  CodeAction,
  CodeActionKind,
  WorkspaceEdit,
  ProviderResult,
  Command,
  Range,
  Position,
} from "vscode";
import { ModuleManager } from "./module-manager";

export class VredCodeActionProvider implements CodeActionProvider {
  constructor(private _moduleManager: ModuleManager) {}

  public provideCodeActions(
    document: TextDocument,
    range: import("vscode").Range | import("vscode").Selection,
    context: CodeActionContext,
    token: CancellationToken
  ): ProviderResult<(Command | CodeAction)[]> {
    const moduleName = this._moduleManager.readModuleNameFromCursor(
      document,
      range
    );

    if (moduleName) {
      const actions = [];
      const importAction = this.createImportAction(moduleName);
      if (importAction) {
        actions.push(importAction);
      }
      actions.push(this.createOrganizeImportsAction());
      return actions;
    } else {
      return;
    }
  }

  private createImportAction(vredModule: string): CodeAction {
    const action = new CodeAction(
      `Add ${vredModule} to imports`,
      CodeActionKind.QuickFix
    );
    action.command = {
      command: "vred-py.add-to-import",
      title: `Add ${vredModule} to imports`,
    };
    action.isPreferred = true;
    return action;
  }

  private createOrganizeImportsAction(): CodeAction {
    const title = "Organize imports";
    const action = new CodeAction(title, CodeActionKind.SourceOrganizeImports);
    // action.command = {
    //   command: "vred-py.add-to-import",
    //   title: `Add ${vredModule} to imports`,
    // };
    return action;
  }
}
