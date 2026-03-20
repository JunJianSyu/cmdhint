#!/usr/bin/env python3
"""
CmdHint v2.0 - Mac/Linux 命令动态提示工具
直接输入命令执行，?命令 查看说明，Tab 触发补全。
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from commands import COMMANDS
from matcher import fuzzy_match, get_flag_completions, format_command_info


# ─────────────────── 补全器（和 test_full.py 相同结构）───────────────────
class CmdHintCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if text.startswith("?"):
            text = text[1:]

        words = text.split()

        # 补全命令名
        if not words or (len(words) == 1 and not text.endswith(" ")):
            query = words[0] if words else ""
            if not query:
                return
            matches = fuzzy_match(query, COMMANDS, threshold=0.25)
            for name, info, score in matches[:12]:
                yield Completion(
                    name,
                    start_position=-len(query),
                    display_meta=f"[{info['category']}] {info['desc']}",
                )

        # 补全参数
        elif len(words) >= 1:
            cmd_name = words[0]
            partial = words[-1] if not text.endswith(" ") else ""
            if cmd_name in COMMANDS:
                flags = get_flag_completions(cmd_name, partial, COMMANDS)
                for flag, desc in flags:
                    yield Completion(
                        flag,
                        start_position=-len(partial),
                        display_meta=desc,
                    )


# ─────────────────── 样式 ───────────────────
STYLE = Style.from_dict({
    "completion-menu.completion":             "bg:#1e1e2e #cdd6f4",
    "completion-menu.completion.current":      "bg:#45475a #f5e0dc bold",
    "completion-menu.meta.completion":         "bg:#1e1e2e #6c7086",
    "completion-menu.meta.completion.current": "bg:#45475a #cba6f7",
    "scrollbar.background":                   "bg:#313244",
    "scrollbar.button":                       "bg:#585b70",
    "bottom-toolbar":                         "bg:#181825 #6c7086",
    "prompt":                                 "#89b4fa bold",
    "auto-suggestion":                        "#585b70",
})


# ─────────────────── 提示符 & 工具栏 ───────────────────
def get_prompt():
    cwd = os.getcwd().replace(os.path.expanduser("~"), "~", 1)
    return HTML(f'<prompt>cmdhint</prompt> <style fg="#6c7086">{cwd}</style> <b>❯</b> ')


def toolbar():
    return HTML(
        '<b>CmdHint</b> │ '
        '直接输入执行 │ '
        '<b>?cmd</b> 查说明 │ '
        '<b>Tab</b> 补全 │ '
        f'共 <b>{len(COMMANDS)}</b> 条'
    )


# ─────────────────── 命令执行 ───────────────────
def execute_command(text):
    parts = text.split()
    cmd = parts[0]

    if cmd == "cd":
        target = parts[1] if len(parts) > 1 else os.path.expanduser("~")
        target = os.path.expanduser(os.path.expandvars(target))
        try:
            os.chdir(target)
            print(f"\033[32m  → {os.getcwd()}\033[0m")
        except FileNotFoundError:
            print(f"\033[31m  目录不存在: {target}\033[0m")
        except PermissionError:
            print(f"\033[31m  权限不足: {target}\033[0m")
        return

    exit_code = os.system(text)
    if hasattr(os, "waitstatus_to_exitstatus"):
        code = os.waitstatus_to_exitstatus(exit_code)
    else:
        code = exit_code >> 8
    if code != 0:
        print(f"\033[31m  退出码: {code}\033[0m")


# ─────────────────── ? 查询 ───────────────────
def handle_hint(text):
    query = text.lstrip("?").strip()
    if not query:
        print("\033[31m  用法: ?命令名  例如 ?grep\033[0m")
        return

    words = query.split()
    cmd_name = words[0]

    if cmd_name in COMMANDS:
        info = COMMANDS[cmd_name]
        print(f"\n{format_command_info(cmd_name, info, verbose=True)}")
        if len(words) > 1:
            flags = info.get("flags", {})
            for arg in words[1:]:
                if arg in flags:
                    print(f"\n  \033[1;35m{arg}\033[0m → {flags[arg]}")
                else:
                    print(f"\n  \033[33m{arg}\033[0m 未在常用参数中记录")
        print()
    else:
        matches = fuzzy_match(cmd_name, COMMANDS)
        if matches:
            print(f"\n\033[33m  未找到 '{cmd_name}'，你是否在找：\033[0m\n")
            for name, info, _ in matches[:5]:
                print(format_command_info(name, info, verbose=False))
            print()
        else:
            print(f"\n\033[31m  未找到命令 '{cmd_name}'\033[0m\n")


# ─────────────────── 内建命令 ───────────────────
def handle_list():
    cats = {}
    for name, info in sorted(COMMANDS.items()):
        cats.setdefault(info["category"], []).append((name, info["desc"]))
    for cat in sorted(cats):
        print(f"\n\033[1;33m━━ {cat} ({len(cats[cat])} 条) ━━\033[0m")
        for name, desc in cats[cat]:
            print(f"  \033[1;36m{name:18s}\033[0m {desc}")


def handle_search(query):
    q = query.lower()
    found = False
    for name, info in sorted(COMMANDS.items()):
        if q in name.lower() or q in info["desc"].lower() or q in info.get("category", "").lower():
            print(format_command_info(name, info, verbose=False))
            found = True
    if not found:
        print(f"\033[31m  未找到与 '{query}' 相关的命令\033[0m")


def handle_stats():
    cats = {}
    total_flags = 0
    for info in COMMANDS.values():
        cats[info["category"]] = cats.get(info["category"], 0) + 1
        total_flags += len(info.get("flags", {}))
    print(f"\n\033[1;33m━━ 命令统计 ━━\033[0m")
    print(f"  总命令数: \033[1;36m{len(COMMANDS)}\033[0m")
    print(f"  总参数数: \033[1;36m{total_flags}\033[0m")
    print(f"  分类数:   \033[1;36m{len(cats)}\033[0m")
    for cat, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"    {cat:10s} \033[35m{'█' * n}\033[0m {n}")


def print_help():
    print("""
