import json
import os
import time
from datetime import datetime
import sys

# --- CONFIG & COLORS ---
FILE_NAME = "tasks.json"
LOG_FILE = "system.log"

# Hacker Palette
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except:
        pass

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except: return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def print_header():
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{CYAN}{BOLD} >>> SYSTEM READY: NEON-SHRED v1.5 [PRIORITY ADAPTIVE] <<<{RESET}")
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

# --- MAIN PROGRAM ---
tasks = load_tasks()
log_event("SYSTEM STARTUP")

while True:
    clear_screen()
    print_header()
    
    if not tasks:
        print(f"\n   {YELLOW}[ STATUS: NO ACTIVE TARGETS ]{RESET}\n")
    else:
        for i, t in enumerate(tasks):
            print(get_task_display(t, i+1))
    
    print(f"\n{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}CMDS:{RESET} {GREEN}add [text] --high/low{RESET} | {RED}shred [id]{RESET} | {YELLOW}search [term]{RESET} | exit")
    
    try:
        raw_input = input(f"\n{BOLD}root@shredder:~#{RESET} ").strip()
    except EOFError: break
    if not raw_input: continue

    parts = raw_input.split(" ", 1)
    command = parts[0].lower()

    # --- ADD COMMAND ---
    if command == "add" and len(parts) > 1:
        full_text = parts[1]
        priority = "mid"
        
        if "--high" in full_text:
            priority = "high"
            full_text = full_text.replace("--high", "").strip()
        elif "--low" in full_text:
            priority = "low"
            full_text = full_text.replace("--low", "").strip()
            
        tasks.append({"name": full_text, "priority": priority})
        save_tasks(tasks)
        log_event(f"ADDED: {full_text} [{priority}]")
        print(f"{GREEN}[+] Data Logged.{RESET}")
        time.sleep(0.4)

    # --- SEARCH COMMAND ---
    elif command == "search" and len(parts) > 1:
        query = parts[1].lower()
        print(f"\n{YELLOW}{BOLD}--- SEARCH RESULTS FOR: '{query}' ---{RESET}")
        found = False
        for i, t in enumerate(tasks):
            if query in t["name"].lower():
                print(get_task_display(t, i+1))
                found = True
        if not found:
            print(f"{RED}No matches found in database.{RESET}")
        input(f"\n{BOLD}Press Enter to return...{RESET}")

    # --- SHRED COMMAND ---
    elif command == "shred" and len(parts) > 1:
        try:
            idx = int(parts[1]) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                log_event(f"PURGED: {removed['name']}")
                print(f"{RED}SHREDDING...{RESET}")
                time.sleep(0.5)
            else: print(f"{RED}[!] Invalid ID.{RESET}"); time.sleep(1)
        except: print(f"{RED}[!] Use numbers.{RESET}"); time.sleep(1)

    elif command == "logs":
        clear_screen()
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                print(f"{YELLOW}{f.read()}{RESET}")
        input(f"\n{BOLD}Press Enter...{RESET}")

    elif command == "exit":
        break