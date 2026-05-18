# SimpleCLI-Notetaker

A lightweight command‑line tool for creating, listing, searching, and deleting personal notes.

## Features
- Add a note with a title and body
- List all notes (showing timestamps)
- Search notes by keyword
- Delete notes by ID
- All data stored locally in `notes.json`

## Installation
```bash
# Clone the repo
git clone https://github.com/yourusername/SimpleCLI-Notetaker.git
cd SimpleCLI-Notetaker

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies (none required beyond the stdlib)
```

## Usage
```bash
# Add a note
python notetaker.py add "Meeting notes" "Discuss project timeline and milestones."

# List all notes
python notetaker.py list

# Search notes
python notetaker.py search "project"

# Delete a note by ID
python notetaker.py delete 2
```

## License
MIT – see the `LICENSE` file for details.
