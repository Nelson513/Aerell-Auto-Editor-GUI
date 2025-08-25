[![Releases](https://img.shields.io/github/v/release/Nelson513/Aerell-Auto-Editor-GUI?label=Releases&color=blue&logo=github)](https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases)  
https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases

# Aerell Auto-Editor GUI — Efficient Media Analysis & Rendering

A modern desktop GUI for auto-editor. It merges the power of automatic media editing with a clear, visual interface. Use it to detect silence, trim content, sync audio and video tracks, batch-process files, and export final renders.

Badges
- [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
- [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
- [![PySide6](https://img.shields.io/badge/UI-PySide6-orange.svg)](https://pypi.org/project/PySide6/)
- [![Releases](https://img.shields.io/badge/Download-Releases-brightgreen.svg)](https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases)

Table of Contents
- Features
- Screenshots
- Quick Start
  - Download and Execute (Releases)
  - Install from Source
- How It Works
  - Import
  - Analyze
  - Edit
  - Render
- Settings and Controls
  - Analysis Settings
  - Rendering Settings
  - Export Profiles
- Supported Formats
- Workflows and Examples
  - Trim filler audio
  - Create highlights reel
  - Podcast cleanup
  - Batch encode for web
- Integration with auto-editor CLI
  - Command mapping
  - Custom flags
- Performance and Resource Tips
- Advanced Usage
  - Automation and presets
  - Watch folder
  - Headless mode
- Developer Guide
  - Architecture
  - Folder layout
  - Build and test
- Contributing
- Troubleshooting
- FAQ
- Changelog & Releases
- License

Features
- Visual analysis for silence, speech, and scene changes.
- Drag-and-drop import for audio and video.
- Preset-based export profiles for web, mobile, and archival.
- Batch processing and queue.
- Built on auto-editor core for robust trimming logic.
- PySide6 GUI that runs on Windows, macOS, and Linux.
- Timeline with waveform and frame preview.
- Manual override tools: split, crop, lock segments.
- Metadata read/write for common containers.

Screenshots

Main window with timeline and waveform:
![Main Window](https://images.unsplash.com/photo-1511512578047-dfb367046420?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=60)

Analysis panel showing silence detection:
![Analysis Panel](https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=60)

Render dialog and export profiles:
![Render Dialog](https://images.unsplash.com/photo-1507679799987-c73779587ccf?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=60)

Quick Start

Download and Execute (Releases)
- Visit the Releases page: https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases
- Choose the asset that matches your OS. For example:
  - Windows: `Aerell-Auto-Editor-GUI-1.0.0-win-x64.exe`
  - macOS: `Aerell-Auto-Editor-GUI-1.0.0-mac.dmg`
  - Linux: `Aerell-Auto-Editor-GUI-1.0.0-x86_64.AppImage` or `Aerell-Auto-Editor-GUI-1.0.0-linux.tar.gz`
- Download the file and execute it. The file you download must be executed to install or run the app.
- If the release does not match your platform or you prefer source builds, follow the source install steps below.

Install from Source
- Ensure Python 3.8 or newer is installed.
- Install dependencies:
  - `pip install -r requirements.txt`
  - Key packages: `auto-editor`, `pyside6`, `ffmpeg-python` (or system ffmpeg), `numpy`
- Run the app:
  - `python -m aerell_gui.main`
- For a dev install:
  - `pip install -e .`
- For headless use, run the bundled CLI wrapper that maps GUI presets to auto-editor flags.

How It Works

Import
- Drag files to the main window or use the File > Open menu.
- The GUI reads audio and video tracks.
- It extracts waveform data and key frames for the timeline.
- It reads metadata like sample rate, channels, codec, and duration.

Analyze
- Use the Analysis button to run the detection pass.
- The GUI uses auto-editor core methods for:
  - Silence detection
  - Loudness detection
  - Scene change detection
- Analysis runs in a background thread.
- The UI shows progress and a visual overlay on the timeline.

Edit
- The GUI maps analysis results to segments.
- Click a segment to view options.
- Use lock to preserve a segment.
- Use split to cut segments at playhead.
- Use ripple edit to shift downstream segments.
- Use trim handles on the timeline to refine boundaries.

Render
- Open the Render dialog to set output options.
- Choose codec, container, bit rate, resolution, and frame rate.
- Select an export preset or set custom flags.
- Start render. The GUI uses a worker process for ffmpeg calls.
- Monitor progress and logs in the render panel.

Settings and Controls

Analysis Settings
- Silence threshold: set dBFS level to mark silence.
- Minimum silence length: set seconds to detect continuous quiet parts.
- Loudness normalization: choose target LUFS if you want consistent loudness.
- Scene threshold: set pixel/OPQ threshold for scene change detection.
- Channels: choose which audio channel(s) to analyze.

Rendering Settings
- Encoder: choose `libx264`, `libx265`, `libvpx-vp9`, or `aac` for audio.
- Container: `mp4`, `mkv`, `webm`, `mov`.
- Resolution: scale or keep source resolution.
- Frame rate: keep or set a target FPS.
- Audio sample rate and channels: set 48000 Hz stereo, or keep source.
- Bitrate control: choose target bitrate or CRF.

Export Profiles
- Web: `mp4` + `libx264`, `aac`, 1080p, crf 23.
- Mobile: 720p, lower bitrate, AAC.
- Archive: lossless or near-lossless settings, higher bitrate, `mkv`.
- Podcast: export audio only, `mp3` or `aac`, loudness target.

Supported Formats
- Video: MP4, MKV, MOV, WEBM, AVI (subject to ffmpeg support).
- Audio: WAV, MP3, AAC, FLAC, OGG.
- Images: PNG, JPG for storyboards and thumbnails.
- Containers and codecs depend on installed ffmpeg build.

Workflows and Examples

Trim filler audio
- Import a long interview.
- Set silence threshold to -40 dB and min silence to 0.5 s.
- Run analysis.
- Inspect segments and lock intro and exit.
- Render with podcast profile.

Create highlights reel
- Import a match or event footage folder.
- Run scene detection and loudness analysis.
- Use auto markers to extract top N loud segments.
- Batch render clips or assemble them into a highlights sequence.

Podcast cleanup
- Import multi-track session.
- Run loudness normalization to -16 LUFS.
- Remove silence and noise between segments.
- Apply a fixed fade for cuts.
- Export multitrack stems or single mixed file.

Batch encode for web
- Add a queue of project files.
- Pick a Web export preset.
- Set maximum concurrent jobs based on CPU threads.
- Start queue and monitor progress.

Integration with auto-editor CLI

Command mapping
- The GUI exposes common auto-editor flags as controls.
  - `--cut` maps to segment trimming mode.
  - `--silent_threshold` maps to Silence threshold control.
  - `--min_clip_length` maps to Minimum cut length.
  - `--export_preset` creates a command line tag that the wrapper uses.

Custom flags
- Use the Advanced > Extra Flags field to pass raw auto-editor flags.
- The GUI composes the final command and runs it in a worker process.
- Error messages and stdout appear in the log panel.

Performance and Resource Tips
- Use a dedicated SSD for working media to reduce I/O wait.
- Increase worker process count only if you have CPU cores to spare.
- GPU hardware encode helps for long renders; choose encoder that supports your GPU.
- Keep project thumbnails low resolution during edit to reduce memory use.
- Close other CPU-heavy apps when rendering.

Advanced Usage

Automation and presets
- Create a preset with analysis and export settings.
- Apply preset to a folder of files.
- Use CLI wrapper to run preset in headless mode for a cron job.

Watch folder
- Enable Watch Folder to process new files automatically.
- The GUI picks a preset and runs analysis and render.
- Use this to offload routine tasks to a server.

Headless mode
- For CI and servers, run the bundled headless wrapper.
- The wrapper accepts JSON project descriptors.
- It maps to auto-editor flags and uses ffmpeg for render.

Developer Guide

Architecture
- UI layer: PySide6 widgets, signals, and slots.
- Core layer: wrappers around auto-editor functions and ffmpeg helpers.
- Worker layer: background tasks for analysis and render.
- IPC: use local sockets for status and logs.
- Config: user settings stored in JSON in the app data folder.

Folder layout (example)
- `aerell_gui/` — main package
  - `ui/` — Qt UI files and layouts
  - `core/` — analysis and render logic
  - `wrappers/` — auto-editor and ffmpeg wrappers
  - `assets/` — icons and images
  - `tests/` — unit and integration tests
- `scripts/` — build helpers and installers
- `requirements.txt` — runtime deps
- `setup.cfg`, `pyproject.toml` — packaging metadata

Build and test
- Run unit tests:
  - `pytest tests/`
- Linting:
  - `flake8 aerell_gui`
- UI compile:
  - `pyside6-uic ui/main.ui -o aerell_gui/ui/main_ui.py`
- Package:
  - Use PyInstaller for a single executable.
  - Use the provided build script `scripts/build_release.sh`.

Contributing
- Fork the repo and create a branch per feature or fix.
- Keep commits small and focused.
- Write tests for logic code.
- Follow the code style used in the project.
- Submit a pull request with a clear title and description.
- Mention related issues and steps to reproduce bugs.

Troubleshooting

Common issues and checks
- App fails to start:
  - Check that Python or the runtime is the right version.
  - For releases, confirm the downloaded file is executable.
- Analysis seems off:
  - Check silence threshold and minimum silence length.
  - Inspect raw waveform to confirm audio level.
- Render fails with ffmpeg error:
  - Verify ffmpeg is installed or the bundled ffmpeg is compatible.
  - Check codec settings and container compatibility.
- High memory use:
  - Reduce preview frame cache.
  - Lower waveform resolution in settings.

Logs and diagnostics
- Open Help > Logs to view analysis and render logs.
- Attach the latest log file when opening an issue.
- The app writes a diagnostics bundle on demand for deeper analysis.

FAQ

Q: Where do I get the latest app?
A: Visit the Releases page: https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases. Download the matching asset for your OS and run the file you downloaded.

Q: Does it require auto-editor installed?
A: The releases bundle auto-editor core in the packaged app. For source installs, add `auto-editor` to your environment.

Q: Can I use custom auto-editor flags?
A: Yes. Use the Advanced > Extra Flags field. Use valid auto-editor flags and values.

Q: Can I process multiple files at once?
A: Yes. Add files to the queue and start batch processing.

Q: Is the app cross-platform?
A: Yes. The GUI runs on Windows, macOS, and Linux. Releases include platform-specific builds.

Changelog & Releases

Stable releases and beta builds appear on the Releases page. Each release includes:
- Platform assets
- SHA256 checksums
- Release notes with breaking changes and migration steps

Go to Releases to download a build or read the notes:
[Download Releases](https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases)

License

This project uses the MIT License. See the LICENSE file for full text.

Appendix: Common Settings and Recommended Values

Silence detection
- Threshold: -38 to -32 dB for speech.
- Minimum silence length: 0.25 to 0.6 s for fast cuts; 0.8 to 1.5 s for slower edits.
- Keep tail: 0.05 to 0.2 s to avoid abrupt cuts.

Loudness
- Podcast: -16 LUFS integrated
- Video: -14 LUFS target for streaming platforms
- Broadcast: -23 LUFS for certain regions

CRF and bitrate
- Web 1080p: CRF 23, preset medium, 8-12 Mbps target
- Archive: CRF 18 or lossless
- Mobile 720p: CRF 28, 2-4 Mbps

Export containers
- MP4 for general compatibility
- MKV for multiple audio tracks and subtitles
- WEBM for web applications using VP9 or AV1

Automated Workflows: JSON Project Descriptor

Fields
- `input`: path or list of paths
- `preset`: export preset name
- `analysis`: object with thresholds and detection options
- `queue`: behavior for batch processing
- `output`: path and naming template

Example (use inline JSON in scripts)
- `{"input":"./media/interview.mp4","preset":"podcast","analysis":{"silence_threshold":-36,"min_silence":0.5},"output":"./out/{name}_clean.mp4"}`

Best Practices

Project organization
- Keep source media in a dedicated folder.
- Use symbolic links for large media when working with project templates.
- Use versioned presets to track export changes.

Backups
- Keep original files untouched.
- Store exported masters on a different drive for redundancy.

Security
- Avoid running releases from untrusted sources.
- Inspect scripts and extra flags before running them on production media.

Accessibility
- Use captions and subtitles export if the project includes speech.
- Export an SRT file alongside video to support translation.

Localization
- The UI supports multiple languages via translation files.
- Add or edit translations under `aerell_gui/i18n/`.

Keyboard Shortcuts (default)
- Space: Play/Pause
- J/K/L: Shuttle back/pause/forward
- S: Split at playhead
- R: Render dialog
- Ctrl+Z: Undo
- Ctrl+Shift+S: Save project

Known Limitations
- Complex multitrack routing may need manual adjustment before render.
- Certain legacy codecs require a full ffmpeg build with non-free libraries.

Contact and Support
- Open an issue on GitHub with logs and reproducible steps.
- Use the Discussions tab for feature ideas and workflow tips.

Credits
- Built on auto-editor for core edit logic.
- UI uses PySide6 and Qt widgets.
- Icons and images come from open-source collections and contributed assets.

Security Reporting
- Report security issues through the repository's issue tracker with private flag if needed.

Project Roadmap (high level)
- Improved GPU-accelerated analysis for scene detection.
- Plugin system for effects and transitions.
- Cloud render integration and remote worker support.
- Advanced stem export and multitrack session support.

Files in Releases (example)
- `Aerell-Auto-Editor-GUI-1.0.0-win-x64.exe` — Installer for Windows.
- `Aerell-Auto-Editor-GUI-1.0.0-mac.dmg` — Installer for macOS.
- `Aerell-Auto-Editor-GUI-1.0.0-x86_64.AppImage` — Portable Linux image.
- `Aerell-Auto-Editor-GUI-1.0.0-source.tar.gz` — Source archive.

If you encounter a release asset that does not run, check the Releases page for alternate files or debug assets. The Releases page will include checksums and platform notes. Visit: https://github.com/Nelson513/Aerell-Auto-Editor-GUI/releases

Project Topics and Tags
- audio
- audio-editing
- audio-processing
- auto-editor
- automatic
- gui
- pyside6
- python
- video
- video-editing
- video-processing

End of file