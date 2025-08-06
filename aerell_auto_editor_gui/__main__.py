import sys

from aerell_auto_editor_gui.ae_arg import AEArgument
from aerell_auto_editor_gui.ae import AE
from aerell_auto_editor_gui.app import App

def main():
    ae = AE()
    arg = AEArgument()
    sys.exit(App(sys.argv, ae=ae, arg=arg).exec())

if __name__ == '__main__':
    main()