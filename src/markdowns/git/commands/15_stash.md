# git stash

Temporarily shelves (stashes) changes in a dirty working directory.

## Basic Usage

```shell
# Stash current changes
$ git stash
Saved working directory and index state WIP on main: abc1234 Last commit message

# Stash with a descriptive message
$ git stash push -m "WIP: auth refactor"
Saved working directory and index state On main: WIP: auth refactor

# Short form (older syntax, still works)
$ git stash save "WIP: auth refactor"
```

## Apply Stashed Changes

```shell
# Apply the most recent stash (keeps it in the stash list)
$ git stash apply
On branch main
Changes not staged for commit:
        modified:   src/app.py

# Apply and remove from stash list
$ git stash pop
On branch main
Changes not staged for commit:
        modified:   src/app.py
Dropped refs/stash@{0} (abc1234567890)

# Apply a specific stash
$ git stash apply stash@{2}
$ git stash pop stash@{1}
```

## List Stashes

```shell
$ git stash list
stash@{0}: On main: WIP: auth refactor
stash@{1}: WIP on feature/auth: def5678 Add middleware
stash@{2}: On main: Quick fix attempt
```

## Show Stash Contents

```shell
# Show summary of latest stash
$ git stash show
 src/app.py   | 5 +++--
 src/utils.py | 3 +++
 2 files changed, 6 insertions(+), 2 deletions(-)

# Show full diff
$ git stash show -p
$ git stash show --patch
diff --git a/src/app.py b/src/app.py
--- a/src/app.py
+++ b/src/app.py
@@ -1,5 +1,6 @@
-    print("Hello")
+    print("Hello, World!")

# Show a specific stash
$ git stash show -p stash@{2}
```

## Stash Specific Files

```shell
# Stash only specific files
$ git stash push -m "stash config only" src/config.py src/settings.py

# Stash with pathspec
$ git stash push -- src/auth/
```

## Stash Options

```shell
# Stash including untracked files
$ git stash -u
$ git stash --include-untracked

# Stash everything (including ignored files)
$ git stash -a
$ git stash --all

# Stash only unstaged changes (keep staged changes staged)
$ git stash --keep-index
$ git stash -k
```

## Partial Stash (Patch Mode)

```shell
# Interactively select hunks to stash
$ git stash -p
$ git stash --patch
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,5 +1,6 @@
 def hello():
-    print("Hello")
+    print("Hello, World!")
Stash this hunk [y,n,q,a,d,s,e,?]?
```

## Drop and Clear Stashes

```shell
# Drop a specific stash
$ git stash drop stash@{0}
Dropped stash@{0} (abc1234567890)

# Drop the latest stash
$ git stash drop

# Clear ALL stashes (DANGEROUS — cannot be undone)
$ git stash clear
```

## Create a Branch from Stash

```shell
# Create a new branch and apply the stash
$ git stash branch feature/from-stash
Switched to a new branch 'feature/from-stash'
On branch feature/from-stash
Changes not staged for commit:
        modified:   src/app.py
Dropped refs/stash@{0} (abc1234567890)

# Useful when stash apply has conflicts on current branch
$ git stash branch feature/from-stash stash@{1}
```

## Common Workflow

```shell
# Scenario: need to switch branches but have uncommitted work
$ git status
Changes not staged for commit:
        modified:   src/app.py

$ git stash push -m "WIP: fixing login bug"
Saved working directory and index state On feature/auth: WIP: fixing login bug

$ git checkout main
# ... do work on main ...

$ git checkout feature/auth
$ git stash pop
# Back to where you were!

# Scenario: pull latest changes with dirty working directory
$ git stash
$ git pull --rebase
$ git stash pop
```
