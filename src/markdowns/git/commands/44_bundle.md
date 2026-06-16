# git bundle

Packages objects and refs into a single file for offline transfer. Like a portable, file-based remote.

## Create a Bundle

```shell
# Bundle the entire repository (all refs)
$ git bundle create repo.bundle --all
Enumerating objects: 500, done.
Counting objects: 100% (500/500), done.
Compressing objects: 100% (250/250), done.
Total 500 (delta 200), reused 480 (delta 190)

# Bundle a specific branch
$ git bundle create main.bundle main

# Bundle multiple branches
$ git bundle create branches.bundle main develop feature/auth

# Bundle with tags
$ git bundle create release.bundle --all --tags
```

## Bundle a Range of Commits

```shell
# Bundle commits since a specific point (incremental bundle)
$ git bundle create update.bundle main ^abc1234
# Includes commits on main that are descendants of abc1234

# Bundle commits since a tag
$ git bundle create since-v1.bundle main ^v1.0.0

# Bundle last N commits
$ git bundle create recent.bundle main~10..main

# Bundle commits between two tags
$ git bundle create v1-to-v2.bundle v1.0.0..v2.0.0
```

## Verify a Bundle

```shell
# Check if a bundle is valid and the prerequisite commits exist
$ git bundle verify repo.bundle
The bundle contains this ref:
abc1234567890 refs/heads/main
def5678901234 refs/heads/develop
The bundle records a complete history.
repo.bundle is okay

# Verify an incremental bundle (checks prerequisites)
$ git bundle verify update.bundle
The bundle contains this ref:
abc1234567890 refs/heads/main
The bundle requires this ref:
def5678901234 commit message here
update.bundle is okay
```

## List Bundle Contents

```shell
# See what refs are in the bundle
$ git bundle list-heads repo.bundle
abc1234567890 refs/heads/main
def5678901234 refs/heads/develop
ghi9012345678 refs/heads/feature/auth
jkl3456789012 refs/tags/v1.0.0
```

## Clone from a Bundle

```shell
# Clone a repository from a bundle file
$ git clone repo.bundle my-project
Cloning into 'my-project'...
Receiving objects: 100% (500/500), done.
Resolving deltas: 100% (200/200), done.

$ cd my-project
$ git log --oneline -5
abc1234 Latest commit
def5678 Previous commit
...

# The remote "origin" points to the bundle file
$ git remote -v
origin  /path/to/repo.bundle (fetch)
origin  /path/to/repo.bundle (push)

# Change origin to the real remote
$ git remote set-url origin git@github.com:user/repo.git
```

## Fetch from a Bundle

```shell
# Fetch updates from a bundle into an existing repo
$ git fetch /path/to/update.bundle main:refs/remotes/bundle/main
From /path/to/update.bundle
 * [new branch]      main       -> bundle/main

# Merge the fetched changes
$ git merge bundle/main

# Or use the bundle as a named remote
$ git remote add usb /media/usb/repo.bundle
$ git fetch usb
$ git merge usb/main
```

## Incremental Bundle Workflow

```shell
# Day 1: Create full bundle
$ git bundle create full.bundle --all

# Day 2: Create incremental bundle (only new commits)
$ git bundle create day2.bundle main ^day1-tag
# Where day1-tag marks the last bundled commit

# On the receiving end:
$ git bundle verify day2.bundle  # check prerequisites exist
$ git fetch day2.bundle main:refs/remotes/bundle/main
$ git merge bundle/main

# Better: use tags to track what's been bundled
$ git tag -a bundled-$(date +%Y%m%d) -m "Last bundled state"
$ git bundle create update-$(date +%Y%m%d).bundle main ^bundled-20250615
```

## Common Workflows

```shell
# Transfer a repo via USB drive (no network)
# On machine A:
$ git bundle create /media/usb/project.bundle --all
# On machine B:
$ git clone /media/usb/project.bundle project
$ cd project
$ git remote set-url origin git@github.com:user/project.git

# Sneakernet updates (air-gapped environments)
# On connected machine:
$ git bundle create update.bundle main ^last-shared-commit
# Copy update.bundle to USB
# On air-gapped machine:
$ git bundle verify update.bundle
$ git fetch update.bundle main:refs/remotes/sneaker/main
$ git merge sneaker/main

# Backup a repository to a single file
$ git bundle create backup-$(date +%Y%m%d).bundle --all

# Share a feature branch offline
$ git bundle create feature.bundle feature/auth ^main
# Colleague:
$ git fetch feature.bundle feature/auth:feature/auth
$ git checkout feature/auth

# Mirror a repo through a restricted network
$ git bundle create mirror.bundle --all --tags
# Transfer the file through the restricted channel
$ git clone mirror.bundle local-mirror
```

## Bundle vs Clone/Archive

```shell
# git bundle: includes full git history + refs, can be fetched/cloned from
# git archive: just a snapshot of files at one point (no history)
# git clone --bare: creates a bare repo directory (not a single file)

# Bundle is the only way to get a single-file, fetchable copy of a repo
```
