from aerell_auto_editor_gui.ae_export_enum import AEExportEnum
from aerell_auto_editor_gui.ae_arg import AEArgument
from aerell_auto_editor_gui.ae import AE
from PySide6.QtCore import (
    Qt
)
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QComboBox,
    QSizePolicy
)

class AEWidget(QWidget):
    def __init__(self, ae: AE, arg: AEArgument):
        super().__init__()

        # Setup
        self._ae = ae
        self._arg = arg

        # Layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # File
        label_title_file = QLabel('File')
        label_title_file.setStyleSheet('font-weight: bold;')

        self._label_full_path = QLabel('')
        self._label_full_path.setVisible(False)
        self._label_full_path.setWordWrap(True)

        button_import = QPushButton('Import')
        button_import.clicked.connect(self._button_import_clicked)

        # Editing Options
        label_title_editing_option = QLabel('Editing Options')
        label_title_editing_option.setStyleSheet('font-weight: bold;')

        layout_combo_export = QHBoxLayout()
        layout_combo_export.setAlignment(Qt.AlignmentFlag.AlignLeft)

        label_combo_export = QLabel('Export')

        self._combo_export = QComboBox()
        for enum in AEExportEnum:
            self._combo_export.addItem(enum.value[0])
        self._combo_export.currentIndexChanged.connect(self._combo_export_current_index_changed)
        self._combo_export.setCurrentIndex(1)

        layout_combo_export.addWidget(label_combo_export)
        layout_combo_export.addWidget(self._combo_export)

        widget_combo_export = QWidget()
        widget_combo_export.setLayout(layout_combo_export)

        widget_gap = QWidget()
        widget_gap.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._button_execute = QPushButton('Execute')
        self._button_execute.setDisabled(True)
        self._button_execute.clicked.connect(self._button_execute_clicked)

        # Layout Add Widget
        layout.addWidget(label_title_file)
        layout.addWidget(self._label_full_path)
        layout.addWidget(button_import)

        layout.addWidget(label_title_editing_option)
        layout.addWidget(widget_combo_export)

        layout.addWidget(widget_gap)

        layout.addWidget(self._button_execute)

        self.setLayout(layout)

    def _button_import_clicked(self):
        full_path, _ = QFileDialog.getOpenFileName(self, "Import media", "", "(*.mp4 *.mov)")

        if full_path:
            self._label_full_path.setText(full_path)
            self._label_full_path.setVisible(True)
            self._arg.input = full_path
            self._button_execute_update()

    def _button_execute_clicked(self):
        self._button_execute.setDisabled(True)
        self._ae.run_arg(self._arg)
        self._button_execute.setDisabled(False)

    def _combo_export_current_index_changed(self, index):
        self._arg.export = list(AEExportEnum)[index]
        self._button_execute_update()

    def _button_execute_update(self):
        if hasattr(self, '_button_execute'):
            self._button_execute.setDisabled(not self._arg.valid())