# ⚡ Terminal CLI TODO

Terminal CLI TODO is a Command Line Interface (CLI) application designed for high-efficiency task management. It features a tactical "root-access" aesthetic, real-time system logging, and mission-data export capabilities.

---

## 🚀 Key Features
* **Tactical Priority System:** Categorize targets as `--high`, `--mid`, or `--low` with adaptive color-coding.
* **Operation Tagging:** Use the `@` symbol to group tasks into specific "Operations" (e.g., `@work`, `@secret`).
* **System Blackbox:** Automatic background logging of every command and system event to `system.log`.
* **Intelligence Reports:** Generate timestamped `.txt` mission reports for external use.
* **Zero-Dependency:** Runs on pure Python 3 without needing external libraries.
* **Cross-Platform:** Full compatibility with Windows (PowerShell/CMD), macOS, and Linux.

---

## 🚀 Easy 1-Minute Install

1. **Install Python:** Download it from [python.org](https://www.python.org/).
2. **Download the Script:** Save the `shred.py` code to your computer.
3. **Run the App:**
   - Open your Terminal (Mac/Linux) or Command Prompt (Windows).
   - Type `python shred.py` and hit **Enter**.

## ⌨️ How to Use

- **Add a task:** `add Hack the bank @ops --high`
- **Add a simple task:** `add Buy coffee`
- **Delete a task:** `shred 1`
- **Save to file:** `export`
- **Close app:** `exit`

## 📂 Where is my data?
- `tasks.json`: Your saved tasks.
- `system.log`: A history of everything you've done.
- `REPORT_*.txt`: Your exported list files.