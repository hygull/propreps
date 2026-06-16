```bash
  ┌─────┬──────────┬──────────────────────────────────────────────────────────────┐
  │  #  │ Command  │                         Description                          │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 00  │ init     │ Create/reinitialize repos, bare repos, shared repos          │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 01  │ clone    │ HTTPS/SSH, shallow, partial, recursive clones                │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 02  │ add      │ Staging files, patterns, patch mode, dry run                 │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 03  │ commit   │ Messages, amend, sign, fixup, squash, verbose                │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 04  │ status   │ Short format, porcelain, branch info, ignored files          │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 05  │ diff     │ Staged, commits, branches, word-diff, filters                │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 06  │ log      │ Pretty formats, graph, filtering by date/author/file/content │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 07  │ branch   │ Create, rename, delete, filter, track upstream               │
  ├─────┼──────────┼──────────────────────────────────────────────────────────────┤
  │ 08  │ checkout │ Switch branches, restore files, detached HEAD, conflicts     │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 09  │ merge       │ Fast-forward, conflicts, squash, strategies, no-commit       │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 10  │ rebase      │ Interactive, autosquash, onto, exec, autostash               │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 11  │ remote      │ Add, remove, rename, change URL, prune, fork workflow        │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 12  │ fetch       │ Prune, tags, shallow, dry run                                │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 13  │ pull        │ Rebase, ff-only, autostash, conflicts                        │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 14  │ push        │ Upstream, force-with-lease, tags, delete remote branch       │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 15  │ stash       │ Push, pop, apply, list, show, patch, branch from stash       │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 16  │ reset       │ Soft/mixed/hard, unstage, undo commits, recovery             │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 17  │ rm          │ Remove files, --cached, patterns, force, dry run             │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 18  │ mv          │ Rename, move, force, case-sensitive rename                   │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 19  │ tag         │ Annotated, lightweight, signed, push, sort                   │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 20  │ cherry-pick │ Single, range, no-commit, conflicts, merge commits           │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 21  │ revert      │ Single, multiple, merge commits, revert vs reset             │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 22  │ clean       │ Dry run, directories, ignored files, interactive             │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 23  │ show        │ Commits, files at commits, tags, formats                     │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 24  │ blame       │ Line range, ignore revs, copy detection, date formats        │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 25  │ bisect      │ Manual, automated, skip, log, custom terms                   │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 26  │ config      │ Identity, aliases, editor, credentials, push/pull behavior   │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 27  │ restore     │ Discard changes, unstage, source, patch mode                 │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 28  │ switch      │ Create branch, track remote, detached HEAD, orphan           │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 29  │ grep        │ Regex, context, multiple patterns, search at commit          │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 30  │ worktree    │ Create, list, remove, prune, lock                            │
  ├─────┼─────────────┼──────────────────────────────────────────────────────────────┤
  │ 31  │ submodule   │ Add, init, update, foreach, remove, sync                     │
  └─────┴─────────────┴──────────────────────────────────────────────────────────────┘
```

```bash
  ┌─────┬─────────────────┬───────────────────────────────────────────────────────────────────┐
  │  #  │     Command     │                            Description                            │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 32  │ format-patch    │ Generate email-formatted patches, cover letters, versioned series │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 33  │ am              │ Apply mailbox patches, 3-way merge, signoff                       │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 34  │ gc              │ Garbage collection, prune, repack, object stats                   │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 35  │ sparse-checkout │ Cone/non-cone mode, monorepo partial checkouts                    │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 36  │ alias           │ Shortcuts, shell aliases, log/branch/diff aliases, starter set    │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 37  │ reflog          │ Recovery safety net, undo reset/rebase/delete, expiration         │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 38  │ shortlog        │ Author summaries, commit counts, changelog generation             │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 39  │ describe        │ Version strings from tags, dirty suffix, build identifiers        │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 40  │ archive         │ Tar/zip exports, release archives, deploy via pipe                │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 41  │ notes           │ Attach metadata to commits, namespaces, push/fetch notes          │
  ├─────┼─────────────────┼───────────────────────────────────────────────────────────────────┤
  │ 42  │ maintenance     │ Scheduled background optimization, commit-graph, prefetch         │
  └─────┴─────────────────┴───────────────────────────────────────────────────────────────────┘

```
