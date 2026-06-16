# git reflog

Records every time HEAD or branch tips move. Your safety net for recovering "lost" commits.

## Basic Usage

```shell
# Show reflog for HEAD (default)
$ git reflog
abc1234 HEAD@{0}: commit: Add user authentication
def5678 HEAD@{1}: checkout: moving from feature/auth to main
ghi9012 HEAD@{2}: commit: WIP auth middleware
jkl3456 HEAD@{3}: checkout: moving from main to feature/auth
mno7890 HEAD@{4}: merge feature/dashboard: Merge made by the 'ort' strategy.
pqr1234 HEAD@{5}: commit: Fix login bug
stu5678 HEAD@{6}: pull: Fast-forward
```

## Reflog for a Specific Branch

```shell
# Show reflog for a specific branch
$ git reflog feature/auth
ghi9012 feature/auth@{0}: commit: WIP auth middleware
jkl3456 feature/auth@{1}: branch: Created from main

# Show reflog for a remote-tracking branch
$ git reflog origin/main
```

## Show with Dates

```shell
# Show with timestamps
$ git reflog --date=iso
abc1234 HEAD@{2025-06-16 10:00:00 +0530}: commit: Add user authentication
def5678 HEAD@{2025-06-16 09:45:00 +0530}: checkout: moving from feature/auth to main

# Relative dates
$ git reflog --date=relative
abc1234 HEAD@{2 hours ago}: commit: Add user authentication
def5678 HEAD@{3 hours ago}: checkout: moving from feature/auth to main
```

## Recover a Lost Commit

```shell
# Scenario: you accidentally reset --hard and lost commits
$ git reset --hard HEAD~3
HEAD is now at mno7890 Old commit

# Find the lost commit in reflog
$ git reflog
mno7890 HEAD@{0}: reset: moving to HEAD~3
abc1234 HEAD@{1}: commit: Add user authentication  # ← this is lost!
def5678 HEAD@{2}: commit: Fix login bug
ghi9012 HEAD@{3}: commit: Add auth middleware

# Recover it
$ git reset --hard abc1234  # restore HEAD to the lost commit
# OR create a branch from it
$ git branch recovered abc1234
$ git checkout recovered
```

## Recover a Deleted Branch

```shell
# Scenario: you deleted a branch with unmerged work
$ git branch -D feature/experimental
Deleted branch feature/experimental (was abc1234).

# Find it in reflog
$ git reflog | grep "feature/experimental"
abc1234 HEAD@{5}: commit: Experimental changes
def5678 HEAD@{6}: checkout: moving from main to feature/experimental

# Recreate the branch
$ git branch feature/experimental abc1234
$ git checkout feature/experimental
# All commits are back!
```

## Recover After Bad Rebase

```shell
# Scenario: rebase went wrong
$ git rebase main
# ... everything is messed up ...
$ git rebase --abort  # if still in progress

# If rebase already completed and you want to undo it:
$ git reflog
abc1234 HEAD@{0}: rebase (finish): returning to refs/heads/feature/auth
def5678 HEAD@{1}: rebase (pick): Add login
ghi9012 HEAD@{2}: rebase (start): checkout main
jkl3456 HEAD@{3}: commit: Add login  # ← pre-rebase state

$ git reset --hard jkl3456
# Branch is back to pre-rebase state
```

## Recover After Bad Merge

```shell
# Find the commit just before the merge
$ git reflog
abc1234 HEAD@{0}: merge feature/broken: Merge made by the 'ort' strategy.
def5678 HEAD@{1}: checkout: moving from feature to main  # ← before merge

$ git reset --hard def5678
# Merge is undone
```

## Expire Reflog Entries

```shell
# Expire entries older than N days
$ git reflog expire --expire=90.days.ago --all

# Expire all unreachable entries immediately
$ git reflog expire --expire-unreachable=now --all

# Expire everything (DANGEROUS — no more recovery)
$ git reflog expire --expire=now --all
$ git gc --prune=now

# Dry run
$ git reflog expire --expire=30.days.ago --dry-run
```

## Reflog with More Detail

```shell
# Show full commit info for each reflog entry
$ git log -g
commit abc1234 (HEAD -> main)
Reflog: HEAD@{0} (User <user@example.com>)
Reflog message: commit: Add user authentication
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

    Add user authentication

# One-line with graph
$ git log -g --oneline
abc1234 HEAD@{0}: commit: Add user authentication
def5678 HEAD@{1}: checkout: moving from feature/auth to main

# Show diffs
$ git log -g -p
```

## Delete a Specific Entry

```shell
# Delete a single reflog entry
$ git reflog delete HEAD@{5}
$ git reflog delete feature/auth@{2}
```

## Common Recovery Patterns

```shell
# "I just lost something" — first step is always reflog
$ git reflog

# "What did I do in the last hour?"
$ git reflog --since="1 hour ago"

# "Where was main before I messed it up?"
$ git reflog main

# "I need to find a specific commit message"
$ git reflog | grep "keyword"

# "I need the state of HEAD from 3 operations ago"
$ git show HEAD@{3}
# Or checkout that state:
$ git checkout HEAD@{3}
```

## Reflog is Local Only

```shell
# Important: reflog is NOT shared with remotes
# Each clone has its own reflog
# It is NOT a backup mechanism — it only records local movements
# Default retention: 90 days (reachable), 30 days (unreachable)
```
