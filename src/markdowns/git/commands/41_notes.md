# git notes

Adds or inspects notes attached to commits without modifying the commits themselves.

## Add a Note

```shell
# Add a note to the current commit (HEAD)
$ git notes add -m "Reviewed by Alice, approved for release"
$ git notes add -m "Performance impact: +15% throughput"

# Add a note to a specific commit
$ git notes add -m "This introduced the auth regression" abc1234

# Open editor to write a note
$ git notes add
# (editor opens)

# Add from a file
$ git notes add -F review-comments.txt abc1234
```

## View Notes

```shell
# Notes appear in git log automatically
$ git log -1
commit abc1234 (HEAD -> main)
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

    Add user authentication

Notes:
    Reviewed by Alice, approved for release

# Show note for a specific commit
$ git notes show abc1234
Reviewed by Alice, approved for release

# Show note for HEAD
$ git notes show
```

## Edit a Note

```shell
# Edit the note on HEAD
$ git notes edit

# Edit note on a specific commit
$ git notes edit abc1234
# (editor opens with existing note content)
```

## Append to a Note

```shell
# Append to an existing note (instead of replacing)
$ git notes append -m "Also reviewed by Bob"

$ git notes show
Reviewed by Alice, approved for release
Also reviewed by Bob

# Append to a specific commit
$ git notes append -m "Backported to release/v1.x" abc1234
```

## Remove Notes

```shell
# Remove note from HEAD
$ git notes remove

# Remove note from a specific commit
$ git notes remove abc1234

# Prune notes for commits that no longer exist
$ git notes prune
```

## List All Notes

```shell
$ git notes list
abc1234567890 def5678901234
ghi9012345678 jkl3456789012
# Format: note-object-hash commit-hash

# Show all commits that have notes
$ git log --oneline --notes
abc1234 Add user authentication
    Notes:
        Reviewed by Alice, approved for release
def5678 Fix login bug
ghi9012 Update README
    Notes:
        Needs grammar review
```

## Multiple Note Namespaces (Refs)

```shell
# Use different namespaces for different types of notes
$ git notes --ref=review add -m "LGTM - Alice" abc1234
$ git notes --ref=testing add -m "All tests pass, coverage 92%" abc1234
$ git notes --ref=deploy add -m "Deployed to production 2025-06-16" abc1234

# View notes from a specific namespace
$ git notes --ref=review show abc1234
LGTM - Alice

$ git notes --ref=testing show abc1234
All tests pass, coverage 92%

# Show notes from a specific ref in log
$ git log --notes=review -1 abc1234
commit abc1234
    Add user authentication

Notes (review):
    LGTM - Alice

# List all note refs
$ git notes --ref=review list
$ git notes --ref=testing list
```

## Copy Notes

```shell
# Copy note from one commit to another
$ git notes copy abc1234 def5678

# Force overwrite if destination already has a note
$ git notes copy -f abc1234 def5678
```

## Push/Fetch Notes

```shell
# Notes are NOT pushed by default — push them explicitly
$ git push origin refs/notes/commits
$ git push origin "refs/notes/*"

# Fetch notes from remote
$ git fetch origin refs/notes/commits:refs/notes/commits
$ git fetch origin "refs/notes/*:refs/notes/*"

# Push notes for a custom ref
$ git push origin refs/notes/review
```

## Merge Notes

```shell
# Merge notes from another ref
$ git notes merge refs/notes/remote-review

# Resolve merge conflicts in notes
$ git notes merge --strategy=cat_sort_uniq refs/notes/review
# Strategies: manual, ours, theirs, union, cat_sort_uniq
```

## Common Workflows

```shell
# Code review annotations
$ git notes --ref=review add -m "LGTM" abc1234

# Tracking deployments
$ git notes --ref=deploy add -m "Deployed to staging: $(date)" HEAD

# Bug tracking cross-reference
$ git notes add -m "Fixes: JIRA-1234" abc1234

# CI results (attached by automation)
$ git notes --ref=ci add -m "Build #456: PASS, 95% coverage" HEAD

# Search for commits with specific notes
$ git log --all --notes --grep="LGTM" --notes=review
```
