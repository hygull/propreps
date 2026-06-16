# git log

Shows the commit history.

## Basic Usage

```shell
$ git log
commit abc1234567890abcdef (HEAD -> main, origin/main)
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

    Add user authentication

commit def5678901234abcdef
Author: User <user@example.com>
Date:   Sun Jun 15 18:30:00 2025 +0530

    Update README with setup instructions
```

## One-Line Format

```shell
$ git log --oneline
abc1234 Add user authentication
def5678 Update README with setup instructions
ghi9012 Fix login validation bug
jkl3456 Add unit tests for auth module
mno7890 Initial commit

# Limit number of commits
$ git log --oneline -5
$ git log --oneline -n 5
```

## Pretty Formats

```shell
# Short format
$ git log --pretty=short
commit abc1234
Author: User <user@example.com>

    Add user authentication

# Full format (includes committer)
$ git log --pretty=full

# Custom format
$ git log --pretty=format:"%h %an %ar %s"
abc1234 User 2 hours ago Add user authentication
def5678 User 1 day ago Update README

# Common format placeholders:
#   %H  — full commit hash
#   %h  — abbreviated hash
#   %an — author name
#   %ae — author email
#   %ar — author date (relative)
#   %ad — author date (format respects --date=)
#   %cn — committer name
#   %s  — subject (first line of message)
#   %b  — body (rest of message)
#   %d  — ref names (branch/tag decorations)

# Format with colors
$ git log --pretty=format:"%C(yellow)%h%C(reset) %C(blue)%an%C(reset) %s %C(green)(%ar)%C(reset)"
```

## Graph View

```shell
# ASCII graph showing branch topology
$ git log --oneline --graph
* abc1234 Merge branch 'feature/auth'
|\
| * def5678 Add login endpoint
| * ghi9012 Add auth middleware
|/
* jkl3456 Update dependencies
* mno7890 Initial commit

# Graph with all branches
$ git log --oneline --graph --all
* abc1234 (HEAD -> main) Merge branch 'feature/auth'
|\
| * def5678 (feature/auth) Add login endpoint
| * ghi9012 Add auth middleware
|/
| * pqr1234 (feature/dashboard) WIP dashboard
|/
* jkl3456 Update dependencies

# Decorated graph
$ git log --oneline --graph --all --decorate
```

## Filtering by Date

```shell
# Commits after a date
$ git log --after="2025-06-01"
$ git log --since="2025-06-01"

# Commits before a date
$ git log --before="2025-06-15"
$ git log --until="2025-06-15"

# Commits in a date range
$ git log --after="2025-06-01" --before="2025-06-15"

# Relative dates
$ git log --since="2 weeks ago"
$ git log --since="yesterday"
$ git log --since="3 days ago"
```

## Filtering by Author

```shell
$ git log --author="User"
$ git log --author="user@example.com"

# Regex match
$ git log --author="User\|Admin"

# Show commits from everyone except one author
$ git log --author="User" --invert-grep
```

## Filtering by Message

```shell
# Search commit messages
$ git log --grep="fix"
$ git log --grep="auth" --oneline

# Case-insensitive search
$ git log --grep="FIX" -i

# Match all terms (AND logic)
$ git log --grep="fix" --grep="login" --all-match

# Regex in messages
$ git log --grep="^feat:" --oneline
```

## Filtering by File

```shell
# Commits that touched a specific file
$ git log -- src/app.py

# Commits that touched any file in a directory
$ git log -- src/auth/

# Commits that touched multiple files
$ git log -- src/app.py src/utils.py

# Follow file renames
$ git log --follow -- src/new-name.py
```

## Filtering by Content (Pickaxe)

```shell
# Commits that added or removed a string
$ git log -S "def authenticate"
$ git log -S "TODO" --oneline

# Commits where the count of a string changed
$ git log -G "authenticate\(" --oneline
```

## Show Diffs in Log

```shell
# Show diff with each commit
$ git log -p
$ git log --patch

# Show diff for last 2 commits
$ git log -p -2

# Show stat (file change summary)
$ git log --stat
commit abc1234
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025

    Add user authentication

 src/auth.py   | 45 +++++++++++++++++++++++++++++++++++++++++++++
 src/config.py |  3 +++
 2 files changed, 48 insertions(+)

# Show just the short stat
$ git log --shortstat
```

## Commit Range

```shell
# Commits on feature branch not yet in main
$ git log main..feature/auth

# Commits on main not yet in feature branch
$ git log feature/auth..main

# Commits reachable from either but not both (symmetric difference)
$ git log main...feature/auth

# Commits between two tags
$ git log v1.0..v2.0 --oneline
```

## Useful Aliases

```shell
# Beautiful one-line log with graph
$ git log --oneline --graph --all --decorate

# Who did what (shortlog)
$ git shortlog -sn
    42  Alice
    31  Bob
    15  Charlie

# Log with relative dates
$ git log --oneline --date=relative --format="%h %ar %s"
```

## Reflog (Recovery)

```shell
# Show reference log (all HEAD movements, even deleted commits)
$ git reflog
abc1234 HEAD@{0}: commit: Add authentication
def5678 HEAD@{1}: checkout: moving from feature to main
ghi9012 HEAD@{2}: commit: WIP feature
jkl3456 HEAD@{3}: reset: moving to HEAD~1

# Useful to recover "lost" commits after reset
$ git reflog
$ git checkout abc1234  # recover a commit you reset away
```
