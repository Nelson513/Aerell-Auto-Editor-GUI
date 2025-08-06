import sys, threading, time
from aerell_auto_editor_gui.ae_arg import AEArgument
from auto_editor.__main__ import main as auto_editor_main

class AE():
    def __init__(self):
        self._version: str | None = None

    @property
    def version(self) -> str | None:
        if self._version == None:
            self._run_internal(args=['--version'], callback=self._set_version)

        return self._version
    
    def _set_version(self, output):
        self._version = output

    def _run_internal(self, args: list) -> int:
        def run():
            old_argv = sys.argv
            sys.argv = ['auto_editor'] + args

            try:
                try:
                    auto_editor_main()
                except Exception as e:
                    print(f"[ERROR] auto_editor crashed: {e}", file=sys.stderr)
                except SystemExit:
                    pass
            finally:
                sys.argv = old_argv

        thread = threading.Thread(target=run, daemon=True)
        thread.start()

        while thread.is_alive():
            time.sleep(0.05)

        thread.join(timeout=1)

        return 0

    def gen(self, arg: AEArgument) -> list[str]:
        if not arg.valid():
            raise ValueError(f'Incomplete argument.')
        
        command: list[str] = []

        if arg.input != None:
            command.append(arg.input)

        if arg.export != None:
            command.append('--export')
            command.append(arg.export.value[0])

        if arg.output != None:
            command.append('--output')
            command.append(arg.output)

        return command

    def run_arg(self, arg: AEArgument) -> int | None:
        return self._run_internal(args=self.gen(arg=arg))