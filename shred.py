import json
import os
import time
from datetime import datetime

FILE_NAME = "tasks.json"
LOG_FILE = "system.log"

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_event(message):
    """Robust logging with automatic file closing"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
      f.write(f"[{timestamp}] {message}\n")

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except: return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def export_report(tasks):
    """Create a professional mission report in TXT format"""
    filename = f"REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("=== NEON-SHRED MISSION DATA EXPORT ===\n")
        f.write(f"Export Date: {datetime.now()}\n")
        f.write("-" * 40 + "\n")
        if not tasks:
            f.write("No active targets found.\n")
        for i, t in enumerate(tasks):
            f.write(f"[{i+1}] {t['name']} | Priority: {t['priority']} | Op: {t['op']}\n")
    return filename

def get_task_display(task_obj, index):
    name = task_obj["name"]
    prio = task_obj.get("priority", "mid")
    op = task_obj.get("op", "DEFAULT")

    op_tag = f"{GRAY}[{op}]{RESET}"
    if prio == "high":
        return f"{RED}[{index}]{RESET} {op_tag}{BOLD}{name.upper()}{RESET}"
    elif prio == "low":
        return f"{GRAY}[{index}]{RESET} {op_tag}{name}"
    else:
        return f"{CYAN}[{index}]{RESET} {op_tag}{name}"

def print_header():
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{CYAN}{BOLD} >>> SYSTEM READY: NEON-SHRED v1.6 <<<{RESET}")
    print(f"{CYAN}{'='*55}{RESET}")

def get_task_display(task_obj, index):
    """Returns a color-formatted string based on priority"""
    name = task_obj["name"]
    prio = task_obj.get("priority", "mid")
    
    if prio == "high":
        return f"  {RED}[{index}]{RESET} {BOLD}{name.upper()} [!!!]{RESET}"
    elif prio == "low":
        return f"  {GRAY}[{index}]{RESET} {name} (low-prio)"
    else:
        return f"  {CYAN}[{index}]{RESET} {name}"

tasks = load_tasks()
log_event("SESSION_START")

while True:
    clear_screen()
    print_header()
    
    if not tasks:
        print(f"\n   {YELLOW}[ STATUS: NO ACTIVE TARGETS ]{RESET}\n")
    else:
        for i, t in enumerate(tasks):
            print(get_task_display(t, i+1))
    
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}COMMANDS:{RESET} {GREEN}add [text] --high{RESET} | {RED}shred [id]{RESET} | {YELLOW}export{RESET} | exit")
    
    try:
        raw_input = input(f"\n{BOLD}root@shredder:~#{RESET} ").strip()
    except EOFError: break
    if not raw_input: continue

    parts = raw_input.split(" ", 1)
    command = parts[0].lower()

    if command == "add" and len(parts) > 1:
        text = parts[1]
        priority = "high" if "--high" in text else "low" if "--low" in text else "mid"
        op = "GENERAL"
        if "@" in text:
            op_parts = text.split("@")
            text = op_parts[0]
            op = op_parts[1].split(" ")[0].upper()
        
        clean_name = text.replace("--high","").replace("--low","").strip()
        tasks.append({"name": clean_name, "priority": priority, "op": op})
        save_tasks(tasks)
        log_event(f"ADDED: {clean_name} [{priority}]")
        print(f"{GREEN}[+] Data Logged.{RESET}")
        time.sleep(0.4)

    elif command == "export":
        fname = export_report(tasks)
        print(f"{GREEN}[+] REPORT GENERATED: {fname}{RESET}")
        log_event(f"REPORT_EXPORTED: {fname}")
        time.sleep(2)

    elif command == "shred" and len(parts) > 1:
        try:
            idx = int(parts[1]) - 1
            removed = tasks.pop(idx)
            save_tasks(tasks)
            log_event(f"TARGEGT_SHREDDED: {removed['name']}")
            print(f"{RED}SHREDDING DATA...{RESET}")
            time.sleep(0.5)
        except: pass

    elif command == "exit":
        log_event("SESSION_END")
        break