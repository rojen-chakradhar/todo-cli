import json
import os
import time

FILE_NAME = "tasks.json"
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear') #clear screen

def load_tasks():
  try:
    if os.path.exists(FILE_NAME):
      with open(FILE_NAME, "r") as f:
        return json.load(f)
  except:
    return []
  return []

def save_tasks(tasks):
  with open(FILE_NAME, "w") as f:
    json.dump(tasks, f)

def print_header():
  print(f"{CYAN}{'='*45}{RESET}")
  print(f"{CYAN}{BOLD} >>> SYSTEM READY: NEON-SHRED V1.1 <<< {RESET}")
  print(f"{CYAN}{'='*45}{RESET}")

tasks = load_tasks()

while True:
  clear_screen()
  print_header()

  if not tasks:
    print(f"\n {YELLOW}[ STATUS: NO TASKS FOUND ]{RESET}\n")
  else:
    for i, task in enumerate(tasks):
      print(f" {CYAN}[{i+1}]{RESET} {tasks}")
  print(f"\n{CYAN}{'='*45}{RESET}")
  print(f"{BOLD}COMMANS:{RESET} {GREEN}add{RESET} [text] | {RED}shred{RESET} [num] | {YELLOW}exit{RESET}")

  raw_input = input(f"\n{BOLD}root@shredder:~#{RESET} ").strip()

  if not raw_input:
    continue
  
  parts = raw_input.split(" ", 1)
  command = parts[0].lower()

  if command == "add":
    if len(parts) > 1:
      tasks.append(parts[1])
      save_tasks(tasks)
      print(f"{GREEN}Task Logged.{RESET}")
      time.sleep(0.5)
    else:
      print(f"{RED}Error: Provide a task name (e.g. add Hack the planet){RESET}")
      time.sleep(1.5)

  elif command == "shred":
    if len(parts) > 1:
      try:
        idx = int(parts[1]) - 1
        if 0 <= idx < len(tasks):
          removed = tasks.pop(idx)
          save_tasks(tasks)
          print(f"\n{RED}SHREDDING: {removed}{RESET}")
          for _ in range(5):
            print(f"{RED}# {RESET}", end="", flush=True)
            time.sleep(0.2)
          print("f{GREEN}PURGE COMPLETE.{RESET}")
          time.sleep(1)
      except ValueError:
          print("f{RED}Error: Use theh task number (e.g. shred 1){RESET}")
          time.sleep(1)
    else:
      print(f"{RED}Error: Dpecify task number.{RESET}")
      time.sleep(2)


  elif command == "exit":
    print(f"{CYAN}Shutting down...{RESET}")
    break