#!/usr/bin/env python3
"""Search past sessions: digests first, then the raw conversations (user/assistant words only).

  recall.py 健身房                  every word must match (case-insensitive)
  recall.py Gion Crystal --raw      also search raw transcripts on this machine
  recall.py --dir /tmp/x 健身房     another digest folder (testing)
Output is capped so it stays cheap to read.
"""
import re
import sys
from pathlib import Path

import digest  # same folder: transcript discovery and extraction

SESSIONS = digest.SESSIONS
MAX_DIGEST_HITS = 5
MAX_RAW_HITS = 8
SNIPPET = 160


def snippet(text, word):
    i = text.lower().find(word.lower())
    s = text[max(0, i - SNIPPET // 2): i + SNIPPET].replace("\n", " ")
    return "…" + s + "…"


def search_digests(folder, words):
    hits = []
    for f in sorted(folder.glob("20*.md"), reverse=True):
        t = f.read_text(encoding="utf-8")
        if all(w.lower() in t.lower() for w in words):
            hits.append(f)
    for f in hits[:MAX_DIGEST_HITS]:
        t = f.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", t, re.M)
        print(f"\n### {f.name}  {title.group(1) if title else ''}")
        for line in t.splitlines():
            if line.startswith("- ") and any(w.lower() in line.lower() for w in words):
                print(line[:300])
    if len(hits) > MAX_DIGEST_HITS:
        print(f"\n(+{len(hits) - MAX_DIGEST_HITS} more digests match; add words to narrow)")
    return hits


def search_raw(words):
    shown = 0
    for path in sorted(digest.find_transcripts(), key=lambda p: p.stat().st_mtime, reverse=True):
        turns, _ = digest.extract(path)
        for when, role, text in turns:
            if all(w.lower() in text.lower() for w in words):
                stamp = when.strftime("%Y-%m-%d %H:%M") if when else "?"
                print(f"- {stamp} [{path.stem[:8]}] {role}: {snippet(text, words[0])}")
                shown += 1
                if shown >= MAX_RAW_HITS:
                    print("(more raw hits omitted; add words to narrow)")
                    return


def main(argv):
    raw = "--raw" in argv
    folder = SESSIONS
    if "--dir" in argv:
        folder = Path(argv[argv.index("--dir") + 1])
        argv = [a for i, a in enumerate(argv) if a != "--dir" and argv[i - 1] != "--dir"]
    words = [a for a in argv if not a.startswith("--")]
    if not words:
        print(__doc__)
        return
    print(f"## 摘要里搜「{' '.join(words)}」")
    hits = search_digests(folder, words)
    if not hits:
        print("（摘要里没有）")
    if raw or not hits:
        print(f"\n## 原始对话里搜（本机 transcript）")
        search_raw(words)


if __name__ == "__main__":
    main(sys.argv[1:])
