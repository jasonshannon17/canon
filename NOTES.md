# Canon Notes

## Current working features

- Streamlit app launches.
- Practice Mode works.
- Questions load from JSON.
- Question order is randomized.
- Enter submits answers.
- Aliases are accepted.
- Feedback appears after each answer in Practice Mode.
- End review screen works.
- Review can show all questions or missed questions only.
- Sidebar shows score, accuracy, progress, difficulty, category, and available question count.
- Missed Questions Practice lets me retry only the questions I missed from a session.
- Saved session history works.
- Recent Sessions shows completed sessions and their mode.
- Most Missed sidebar section works.
- Weakest Categories sidebar section works.
- Question Bank health checks work.
- Bank by Category sidebar section works.
- Start New Session / Shuffle resets and reshuffles the current filters.
- Current session summary appears above each clue.

## Question bank

- Question bank currently has 240 questions.
- Questions are stored in `data/questions.json`.
- Session history is stored in `data/session_history.json`.
- Pack 5 added: Language / Vocabulary / Wordplay.
- Language / Vocabulary currently has 40 questions.

## Keyboard flow

- Keyboard Flow Phase 2 complete.
- Enter submits answers.
- After feedback appears in Practice Mode, pressing Enter advances to the next question.
- Autofocus works in Practice Mode.
- Autofocus works in Anytime Test Mode using a question-specific focus key.
- Current practice flow is mostly mouse-free.

## Modes and filters

### Practice Mode

- Standard mode.
- Shows immediate feedback after each answer.
- Supports category filters.
- Supports difficulty filters.
- Supports session length selection.

### Weak Spots Mode

- Weak Spots category filter added.
- Weak Spots currently uses a manual category list in `app.py`:

```text
Classical Music
World History
Science
Literature
Language / Vocabulary
Theatre
Art
Math
Opera
Shakespeare
Bible
Philosophy
```

- Future improvement: make Weak Spots dynamic based on real saved session history.

### Active Misses Mode

- Active Misses category filter added.
- Active Misses v1 includes questions that have been missed in saved sessions.
- Current implementation is intentionally simple.
- Future improvement: distinguish unresolved misses from old misses that have since been mastered.

### Daily 20 Mode

- Daily 20 Mode added.
- Daily 20 v1 builds a 20-question session from:
  - up to 10 Active Misses
  - up to 10 Weak Spots
- Daily 20 is intended to become the default daily training habit.

### Anytime Test Mode

- Anytime Test Mode added.
- Anytime Test currently pulls 50 questions using a weighted difficulty mix:
  - 5 difficulty 1
  - 25 difficulty 2
  - 20 difficulty 3+
- Immediate feedback is suppressed in Anytime Test Mode.
- Score and accuracy are hidden during Anytime Test Mode.
- Autofocus works in Anytime Test Mode.
- Anytime Test currently does not have a timer yet.
- Future improvement: add 15-second timing per clue.

## Real Jeopardy / Anytime Test observations

- Enter submits answers.
- Older entrance test displayed the category above the clue.
- Anytime Mode should imitate the real test as closely as possible.
- Practice Mode can differ from the real test when it helps learning.
- Anytime Test Mode should be treated as the “realistic simulation” mode.
- Practice Mode, Weak Spots, Active Misses, and Daily 20 are training modes.

## Mode philosophy

- Learning Mode can include easy foundational canon.
- Practice Mode can be mixed and give immediate feedback.
- Challenge Mode should reduce easy questions and expose weak areas.
- Anytime Test Mode should simulate the real test: 50 clues, 15 seconds, no feedback until the end.
- Anytime Test Mode should use a weighted difficulty mix, not pure random selection.
- Easy questions are useful for learning but should not inflate readiness estimates.
- Active Misses should eventually represent unresolved misses, not lifetime punishment for old misses.

## Current caveat about history data

- Current saved Canon history includes testing data.
- Current miss statistics should not be treated as a fully reliable diagnostic profile yet.
- Before serious long-term tracking, archive/reset the current session history.
- `archive_history.py` exists to archive current history and reset `session_history.json`.

## Helper scripts

Helper scripts live in the `tools` folder.

- `add_alias.py` safely adds an alias to a question by ID.
- `analyze_history.py` prints category accuracy from saved sessions.
- `validate_questions.py` checks the question bank for duplicate IDs, missing fields, bad aliases, and invalid difficulty values.
- `search_questions.py` searches the question bank.
- `category_report.py` shows question counts by category.
- `active_misses_report.py` reports missed questions and misses by category.
- `archive_history.py` archives current session history and resets tracking.

## Technical notes

- Sidebar helper functions currently write directly to `st.sidebar`.
- If we want collapsible sidebar sections later, those helper functions should be refactored to accept a display container.
- Attempted sidebar expander cleanup on 2026-10-09, but reverted because helper output did not appear correctly inside dropdowns.
- The question-specific autofocus key fixed autofocus in Anytime Test Mode.

## Deployment / show-and-tell target

- Goal: deploy by Wednesday for Friday show-and-tell.
- Preferred deployment path:
  - GitHub repo
  - Streamlit Community Cloud
  - Demo URL opened from work laptop
- Before deployment:
  - Make sure app runs clean after restart.
  - Create `requirements.txt`.
  - Add `.gitignore`.
  - Do not upload `venv`.
  - Archive/reset messy test history if needed.
  - Test deployed URL in another browser/device.

## Future roadmap

### Near-term

- Finish Anytime Test Mode polish.
- Add end-screen wording specific to Anytime Test Mode.
- Create `requirements.txt`.
- Add `.gitignore`.
- Prepare GitHub repo.
- Deploy to Streamlit Community Cloud.

### Medium-term

- Add more content packs:
  - Presidents & Government
  - Poetry
  - Food & Drink
  - Business / Economics
  - Medicine & Anatomy
  - Geography physical features
  - World Religion
  - Art & Architecture
- Improve Active Misses using recent performance, streaks, and last result.
- Add a true Dynamic Weak Spots mode.
- Add 15-second timer to Anytime Test Mode.

### Long-term / dream-state ideas

- Move from question-first data to concept-first data.
- Track concepts, facts, clue angles, aliases, and related ideas.
- Add spaced repetition.
- Migrate from JSON to SQLite when the question bank becomes too large.
- Add optional “Learn More” links to relevant Wikipedia pages.
- Show Learn More links in missed-answer review and possibly full review.
- Eventually support multiple clues connected to the same concept page.