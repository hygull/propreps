# git add

Adds file contents to the staging area (index) for the next commit.

## Basic Usage

```shell
# Stage a single file
$ git add README.md

# Stage multiple files
$ git add file1.py file2.py file3.py

# Stage all changes in current directory (new, modified, deleted)
$ git add .

# Stage all changes in the entire repository
$ git add -A
$ git add --all
```

## Stage by Pattern

```shell
# Stage all Python files
$ git add "*.py"

# Stage all files in a specific directory
$ git add src/

# Stage all markdown files recursively
$ git add "**/*.md"

# Stage all .js and .ts files
$ git add "*.js" "*.ts"
```

## Partial Staging (Patch Mode)

```shell
# Interactively choose hunks to stage from each file
$ git add -p
$ git add --patch
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,5 +1,6 @@
 def hello():
-    print("Hello")
+    print("Hello, World!")
+    print("Welcome")
     return True
Stage this hunk [y,n,q,a,d,s,e,?]?
# y = stage this hunk
# n = skip this hunk
# s = split into smaller hunks
# q = quit (already staged hunks remain staged)
# a = stage this and all remaining hunks in the file

# Patch mode on a specific file
$ git add -p utils.py
```

## Dry Run

```shell
# See what would be staged without actually staging
$ git add --dry-run .
add 'new-file.txt'
add 'src/utils.py'

$ git add -n .
```

## Force Add (Override .gitignore)

```shell
# Stage a file that's in .gitignore
$ git add --force build/output.js
$ git add -f .env.example

# Check which files are ignored
$ git status --ignored
```

## Update and Intent to Add

```shell
# Stage only modified and deleted files (not new/untracked files)
$ git add -u
$ git add --update

# Mark untracked files as "intent to add" (shows in diff but empty staging)
$ git add -N new-file.txt
$ git add --intent-to-add new-file.txt

# Now git diff will show the file's contents
$ git diff
diff --git a/new-file.txt b/new-file.txt
--- a/new-file.txt
+++ b/new-file.txt
@@ -0,0 +1,3 @@
+line 1
+line 2
+line 3
```

## Verbose Output

```shell
# Show which files are being staged
$ git add -v .
add 'src/main.py'
add 'src/utils.py'
add 'tests/test_main.py'
```

## Unstage (Undo git add)

```shell
# Unstage a specific file (keeps changes in working directory)
$ git restore --staged file.py

# Unstage everything
$ git restore --staged .

# Older syntax (still works)
$ git reset HEAD file.py
```

## Checking What's Staged

```shell
# See staged changes
$ git diff --staged
$ git diff --cached

# See status summary
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   src/app.py
        new file:   src/utils.py

Changes not staged for commit:
        modified:   README.md

Untracked files:
        docs/
```
