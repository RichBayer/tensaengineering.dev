#!/usr/bin/env python3
"""Session check: the one check Rich runs at resume and closeout.

Rich runs the command in docs/ai-operations/operating_rules.md (V2 continuity)
from the project folder. It fetches GitHub's copy of this script and runs it:

    python3 /tmp/tensa_website_session_check.py <branch> [<work log name>]

<branch> is the branch the work is on. <work log name> is the path name in
docs/logs/<name>.md; leave it off for a path with no work log (the menu and
caps are still checked).

It prints a red/green table and always ends with exactly one verdict line,
"SESSION CHECK: PASS" or "SESSION CHECK: FAIL (...)". Only a final PASS is
success. It exits 0 whenever it printed a verdict, so the outer command's
"|| echo ... could not fetch or run" fires only when the download or Python
itself failed. Read-only: it never changes files, branches or GitHub.

Caps and work-log rules come from docs/ai-operations/operating_rules.md;
caps count lines below any front matter, on GitHub's copy. This script assumes
the default branch is `main`; change DEFAULT if the project uses another.
"""
import os
import re
import subprocess
import sys

DEFAULT = "main"
CAPS_DEFAULT = [
    ("README.md", 80),
    ("docs/ai-operations/tensa_website_resume_prompt.md", 40),
    ("docs/ai-operations/operating_rules.md", 150),
]
LOG_CAP = 80
HEADINGS = ["Purpose", "Gates", "Last session", "Decisions in force", "Next",
            "Read before working", "Closeout updates"]
STATUSES = {"PASS", "OPEN", "FAIL"}
# Continuity files only. README and project files change on work branches.
# Branch-specific continuity edits are checked against the merge base.
MAX_READ = 6

COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ
RED, GREEN, YELLOW, RESET = (("\033[31m", "\033[32m", "\033[33m", "\033[0m")
                             if COLOR else ("", "", "", ""))
problems = []


class GitError(Exception):
    pass


