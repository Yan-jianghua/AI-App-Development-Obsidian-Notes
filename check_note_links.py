"""检查本知识库的 Obsidian wiki 链接是否有唯一目标。"""

from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def main() -> None:
    notes = list(ROOT.rglob("*.md"))
    by_stem: dict[str, list[Path]] = defaultdict(list)
    by_path: dict[str, Path] = {}
    for note in notes:
        by_stem[note.stem].append(note)
        by_path[note.relative_to(ROOT).with_suffix("").as_posix()] = note
    missing: list[str] = []
    ambiguous: list[str] = []
    for note in notes:
        text = note.read_text(encoding="utf-8-sig")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
        for target in re.findall(r"\[\[([^\]\n]+)\]\]", text):
            target = target.split("|", 1)[0].split("#", 1)[0].removesuffix(".md")
            if not target or target.lower().endswith((".docx", ".png", ".pdf")):
                continue
            if "/" in target:
                found = target in by_path
            else:
                found = target in by_stem
                if len(by_stem.get(target, [])) > 1:
                    ambiguous.append(f"{note.relative_to(ROOT)} -> {target}")
            if not found:
                missing.append(f"{note.relative_to(ROOT)} -> {target}")
    print(f"笔记 {len(notes)} 篇；未解析链接 {len(missing)}；同名目标 {len(ambiguous)}")
    for issue in missing[:60]:
        print("MISSING", issue)
    for issue in ambiguous[:30]:
        print("AMBIGUOUS", issue)


if __name__ == "__main__":
    main()
