# git alias

Git aliases are shortcuts for frequently used commands. Configured via `git config`.

## Create Aliases

```shell
# Basic aliases
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
$ git config --global alias.sw switch
$ git config --global alias.cp cherry-pick

# Now use them
$ git co main          # git checkout main
$ git br -a            # git branch -a
$ git ci -m "message"  # git commit -m "message"
$ git st               # git status
$ git sw feature/auth  # git switch feature/auth
```

## Log Aliases

```shell
# Pretty one-line graph log
$ git config --global alias.lg "log --oneline --graph --all --decorate"
$ git lg
* abc1234 (HEAD -> main) Merge feature/auth
|\
| * def5678 (feature/auth) Add login
|/
* ghi9012 Initial commit

# Compact log with relative dates
$ git config --global alias.ll "log --oneline --graph --decorate -20"

# Log with full details
$ git config --global alias.lf "log --pretty=format:'%C(yellow)%h%C(reset) %C(blue)%an%C(reset) %s %C(green)(%ar)%C(reset)%C(red)%d%C(reset)'"
$ git lf
abc1234 Alice Add auth (2 hours ago) (HEAD -> main)
def5678 Bob Fix login bug (1 day ago)

# Show last commit
$ git config --global alias.last "log -1 HEAD --stat"
$ git last
commit abc1234 (HEAD -> main)
Author: Alice <alice@example.com>
    Add user authentication
 src/auth.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)
```

## Shortcut Aliases

```shell
# Unstage files
$ git config --global alias.unstage "restore --staged"
$ git unstage file.py    # git restore --staged file.py

# Discard changes
$ git config --global alias.discard "restore"
$ git discard file.py    # git restore file.py

# Amend without editing message
$ git config --global alias.amend "commit --amend --no-edit"
$ git add forgotten.py
$ git amend              # git commit --amend --no-edit

# Quick add and commit
$ git config --global alias.ac "!git add -A && git commit"
$ git ac -m "Quick commit"

# Status short
$ git config --global alias.s "status -sb"
$ git s
## main...origin/main
 M src/app.py
?? new-file.txt
```

## Diff Aliases

```shell
# Diff of staged changes
$ git config --global alias.ds "diff --staged"
$ git ds

# Word diff
$ git config --global alias.dw "diff --word-diff"

# Diff stat only
$ git config --global alias.dstat "diff --stat"
```

## Shell Command Aliases (! prefix)

```shell
# Aliases starting with ! run as shell commands
# They execute from the repository root directory

# Open repo in browser
$ git config --global alias.browse '!open $(git remote get-url origin | sed "s/git@/https:\/\//" | sed "s/\.git$//" | sed "s/:/\//")'

# Delete all merged branches
$ git config --global alias.cleanup '!git branch --merged main | grep -v "main\|master\|\*" | xargs -r git branch -d'
$ git cleanup
Deleted branch feature/old (was abc1234).
Deleted branch hotfix/done (was def5678).

# Show contributors ranked by commit count
$ git config --global alias.contributors 'shortlog -sn --all'
$ git contributors
    42  Alice
    31  Bob
    15  Charlie

# Find a file across history
$ git config --global alias.find '!git ls-files | grep -i'
$ git find auth
src/auth.py
src/auth_middleware.py
tests/test_auth.py

# Show today's commits
$ git config --global alias.today 'log --since=midnight --oneline --author=$(git config user.email)'
$ git today
abc1234 Add user authentication
def5678 Fix login validation

# Undo last commit (keep changes)
$ git config --global alias.undo 'reset HEAD~1 --mixed'
$ git undo
Unstaged changes after reset:
M       src/app.py

# WIP commit (quick save)
$ git config --global alias.wip '!git add -A && git commit -m "WIP: work in progress [skip ci]"'
$ git wip
[feature/auth abc1234] WIP: work in progress [skip ci]

# Unwip (undo the WIP commit)
$ git config --global alias.unwip '!git log -1 --format="%s" | grep -q "^WIP" && git reset HEAD~1 || echo "Last commit is not a WIP"'
```

## Branch Aliases

```shell
# List branches sorted by last commit date
$ git config --global alias.recent 'branch --sort=-committerdate --format="%(committerdate:relative)%09%(refname:short)"'
$ git recent
2 hours ago     main
1 day ago       feature/auth
3 days ago      develop

# Show current branch name
$ git config --global alias.current 'branch --show-current'
$ git current
main

# Create and switch to branch
$ git config --global alias.cb 'switch -c'
$ git cb feature/new-feature
```

## List All Aliases

```shell
# Show all configured aliases
$ git config --get-regexp alias
alias.co checkout
alias.br branch
alias.ci commit
alias.st status
alias.lg log --oneline --graph --all --decorate

# Alias to list aliases!
$ git config --global alias.aliases 'config --get-regexp alias'
$ git aliases

# More readable format
$ git config --global alias.alias '!git config --get-regexp alias | sed "s/alias\.\([^ ]*\)/\1\t=>/" | sort'
$ git alias
amend   =>  commit --amend --no-edit
br      =>  branch
ci      =>  commit
co      =>  checkout
lg      =>  log --oneline --graph --all --decorate
st      =>  status
```

## Remove an Alias

```shell
$ git config --global --unset alias.co
```

## Where Aliases Are Stored

```shell
# Global aliases are in ~/.gitconfig
$ cat ~/.gitconfig
[alias]
    co = checkout
    br = branch
    lg = log --oneline --graph --all --decorate

# Local (repo-only) aliases are in .git/config
$ git config alias.deploy '!./scripts/deploy.sh'

# Edit directly
$ git config --global --edit
```

## Recommended Starter Set

```shell
git config --global alias.s "status -sb"
git config --global alias.co "checkout"
git config --global alias.sw "switch"
git config --global alias.cb "switch -c"
git config --global alias.br "branch"
git config --global alias.ci "commit"
git config --global alias.amend "commit --amend --no-edit"
git config --global alias.unstage "restore --staged"
git config --global alias.discard "restore"
git config --global alias.undo "reset HEAD~1 --mixed"
git config --global alias.last "log -1 HEAD --stat"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.ll "log --oneline -20"
git config --global alias.ds "diff --staged"
git config --global alias.cleanup '!git branch --merged main | grep -v "main\|master\|\*" | xargs -r git branch -d'
git config --global alias.aliases "config --get-regexp alias"
```
