# git revert

Creates a new commit that undoes the changes from a previous commit. Safe for shared history (unlike reset).

## Basic Usage

```shell
# Revert the most recent commit
$ git revert HEAD
[main abc1234] Revert "Add broken feature"
 1 file changed, 5 deletions(-)

# Revert a specific commit
$ git revert def5678
[main ghi9012] Revert "Introduce bug in auth"
 1 file changed, 3 insertions(+), 3 deletions(-)
```

## Revert Multiple Commits

```shell
# Revert multiple commits (creates one revert commit per original)
$ git revert abc1234 def5678 ghi9012

# Revert a range of commits
$ git revert abc1234..ghi9012
# Reverts def5678 and ghi9012 (newest first)

# Revert a range including the start
$ git revert abc1234^..ghi9012
```

## Revert Without Committing

```shell
# Apply the revert changes but don't auto-commit
$ git revert --no-commit abc1234
$ git revert -n abc1234

# Useful to batch multiple reverts into one commit
$ git revert -n abc1234
$ git revert -n def5678
$ git commit -m "Revert auth changes (abc1234 and def5678)"
```

## Handling Conflicts

```shell
$ git revert abc1234
CONFLICT (content): Merge conflict in src/app.py
error: could not revert abc1234... Add feature

# Fix conflicts, then:
$ git add src/app.py
$ git revert --continue

# Or skip this revert
$ git revert --skip

# Or abort entirely
$ git revert --abort
```

## Revert a Merge Commit

```shell
# Merge commits have multiple parents — specify which to revert to
# -m 1: revert to the first parent (undo the merge, keep the base branch)
$ git revert -m 1 abc1234
[main def5678] Revert "Merge branch 'feature/auth'"

# -m 2: revert to the second parent (rare — undo the base branch changes)
$ git revert -m 2 abc1234
```

## Edit the Revert Message

```shell
# Custom revert message
$ git revert abc1234
# Editor opens with "Revert "original message"" — edit as desired

# No editor, use default message
$ git revert --no-edit abc1234
```

## Revert vs Reset

```shell
# git revert: creates a NEW commit that undoes changes (safe for shared branches)
$ git log --oneline
abc1234 Add broken feature
def5678 Previous good commit

$ git revert abc1234
$ git log --oneline
ghi9012 Revert "Add broken feature"    # ← NEW commit
abc1234 Add broken feature
def5678 Previous good commit

# git reset: REMOVES commits from history (only safe for local/unpushed work)
$ git reset --hard HEAD~1
$ git log --oneline
def5678 Previous good commit
# abc1234 is gone from history
```

## Common Workflows

```shell
# Revert a bad deployment
$ git revert HEAD
$ git push origin main
# CI/CD picks up the revert and redeploys

# Revert a feature that caused issues
$ git log --oneline --merges -5
abc1234 Merge branch 'feature/auth'
def5678 Merge branch 'feature/dashboard'

$ git revert -m 1 abc1234
$ git push origin main

# Revert the revert (re-apply the feature later)
$ git revert ghi9012  # ghi9012 is the revert commit
# This effectively re-applies the original changes
```
