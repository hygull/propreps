# git show

Shows various types of objects (commits, tags, trees, blobs).

## Show a Commit

```shell
# Show the latest commit (diff + message)
$ git show
commit abc1234567890 (HEAD -> main)
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

    Add user authentication

diff --git a/src/auth.py b/src/auth.py
new file mode 100644
--- /dev/null
+++ b/src/auth.py
@@ -0,0 +1,15 @@
+def authenticate(username, password):
+    ...

# Show a specific commit
$ git show def5678
$ git show HEAD~3
```

## Show Without Diff

```shell
# Show only the commit message and stats
$ git show --stat abc1234
commit abc1234567890
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025

    Add user authentication

 src/auth.py   | 15 +++++++++++++++
 src/config.py |  3 +++
 2 files changed, 18 insertions(+)

# Show just the message (no diff, no stats)
$ git show --no-patch abc1234
$ git show -s abc1234
commit abc1234567890
Author: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025

    Add user authentication
```

## Show Specific File at a Commit

```shell
# Show a file's contents at a specific commit
$ git show abc1234:src/app.py
def main():
    print("Hello, World!")
    ...

# Show a file at HEAD
$ git show HEAD:README.md

# Show a file from another branch
$ git show feature/auth:src/auth.py
```

## Show a Tag

```shell
# Show annotated tag info
$ git show v1.0.0
tag v1.0.0
Tagger: User <user@example.com>
Date:   Mon Jun 16 10:00:00 2025 +0530

Release version 1.0.0

commit abc1234567890
Author: User <user@example.com>
Date:   Mon Jun 16 09:50:00 2025 +0530

    Final changes for v1.0.0

diff --git a/...
```

## Format Options

```shell
# One-line format
$ git show --oneline --no-patch abc1234
abc1234 Add user authentication

# Custom format
$ git show --format="%H%n%an%n%ae%n%s" --no-patch abc1234
abc1234567890abcdef
User
user@example.com
Add user authentication

# Show only file names changed
$ git show --name-only abc1234
commit abc1234567890
    Add user authentication

src/auth.py
src/config.py

# Show file names with status
$ git show --name-status abc1234
commit abc1234567890
    Add user authentication

A       src/auth.py
M       src/config.py
```

## Show a Tree (Directory)

```shell
# List files in a directory at a specific commit
$ git show abc1234:src/
tree abc1234:src/

app.py
auth.py
config.py
utils.py
```

## Show Multiple Objects

```shell
# Show multiple commits
$ git show abc1234 def5678

# Show range of commits
$ git show HEAD~3..HEAD
```

## Word Diff

```shell
# Show word-level changes
$ git show --word-diff abc1234
def hello():
    print({-"Hello"-}{+"Hello, World!"+})
```

## Common Uses

```shell
# Quick peek at what the last commit changed
$ git show --stat

# See the full file at last release
$ git show v1.0.0:src/app.py

# See what a coworker committed
$ git show origin/feature/auth

# Compare a file between two commits
$ git show abc1234:file.py > /tmp/old.py
$ git show def5678:file.py > /tmp/new.py
$ diff /tmp/old.py /tmp/new.py
```
