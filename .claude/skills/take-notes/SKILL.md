---
name: take-notes
description: Create organized notes on any topic. Automatically groups notes into relevant subdirectories under src/notes/ (e.g., src/notes/python/loops/, src/notes/agents/, src/notes/docker/). Use this when the user wants to take notes, save explanations, or document concepts.
argument-hint: <topic>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

You are a notes-taker for the **propreps** repository. Your job is to create well-structured, concise notes on the topic provided by the user.

## Topic

$ARGUMENTS

## Instructions

1. **Determine the category and subcategory** from the topic. Map the topic to an appropriate directory path under `src/notes/`. Examples:
   - "Agents vs Skills" -> `src/notes/agents/agents_vs_skills.md`
   - "Python decorators" -> `src/notes/python/decorators.md`
   - "Python for loops" -> `src/notes/python/loops/for_loops.md`
   - "Docker volumes" -> `src/notes/docker/volumes.md`
   - "Git rebase vs merge" -> `src/notes/git/rebase_vs_merge.md`
   - "React hooks" -> `src/notes/react/hooks.md`
   - "REST vs GraphQL" -> `src/notes/api/rest_vs_graphql.md`
   - "SQL joins" -> `src/notes/sql/joins.md`
   - "Data structures" -> `src/notes/data_structures/overview.md`
   - "AWS Lambda" -> `src/notes/aws/lambda.md`
   - If the topic doesn't fit a clear tech category, use a sensible general category (e.g., `src/notes/concepts/`, `src/notes/architecture/`, `src/notes/tools/`)

2. **Check for existing notes** in the target directory. If a related file already exists, append to or update it rather than creating a duplicate.

3. **Create the directory** if it doesn't exist yet.

4. **Write the notes file** in Markdown with this structure:
   ```
   # <Topic Title>

   > <One-line summary of the topic>

   ## Key Points

   - Point 1
   - Point 2
   - ...

   ## Details

   <Explanation with examples, code snippets, comparisons as appropriate>

   ## Examples

   <Code examples if applicable, using fenced code blocks with language tags>

   ## Summary

   <Brief recap / when to use what>

   ---
   *Notes created: <YYYY-MM-DD>*
   ```

5. **Adapt the template** to the topic:
   - For comparison topics (X vs Y): include a comparison table
   - For code-related topics: include runnable code examples
   - For concept topics: include real-world analogies where helpful
   - Skip sections that don't apply (e.g., no "Examples" section for a pure theory topic)

6. **Keep notes concise but complete** -- aim for quick reference material, not a textbook.

7. **After creating the file**, confirm the path and give a brief summary of what was written.
