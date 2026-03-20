"""
CmdHint - Mac/Linux 命令动态提示工具

核心逻辑：模糊匹配、命令补全、参数提示
"""

from difflib import SequenceMatcher


def fuzzy_match(query, candidates, threshold=0.3):
    """
    模糊匹配：对查询字符串与候选命令进行匹配打分。
    
    匹配策略（按优先级）：
    1. 精确前缀匹配  → 最高分
    2. 子序列匹配    → 高分
    3. 模糊相似度    → 中等分数
    """
    results = []
    query_lower = query.lower()

    for name, info in candidates.items():
        score = 0.0
        name_lower = name.lower()

        # 1) 精确前缀匹配
        if name_lower.startswith(query_lower):
            score = 1.0 - (len(name) - len(query)) * 0.01

        # 2) 子序列匹配
        elif is_subsequence(query_lower, name_lower):
            score = 0.7 - (len(name) - len(query)) * 0.01

        # 3) SequenceMatcher 模糊相似度
        else:
            ratio = SequenceMatcher(None, query_lower, name_lower).ratio()
            if ratio >= threshold:
                score = ratio * 0.6

        # 4) 描述中包含查询词 → 额外加分
        if query_lower in info.get("desc", "").lower():
            score = max(score, 0.3)

        if score > 0:
            results.append((name, info, score))

    results.sort(key=lambda x: -x[2])
    return results


def is_subsequence(query, target):
    """检查 query 是否为 target 的子序列"""
    it = iter(target)
    return all(c in it for c in query)


def get_flag_completions(cmd_name, partial_flag, commands):
    """获取命令参数/标志的补全建议"""
    if cmd_name not in commands:
        return []

    flags = commands[cmd_name].get("flags", {})
    if not flags:
        return []

    results = []
    for flag, desc in flags.items():
        if flag.startswith(partial_flag) or not partial_flag:
            results.append((flag, desc))

    return results


def format_command_info(name, info, verbose=False):
    """格式化命令信息为显示字符串"""
    lines = []
    lines.append(f"  \033[1;36m{name}\033[0m - {info['desc']}")

    if verbose:
        lines.append(f"    \033[33m用法:\033[0m {info['usage']}")
        lines.append(f"    \033[33m分类:\033[0m {info['category']}")

        if info.get("examples"):
            lines.append(f"    \033[33m示例:\033[0m")
            for ex in info["examples"][:3]:
                lines.append(f"      \033[32m$ {ex}\033[0m")

        if info.get("flags"):
            lines.append(f"    \033[33m常用参数:\033[0m")
            for flag, desc in list(info["flags"].items())[:5]:
                lines.append(f"      \033[35m{flag:12s}\033[0m {desc}")

    return "\n".join(lines)
