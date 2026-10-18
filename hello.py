# -*- coding: utf-8 -*-
"""我的第一个仓库里的第一个程序。

把 PRINT_LINE 改成你自己的话，然后体验一遍：
    git status
    git add .
    git commit -m "改了一句话"
    git push
"""

PRINT_LINE = "你好，这是我的第一个 GitHub 仓库。"


def greet(name: str) -> str:
    """拼一句问候语。"""
    return f"你好，{name}！"


def main() -> None:
    print(PRINT_LINE)
    print(greet("GitHub"))
    print("-" * 30)
    print(f"Python {__import__('sys').version.split()[0]}")


if __name__ == "__main__":
    main()
