import subprocess
import random
import os
from datetime import datetime, timedelta
from collections import Counter

def parse_date(prompt):
    """Parse date input from user"""
    while True:
        try:
            date_str = input(prompt).strip()
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD (e.g., 2025-08-01)")

def get_file_operation(day_num, commit_num):
    """Generate random file operation"""
    
    # Create new files
    new_files = [
        ("config/settings.json", '{"version": "' + str(day_num) + '.' + str(commit_num) + '", "updated": true, "timestamp": ' + str(random.randint(1600000000, 1700000000)) + '}'),
        ("src/utils.js", '// Utility function ' + str(commit_num) + '\nfunction processData() {\n  return { status: "success", code: ' + str(random.randint(200, 500)) + ' };\n}\n'),
        ("src/handlers.py", '# Handler ' + str(commit_num) + '\ndef handle_request():\n    return {"message": "processed", "id": ' + str(random.randint(1000, 9999)) + '}\n'),
        ("src/models.json", '{"model": "v' + str(day_num) + '.' + str(commit_num) + '", "type": "' + random.choice(['user', 'product', 'order', 'transaction']) + '", "active": true}'),
        ("docs/CHANGELOG.md", '## Version ' + str(day_num) + '.' + str(commit_num) + '\n- Bug fix #' + str(random.randint(100, 999)) + '\n- Feature improvement\n- Performance optimization\n'),
        ("tests/test_unit.js", 'describe("Test ' + str(commit_num) + '", () => {\n  it("should work", () => {\n    expect(true).toBe(true);\n  });\n});\n'),
        ("data/metrics.json", '{"timestamp": ' + str(random.randint(1600000000, 1700000000)) + ', "value": ' + str(random.randint(10, 1000)) + ', "status": "' + random.choice(['active', 'pending', 'completed']) + '"}'),
    ]
    
    # Modify existing files
    append_files = [
        ("changes/log.txt", '[' + datetime.now().isoformat() + '] Processing batch ' + str(commit_num) + ': ' + str(random.randint(100, 10000)) + ' records\n'),
        ("changes/history.md", '- Processed data set ' + str(day_num) + '-' + str(commit_num) + '\n'),
    ]
    
    # Decide operation type
    op_type = random.choice(["new", "new", "new", "append", "append"])
    
    if op_type == "new":
        file_path, content = random.choice(new_files)
        return ("create", file_path, content)
    else:
        file_path, content = random.choice(append_files)
        return ("append", file_path, content)

def get_commit_message():
    """Generate realistic commit message"""
    prefixes = ["fix", "feat", "chore", "refactor", "perf", "docs", "style", "test"]
    actions = [
        "bug in data processing",
        "API endpoint handling",
        "database connection",
        "cache invalidation",
        "user authentication",
        "error handling",
        "logging system",
        "validation logic",
        "performance bottleneck",
        "memory leak",
        "response formatting",
        "input sanitization",
    ]
    
    prefix = random.choice(prefixes)
    action = random.choice(actions)
    
    if prefix == "fix":
        return f"fix: {action}"
    elif prefix == "feat":
        return f"feat: add support for {action}"
    elif prefix == "chore":
        return f"chore: update {action}"
    elif prefix == "refactor":
        return f"refactor: improve {action}"
    elif prefix == "perf":
        return f"perf: optimize {action}"
    elif prefix == "docs":
        return f"docs: update documentation for {action}"
    elif prefix == "test":
        return f"test: add tests for {action}"
    else:
        return f"style: clean up {action}"

# Main script
print("="*70)
print("GIT CONTRIBUTION GENERATOR - Interactive Mode")
print("="*70)
print()

start_date = parse_date("📅 Enter start date (YYYY-MM-DD): ")
end_date = parse_date("📅 Enter end date (YYYY-MM-DD): ")

if start_date >= end_date:
    print("❌ Start date must be before end date!")
    exit(1)

total_days = (end_date - start_date).days + 1
print(f"\n✓ Date range: {start_date.date()} to {end_date.date()} ({total_days} days)")

try:
    NUM_DAYS = int(input(f"\n🎯 How many days should have commits? (1-{total_days}, recommended 80-150): "))
    if NUM_DAYS < 1 or NUM_DAYS > total_days:
        print(f"❌ Enter number between 1 and {total_days}")
        exit(1)
