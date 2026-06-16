# git bisect

Uses binary search to find the commit that introduced a bug.

## Basic Workflow

```shell
# Start bisecting
$ git bisect start

# Mark the current commit as bad (has the bug)
$ git bisect bad

# Mark a known good commit (didn't have the bug)
$ git bisect good abc1234
Bisecting: 12 revisions left to test after this (roughly 4 steps)
[def5678] Some commit message

# Git checks out a middle commit — test it, then mark it
$ python -m pytest  # or whatever test you use
$ git bisect good   # if the bug is NOT present here
Bisecting: 6 revisions left to test after this (roughly 3 steps)

$ python -m pytest
$ git bisect bad    # if the bug IS present here
Bisecting: 3 revisions left to test after this (roughly 2 steps)

# Keep going until git finds the exact commit
$ git bisect good
abc1234def5678901234 is the first bad commit
commit abc1234def5678901234
Author: Bob <bob@example.com>
Date:   Wed Jun 11 14:30:00 2025

    Refactor auth middleware

# End the bisect session
$ git bisect reset
Previous HEAD position was abc1234
Switched to branch 'main'
```

## Automated Bisect

```shell
# Run a script automatically at each step
# Script must exit 0 for good, non-0 for bad
$ git bisect start HEAD abc1234
$ git bisect run python -m pytest tests/test_auth.py
running 'python -m pytest tests/test_auth.py'
...
Bisecting: 6 revisions left to test after this
running 'python -m pytest tests/test_auth.py'
...
abc1234 is the first bad commit

# Use any command/script
$ git bisect run ./test-script.sh
$ git bisect run make test
```

## Start with Known Good and Bad

```shell
# Combine start + good + bad in one command
$ git bisect start HEAD v1.0.0
# HEAD is bad, v1.0.0 is good

$ git bisect start HEAD abc1234 -- src/auth/
# Only consider commits that touch src/auth/
```

## Skip a Commit

```shell
# If you can't test the current commit (e.g., doesn't compile)
$ git bisect skip
Bisecting: 5 revisions left to test after this

# Skip a range of commits
$ git bisect skip abc1234..def5678
```

## View Bisect Log

```shell
# See the bisect history
$ git bisect log
git bisect start
# bad: [abc1234] Latest commit
git bisect bad abc1234
# good: [def5678] Known good release
git bisect good def5678
# good: [ghi9012] Midpoint commit
git bisect good ghi9012
# bad: [jkl3456] Another midpoint
git bisect bad jkl3456

# Save the log to replay later
$ git bisect log > bisect-log.txt

# Replay a saved bisect session
$ git bisect replay bisect-log.txt
```

## Visualize Bisect

```shell
# Show remaining suspects
$ git bisect visualize
$ git bisect view
# Opens gitk or log view of remaining commits

# With oneline
$ git bisect visualize --oneline
```

## Terms (Old/New Instead of Good/Bad)

```shell
# Use custom terms (e.g., for finding when a feature was added, not a bug)
$ git bisect start --term-old=before --term-new=after

$ git bisect after HEAD     # current has the feature
$ git bisect before v1.0.0  # v1.0.0 doesn't have it

# Test and mark
$ git bisect before  # feature not here yet
$ git bisect after   # feature is here
```

## Common Workflows

```shell
# Find which commit broke the tests
$ git bisect start
$ git bisect bad HEAD
$ git bisect good v1.5.0
$ git bisect run python -m pytest tests/
# Let it run automatically to completion

# Find which commit introduced a performance regression
$ git bisect start HEAD v1.0.0
# At each step, run your benchmark and mark good/bad

# After finding the bad commit, examine it
$ git show <first-bad-commit>
$ git bisect reset
```
