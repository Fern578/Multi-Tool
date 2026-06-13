import os
import platform
import hashlib
import uuid
import json
import subprocess
import random
import string
from datetime import datetime

PASSWORD = "123"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter...")

def login():
    clear()
    return input("Password: ") == PASSWORD

# ------------------------
# Utilities
# ------------------------

def calculator():
    try:
        print(eval(input("Equation: ")))
    except Exception as e:
        print(e)
    pause()

def password_generator():
    length = int(input("Length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    print("".join(random.choice(chars) for _ in range(length)))
    pause()

def notes():
    note = input("Note: ")
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("Saved.")
    pause()

# ------------------------
# Developer
# ------------------------

def sha256_tool():
    text = input("Text: ")
    print(hashlib.sha256(text.encode()).hexdigest())
    pause()

def uuid_tool():
    print(uuid.uuid4())
    pause()

def json_validator():
    text = input("JSON: ")
    try:
        print(json.dumps(json.loads(text), indent=4))
    except Exception as e:
        print(e)
    pause()

# ------------------------
# System
# ------------------------

def system_info():
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    pause()

def terminal():
    try:
        if os.name == "nt":
            subprocess.Popen("cmd")
        else:
            subprocess.Popen(["bash"])
    except Exception as e:
        print(e)
    pause()

# ------------------------
# Menus
# ------------------------

def utilities_menu():
    while True:
        clear()
        print("1. Calculator")
        print("2. Password Generator")
        print("3. Notes")
        print("0. Back")
        c = input("> ")

        if c == "1":
            calculator()
        elif c == "2":
            password_generator()
        elif c == "3":
            notes()
        elif c == "0":
            return

def developer_menu():
    while True:
        clear()
        print("1. SHA256")
        print("2. UUID Generator")
        print("3. JSON Validator")
        print("0. Back")
        c = input("> ")

        if c == "1":
            sha256_tool()
        elif c == "2":
            uuid_tool()
        elif c == "3":
            json_validator()
        elif c == "0":
            return

def system_menu():
    while True:
        clear()
        print("1. System Info")
        print("2. Launch Terminal")
        print("0. Back")
        c = input("> ")

        if c == "1":
            system_info()
        elif c == "2":
            terminal()
        elif c == "0":
            return

def main():
    if not login():
        print("Wrong password.")
        return

    while True:
        clear()
        print("=== MULTITOOL ===")
        print("1. Utilities")
        print("2. Developer Tools")
        print("3. System Tools")
        print("0. Exit")

        c = input("> ")

        if c == "1":
            utilities_menu()
        elif c == "2":
            developer_menu()
        elif c == "3":
            system_menu()
        elif c == "0":
            break

if __name__ == "__main__":
    main()