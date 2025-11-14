# Python Project Games

A collection of simple beginner-friendly Python terminal games.

## Games Included

1. **Guess Number** (`guess_number.py`)  
   Choose a range and try to guess the secret number within limited attempts.
2. **Rock Paper Scissors** (`rock_paper_scissors.py`)  
   Play against the computer with emojis and a running score.
3. **Rainbow Quest Adventure** (`choose_your_own_adventure.py`)  
   Kid-friendly text adventure with simple choices, items, and a final guardian.
4. **Quiz Game** (`Quiz game/quiz_game.py`)  
   Multiple-choice shuffled questions with explanations.
5. **Pig Dice Game** (`pig.py`) 🎲  
   Classic dice game - roll to score points, but don't roll a 1!
6. **Password Manager** (`password_manager.py`) 🔒  
   Securely store and retrieve passwords with encryption.

## How to Run (Windows PowerShell)

```powershell
cd "c:\Users\ksvar\OneDrive\Desktop\Python project"
python guess_number.py
python rock_paper_scissors.py
python choose_your_own_adventure.py
python pig.py
python ".\Quiz game\quiz_game.py"
```

### Password Manager Setup & Run

⚠️ **First-time setup required:**

```powershell
# Install cryptography package
pip install cryptography

# Generate encryption key (ONLY run this ONCE!)
python -c "from cryptography.fernet import Fernet; key = Fernet.generate_key(); open('key.key', 'wb').write(key); print('Key generated')"

# Create empty password storage file
New-Item -ItemType File -Path "passwords.txt" -Force

# Run the password manager
python password_manager.py
```

**Commands:**
- `add` - Store a new account and password
- `view` - Display all saved passwords
- `q` - Quit

**⚠️ SECURITY WARNINGS:**
- **NEVER share or commit `key.key`** - Anyone with this file can decrypt your passwords
- **NEVER commit `passwords.txt`** - Contains your encrypted passwords
- **Backup `key.key` safely** - If lost, passwords cannot be recovered
- The master password prompt is for demonstration only (not validated)
- This is a learning project, not production-ready for sensitive passwords

Run one command at a time. Each game is interactive in the terminal.

## Requirements
- Python 3.8+ recommended
- No external dependencies for games
- **Password Manager requires:** `pip install cryptography`

## Folder Structure
```
Python project/
  choose_your_own_adventure.py
  guess_number.py
  rock_paper_scissors.py
  pig.py
  password_manager.py
  Quiz game/
    quiz_game.py
  README.md
  .gitignore
  key.key (generated locally, not in repo)
  passwords.txt (generated locally, not in repo)
```

## Contributing
Feel free to fork and add:
- New quiz questions
- Difficulty levels
- Score persistence
- Timers or achievements

## License
MIT (adjust if you prefer a different license).