except ValueError:
    print("❌ Enter a valid number")
    exit(1)

# Randomly select days
all_days = [start_date + timedelta(days=i) for i in range(total_days)]
random.shuffle(all_days)
selected_days = sorted(all_days[:NUM_DAYS])

# Create commits with random intensity
commit_dates = []
for day in selected_days:
    num_commits = random.randint(1, 6)
    for _ in range(num_commits):
        time = day.replace(hour=random.randint(8, 18), minute=random.randint(0, 59))
        commit_dates.append(time)

commit_dates.sort()

# Show preview
print("\n" + "="*70)
print("COMMIT PREVIEW")
print("="*70)
date_count = Counter([d.strftime("%Y-%m-%d") for d in commit_dates])
light = sum(1 for c in date_count.values() if c == 1)
medium = sum(1 for c in date_count.values() if 2 <= c <= 3)
dark = sum(1 for c in date_count.values() if c >= 4)

print(f"\n🟩 Light green   (1 commit):     {light} days")
print(f"🟩 Medium green  (2-3 commits):  {medium} days")
print(f"🟩 Dark green    (4-6 commits):  {dark} days")
print(f"\n📊 Statistics:")
print(f"   Total commits: {len(commit_dates)}")
print(f"   Total days: {len(date_count)}")
print(f"   Average per day: {len(commit_dates) / len(date_count):.1f}")

print("\n📆 Sample dates:")
for date_str in sorted(date_count.keys())[:5]:
    count = date_count[date_str]
    print(f"   {date_str}: {count} commit(s)")
print("   ...")
print()

confirm = input("Proceed? (yes/no): ").strip().lower()
if confirm != 'yes':
    print("❌ Cancelled.")
    exit(0)

print("\n" + "="*70)
print("CREATING COMMITS")
print("="*70 + "\n")

# Create necessary directories
os.makedirs("changes", exist_ok=True)
os.makedirs("config", exist_ok=True)
os.makedirs("src", exist_ok=True)
os.makedirs("docs", exist_ok=True)
os.makedirs("tests", exist_ok=True)
os.makedirs("data", exist_ok=True)

successful = 0
failed = 0

for i, commit_date in enumerate(commit_dates, 1):
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Get file operation
        op_type, file_path, content = get_file_operation(i, i % 100)
        
        # Perform file operation
        if op_type == "create":
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
        elif op_type == "append":
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'a') as f:
                f.write(content)
        
        # Stage all changes
        subprocess.run(['git', 'add', '.'], capture_output=True, check=True)
        
        # Get commit message
        msg = get_commit_message()
        
        # Create commit with date
        result = subprocess.run(
            ['git', 'commit', '--date', date_str, '-m', msg],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            successful += 1
            print(f"✓ [{i:3d}] {msg:45s} | {commit_date.strftime('%Y-%m-%d %H:%M')}")
        else:
            failed += 1
            if "nothing to commit" not in result.stderr.lower():
                print(f"✗ [{i:3d}] Failed - {result.stderr[:50]}")
        
        if i % 50 == 0:
            print(f"\n   ... processing {i}/{len(commit_dates)} ...\n")
    
    except Exception as e:
        failed += 1
        print(f"✗ [{i:3d}] Error: {str(e)[:50]}")

print("\n" + "="*70)
print("COMPLETION SUMMARY")
print("="*70)
print(f"\n✅ Script finished!")
print(f"   Total commits created: {successful}")
print(f"   Failed/Skipped: {failed}")
print(f"   Across {len(date_count)} days")
print(f"   Date range: {min(d.date() for d in commit_dates)} to {max(d.date() for d in commit_dates)}")

print("\n📁 Files created in:")
print("   - changes/    (logs, history)")
print("   - config/     (settings)")
print("   - src/        (code files)")
print("   - docs/       (documentation)")
print("   - tests/      (test files)")
print("   - data/       (data files)")

print("\n📝 NEXT STEPS:")
print("   1. Review changes: git log --oneline | head -30")
print("   2. Check file structure: ls -la")
print("   3. Push to GitHub: git push origin main")

print("\n⏱️  After pushing, your GitHub contribution graph updates in 5-10 minutes.")
print("="*70 + "\n")
