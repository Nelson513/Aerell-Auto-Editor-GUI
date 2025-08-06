from aerell_auto_editor_gui.ae_export_enum import AEExportEnum

class AEArgument():
    def __init__(
            self, 
            input: str | None = None, 
            export: AEExportEnum | None = None, 
            output: str | None = None
    ):
        self._input: str | None = input

        # Editing Options
        self._export: AEExportEnum | None = export
        self._output: str | None = output

    def clear(self):
        self._input = None
        self._export = None
        self._output = None

    def valid(self) -> bool:
        return self._input != None

    @property
    def input(self) -> str | None:
        return self._input
    
    @property
    def export(self) -> AEExportEnum | None:
        return self._export
    
    @property
    def output(self) -> str | None:
        return self._output
    
    @input.setter
    def input(self, value: str | None):
        self._input = value

    @export.setter
    def export(self, value: AEExportEnum | None):
        self._export = value

    @output.setter
    def output(self, value: str | None):
        self._output = value