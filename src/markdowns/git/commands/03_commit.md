# git commit

Records changes to the repository by creating a new commit.

## Basic Usage

```shell
# Commit staged changes with a message
$ git commit -m "Add user authentication"
[main abc1234] Add user authentication
 3 files changed, 45 insertions(+), 2 deletions(-)

# Open editor to write a commit message
$ git commit
# (opens $EDITOR / $GIT_EDITOR — write message, save, close to commit)

# Commit with a multi-line message
$ git commit -m "Add user authentication" -m "Implements JWT-based auth with refresh tokens."
```

## Stage and Commit Together

```shell
# Automatically stage all modified/deleted tracked files and commit
# (does NOT include new/untracked files)
$ git commit -a -m "Fix typo in config"
$ git commit -am "Fix typo in config"
```

## Amend the Last Commit

```shell
# Change the last commit message
$ git commit --amend -m "Better commit message"

# Add forgotten files to the last commit (keep same message)
$ git add forgotten-file.py
$ git commit --amend --no-edit
[main def5678] Better commit message
 Date: Mon Jun 16 10:00:00 2025 +0530
 4 files changed, 50 insertions(+), 2 deletions(-)

# Change author of the last commit
$ git commit --amend --author="Name <email@example.com>"
```

## Empty Commits

```shell
# Create a commit with no changes (useful for triggering CI)
$ git commit --allow-empty -m "Trigger CI rebuild"
[main ghi9012] Trigger CI rebuild
```

## Commit with Date Override

```shell
# Set a specific author date
$ GIT_AUTHOR_DATE="2025-01-15T10:00:00" git commit -m "Backdated commit"

# Set both author and committer date
$ GIT_AUTHOR_DATE="2025-01-15" GIT_COMMITTER_DATE="2025-01-15" git commit -m "Specific date"
```

## Verbose Commit

```shell
# Show the diff in the editor while writing the commit message
$ git commit -v
# The diff is shown below the commit message area (not included in the message)

# Even more verbose — show diff of what's NOT staged too
$ git commit -v -v
```

## Signing Commits

```shell
# Sign a commit with GPG
$ git commit -S -m "Signed commit"

# Sign all commits by default
$ git config --global commit.gpgSign true

# Verify a signed commit
$ git log --show-signature -1
commit abc1234 (HEAD -> main)
gpg: Signature made Mon Jun 16 10:00:00 2025
gpg: Good signature from "User <user@example.com>"
```

## Fixup and Squash Commits

```shell
# Create a fixup commit (for later squashing with rebase)
$ git commit --fixup=abc1234
[main jkl5678] fixup! Original commit message

# Create a squash commit (like fixup but lets you edit the message)
$ git commit --squash=abc1234

# Auto-squash during rebase
$ git rebase -i --autosquash main
```

## Commit Message from File

```shell
# Read commit message from a file
$ git commit -F commit-message.txt

# Read from stdin
$ echo "Auto commit" | git commit -F -

# Use a template for commit messages
$ git config commit.template ~/.gitmessage.txt
```

## View Commit Details

```shell
# Show the latest commit
$ git log -1
commit abc1234 (HEAD -> main)
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

    Add user authentication

# Show commit with diff
$ git show abc1234

# Show commit stats
$ git show --stat abc1234
 src/auth.py    | 30 ++++++++++++++++++++++++++++++
 src/config.py  |  5 +++++
 tests/test_auth.py | 15 +++++++++++++++
 3 files changed, 50 insertions(+)

# One-line log
$ git log --oneline -5
abc1234 Add user authentication
def5678 Update README
ghi9012 Fix login bug
jkl3456 Add tests
mno7890 Initial commit
```

## Undo a Commit

```shell
# Undo last commit but keep changes staged
$ git reset --soft HEAD~1

# Undo last commit and unstage changes (keep in working directory)
$ git reset HEAD~1
$ git reset --mixed HEAD~1

# Undo last commit and discard all changes (DANGEROUS)
$ git reset --hard HEAD~1

# Create a new commit that reverses a previous commit (safe for shared history)
$ git revert abc1234
[main pqr3456] Revert "Add user authentication"
```
