#!/usr/bin/env python3
"""SimpleCLI-Notetaker
A tiny command‑line note‑taking app.
Stores notes in notes.json (list of dicts with id, title, body, timestamp).
"""
import argparse
import json
import os
import sys
from datetime import datetime

DATA_FILE = "notes.json"

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def get_next_id(notes):
    return max((note["id"] for note in notes), default=0) + 1

def add_note(args):
    notes = load_notes()
    note = {
        "id": get_next_id(notes),
        "title": args.title,
        "body": args.body,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    notes.append(note)
    save_notes(notes)
    print(f"Added note #{note['id']}: {note['title']}")

def list_notes(_):
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        ts = note["timestamp"][:19].replace("T", " ")
        print(f"[{note['id']}] {ts} - {note['title']}")

def search_notes(args):
    notes = load_notes()
    keyword = args.keyword.lower()
    matches = [n for n in notes if keyword in n["title"].lower() or keyword in n["body"].lower()]
    if not matches:
        print("No matching notes.")
        return
    for note in matches:
        ts = note["timestamp"][:19].replace("T", " ")
        print(f"[{note['id']}] {ts} - {note['title']}")
        print(f"    {note['body']}")

def delete_note(args):
    notes = load_notes()
    note_id = args.id
    new_notes = [n for n in notes if n["id"] != note_id]
    if len(new_notes) == len(notes):
        print(f"Note #{note_id} not found.")
        return
    save_notes(new_notes)
    print(f"Deleted note #{note_id}.")

def main():
    parser = argparse.ArgumentParser(prog="notetaker", description="Simple CLI note‑taking utility.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = subparsers.add_parser("add", help="Add a new note")
    p_add.add_argument("title", help="Title of the note")
    p_add.add_argument("body", help="Body/content of the note")
    p_add.set_defaults(func=add_note)

    # list
    p_list = subparsers.add_parser("list", help="List all notes")
    p_list.set_defaults(func=list_notes)

    # search
    p_search = subparsers.add_parser("search", help="Search notes by keyword")
    p_search.add_argument("keyword", help="Keyword to search in title/body")
    p_search.set_defaults(func=search_notes)

    # delete
    p_del = subparsers.add_parser("delete", help="Delete a note by its ID")
    p_del.add_argument("id", type=int, help="ID of the note to delete")
    p_del.set_defaults(func=delete_note)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