\033[1;33m━━ CmdHint 使用帮助 ━━\033[0m

  \033[1m基本用法:\033[0m
    直接输入命令回车执行，按 \033[32mTab\033[0m 触发补全菜单。
    输入 \033[32m?\033[0m 加命令名查看详细说明。

  \033[1m操作示例:\033[0m
    \033[36mls -la\033[0m           直接执行
    \033[36m?grep\033[0m            查看说明
    \033[36m?grep -r\033[0m         查看参数
    \033[36m?grpe\033[0m            模糊查找 → grep

  \033[1m特殊命令:\033[0m
    \033[32m:list\033[0m            列出所有命令
    \033[32m:search <词>\033[0m     搜索命令
    \033[32m:stats\033[0m           统计信息
    \033[32m:help\033[0m            本帮助
    \033[32m:quit\033[0m            退出
""")


# ─────────────────── Banner ───────────────────
def print_banner():
    print("""
\033[1;36m   _____ __  __ ____  _    _ _____ _   _ _______
  / ____|  \\/  |  _ \\| |  | |_   _| \\ | |__   __|
 | |    | \\  / | | | | |__| | | | |  \\| |  | |
 | |    | |\\/| | | | |  __  | | | | . ` |  | |
 | |____| |  | | |_| | |  | |_| |_| |\\  |  | |
  \\_____|_|  |_|____/|_|  |_|_____|_| \\_|  |_|\033[0m

\033[33m  Mac/Linux 命令动态提示工具 v2.0\033[0m
\033[90m  ─────────────────────────────────────────\033[0m
  \033[36mls -la\033[0m          直接执行命令
  \033[36m?grep\033[0m           查看命令说明
  \033[36m?grep -r\033[0m        查看参数说明
  \033[32mTab\033[0m             触发智能补全
  \033[32m:help\033[0m           查看所有功能
\033[90m  ─────────────────────────────────────────\033[0m
""")


# ─────────────────── 主循环 ───────────────────
def main():
    print_banner()

    os.environ.setdefault("CLICOLOR", "1")
    os.environ.setdefault("CLICOLOR_FORCE", "1")
    os.environ.setdefault("TERM", "xterm-256color")
    os.environ.setdefault("LSCOLORS", "GxFxCxDxBxegedabagaced")
    os.environ.setdefault("LS_COLORS", "di=1;34:ln=1;36:so=1;35:pi=33:ex=1;32:bd=1;33:cd=1;33")

    session = PromptSession(
        completer=CmdHintCompleter(),
        style=STYLE,
        history=FileHistory(os.path.expanduser("~/.cmdhint_history")),
        bottom_toolbar=toolbar,
        complete_while_typing=False,
        auto_suggest=AutoSuggestFromHistory(),
    )

    while True:
        try:
            text = session.prompt(get_prompt()).strip()

            if not text:
                continue

            if text in (":quit", ":q", "exit", "quit"):
                print("\n\033[33m  再见！\033[0m\n")
                break
            elif text == ":list":
                handle_list()
            elif text.startswith(":search"):
                parts = text.split(maxsplit=1)
                if len(parts) > 1:
                    handle_search(parts[1])
                else:
                    print("\033[31m  用法: :search <关键词>\033[0m")
            elif text == ":stats":
                handle_stats()
            elif text == ":help":
                print_help()
            elif text.startswith(":"):
                print(f"\033[31m  未知命令: {text}\033[0m，输入 :help 查看帮助")
            elif text.startswith("?"):
                handle_hint(text)
            else:
                execute_command(text)

        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print("\n\033[33m  再见！\033[0m\n")
            break


if __name__ == "__main__":
    main()
