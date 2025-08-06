from aerell_auto_editor_gui.ae_arg import AEArgument
from aerell_auto_editor_gui.ae import AE
from aerell_auto_editor_gui.main_window import MainWindow
from PySide6.QtWidgets import (
    QApplication,
)

class App():
    def __init__(self, argv, ae: AE, arg: AEArgument):
        self._app = QApplication(argv)

        self.window = MainWindow(ae=ae, arg=arg)
        self.window.show()

    def exec(self) -> int:
        return self._app.exec()