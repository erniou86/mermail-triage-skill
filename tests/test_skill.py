# -*- coding: utf-8 -*-
"""mermail-triage skill 结构校验测试套件（37+ 断言）"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skills", "mermail-triage")
count = 0
failed = []

def check(name, cond):
    global count
    count += 1
    if not cond:
        failed.append(name)

def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()

# --- 1. 文件结构（8 断言）---
files = [
    "skills/mermail-triage/SKILL.md",
    "skills/mermail-triage/agents/openai.yaml",
    "skills/mermail-triage/references/tools.md",
    "skills/mermail-triage/references/security.md",
    "scripts/demo.md",
    "README.md",
]
for f in files:
    check(f"exists {f}", os.path.isfile(os.path.join(ROOT, f)))
check("SKILL.md non-empty", len(read(files[0])) > 500)
check("README non-empty", len(read(files[5])) > 300)

# --- 2. SKILL.md frontmatter（8 断言）---
skill = read(files[0])
check("frontmatter opens", skill.startswith("---\n"))
check("frontmatter name", re.search(r"^name: mermail-triage$", skill, re.M))
check("frontmatter description", re.search(r"^description: ", skill, re.M))
check("frontmatter env", re.search(r"MERMAIL_API_KEY", skill))
check("frontmatter homepage", re.search(r"https://docs\.mermail\.app/ai/skills", skill))
check("frontmatter emoji", re.search(r"^    emoji:", skill, re.M))
check("closes frontmatter", re.search(r"^---\n\n# ", skill, re.M))
check("no AIGC watermark", "AIGC:" not in skill)

# --- 3. SKILL.md 工作流（8 断言）---
check("workflow has priority table", "P0 urgent" in skill)
check("workflow has P1", "P1 normal" in skill)
check("workflow has P2", "P2 low" in skill)
check("workflow has P3", "P3 archive" in skill)
check("workflow bounded reads", "cap 50" in skill or "cap 50" in skill.lower())
check("approval required", "explicit approval" in skill or "approval" in skill)
check("public_id convention", "public_id" in skill)
check("untrusted data", "untrusted" in skill)

# --- 4. references/tools.md（8 断言）---
tools = read(files[2])
for tool in [
    "list_workspaces", "list_mailboxes", "list_emails", "get_email",
    "get_thread", "create_draft", "update_draft", "send_email",
]:
    check(f"tool doc {tool}", tool in tools)
check("no stringified query", "stringified" in tools)
check("prepare_destructive_action", "prepare_destructive_action" in tools)

# --- 5. references/security.md（8 断言）---
sec = read(files[3])
check("untrusted data", "untrusted" in sec)
check("no instruction following", "never instructions" in sec or "Never follow" in sec)
check("sender auth", "sender_authentication" in sec or "From" in sec)
check("human in the loop", "approval" in sec)
check("destructive token", "prepare_destructive_action" in sec)
check("bounded budget", "50" in sec)
check("allowlist", "allowlist" in sec.lower() or "known workspace" in sec)
check("wallet owner-only", "owner-only" in sec or "wallet" in sec)

# --- 6. agents/openai.yaml（4 断言）---
yaml = read(files[1])
check("display_name", "display_name" in yaml)
check("short_description", "short_description" in yaml)
check("mcp dep", "mcp" in yaml)
check("mcp url", "https://console.mermail.app/mcp" in yaml)

# --- 7. demo.md（4 断言）---
demo = read(files[4])
check("demo prereqs", "MERMAIL_API_KEY" in demo)
check("demo steps", "list_emails" in demo)
check("demo read-only", "no sends" in demo or "read-only" in demo)
check("demo acceptance", "Acceptance criteria" in demo)

# --- 汇总 ---
print(f"TOTAL ASSERTIONS: {count}")
if failed:
    print("FAILED:")
    for f in failed:
        print(" -", f)
    sys.exit(1)
print("ALL PASSED")