def git(*args):
    r = subprocess.run(["git", "--no-pager", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise GitError(f"git {' '.join(args)}: {(r.stderr or r.stdout).strip()}")
    return r.stdout


def show(ref, path):
    """GitHub's copy of a file, or None if it does not exist there."""
    try:
        return git("show", f"{ref}:{path}")
    except GitError:
        return None


def body(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:], lines[1:i]
    return lines, []


def row(ok, label, detail=""):
    mark = f"{GREEN}ok  {RESET}" if ok else f"{RED}FAIL{RESET}"
    print(f"  {mark} {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        problems.append(label)


def note(label):
    print(f"  {YELLOW}note{RESET} {label}")


def section(lines, heading):
    out, inside = [], False
    for line in lines:
        if line.startswith("## "):
            inside = line[3:].strip() == heading
            continue
        if inside:
            out.append(line)
    return out


def log_gates(lines):
    gates = []
    for line in section(lines, "Gates"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0] in ("Gate", "") or set(cells[0]) <= set("-: "):
            continue
        gates.append((cells[0].strip("*` "), cells[1].strip("*` ") if len(cells) > 1 else ""))
    return gates


def main():
    if len(sys.argv) not in (2, 3):
        print("usage: session_check.py <branch> [<work log name>]")
        print("SESSION CHECK: FAIL (wrong arguments)")
        return 0
    branch = sys.argv[1]
    name = sys.argv[2].strip("/") if len(sys.argv) == 3 else None
    remote = f"origin/{branch}"
    default_ref = f"origin/{DEFAULT}"
    print(f"Session check: branch {branch}" + (f", work log {name}" if name else ""))

    # 1. Location and local state.
    print("\nLocation and local state")
    here = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    row(here == branch, "this folder is on the named branch", f"(on {here})")
    git("rev-parse", "--verify", "-q", f"{remote}^{{commit}}")
    status = [l for l in git("status", "--porcelain").splitlines() if l.strip()]
    ahead, behind = (int(x) for x in
                     git("rev-list", "--left-right", "--count", f"HEAD...{remote}").split())
    note(f"uncommitted files: {len(status)}")
    for l in status:
        print(f"         {l}")
    note(f"ahead of GitHub: {ahead}, behind GitHub: {behind}")
    log_path = f"docs/logs/{name}.md" if name else None
    safe = here == branch and ahead == 0 and behind == 0 and not status
    word = f"{GREEN}SAFE{RESET}" if safe else f"{RED}NOT SAFE{RESET}"
    print(f"  CONNECTOR WRITE TO THIS BRANCH: {word}")
    if status:
        note("uncommitted files block connector writes, not resuming")
    if branch == DEFAULT:
        log_safe = safe
    else:
        # A Blog worktree cannot certify the cleanliness of the main worktree.
        # The owner must run a separate session check while on main to save logs.
        log_safe = False
        note("To save a main-owned log, run the check from the main worktree")
    print("  LOG SAVE TO main: " +
          (f"{GREEN}SAFE{RESET}" if log_safe else f"{RED}NOT SAFE{RESET}"))

    # 2. Caps, on GitHub's copy.
    print("\nCaps (GitHub's copy, lines below front matter)")
    files = [(default_ref, p, c) for p, c in CAPS_DEFAULT]
    if name:
        files.append((default_ref, log_path, LOG_CAP))
    for ref, path, cap in files:
        text = show(ref, path)
        if text is None:
            row(False, f"{path}", f"missing on {ref}")
            continue
        n = len(body(text)[0])
        row(n <= cap, f"{path:<44} {n:>4} / {cap}")

    log_lines = []
    if name:
        log_lines = body(show(default_ref, log_path) or "")[0]

        # 3. Work log shape.
        print("\nWork log")
        found = [l[3:].strip() for l in log_lines if l.startswith("## ")]
        row(found == HEADINGS, "seven headings in order",
            "" if found == HEADINGS else f"(found: {', '.join(found) or 'none'})")
        reads = [m.group(1) for l in section(log_lines, "Read before working")
                 if (m := re.match(r"^\s*-\s+`([^`]+)`", l))]
        row(len(reads) <= MAX_READ, f"'Read before working' has {len(reads)} of at most {MAX_READ}")
        for p in reads:
            if name == "blog" and p.startswith("docs/planning/blog_"):
                # These files contain newer approved research on the work branch.
                exists = show(remote, p) is not None
            else:
                exists = show(default_ref, p) is not None or show(remote, p) is not None
            row(exists, f"exists in Git: {p}")

        # 4. Gates.
        gates = log_gates(log_lines)
        labels = [g for g, _ in gates]
        row(bool(gates), "Gates table has at least one row")
        row(len(labels) == len(set(labels)), "gate labels are unique")
        bad = [g for g, s in gates if s not in STATUSES]
        row(not bad, "every gate status is PASS, OPEN or FAIL",
            f"(check: {', '.join(bad)})" if bad else "")

    # 5. Divergence is routine for a long-running content branch. It is
    # an integration concern, not a session-resume failure.
    if branch != DEFAULT:
        print("\nBranch integration state")
        branch_only, main_only = (int(x) for x in
            git("rev-list", "--left-right", "--count",
                f"{remote}...{default_ref}").split())
        note(f"branch-only commits: {branch_only}; main-only commits: {main_only}")
        if main_only:
            note("merge main into this branch before publication (not every save)")
        # Old Blog-branch ai-operations files predate V2 and may already
        # differ historically. Protect the new main-owned V2 logs/checker,
        # and flag legacy process differences for human reconciliation.
        fork = git("merge-base", remote, default_ref).strip()
        changed = git("diff", "--name-only", fork, remote, "--",
                      "docs/logs", "scripts/session_check.py").splitlines()
        row(not changed, "no branch-specific V2 log/checker edits",
            (", ".join(changed)) if changed else "")
        legacy = git("diff", "--name-only", fork, remote, "--",
                     "docs/ai-operations").splitlines()
        if legacy:
            note("legacy branch-specific ai-operations files: " +
                 ", ".join(legacy) + "; use main as authority")
        if changed:
            safe = False
            print(f"  CONNECTOR WRITE TO THIS BRANCH: {RED}NOT SAFE{RESET}"
                  " (branch-specific V2 edits)")
        if name == "blog":
            for p in ["docs/planning/blog_strategy.md",
                      "docs/planning/blog_reader_experience.md",
                      "docs/planning/blog_engagement_strategy.md"]:
                row(show(remote, p) is not None, f"Blog research exists on branch: {p}")

    # 6. Context for a model that cannot read branches.
    if name:
        print("\nWork log: Next")
        for l in section(log_lines, "Next"):
            print(f"  {l}")
    print(f"\nLast 10 commits on {remote}")
    for l in git("log", "--format=%h %ad %s", "--date=short", "-10", remote).splitlines():
        print(f"  {l}")
    print("\nMain-owned files changed by recent save/handoff/closeout commits")
    hits = 0
    for l in git("log", "--format=%h %s", "-10", default_ref).splitlines():
        sha, _, subject = l.partition(" ")
        if re.match(r"^(save|handoff|closeout)\(", subject):
            hits += 1
            names = git("show", "--name-only", "--format=", sha).split()
            print(f"  {sha} {subject}")
            print(f"         {', '.join(names) or '(no files)'}")
    if not hits:
        print("  none in the last 10")

    print()
    if problems:
        print(f"{RED}SESSION CHECK: FAIL ({len(problems)} problem(s): {'; '.join(problems)}){RESET}")
    else:
        print(f"{GREEN}SESSION CHECK: PASS{RESET}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GitError as e:
        print(f"\n{RED}SESSION CHECK: FAIL (Git error: {e}){RESET}")
        sys.exit(0)
    except Exception as e:  # never let a crash look like anything but a failure
        print(f"\n{RED}SESSION CHECK: FAIL (script error: {type(e).__name__}: {e}){RESET}")
        sys.exit(0)
