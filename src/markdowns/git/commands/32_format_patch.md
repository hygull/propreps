# git format-patch

Generates patch files from commits, formatted as email messages. Used for sharing changes outside of push/pull workflows.

## Basic Usage

```shell
# Create a patch for the last commit
$ git format-patch -1
0001-Add-user-authentication.patch

# Create patches for the last N commits
$ git format-patch -3
0001-Add-auth-middleware.patch
0002-Add-login-endpoint.patch
0003-Add-JWT-token-refresh.patch

# Create patches for commits since a specific commit
$ git format-patch abc1234
0001-Fix-typo.patch
0002-Add-feature.patch
```

## Patch from Branch Diff

```shell
# Patches for all commits on feature branch not in main
$ git format-patch main
0001-Add-auth-middleware.patch
0002-Add-login-endpoint.patch
0003-Add-JWT-token-refresh.patch

# Same thing, explicit range
$ git format-patch main..feature/auth

# Patches for commits between two tags
$ git format-patch v1.0.0..v2.0.0
```

## Output to a Directory

```shell
# Save patches to a specific directory
$ git format-patch -3 -o patches/
patches/0001-Add-auth-middleware.patch
patches/0002-Add-login-endpoint.patch
patches/0003-Add-JWT-token-refresh.patch

# Create the directory if it doesn't exist
$ git format-patch main -o /tmp/my-patches/
```

## Single Combined Patch

```shell
# Combine all commits into one patch file (stdout)
$ git format-patch main --stdout > all-changes.patch

# Useful for mailing lists or code review
$ git format-patch -3 --stdout > feature-auth.patch
```

## Cover Letter

```shell
# Generate a cover letter (summary) along with patches
$ git format-patch main --cover-letter
0000-cover-letter.patch
0001-Add-auth-middleware.patch
0002-Add-login-endpoint.patch

# The cover letter has placeholder text to fill in:
# Subject: [PATCH 0/2] *** SUBJECT HERE ***
# *** BLURB HERE ***
```

## Customize Subject Prefix

```shell
# Change the [PATCH] prefix
$ git format-patch -1 --subject-prefix="RFC"
# Subject: [RFC] Add user authentication

$ git format-patch -1 --subject-prefix="PATCH v2"
# Subject: [PATCH v2] Add user authentication

# No prefix
$ git format-patch -1 --no-prefix
```

## Include Extra Info

```shell
# Add diffstat after the --- line
$ git format-patch -1 --stat

# Add a signature
$ git format-patch -1 --signature="Sent from my dev machine"

# Number patches (for multi-part series)
$ git format-patch -3 --numbered
# [PATCH 1/3] Add auth middleware
# [PATCH 2/3] Add login endpoint
# [PATCH 3/3] Add JWT token refresh

# Add version info to subject
$ git format-patch -1 -v2
# Subject: [PATCH v2] Add user authentication
```

## Binary Patches

```shell
# Include binary file diffs (images, compiled files)
$ git format-patch -1 --binary
```

## Patch File Contents

```shell
# A patch file looks like:
$ cat 0001-Add-auth-middleware.patch
From abc1234567890 Mon Sep 17 00:00:00 2001
From: User <user@example.com>
Date: Mon, 16 Jun 2025 10:00:00 +0530
Subject: [PATCH] Add auth middleware

---
 src/auth.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

diff --git a/src/auth.py b/src/auth.py
new file mode 100644
--- /dev/null
+++ b/src/auth.py
@@ -0,0 +1,15 @@
+def authenticate(token):
+    ...
--
2.39.0
```

## Apply Patches (See Also: git am)

```shell
# Quick check if a patch applies cleanly
$ git apply --check 0001-Add-auth-middleware.patch

# Apply without committing (just modify working tree)
$ git apply 0001-Add-auth-middleware.patch

# Apply as commits (preserves author, date, message)
$ git am 0001-Add-auth-middleware.patch
$ git am patches/*.patch
```

## Common Workflows

```shell
# Share changes with a colleague via email/file
$ git format-patch -3 -o /tmp/patches/
# Send the .patch files
# Colleague applies:
$ git am /tmp/patches/*.patch

# Submit patches to an open-source mailing list
$ git format-patch main --cover-letter -v2 --subject-prefix="PATCH v2"
$ git send-email patches/*.patch

# Create a patch for a specific commit to backport
$ git format-patch -1 abc1234 -o backports/
```
