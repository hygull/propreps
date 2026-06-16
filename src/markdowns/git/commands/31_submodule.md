# git submodule

Manages repositories nested inside another repository.

## Add a Submodule

```shell
# Add a submodule
$ git submodule add https://github.com/user/library.git libs/library
Cloning into 'libs/library'...
done.

# Add with a specific branch
$ git submodule add -b main https://github.com/user/library.git libs/library

# Creates two things:
# 1. The directory libs/library/ (cloned repo)
# 2. A .gitmodules file:
$ cat .gitmodules
[submodule "libs/library"]
    path = libs/library
    url = https://github.com/user/library.git
```

## Initialize and Update

```shell
# After cloning a repo with submodules, initialize them
$ git submodule init
Submodule 'libs/library' (https://github.com/user/library.git) registered for path 'libs/library'

# Fetch and checkout submodule contents
$ git submodule update
Cloning into 'libs/library'...
Submodule path 'libs/library': checked out 'abc1234'

# Or do both at once
$ git submodule update --init

# Recursively init and update nested submodules
$ git submodule update --init --recursive
```

## Clone with Submodules

```shell
# Clone and automatically init all submodules
$ git clone --recurse-submodules https://github.com/user/repo.git

# If you already cloned without submodules
$ git submodule update --init --recursive
```

## Check Submodule Status

```shell
$ git submodule status
 abc1234 libs/library (v1.2.0)
 def5678 libs/another-lib (heads/main)
+ghi9012 libs/modified-lib (v2.0.0)
# + means submodule has local changes
# - means submodule is not initialized
```

## Update Submodule to Latest

```shell
# Pull latest changes in a submodule
$ cd libs/library
$ git pull origin main
$ cd ../..
$ git add libs/library
$ git commit -m "Update library submodule to latest"

# Or use submodule update --remote
$ git submodule update --remote libs/library
Submodule path 'libs/library': checked out 'jkl3456'

# Update all submodules to latest
$ git submodule update --remote

# Set which branch to track for remote updates
$ git config -f .gitmodules submodule.libs/library.branch develop
```

## Foreach (Run Command in All Submodules)

```shell
# Run a command in each submodule
$ git submodule foreach 'git status'
Entering 'libs/library'
On branch main
nothing to commit, working tree clean
Entering 'libs/another-lib'
On branch main
nothing to commit, working tree clean

# Pull latest in all submodules
$ git submodule foreach 'git pull origin main'

# Recursive (includes nested submodules)
$ git submodule foreach --recursive 'git checkout main'
```

## Remove a Submodule

```shell
# Remove a submodule (Git 1.8.5+)
$ git submodule deinit libs/library
$ git rm libs/library
$ rm -rf .git/modules/libs/library
$ git commit -m "Remove library submodule"

# Or manually:
# 1. Delete from .gitmodules
# 2. Delete from .git/config
# 3. git rm --cached libs/library
# 4. rm -rf .git/modules/libs/library
# 5. rm -rf libs/library
# 6. git commit
```

## Summary of Changes

```shell
# Show a summary of submodule changes
$ git submodule summary
* libs/library abc1234...def5678 (3):
  > Fix memory leak
  > Add caching
  > Update dependencies
```

## Sync URLs

```shell
# If the remote URL changed, sync it
$ git submodule sync
Synchronizing submodule url for 'libs/library'

# Then update
$ git submodule update --init --recursive
```

## Common Workflows

```shell
# Initial setup after cloning
$ git clone https://github.com/user/repo.git
$ cd repo
$ git submodule update --init --recursive

# Keep submodules up to date
$ git submodule update --remote --merge
$ git add .
$ git commit -m "Update submodules to latest"

# Check out a specific version of a submodule
$ cd libs/library
$ git checkout v1.5.0
$ cd ../..
$ git add libs/library
$ git commit -m "Pin library to v1.5.0"
```
