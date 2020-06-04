import { workspace, Uri, TextDocument, Range } from "vscode";
import * as path from "path";

export class ModuleManager {
  private regEx = /def\s(.+)\(.*\)/g;

  private functionModuleMapping: Map<string, string> = new Map<
    string,
    string
  >();

  private moduleSet: Set<string> = new Set<string>();

  constructor() {}

  public async init(pythonDirectory: Uri) {
    const pythonFiles = await this.getPythonFiles(pythonDirectory);
    await this.buildModuleSet(pythonFiles);
    await this.buildFunctionModuleMapping(pythonFiles);
  }

  public readModuleNameFromCursor(
    document: TextDocument,
    range: Range
  ): string | undefined {
    const selectedWordRange = document.getWordRangeAtPosition(range.start);

    if (selectedWordRange) {
      const wordUnderCursor = document.getText(selectedWordRange);

      if (this.isModule(wordUnderCursor)) {
        return wordUnderCursor;
      }

      if (this.isMethodOfModule(wordUnderCursor)) {
        return this.functionModuleMapping.get(wordUnderCursor);
      }
    }
    return undefined;
  }

  private isModule(word: string): boolean {
    return this.moduleSet.has(word);
  }

  private isMethodOfModule(word: string): boolean {
    return this.functionModuleMapping.has(word);
  }

  private async buildModuleSet(pythonFiles: [string, string][]) {
    this.moduleSet.clear();
    pythonFiles.forEach((pythonFile) => {
      this.moduleSet.add(pythonFile[0].split(".")[0]);
    });
  }

  private async buildFunctionModuleMapping(pythonFiles: [string, string][]) {
    await Promise.all(
      pythonFiles.map(async (pythonFile) => {
        const fileUri = Uri.file(pythonFile[1]);
        const moduleName = pythonFile[0].split(".")[0];
        const methodNames = await this.extractMethods(fileUri);

        methodNames.forEach((methodName) => {
          this.functionModuleMapping.set(methodName, moduleName);
        });
      })
    );
  }

  private async extractMethods(documentUri: Uri): Promise<string[]> {
    return workspace.openTextDocument(documentUri).then((document) => {
      const methods = [];
      if (document) {
        for (let i = 0; i < document.lineCount; i++) {
          const line = document.lineAt(i).text.trim();

          if (line.startsWith("def")) {
            const matches = this.regEx.exec(line);
            if (matches && matches.length > 1) {
              methods.push(matches[1]);
            }
          }
        }
      }
      return methods;
    });
  }

  private async getPythonFiles(directory: Uri): Promise<[string, string][]> {
    const pythonFiles: [string, string][] = [];

    const files = await workspace.fs.readDirectory(directory);
    files.forEach((tuple) => {
      const fileName = tuple[0].split(".")[0];
      const absolutePath = path.join(directory.fsPath, `${fileName}.py`);
      pythonFiles.push([fileName, absolutePath]);
    });

    return pythonFiles;
  }
}
