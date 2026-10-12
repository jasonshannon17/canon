# Canon

Canon is a personal Jeopardy training app built with Streamlit.

## Current features

- Practice Mode
- Randomized sessions
- Session length selection
- Difficulty filter
- Category filter
- Keyboard-first flow
- Autofocus answer box
- Enter submits answers
- Enter advances after feedback
- Saved session history
- Recent sessions
- Most missed questions
- Weakest categories
- Training dashboard
- Missed Questions Practice
- Question bank health checks

## Running Canon

From the main project folder:

```powershell
cd C:\Users\jason\Documents\Projects\canon
venv\Scripts\activate
streamlit run app.py
```

If Streamlit is not recognized, use:

```powershell
venv\Scripts\python.exe -m streamlit run app.py
```

## Helper scripts

Helper scripts live in the `tools` folder.

To run them:

```powershell
cd C:\Users\jason\Documents\Projects\canon\tools
```

### Validate the question bank

```powershell
python validate_questions.py
```

### View category balance

```powershell
python category_report.py
```

### Analyze saved history

```powershell
python analyze_history.py
```

### Search the question bank

Edit `SEARCH_TERM` in `search_questions.py`, then run:

```powershell
python search_questions.py
```

### Add an alias safely

Edit these lines in `add_alias.py`:

```python
QUESTION_ID = 70
NEW_ALIAS = "Strauss II"
```

Then run:

```powershell
python add_alias.py
```

## Data files

Main question bank:

```text
data/questions.json
```

Saved session history:

```text
data/session_history.json
```

## Project philosophy

Canon has two goals:

1. Build foundational Jeopardy canon knowledge.
2. Train realistic test performance over time.

Easy questions are useful for learning, but realistic test modes should eventually use weighted difficulty so scores are not inflated by too many foundational clues.

## Future priorities

- Keyboard-first flow polish
- Weak Spot Mode
- Anytime Test Mode
- Realistic 50-question / 15-second test simulation
- Larger question bank
- Concept-based question structure
- Spaced repetition
- SQLite database migration