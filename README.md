# json-climb 🌲

## What is this?

A **GitHub contribution graph generator** that creates realistic backdated commits with interactive date ranges and actual file modifications. Perfect for quickly populating your GitHub contribution calendar with a history of work.

## Features

✨ **Interactive Date Selection**
- Choose custom start and end dates
- Specify how many days should have commits
- Real-time preview of contribution intensity (light → dark green squares)

🎯 **Realistic Commits**
- Actual file creation and modification in `/changes`, `/config`, `/src`, `/docs`, `/tests`, `/data`
- Realistic commit messages: "fix: bug in API handling", "feat: add validation logic", etc.
- Random content: JSON configs, Python handlers, JavaScript tests, documentation

📊 **Smart Distribution**
- Random 1-6 commits per active day
- Realistic time variations (8 AM - 6 PM)
- Commits randomly distributed across selected date range

🚀 **Easy to Use**
```bash
python git.py
```

Then:
1. Enter start date (YYYY-MM-DD)
2. Enter end date (YYYY-MM-DD)
3. Specify number of days to have commits
4. Review the preview
5. Confirm with "yes"
6. Commits are created locally
7. Push to GitHub: `git push origin main`

## Example

```
📅 Enter start date (YYYY-MM-DD): 2025-08-01
📅 Enter end date (YYYY-MM-DD): 2026-05-25
🎯 How many days should have commits? (1-298, recommended 80-150): 120
```

Creates ~400-500 commits across 120 randomly selected days, with varying commit intensities creating a realistic GitHub contribution graph.

## Output Structure

- **changes/** - Logs and history of changes
- **config/** - Configuration files (JSON)
- **src/** - Source code (JavaScript, Python, JSON)
- **docs/** - Documentation (Markdown)
- **tests/** - Test files (JavaScript)
- **data/** - Data files (JSON, metrics)

## Important

⚠️ All commits are created **locally only**. You must manually push to GitHub:

```bash
git push origin main
```

After pushing, your contribution graph updates in **5-10 minutes**.

## How It Works

1. Randomly selects specified number of days in your date range
2. Generates 1-6 commits per selected day at random times
3. Creates/modifies files in project directories
4. Commits with backdated timestamps using `git commit --date`
5. Stages and commits using Python's `subprocess` module (reliable execution)

## Files & Folders

- `git.py` - Main contribution generator script
- `changes/` - Generated logs and history
- `config/`, `src/`, `docs/`, `tests/`, `data/` - Generated project files

---

**Use responsibly!** This is meant for personal projects or learning, not for misrepresenting work history on professional profiles.