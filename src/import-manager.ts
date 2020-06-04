import {
  TextDocument,
  Range,
  WorkspaceEdit,
  TextEditor,
  Position,
} from "vscode";
import { ModuleManager } from "./module-manager";

export class ImportManager {
  private imports: { module: string; line: number }[] = [];

  constructor(private _moduleManager: ModuleManager) {}

  public updateImports(document: TextDocument) {
    this.imports = [];

    for (let i = 0; i < document.lineCount; i++) {
      const line = document.lineAt(i).text;

      if (line.startsWith("import")) {
        const importedModule = line.trim().substring(7).trim();
        this.imports.push({ module: importedModule, line: i });
      }

      if (line.startsWith("from")) {
        this.imports.push({ module: "", line: i });
      }
    }
  }

  public addImportToDocument(editor: TextEditor) {
    const document = editor.document;
    const range = editor.selection;

    const moduleName = this._moduleManager.readModuleNameFromCursor(
      document,
      range
    );

    if (this.hasImport(moduleName)) {
      return;
    }

    if (moduleName) {
      const injectLine = this.searchImportInjectLine(document);
      const importStatement = `import ${moduleName}\n`;
      editor.edit((editorBuilder) => {
        editorBuilder.insert(new Position(injectLine, 0), importStatement);
      });
    }
  }

  private hasImport(module: string | undefined): boolean {
    if (module) {
      return !!this.imports.find((tuple) => tuple.module === module);
    }
    return false;
  }

  private searchImportInjectLine(document: TextDocument): number {
    /*
    Search the first line after the first bunch of imports.
    Otherwise add to the top
    */

    let injectLine = 0;

    if (this.imports.length) {
      const linesWithImports = this.imports.map((tuple) => tuple.line);

      let lineHasImport = false;
      for (let i = 0; i < document.lineCount; i++) {
        if (linesWithImports.includes(i)) {
          lineHasImport = true;
          continue;
        }

        if (lineHasImport && !linesWithImports.includes(i)) {
          injectLine = i;
          break;
        }
      }
    }

    return injectLine;
  }
}
