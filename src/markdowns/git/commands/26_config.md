# git config

Gets and sets repository or global configuration options.

## Configuration Levels

```shell
# System level (all users on this machine)
$ git config --system core.autocrlf true
# Stored in: /etc/gitconfig

# Global level (current user, all repos)
$ git config --global user.name "Alice"
# Stored in: ~/.gitconfig or ~/.config/git/config

# Local level (current repository only — default)
$ git config --local core.ignorecase false
$ git config core.ignorecase false
# Stored in: .git/config

# Priority: local > global > system
```

## User Identity

```shell
# Set your name and email (required for commits)
$ git config --global user.name "Alice Smith"
$ git config --global user.email "alice@example.com"

# Set per-repo identity (for work vs personal)
$ git config user.name "Alice Corporate"
$ git config user.email "alice@company.com"

# Verify
$ git config user.name
Alice Smith
$ git config user.email
alice@example.com
```

## View Configuration

```shell
# List all settings (merged from all levels)
$ git config --list
user.name=Alice Smith
user.email=alice@example.com
core.editor=vim
push.default=current
...

# List with origin (which file each setting comes from)
$ git config --list --show-origin
file:/home/alice/.gitconfig    user.name=Alice Smith
file:.git/config               remote.origin.url=git@github.com:user/repo.git

# Get a specific value
$ git config user.name
Alice Smith

# Check which level a setting comes from
$ git config --show-origin user.name
file:/home/alice/.gitconfig    Alice Smith
```

## Editor

```shell
$ git config --global core.editor "vim"
$ git config --global core.editor "code --wait"     # VS Code
$ git config --global core.editor "nano"
$ git config --global core.editor "subl -n -w"      # Sublime Text
```

## Default Branch Name

```shell
$ git config --global init.defaultBranch main
```

## Aliases

```shell
# Create shortcuts for common commands
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status

# Now use them
$ git co main
$ git br -a
$ git ci -m "Quick commit"
$ git st

# Complex aliases
$ git config --global alias.lg "log --oneline --graph --all --decorate"
$ git config --global alias.last "log -1 HEAD"
$ git config --global alias.unstage "reset HEAD --"
$ git config --global alias.amend "commit --amend --no-edit"

# Alias with shell command (prefix with !)
$ git config --global alias.cleanup '!git branch --merged | grep -v main | xargs git branch -d'
```

## Merge and Diff Tools

```shell
# Set merge tool
$ git config --global merge.tool vimdiff
$ git config --global merge.tool vscode
$ git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Set diff tool
$ git config --global diff.tool vscode
$ git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

## Line Endings

```shell
# Auto-convert line endings
$ git config --global core.autocrlf true     # Windows (CRLF → LF on commit, LF → CRLF on checkout)
$ git config --global core.autocrlf input    # macOS/Linux (CRLF → LF on commit, no conversion on checkout)
$ git config --global core.autocrlf false    # No conversion
```

## Push/Pull Behavior

```shell
# Default push behavior
$ git config --global push.default current
$ git config --global push.autoSetupRemote true

# Default pull behavior
$ git config --global pull.rebase true       # rebase instead of merge
$ git config --global pull.ff only           # fast-forward only

# Auto-stash on pull/rebase
$ git config --global rebase.autoStash true
```

## Credential Storage

```shell
# Cache credentials in memory (default 15 min timeout)
$ git config --global credential.helper cache
$ git config --global credential.helper 'cache --timeout=3600'

# Store credentials permanently (plain text — less secure)
$ git config --global credential.helper store

# Use macOS Keychain
$ git config --global credential.helper osxkeychain
```

## Color Settings

```shell
# Enable colored output
$ git config --global color.ui auto

# Customize colors
$ git config --global color.status.added green
$ git config --global color.status.changed yellow
$ git config --global color.status.untracked red
```

## Remove/Unset Settings

```shell
# Remove a single setting
$ git config --global --unset user.email

# Remove all values for a key
$ git config --global --unset-all alias.co

# Remove an entire section
$ git config --global --remove-section alias

# Edit config file directly
$ git config --global --edit
# Opens ~/.gitconfig in your editor
```

## Useful Settings Collection

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
$ git config --global init.defaultBranch main
$ git config --global push.default current
$ git config --global push.autoSetupRemote true
$ git config --global pull.rebase true
$ git config --global rebase.autoStash true
$ git config --global core.editor "code --wait"
$ git config --global alias.lg "log --oneline --graph --all --decorate"
$ git config --global alias.st status
$ git config --global alias.co checkout
```
