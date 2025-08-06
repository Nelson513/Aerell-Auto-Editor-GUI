# Aerell Auto Editor GUI

Aerell Auto Editor GUI is a graphical user interface (GUI) application designed to simplify video editing using the powerful [Auto-Editor](https://github.com/WyattBlue/auto-editor) tool by WyattBlue.

Built with **PySide6**, this application provides an intuitive interface for users who prefer visual controls over command-line operations. It can be compiled into a standalone executable using **Nuitka**, making it easy to distribute and run without requiring a Python environment.

## Features
- User-friendly GUI for Auto-Editor
- Built with PySide6 for native look and feel
- Pre-configured with `pyproject.toml` and `uv.lock` for reliable dependency management
- Standalone executable build support via Nuitka (Windows-ready with `build.cmd`)
- Inspired by [auto-editor-gui](https://github.com/sashminea/auto-editor-gui) by sashminea

## Requirements
- [Python](https://www.python.org/downloads/) (recommended: 3.12)
- [uv](https://github.com/astral-sh/uv) – Fast Python package installer and resolver
- Windows (for pre-built `build.cmd`; Linux/macOS users can create custom build scripts)

## Installation
This project uses `uv` for virtual environment and dependency management.

1. **Create virtual environment and install dependencies**:
   ```bash
   uv sync
   ```
   > This will create a virtual environment and install all required packages based on `pyproject.toml` and `uv.lock`.

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

## Usage
After installation, run the application with:
```bash
uv run -m aerell_auto_editor_gui
```

Use the GUI to:
- Select your video/audio file
- Adjust editing settings (silence threshold, speed changes, etc.) (Not all of them, only the export feature)
- Process the file using Auto-Editor’s smart cutting algorithm

## Building Standalone Executable (Windows)
A pre-made build script is included for Windows users.

1. Run the batch script:
   ```cmd
   build.cmd
   ```
   
2. An executable file will be created in a new folder that will appear in the root folder with the name `aerell-auto-editor-gui.exe`.

> **Note for Linux/macOS users**: The `build.cmd` script is Windows-specific. You can create your own build script using a similar Nuitka command (adjust paths and flags as needed).

## Credits
- [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) – Core video/audio editing engine
- [sashminea/auto-editor-gui](https://github.com/sashminea/auto-editor-gui) – GUI inspiration
- [Astral.sh uv](https://github.com/astral-sh/uv) – Modern Python packaging
- **Aerell** – Developer of this GUI adaptation

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.