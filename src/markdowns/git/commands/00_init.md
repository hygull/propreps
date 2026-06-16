# git init

Creates a new Git repository or reinitializes an existing one.

## Basic Usage

```shell
# Create a new repository in the current directory
$ git init
Initialized empty Git repository in /home/user/my-project/.git/

# Create a new repository in a specific directory
$ git init my-new-project
Initialized empty Git repository in /home/user/my-new-project/.git/

# What it creates
$ ls -la .git/
drwxr-xr-x  HEAD
drwxr-xr-x  config
drwxr-xr-x  description
drwxr-xr-x  hooks/
drwxr-xr-x  info/
drwxr-xr-x  objects/
drwxr-xr-x  refs/
```

## Setting Default Branch Name

```shell
# Initialize with a specific branch name (instead of "master")
$ git init --initial-branch=main
Initialized empty Git repository in /home/user/project/.git/

# Short form
$ git init -b main

# Set default branch name globally (affects all future git init)
$ git config --global init.defaultBranch main
```

## Bare Repository

```shell
# Create a bare repository (no working directory — used for remotes/servers)
$ git init --bare my-project.git
Initialized empty Git repository in /home/user/my-project.git/

# A bare repo has no working tree — only the .git internals
$ ls my-project.git/
HEAD  config  description  hooks/  info/  objects/  refs/

# Typical use: set up a shared remote on a server
$ ssh server "git init --bare /srv/git/project.git"
$ git remote add origin server:/srv/git/project.git
$ git push -u origin main
```

## Reinitialize an Existing Repository

```shell
# Running git init in an existing repo is safe — it won't overwrite things
$ git init
Reinitialized existing Git repository in /home/user/my-project/.git/

# Useful for: adding template hooks or changing the format
$ git init --template=/path/to/custom-templates
```

## Common Workflow After Init

```shell
$ mkdir my-project && cd my-project
$ git init
Initialized empty Git repository in /home/user/my-project/.git/

$ echo "# My Project" > README.md
$ git add README.md
$ git commit -m "Initial commit"
[main (root-commit) abc1234] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

$ git status
On branch main
nothing to commit, working tree clean
```

## Shared Repository (Team Setup)

```shell
# Initialize with group-writable permissions
$ git init --shared=group
Initialized empty shared Git repository in /srv/git/team-project/.git/

# --shared options:
#   false    — default, no special permissions
#   true/group — group-writable
#   all/world  — world-readable, group-writable
#   0xxx     — explicit umask value
```
