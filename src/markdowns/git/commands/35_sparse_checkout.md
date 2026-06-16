# git sparse-checkout

Reduces your working tree to a subset of tracked files. Essential for working with monorepos where you only need specific directories.

## Enable Sparse Checkout

```shell
# Initialize sparse checkout (cone mode — recommended)
$ git sparse-checkout init --cone
# Working tree is reduced to only top-level files

# Check current state
$ git sparse-checkout list
# (empty — only top-level files are checked out)

$ ls
README.md  package.json  .gitignore
# Subdirectories are excluded
```

## Add Directories

```shell
# Check out specific directories
$ git sparse-checkout set src/auth src/config
# Only src/auth/ and src/config/ (plus top-level files) are in the working tree

$ ls src/
auth/  config/
# Other directories like src/dashboard/, src/utils/ are excluded

# Add more directories without replacing existing ones
$ git sparse-checkout add src/utils tests/
$ git sparse-checkout list
src/auth
src/config
src/utils
tests
```

## Set Patterns (Non-Cone Mode)

```shell
# For fine-grained patterns, use non-cone mode
$ git sparse-checkout init --no-cone

# Set gitignore-style patterns
$ git sparse-checkout set "src/*.py" "tests/" "docs/api/"

# Edit patterns directly
$ git sparse-checkout edit
# Opens editor with current patterns
```

## Cone Mode vs Non-Cone Mode

```shell
# Cone mode (default, recommended):
# - Faster performance
# - Works with directory paths only
# - Includes all files in specified directories
$ git sparse-checkout init --cone
$ git sparse-checkout set src/auth src/config

# Non-cone mode:
# - Supports gitignore-style patterns
# - Can include/exclude individual files
# - Slower for large repos
$ git sparse-checkout init --no-cone
$ git sparse-checkout set
/*
!/src/
/src/auth/
/src/config/
*.md
```

## Disable Sparse Checkout

```shell
# Restore the full working tree
$ git sparse-checkout disable
# All files are checked out again
```

## Reapply Rules

```shell
# Re-apply sparse checkout rules (useful after merge/rebase)
$ git sparse-checkout reapply
```

## Check Status

```shell
# List current sparse-checkout directories
$ git sparse-checkout list
src/auth
src/config
tests

# Check if sparse checkout is enabled
$ git config core.sparseCheckout
true

# See the sparse-checkout file directly
$ cat .git/info/sparse-checkout
/*
!/*/
/src/auth/
/src/config/
/tests/
```

## Clone + Sparse Checkout

```shell
# Clone with sparse checkout from the start (most efficient)
$ git clone --sparse https://github.com/big-org/monorepo.git
Cloning into 'monorepo'...
$ cd monorepo

# Only top-level files are present
$ ls
README.md  CONTRIBUTING.md  .gitignore

# Add the directories you need
$ git sparse-checkout set services/auth services/api libs/shared

# Combine with partial clone for maximum efficiency
$ git clone --sparse --filter=blob:none https://github.com/big-org/monorepo.git
$ cd monorepo
$ git sparse-checkout set services/auth
# Only downloads blobs for files in services/auth/
```

## Sparse Checkout with Depth

```shell
# Combine sparse checkout with shallow clone
$ git clone --sparse --depth=1 https://github.com/big-org/monorepo.git
$ cd monorepo
$ git sparse-checkout set packages/my-package
# Minimal clone: only latest commit + only your package's files
```

## Common Workflows

```shell
# Monorepo: work on just your team's service
$ git clone --sparse --filter=blob:none https://github.com/company/monorepo.git
$ cd monorepo
$ git sparse-checkout set services/auth libs/common configs/
# Fast clone, small working tree

# Add a dependency temporarily
$ git sparse-checkout add services/notifications
# ... review code ...
$ git sparse-checkout set services/auth libs/common configs/
# Remove it by re-setting without it

# CI: only checkout what's needed for a specific job
$ git clone --sparse --depth=1 https://github.com/company/monorepo.git
$ cd monorepo
$ git sparse-checkout set services/auth tests/auth
$ npm test

# Gradually expand as needed
$ git sparse-checkout add docs/
$ git sparse-checkout list
services/auth
libs/common
configs
docs
```

## Troubleshooting

```shell
# Files still showing after sparse-checkout? Reapply:
$ git sparse-checkout reapply

# Check if sparse index is enabled (faster for very large repos)
$ git sparse-checkout init --cone --sparse-index

# If a merge/rebase adds files outside your sparse set:
$ git sparse-checkout reapply
# Files outside the set become "skip-worktree" again
```
