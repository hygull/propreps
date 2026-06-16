# git tag

Creates, lists, deletes, or verifies tags. Tags mark specific points in history (usually releases).

## List Tags

```shell
$ git tag
v1.0.0
v1.1.0
v2.0.0

# Filter tags by pattern
$ git tag -l "v1.*"
v1.0.0
v1.1.0
v1.2.0-beta

# List with details
$ git tag -n
v1.0.0    Initial release
v1.1.0    Bug fixes and performance
v2.0.0    Major rewrite

# List with more lines of annotation
$ git tag -n3
```

## Create Annotated Tags (Recommended)

```shell
# Annotated tags store metadata (tagger, date, message, can be signed)
$ git tag -a v1.0.0 -m "Release version 1.0.0"

# Create and open editor for the message
$ git tag -a v2.0.0
# (editor opens for tag message)

# Tag a specific commit (not HEAD)
$ git tag -a v1.0.0 -m "Release 1.0.0" abc1234
```

## Create Lightweight Tags

```shell
# Lightweight tags are just pointers (no metadata)
$ git tag v1.0.0-rc1

# Tag a specific commit
$ git tag v1.0.0-rc1 abc1234
```

## Show Tag Details

```shell
# Show annotated tag info + the commit it points to
$ git show v1.0.0
tag v1.0.0
Tagger: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

Release version 1.0.0

commit abc1234567890
Author: User <user@example.com>
Date:   Mon Jun 16 09:50:00 2025 +0530

    Final changes for v1.0.0

# Show just the tag message (not the commit)
$ git tag -l -n1 v1.0.0
v1.0.0    Release version 1.0.0
```

## Delete Tags

```shell
# Delete a local tag
$ git tag -d v1.0.0
Deleted tag 'v1.0.0' (was abc1234)

# Delete a remote tag
$ git push origin --delete v1.0.0
$ git push origin :refs/tags/v1.0.0
```

## Push Tags to Remote

```shell
# Push a specific tag
$ git push origin v1.0.0

# Push all tags
$ git push origin --tags

# Push only annotated tags (not lightweight)
$ git push origin --follow-tags
```

## Signed Tags (GPG)

```shell
# Create a GPG-signed tag
$ git tag -s v1.0.0 -m "Signed release 1.0.0"

# Verify a signed tag
$ git tag -v v1.0.0
object abc1234567890
type commit
tag v1.0.0
tagger User <user@example.com>

Signed release 1.0.0
gpg: Signature made Mon Jun 16 10:00:00 2025
gpg: Good signature from "User <user@example.com>"
```

## Checkout a Tag

```shell
# View code at a tag (detached HEAD)
$ git checkout v1.0.0
Note: switching to 'v1.0.0'.
You are in 'detached HEAD' state.

# Create a branch from a tag
$ git checkout -b hotfix/v1.0.1 v1.0.0

# Using switch
$ git switch --detach v1.0.0
```

## Replace/Move a Tag

```shell
# Force-move a tag to a different commit
$ git tag -f v1.0.0 def5678
Updated tag 'v1.0.0' (was abc1234)

# Update on remote too
$ git push origin -f v1.0.0
```

## Sorting Tags

```shell
# Sort by version number
$ git tag --sort=version:refname
v1.0.0
v1.1.0
v1.2.0
v2.0.0
v10.0.0

# Sort by creation date (newest first)
$ git tag --sort=-creatordate
v2.0.0
v1.2.0
v1.1.0
v1.0.0
```

## Common Workflows

```shell
# Release workflow
$ git checkout main
$ git pull
$ git tag -a v1.2.0 -m "Release 1.2.0: added dashboard feature"
$ git push origin v1.2.0

# See commits between two tags
$ git log v1.0.0..v2.0.0 --oneline
abc1234 Add dashboard
def5678 Refactor auth
ghi9012 Fix login bug

# Generate changelog between tags
$ git log v1.0.0..v2.0.0 --pretty=format:"- %s (%h)" --no-merges
- Add dashboard (abc1234)
- Refactor auth (def5678)
- Fix login bug (ghi9012)
```
