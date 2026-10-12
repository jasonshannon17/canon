import json
import shutil
from datetime import datetime
from pathlib import Path


history_path = Path("../data/session_history.json")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
archive_path = Path(f"../data/session_history_archive_{timestamp}.json")


if not history_path.exists():
    print("No session_history.json file found.")
    raise SystemExit


with open(history_path, "r", encoding="utf-8") as file:
    history = json.load(file)


print()
print("Archive Session History")
print("-----------------------")
print(f"Current sessions found: {len(history)}")
print(f"Archive will be created at: {archive_path}")
print()

confirm = input("Type ARCHIVE to archive current history and reset session_history.json: ")

if confirm != "ARCHIVE":
    print("Archive cancelled. No files were changed.")
    raise SystemExit


shutil.copy(history_path, archive_path)

with open(history_path, "w", encoding="utf-8") as file:
    json.dump([], file, indent=4)


print()
print("Archive complete.")
print(f"Saved old history to: {archive_path}")
print("Reset data/session_history.json to an empty list.")