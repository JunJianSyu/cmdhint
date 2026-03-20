"""
Comprehensive Mac/Linux command database with descriptions, usage, and categories.
"""

COMMANDS = {
    # ============================================================
    # File & Directory Operations
    # ============================================================
    "ls": {
        "desc": "列出当前目录的文件和文件夹",
        "usage": "ls [-alRh] [path]",
        "category": "文件操作",
        "examples": ["ls -la", "ls -lh /tmp", "ls -R src/"],
        "flags": {
            "-a": "显示隐藏文件",
            "-l": "详细列表格式",
            "-h": "人类可读的文件大小",
            "-R": "递归列出子目录",
            "-t": "按修改时间排序",
            "-S": "按文件大小排序",
            "-r": "反转排序顺序",
        },
    },
    "cd": {
        "desc": "切换当前工作目录",
        "usage": "cd [directory]",
        "category": "文件操作",
        "examples": ["cd /home", "cd ..", "cd ~", "cd -"],
        "flags": {},
    },
    "pwd": {
        "desc": "显示当前工作目录的绝对路径",
        "usage": "pwd",
        "category": "文件操作",
        "examples": ["pwd"],
        "flags": {},
    },
    "mkdir": {
        "desc": "创建新目录",
        "usage": "mkdir [-pv] directory",
        "category": "文件操作",
        "examples": ["mkdir mydir", "mkdir -p a/b/c"],
        "flags": {
            "-p": "递归创建父目录",
            "-v": "显示创建过程",
        },
    },
    "rmdir": {
        "desc": "删除空目录",
        "usage": "rmdir directory",
        "category": "文件操作",
        "examples": ["rmdir empty_dir"],
        "flags": {},
    },
    "cp": {
        "desc": "复制文件或目录",
        "usage": "cp [-riv] source dest",
        "category": "文件操作",
        "examples": ["cp file.txt backup.txt", "cp -r dir1/ dir2/"],
        "flags": {
            "-r": "递归复制目录",
            "-i": "覆盖前确认",
            "-v": "显示复制过程",
            "-a": "保留所有属性（归档模式）",
        },
    },
    "mv": {
        "desc": "移动或重命名文件/目录",
        "usage": "mv [-iv] source dest",
        "category": "文件操作",
        "examples": ["mv old.txt new.txt", "mv file.txt /tmp/"],
        "flags": {
            "-i": "覆盖前确认",
            "-v": "显示移动过程",
            "-n": "不覆盖已有文件",
        },
    },
    "rm": {
        "desc": "删除文件或目录",
        "usage": "rm [-rfi] file",
        "category": "文件操作",
        "examples": ["rm file.txt", "rm -rf build/"],
        "flags": {
            "-r": "递归删除目录",
            "-f": "强制删除不提示",
            "-i": "删除前确认",
        },
    },
    "touch": {
        "desc": "创建空文件或更新文件时间戳",
        "usage": "touch file",
        "category": "文件操作",
        "examples": ["touch newfile.txt", "touch -t 202301010000 file.txt"],
        "flags": {
            "-t": "指定时间戳",
            "-a": "只修改访问时间",
            "-m": "只修改修改时间",
        },
    },
    "ln": {
        "desc": "创建链接（硬链接或符号链接）",
        "usage": "ln [-s] target link_name",
        "category": "文件操作",
        "examples": ["ln -s /usr/bin/python3 python", "ln file hardlink"],
        "flags": {
            "-s": "创建符号链接（软链接）",
            "-f": "覆盖已存在的链接",
        },
    },
    "stat": {
        "desc": "显示文件的详细状态信息",
        "usage": "stat file",
        "category": "文件操作",
        "examples": ["stat myfile.txt"],
        "flags": {},
    },
    "file": {
        "desc": "检测文件类型",
        "usage": "file filename",
        "category": "文件操作",
        "examples": ["file image.png", "file script.sh"],
        "flags": {},
    },
    "tree": {
        "desc": "以树状结构显示目录内容",
        "usage": "tree [-L level] [directory]",
        "category": "文件操作",
        "examples": ["tree", "tree -L 2 src/"],
        "flags": {
            "-L": "限制显示深度",
            "-d": "只显示目录",
            "-a": "显示隐藏文件",
        },
    },
    "realpath": {
        "desc": "显示文件的绝对路径（解析符号链接）",
        "usage": "realpath file",
        "category": "文件操作",
        "examples": ["realpath ./script.sh"],
        "flags": {},
    },
    "basename": {
        "desc": "从路径中提取文件名部分",
        "usage": "basename path [suffix]",
        "category": "文件操作",
        "examples": ["basename /home/user/file.txt", "basename file.txt .txt"],
        "flags": {},
    },
    "dirname": {
        "desc": "从路径中提取目录部分",
        "usage": "dirname path",
        "category": "文件操作",
        "examples": ["dirname /home/user/file.txt"],
        "flags": {},
    },

    # ============================================================
    # File Content Viewing & Editing
    # ============================================================
    "cat": {
        "desc": "查看文件内容或合并文件",
        "usage": "cat [-n] file",
        "category": "文件查看",
        "examples": ["cat file.txt", "cat -n file.txt", "cat a.txt b.txt > merged.txt"],
        "flags": {
            "-n": "显示行号",
            "-b": "非空行显示行号",
            "-s": "压缩连续空行",
        },
    },
    "less": {
        "desc": "分页查看文件内容（支持上下翻页）",
        "usage": "less file",
        "category": "文件查看",
        "examples": ["less large_file.log"],
        "flags": {
            "-N": "显示行号",
            "-S": "不自动换行",
        },
    },
    "more": {
        "desc": "分页查看文件内容（逐页向下）",
        "usage": "more file",
        "category": "文件查看",
        "examples": ["more file.txt"],
        "flags": {},
    },
    "head": {
        "desc": "查看文件开头部分（默认前10行）",
        "usage": "head [-n lines] file",
        "category": "文件查看",
        "examples": ["head file.txt", "head -n 20 file.txt"],
        "flags": {
            "-n": "指定显示行数",
            "-c": "指定显示字节数",
        },
    },
    "tail": {
        "desc": "查看文件末尾部分（默认后10行）",
        "usage": "tail [-n lines] [-f] file",
        "category": "文件查看",
        "examples": ["tail file.txt", "tail -f /var/log/syslog", "tail -n 50 log.txt"],
        "flags": {
            "-n": "指定显示行数",
            "-f": "实时跟踪文件新增内容",
            "-F": "跟踪文件（支持文件轮转）",
        },
    },
    "wc": {
        "desc": "统计文件的行数、字数和字节数",
        "usage": "wc [-lwc] file",
        "category": "文件查看",
        "examples": ["wc file.txt", "wc -l file.txt"],
        "flags": {
            "-l": "只统计行数",
            "-w": "只统计字数",
            "-c": "只统计字节数",
            "-m": "只统计字符数",
        },
    },
    "nano": {
        "desc": "简单易用的终端文本编辑器",
        "usage": "nano file",
        "category": "文件查看",
        "examples": ["nano config.yml"],
        "flags": {},
    },
    "vim": {
        "desc": "强大的终端文本编辑器",
        "usage": "vim file",
        "category": "文件查看",
        "examples": ["vim script.py"],
        "flags": {},
    },
    "vi": {
        "desc": "经典终端文本编辑器（vim的前身）",
        "usage": "vi file",
        "category": "文件查看",
        "examples": ["vi config.txt"],
        "flags": {},
    },
    "diff": {
        "desc": "比较两个文件的差异",
        "usage": "diff [-u] file1 file2",
        "category": "文件查看",
        "examples": ["diff old.txt new.txt", "diff -u a.py b.py"],
        "flags": {
            "-u": "统一格式输出",
            "-r": "递归比较目录",
            "-q": "只报告是否不同",
        },
    },
    "tee": {
        "desc": "将标准输入同时写入文件和标准输出",
        "usage": "command | tee file",
        "category": "文件查看",
        "examples": ["echo hello | tee output.txt", "ls | tee -a log.txt"],
        "flags": {
            "-a": "追加模式（不覆盖）",
        },
    },
    "sort": {
        "desc": "对文件内容进行排序",
        "usage": "sort [-rnuk] file",
        "category": "文件查看",
        "examples": ["sort names.txt", "sort -rn numbers.txt"],
        "flags": {
            "-r": "逆序排列",
            "-n": "按数字排序",
            "-u": "去重",
            "-k": "按指定列排序",
            "-t": "指定分隔符",
        },
    },
    "uniq": {
        "desc": "删除排序后文件中的重复行",
        "usage": "uniq [-cd] file",
        "category": "文件查看",
        "examples": ["sort file.txt | uniq", "sort file.txt | uniq -c"],
        "flags": {
            "-c": "统计重复次数",
            "-d": "只显示重复行",
            "-u": "只显示唯一行",
        },
    },
    "cut": {
        "desc": "按列提取文件内容",
        "usage": "cut -d delimiter -f fields file",
        "category": "文件查看",
        "examples": ["cut -d',' -f1,3 data.csv", "cut -c1-10 file.txt"],
        "flags": {
            "-d": "指定分隔符",
            "-f": "指定提取的字段",
            "-c": "按字符位置提取",
        },
    },
    "paste": {
        "desc": "将多个文件按行合并",
        "usage": "paste file1 file2",
        "category": "文件查看",
        "examples": ["paste names.txt scores.txt"],
        "flags": {
            "-d": "指定分隔符",
        },
    },
    "tr": {
        "desc": "替换或删除字符",
        "usage": "tr [options] set1 [set2]",
        "category": "文件查看",
        "examples": ["echo hello | tr 'a-z' 'A-Z'", "echo 'a:b:c' | tr ':' '\\n'"],
        "flags": {
            "-d": "删除指定字符",
            "-s": "压缩连续重复字符",
        },
    },
    "rev": {
        "desc": "反转每一行的字符顺序",
        "usage": "rev [file]",
        "category": "文件查看",
        "examples": ["echo 'hello' | rev"],
        "flags": {},
    },
    "column": {
        "desc": "将输入格式化为整齐的列",
        "usage": "column [-t] [-s sep] file",
        "category": "文件查看",
        "examples": ["cat data.txt | column -t"],
        "flags": {
            "-t": "自动对齐列",
            "-s": "指定分隔符",
        },
    },
    "nl": {
        "desc": "给文件内容添加行号",
        "usage": "nl file",
        "category": "文件查看",
        "examples": ["nl script.py"],
        "flags": {},
    },
    "fold": {
        "desc": "按指定宽度折叠行",
        "usage": "fold [-w width] file",
        "category": "文件查看",
        "examples": ["fold -w 80 long_lines.txt"],
        "flags": {
            "-w": "指定宽度",
            "-s": "在空格处断行",
        },
    },
    "od": {
        "desc": "以八进制/十六进制显示文件内容",
        "usage": "od [-A radix] [-t type] file",
        "category": "文件查看",
        "examples": ["od -c file.bin", "od -x file.bin"],
        "flags": {
            "-c": "显示字符",
            "-x": "十六进制显示",
        },
    },
    "xxd": {
        "desc": "以十六进制形式查看文件内容",
        "usage": "xxd file",
        "category": "文件查看",
        "examples": ["xxd binary.dat"],
        "flags": {},
    },

    # ============================================================
    # Search & Find
    # ============================================================
    "find": {
        "desc": "在目录树中搜索文件和目录",
        "usage": "find [path] [options] [expression]",
        "category": "搜索",
        "examples": [
            "find . -name '*.py'",
            "find /tmp -type f -mtime -7",
            "find . -size +100M",
        ],
        "flags": {
            "-name": "按文件名匹配",
            "-type": "按类型过滤（f=文件, d=目录）",
            "-size": "按大小过滤",
            "-mtime": "按修改时间过滤",
            "-exec": "对找到的文件执行命令",
            "-iname": "不区分大小写匹配文件名",
            "-maxdepth": "限制搜索深度",
        },
    },
    "grep": {
        "desc": "在文件中搜索匹配文本的行",
        "usage": "grep [-rinl] pattern [file]",
        "category": "搜索",
        "examples": [
            "grep 'error' log.txt",
            "grep -rn 'TODO' src/",
            "grep -i 'hello' file.txt",
        ],
        "flags": {
            "-r": "递归搜索目录",
            "-i": "不区分大小写",
            "-n": "显示行号",
            "-l": "只显示文件名",
            "-v": "反向匹配（排除）",
            "-c": "只计数匹配行数",
            "-E": "使用扩展正则表达式",
            "-w": "匹配整个单词",
            "-A": "同时显示匹配行之后N行",
            "-B": "同时显示匹配行之前N行",
        },
    },
    "egrep": {
        "desc": "使用扩展正则表达式搜索文件",
        "usage": "egrep pattern file",
        "category": "搜索",
        "examples": ["egrep '(error|warn)' log.txt"],
        "flags": {},
    },
    "fgrep": {
        "desc": "搜索固定字符串（不使用正则表达式）",
        "usage": "fgrep string file",
        "category": "搜索",
        "examples": ["fgrep 'exact match' file.txt"],
        "flags": {},
    },
    "rg": {
        "desc": "ripgrep - 极速文件内容搜索工具",
        "usage": "rg [options] pattern [path]",
        "category": "搜索",
        "examples": ["rg 'TODO' src/", "rg -t py 'import'"],
        "flags": {
            "-i": "不区分大小写",
            "-t": "指定文件类型",
            "--hidden": "搜索隐藏文件",
            "-l": "只显示文件名",
        },
    },
    "ag": {
        "desc": "The Silver Searcher - 快速代码搜索工具",
        "usage": "ag [options] pattern [path]",
        "category": "搜索",
        "examples": ["ag 'function' src/"],
        "flags": {},
    },
    "locate": {
        "desc": "通过数据库快速定位文件",
        "usage": "locate filename",
        "category": "搜索",
        "examples": ["locate nginx.conf"],
        "flags": {},
    },
    "which": {
        "desc": "显示命令的可执行文件路径",
        "usage": "which command",
        "category": "搜索",
        "examples": ["which python", "which node"],
        "flags": {},
    },
    "whereis": {
        "desc": "查找命令的二进制文件、源码和手册页",
        "usage": "whereis command",
        "category": "搜索",
        "examples": ["whereis gcc"],
        "flags": {},
    },
    "type": {
        "desc": "显示命令的类型（内建/别名/文件）",
        "usage": "type command",
        "category": "搜索",
        "examples": ["type ls", "type cd"],
        "flags": {},
    },

    # ============================================================
    # Text Processing
    # ============================================================
    "sed": {
        "desc": "流编辑器 - 对文本进行替换/删除等操作",
        "usage": "sed [options] 'command' file",
        "category": "文本处理",
        "examples": [
            "sed 's/old/new/g' file.txt",
            "sed -n '5,10p' file.txt",
            "sed -i '' 's/foo/bar/g' file.txt",
        ],
        "flags": {
            "-i": "直接修改文件",
            "-n": "抑制默认输出",
            "-e": "指定多个编辑命令",
        },
    },
    "awk": {
        "desc": "强大的文本处理和数据提取工具",
        "usage": "awk 'pattern {action}' file",
        "category": "文本处理",
        "examples": [
            "awk '{print $1}' file.txt",
            "awk -F',' '{print $2}' data.csv",
            "awk '/error/ {count++} END {print count}' log.txt",
        ],
        "flags": {
            "-F": "指定字段分隔符",
            "-v": "定义变量",
        },
    },
    "xargs": {
        "desc": "将标准输入转换为命令参数",
        "usage": "command | xargs [options] command",
        "category": "文本处理",
        "examples": [
            "find . -name '*.log' | xargs rm",
            "cat urls.txt | xargs -I{} curl {}",
        ],
        "flags": {
            "-I": "指定替换字符串",
            "-n": "每次传递N个参数",
            "-P": "并行执行数量",
        },
    },
    "jq": {
        "desc": "命令行 JSON 处理器",
        "usage": "jq [filter] file",
        "category": "文本处理",
        "examples": ["cat data.json | jq '.name'", "jq '.items[]' list.json"],
        "flags": {
            "-r": "输出原始字符串",
            "-c": "紧凑输出",
        },
    },
    "bc": {
        "desc": "命令行计算器",
        "usage": "echo 'expression' | bc",
        "category": "文本处理",
        "examples": ["echo '3.14 * 2' | bc", "echo 'scale=2; 10/3' | bc"],
        "flags": {
            "-l": "加载数学库",
        },
    },
    "expr": {
        "desc": "表达式求值",
        "usage": "expr expression",
        "category": "文本处理",
        "examples": ["expr 5 + 3", "expr length 'hello'"],
        "flags": {},
    },

    # ============================================================
    # Permissions & Ownership
    # ============================================================
    "chmod": {
        "desc": "修改文件/目录权限",
        "usage": "chmod [options] mode file",
        "category": "权限管理",
        "examples": ["chmod 755 script.sh", "chmod +x run.sh", "chmod -R 644 docs/"],
        "flags": {
            "-R": "递归修改",
            "-v": "显示修改详情",
        },
    },
    "chown": {
        "desc": "修改文件/目录的所有者",
        "usage": "chown [options] user[:group] file",
        "category": "权限管理",
        "examples": ["chown user:group file.txt", "chown -R www-data:www-data /var/www"],
        "flags": {
            "-R": "递归修改",
        },
    },
    "chgrp": {
        "desc": "修改文件/目录的所属组",
        "usage": "chgrp group file",
        "category": "权限管理",
        "examples": ["chgrp staff project/"],
        "flags": {
            "-R": "递归修改",
        },
    },
    "umask": {
        "desc": "设置新建文件的默认权限掩码",
        "usage": "umask [mask]",
        "category": "权限管理",
        "examples": ["umask", "umask 022"],
        "flags": {},
    },
    "sudo": {
        "desc": "以超级管理员权限执行命令",
        "usage": "sudo command",
        "category": "权限管理",
        "examples": ["sudo apt update", "sudo vim /etc/hosts"],
        "flags": {
            "-u": "以指定用户身份执行",
            "-i": "切换到root shell",
            "-s": "启动一个shell",
        },
    },
    "su": {
        "desc": "切换用户身份",
        "usage": "su [-l] [username]",
        "category": "权限管理",
        "examples": ["su -", "su - username"],
        "flags": {
            "-l": "模拟完整登录",
        },
    },

    # ============================================================
    # Process Management
    # ============================================================
    "ps": {
        "desc": "查看当前运行的进程列表",
        "usage": "ps [options]",
        "category": "进程管理",
        "examples": ["ps aux", "ps -ef", "ps aux | grep python"],
        "flags": {
            "a": "显示所有用户进程",
            "u": "用户友好的输出格式",
            "x": "包括无终端进程",
            "-e": "显示所有进程",
            "-f": "完整格式输出",
        },
    },
    "top": {
        "desc": "实时显示系统进程和资源使用情况",
        "usage": "top",
        "category": "进程管理",
        "examples": ["top", "top -o cpu"],
        "flags": {
            "-o": "按指定列排序",
        },
    },
    "htop": {
        "desc": "增强版进程查看器（交互式）",
        "usage": "htop",
        "category": "进程管理",
        "examples": ["htop"],
        "flags": {},
    },
    "kill": {
        "desc": "向进程发送信号（默认终止进程）",
        "usage": "kill [-signal] PID",
        "category": "进程管理",
        "examples": ["kill 1234", "kill -9 1234", "kill -SIGTERM 1234"],
        "flags": {
            "-9": "强制终止（SIGKILL）",
            "-15": "正常终止（SIGTERM）",
            "-l": "列出所有信号",
        },
    },
    "killall": {
        "desc": "按名称终止所有匹配的进程",
        "usage": "killall process_name",
        "category": "进程管理",
        "examples": ["killall firefox", "killall -9 node"],
        "flags": {
            "-9": "强制终止",
        },
    },
    "pkill": {
        "desc": "按名称模式终止进程",
        "usage": "pkill [-signal] pattern",
        "category": "进程管理",
        "examples": ["pkill -f 'python server'"],
        "flags": {
            "-f": "匹配完整命令行",
        },
    },
    "pgrep": {
        "desc": "按名称模式查找进程PID",
        "usage": "pgrep pattern",
        "category": "进程管理",
        "examples": ["pgrep python", "pgrep -l node"],
        "flags": {
            "-l": "同时显示进程名",
            "-f": "匹配完整命令行",
        },
    },
    "bg": {
        "desc": "将挂起的任务放到后台运行",
        "usage": "bg [job_id]",
        "category": "进程管理",
        "examples": ["bg %1"],
        "flags": {},
    },
    "fg": {
        "desc": "将后台任务切换到前台运行",
        "usage": "fg [job_id]",
        "category": "进程管理",
        "examples": ["fg %1"],
        "flags": {},
    },
    "jobs": {
        "desc": "显示当前终端的后台任务",
        "usage": "jobs",
        "category": "进程管理",
        "examples": ["jobs", "jobs -l"],
        "flags": {
            "-l": "显示PID",
        },
    },
    "nohup": {
        "desc": "使命令在退出终端后继续运行",
        "usage": "nohup command &",
        "category": "进程管理",
        "examples": ["nohup python server.py &"],
        "flags": {},
    },
    "nice": {
        "desc": "以指定优先级运行命令",
        "usage": "nice [-n priority] command",
        "category": "进程管理",
        "examples": ["nice -n 10 make build"],
        "flags": {
            "-n": "优先级值（-20到19）",
        },
    },
    "renice": {
        "desc": "修改正在运行的进程的优先级",
        "usage": "renice priority -p PID",
        "category": "进程管理",
        "examples": ["renice 10 -p 1234"],
        "flags": {},
    },
    "wait": {
        "desc": "等待后台进程完成",
        "usage": "wait [PID]",
        "category": "进程管理",
        "examples": ["wait", "wait 1234"],
        "flags": {},
    },
    "lsof": {
        "desc": "列出打开的文件和网络连接",
        "usage": "lsof [options]",
        "category": "进程管理",
        "examples": ["lsof -i :8080", "lsof -p 1234", "lsof +D /tmp"],
        "flags": {
            "-i": "按网络连接过滤",
            "-p": "按进程PID过滤",
            "+D": "按目录过滤",
        },
    },
    "strace": {
        "desc": "跟踪进程的系统调用",
        "usage": "strace [-p PID | command]",
        "category": "进程管理",
        "examples": ["strace ls", "strace -p 1234"],
        "flags": {
            "-p": "附加到运行中的进程",
            "-e": "过滤特定调用",
        },
    },
    "time": {
        "desc": "测量命令的执行时间",
        "usage": "time command",
        "category": "进程管理",
        "examples": ["time python script.py", "time make build"],
        "flags": {},
    },
    "timeout": {
        "desc": "限制命令的最大执行时间",
        "usage": "timeout duration command",
        "category": "进程管理",
        "examples": ["timeout 30s curl https://example.com"],
        "flags": {},
    },
    "watch": {
        "desc": "定期重复执行命令并显示结果",
        "usage": "watch [-n seconds] command",
        "category": "进程管理",
        "examples": ["watch -n 2 'df -h'", "watch 'ls -la'"],
        "flags": {
            "-n": "执行间隔秒数",
            "-d": "高亮变化部分",
        },
    },
    "screen": {
        "desc": "终端多路复用器（会话管理）",
        "usage": "screen [options]",
        "category": "进程管理",
        "examples": ["screen", "screen -r", "screen -ls"],
        "flags": {
            "-r": "恢复会话",
            "-ls": "列出所有会话",
            "-S": "指定会话名称",
        },
    },
    "tmux": {
        "desc": "现代终端多路复用器",
        "usage": "tmux [command]",
        "category": "进程管理",
        "examples": ["tmux", "tmux new -s mysession", "tmux attach -t mysession"],
        "flags": {},
    },

    # ============================================================
    # System Information
    # ============================================================
    "uname": {
        "desc": "显示系统信息",
        "usage": "uname [-a]",
        "category": "系统信息",
        "examples": ["uname -a", "uname -r"],
        "flags": {
            "-a": "显示所有信息",
            "-r": "内核版本号",
            "-s": "操作系统名称",
            "-m": "硬件架构",
        },
    },
    "hostname": {
        "desc": "显示或设置系统主机名",
        "usage": "hostname",
        "category": "系统信息",
        "examples": ["hostname", "hostname -I"],
        "flags": {
            "-I": "显示所有IP地址",
        },
    },
    "whoami": {
        "desc": "显示当前登录的用户名",
        "usage": "whoami",
        "category": "系统信息",
        "examples": ["whoami"],
        "flags": {},
    },
    "who": {
        "desc": "显示当前登录的所有用户",
        "usage": "who",
        "category": "系统信息",
        "examples": ["who"],
        "flags": {},
    },
    "w": {
        "desc": "显示当前登录用户及其活动",
        "usage": "w",
        "category": "系统信息",
        "examples": ["w"],
        "flags": {},
    },
    "id": {
        "desc": "显示用户的 UID、GID 和所属组",
        "usage": "id [username]",
        "category": "系统信息",
        "examples": ["id", "id root"],
        "flags": {},
    },
    "uptime": {
        "desc": "显示系统运行时间和负载",
        "usage": "uptime",
        "category": "系统信息",
        "examples": ["uptime"],
        "flags": {},
    },
    "date": {
        "desc": "显示或设置系统日期和时间",
        "usage": "date [+format]",
        "category": "系统信息",
        "examples": ["date", "date +%Y-%m-%d", "date '+%H:%M:%S'"],
        "flags": {},
    },
    "cal": {
        "desc": "显示日历",
        "usage": "cal [month] [year]",
        "category": "系统信息",
        "examples": ["cal", "cal 2025", "cal 3 2025"],
        "flags": {},
    },
    "env": {
        "desc": "显示当前环境变量",
        "usage": "env",
        "category": "系统信息",
        "examples": ["env", "env | grep PATH"],
        "flags": {},
    },
    "printenv": {
        "desc": "打印指定或所有环境变量",
        "usage": "printenv [variable]",
        "category": "系统信息",
        "examples": ["printenv HOME", "printenv"],
        "flags": {},
    },
    "export": {
        "desc": "设置环境变量",
        "usage": "export VAR=value",
        "category": "系统信息",
        "examples": ["export PATH=$PATH:/usr/local/bin", "export LANG=en_US.UTF-8"],
        "flags": {},
    },
    "echo": {
        "desc": "输出文本到终端",
        "usage": "echo [options] text",
        "category": "系统信息",
        "examples": ["echo 'Hello World'", "echo $HOME", "echo -n 'no newline'"],
        "flags": {
            "-n": "不输出末尾换行符",
            "-e": "启用转义字符解析",
        },
    },
    "printf": {
        "desc": "格式化输出文本",
        "usage": "printf format [arguments]",
        "category": "系统信息",
        "examples": ["printf '%s\\n' hello", "printf '%-10s %5d\\n' name 42"],
        "flags": {},
    },
    "alias": {
        "desc": "创建命令别名",
        "usage": "alias name='command'",
        "category": "系统信息",
        "examples": ["alias ll='ls -la'", "alias gs='git status'"],
        "flags": {},
    },
    "unalias": {
        "desc": "删除命令别名",
        "usage": "unalias name",
        "category": "系统信息",
        "examples": ["unalias ll"],
        "flags": {},
    },
    "history": {
        "desc": "显示命令历史记录",
        "usage": "history [n]",
        "category": "系统信息",
        "examples": ["history", "history 20", "history | grep ssh"],
        "flags": {},
    },
    "man": {
        "desc": "查看命令的手册页",
        "usage": "man command",
        "category": "系统信息",
        "examples": ["man ls", "man grep"],
        "flags": {},
    },
    "info": {
        "desc": "查看命令的 info 文档",
        "usage": "info command",
        "category": "系统信息",
        "examples": ["info coreutils"],
        "flags": {},
    },
    "whatis": {
        "desc": "显示命令的简短描述",
        "usage": "whatis command",
        "category": "系统信息",
        "examples": ["whatis ls"],
        "flags": {},
    },
    "apropos": {
        "desc": "按关键字搜索命令手册",
        "usage": "apropos keyword",
        "category": "系统信息",
        "examples": ["apropos compress"],
        "flags": {},
    },

    # ============================================================
    # Disk & Storage
    # ============================================================
    "df": {
        "desc": "显示磁盘空间使用情况",
        "usage": "df [-h]",
        "category": "磁盘存储",
        "examples": ["df -h", "df -hT"],
        "flags": {
            "-h": "人类可读格式",
            "-T": "显示文件系统类型",
            "-i": "显示 inode 使用情况",
        },
    },
    "du": {
        "desc": "统计文件/目录的磁盘占用空间",
        "usage": "du [-sh] [path]",
        "category": "磁盘存储",
        "examples": ["du -sh *", "du -h --max-depth=1", "du -sh /var/log"],
        "flags": {
            "-s": "只显示总计",
            "-h": "人类可读格式",
            "--max-depth": "限制显示深度",
        },
    },
    "mount": {
        "desc": "挂载文件系统",
        "usage": "mount device mount_point",
        "category": "磁盘存储",
        "examples": ["mount", "mount /dev/sdb1 /mnt/usb"],
        "flags": {},
    },
    "umount": {
        "desc": "卸载文件系统",
        "usage": "umount mount_point",
        "category": "磁盘存储",
        "examples": ["umount /mnt/usb"],
        "flags": {},
    },
    "fdisk": {
        "desc": "磁盘分区管理工具",
        "usage": "fdisk [options] device",
        "category": "磁盘存储",
        "examples": ["fdisk -l"],
        "flags": {
            "-l": "列出所有分区",
        },
    },
    "lsblk": {
        "desc": "列出所有块设备（磁盘/分区）",
        "usage": "lsblk",
        "category": "磁盘存储",
        "examples": ["lsblk", "lsblk -f"],
        "flags": {
            "-f": "显示文件系统信息",
        },
    },
    "blkid": {
        "desc": "显示块设备的 UUID 和类型",
        "usage": "blkid",
        "category": "磁盘存储",
        "examples": ["blkid"],
        "flags": {},
    },
    "free": {
        "desc": "显示系统内存使用情况",
        "usage": "free [-h]",
        "category": "磁盘存储",
        "examples": ["free -h", "free -m"],
        "flags": {
            "-h": "人类可读格式",
            "-m": "以MB为单位",
            "-g": "以GB为单位",
        },
    },
    "sync": {
        "desc": "将缓冲区数据写入磁盘",
        "usage": "sync",
        "category": "磁盘存储",
        "examples": ["sync"],
        "flags": {},
    },

    # ============================================================
    # Compression & Archives
    # ============================================================
    "tar": {
        "desc": "归档和压缩文件（打包/解包）",
        "usage": "tar [options] [archive] [files]",
        "category": "压缩归档",
        "examples": [
            "tar -czf archive.tar.gz dir/",
            "tar -xzf archive.tar.gz",
            "tar -tf archive.tar.gz",
        ],
        "flags": {
            "-c": "创建归档",
            "-x": "解压归档",
            "-z": "使用gzip压缩",
            "-j": "使用bzip2压缩",
            "-f": "指定归档文件名",
            "-v": "显示详细过程",
            "-t": "列出归档内容",
        },
    },
    "gzip": {
        "desc": "使用 gzip 压缩文件",
        "usage": "gzip [options] file",
        "category": "压缩归档",
        "examples": ["gzip file.txt", "gzip -d file.txt.gz"],
        "flags": {
            "-d": "解压",
            "-k": "保留原文件",
            "-9": "最高压缩率",
        },
    },
    "gunzip": {
        "desc": "解压 gzip 压缩文件",
        "usage": "gunzip file.gz",
        "category": "压缩归档",
        "examples": ["gunzip file.txt.gz"],
        "flags": {},
    },
    "bzip2": {
        "desc": "使用 bzip2 压缩文件（更高压缩比）",
        "usage": "bzip2 file",
        "category": "压缩归档",
        "examples": ["bzip2 file.txt", "bzip2 -d file.txt.bz2"],
        "flags": {
            "-d": "解压",
            "-k": "保留原文件",
        },
    },
    "xz": {
        "desc": "使用 xz 压缩文件（极高压缩比）",
        "usage": "xz file",
        "category": "压缩归档",
        "examples": ["xz file.txt", "xz -d file.txt.xz"],
        "flags": {
            "-d": "解压",
            "-k": "保留原文件",
        },
    },
    "zip": {
        "desc": "创建 zip 压缩包",
        "usage": "zip [options] archive.zip files",
        "category": "压缩归档",
        "examples": ["zip archive.zip file1.txt file2.txt", "zip -r archive.zip dir/"],
        "flags": {
            "-r": "递归压缩目录",
            "-e": "加密压缩",
        },
    },
    "unzip": {
        "desc": "解压 zip 压缩包",
        "usage": "unzip archive.zip [-d dest]",
        "category": "压缩归档",
        "examples": ["unzip archive.zip", "unzip archive.zip -d output/"],
        "flags": {
            "-d": "解压到指定目录",
            "-l": "列出内容不解压",
        },
    },
    "zcat": {
        "desc": "查看 gzip 压缩文件内容（无需解压）",
        "usage": "zcat file.gz",
        "category": "压缩归档",
        "examples": ["zcat file.txt.gz"],
        "flags": {},
    },
    "zgrep": {
        "desc": "在 gzip 压缩文件中搜索",
        "usage": "zgrep pattern file.gz",
        "category": "压缩归档",
        "examples": ["zgrep 'error' log.gz"],
        "flags": {},
    },

    # ============================================================
    # Network
    # ============================================================
    "ping": {
        "desc": "测试网络连通性",
        "usage": "ping [-c count] host",
        "category": "网络",
        "examples": ["ping google.com", "ping -c 4 192.168.1.1"],
        "flags": {
            "-c": "指定发送次数",
            "-i": "发送间隔秒数",
            "-t": "设置TTL值",
        },
    },
    "curl": {
        "desc": "命令行 HTTP 客户端（请求URL）",
        "usage": "curl [options] URL",
        "category": "网络",
        "examples": [
            "curl https://api.example.com",
            "curl -o file.zip URL",
            "curl -X POST -d 'data' URL",
        ],
        "flags": {
            "-o": "保存输出到文件",
            "-O": "以URL中文件名保存",
            "-X": "指定请求方法",
            "-d": "发送POST数据",
            "-H": "添加请求头",
            "-L": "跟随重定向",
            "-s": "静默模式",
            "-v": "详细输出",
            "-k": "忽略SSL证书",
        },
    },
    "wget": {
        "desc": "从网络下载文件",
        "usage": "wget [options] URL",
        "category": "网络",
        "examples": ["wget https://example.com/file.zip", "wget -c URL"],
        "flags": {
            "-c": "断点续传",
            "-O": "指定输出文件名",
            "-q": "静默模式",
            "-r": "递归下载",
        },
    },
    "ssh": {
        "desc": "安全远程登录（SSH协议）",
        "usage": "ssh [options] user@host",
        "category": "网络",
        "examples": [
            "ssh user@192.168.1.100",
            "ssh -p 2222 user@host",
            "ssh -i key.pem user@host",
        ],
        "flags": {
            "-p": "指定端口",
            "-i": "指定私钥文件",
            "-L": "本地端口转发",
            "-R": "远程端口转发",
            "-N": "不执行远程命令",
            "-v": "详细输出",
        },
    },
    "scp": {
        "desc": "通过SSH安全复制文件",
        "usage": "scp [options] source dest",
        "category": "网络",
        "examples": [
            "scp file.txt user@host:/tmp/",
            "scp user@host:/tmp/file.txt .",
            "scp -r dir/ user@host:/opt/",
        ],
        "flags": {
            "-r": "递归复制目录",
            "-P": "指定端口",
            "-i": "指定私钥文件",
        },
    },
    "rsync": {
        "desc": "高效文件同步和传输工具",
        "usage": "rsync [options] source dest",
        "category": "网络",
        "examples": [
            "rsync -avz dir/ user@host:/backup/",
            "rsync -avz --delete src/ dest/",
        ],
        "flags": {
            "-a": "归档模式（保留属性）",
            "-v": "详细输出",
            "-z": "传输时压缩",
            "--delete": "删除目标多余文件",
            "--progress": "显示传输进度",
            "-n": "模拟运行（不实际操作）",
        },
    },
    "sftp": {
        "desc": "安全FTP文件传输",
        "usage": "sftp user@host",
        "category": "网络",
        "examples": ["sftp user@host"],
        "flags": {},
    },
    "ifconfig": {
        "desc": "显示和配置网络接口",
        "usage": "ifconfig [interface]",
        "category": "网络",
        "examples": ["ifconfig", "ifconfig en0"],
        "flags": {},
    },
    "ip": {
        "desc": "现代网络配置工具（替代ifconfig）",
        "usage": "ip [options] object command",
        "category": "网络",
        "examples": ["ip addr", "ip route", "ip link show"],
        "flags": {},
    },
    "netstat": {
        "desc": "显示网络连接和端口状态",
        "usage": "netstat [options]",
        "category": "网络",
        "examples": ["netstat -tulnp", "netstat -an"],
        "flags": {
            "-t": "TCP连接",
            "-u": "UDP连接",
            "-l": "监听端口",
            "-n": "数字显示地址",
            "-p": "显示进程信息",
        },
    },
    "ss": {
        "desc": "显示套接字信息（替代netstat）",
        "usage": "ss [options]",
        "category": "网络",
        "examples": ["ss -tulnp", "ss -s"],
        "flags": {
            "-t": "TCP连接",
            "-u": "UDP连接",
            "-l": "监听端口",
            "-n": "数字显示",
            "-p": "显示进程",
        },
    },
    "dig": {
        "desc": "DNS 查询工具",
        "usage": "dig [options] domain",
        "category": "网络",
        "examples": ["dig google.com", "dig +short google.com", "dig MX gmail.com"],
        "flags": {
            "+short": "简洁输出",
        },
    },
    "nslookup": {
        "desc": "查询 DNS 域名解析",
        "usage": "nslookup domain",
        "category": "网络",
        "examples": ["nslookup google.com"],
        "flags": {},
    },
    "host": {
        "desc": "DNS 查找工具（简洁版）",
        "usage": "host domain",
        "category": "网络",
        "examples": ["host google.com"],
        "flags": {},
    },
    "traceroute": {
        "desc": "追踪数据包到目标的路由路径",
        "usage": "traceroute host",
        "category": "网络",
        "examples": ["traceroute google.com"],
        "flags": {},
    },
    "mtr": {
        "desc": "结合 ping 和 traceroute 的网络诊断工具",
        "usage": "mtr host",
        "category": "网络",
        "examples": ["mtr google.com"],
        "flags": {},
    },
    "nc": {
        "desc": "网络工具（TCP/UDP连接、端口扫描）",
        "usage": "nc [options] host port",
        "category": "网络",
        "examples": ["nc -zv host 80", "nc -l 8080"],
        "flags": {
            "-z": "扫描模式",
            "-v": "详细输出",
            "-l": "监听模式",
        },
    },
    "nmap": {
        "desc": "网络端口扫描和安全审计工具",
        "usage": "nmap [options] target",
        "category": "网络",
        "examples": ["nmap 192.168.1.1", "nmap -sV -p 1-1000 host"],
        "flags": {
            "-sV": "检测服务版本",
            "-p": "指定端口范围",
            "-sS": "SYN扫描",
        },
    },
    "arp": {
        "desc": "显示和管理 ARP 缓存表",
        "usage": "arp [-a]",
        "category": "网络",
        "examples": ["arp -a"],
        "flags": {
            "-a": "显示所有条目",
        },
    },
    "route": {
        "desc": "显示和管理路由表",
        "usage": "route [-n]",
        "category": "网络",
        "examples": ["route -n"],
        "flags": {
            "-n": "数字显示",
        },
    },
    "iptables": {
        "desc": "Linux 防火墙规则管理",
        "usage": "iptables [options]",
        "category": "网络",
        "examples": ["iptables -L", "iptables -A INPUT -p tcp --dport 80 -j ACCEPT"],
        "flags": {
            "-L": "列出规则",
            "-A": "添加规则",
            "-D": "删除规则",
        },
    },
    "tcpdump": {
        "desc": "网络数据包抓取和分析工具",
        "usage": "tcpdump [options]",
        "category": "网络",
        "examples": ["tcpdump -i eth0", "tcpdump port 80"],
        "flags": {
            "-i": "指定网络接口",
            "-n": "不解析主机名",
            "-w": "保存到文件",
        },
    },

    # ============================================================
    # Package Management
    # ============================================================
    "apt": {
        "desc": "Debian/Ubuntu 包管理器",
        "usage": "apt [command] [package]",
        "category": "包管理",
        "examples": [
            "apt update",
            "apt install package",
            "apt remove package",
            "apt search keyword",
        ],
        "flags": {
            "update": "更新包索引",
            "upgrade": "升级所有包",
            "install": "安装包",
            "remove": "卸载包",
            "search": "搜索包",
        },
    },
    "apt-get": {
        "desc": "Debian/Ubuntu 传统包管理器",
        "usage": "apt-get [command] [package]",
        "category": "包管理",
        "examples": ["apt-get update && apt-get upgrade"],
        "flags": {},
    },
    "dpkg": {
        "desc": "Debian 底层包管理工具",
        "usage": "dpkg [options] package.deb",
        "category": "包管理",
        "examples": ["dpkg -i package.deb", "dpkg -l"],
        "flags": {
            "-i": "安装包",
            "-l": "列出已安装的包",
            "-r": "卸载包",
        },
    },
    "yum": {
        "desc": "RHEL/CentOS 包管理器",
        "usage": "yum [command] [package]",
        "category": "包管理",
        "examples": ["yum install package", "yum update"],
        "flags": {},
    },
    "dnf": {
        "desc": "Fedora/RHEL8+ 包管理器",
        "usage": "dnf [command] [package]",
        "category": "包管理",
        "examples": ["dnf install package"],
        "flags": {},
    },
    "rpm": {
        "desc": "Red Hat 底层包管理工具",
        "usage": "rpm [options] package.rpm",
        "category": "包管理",
        "examples": ["rpm -ivh package.rpm", "rpm -qa"],
        "flags": {
            "-i": "安装",
            "-q": "查询",
            "-a": "所有已安装包",
        },
    },
    "pacman": {
        "desc": "Arch Linux 包管理器",
        "usage": "pacman [options] [package]",
        "category": "包管理",
        "examples": ["pacman -Syu", "pacman -S package"],
        "flags": {
            "-S": "安装包",
            "-Syu": "完整系统更新",
            "-R": "卸载包",
            "-Ss": "搜索包",
        },
    },
    "brew": {
        "desc": "macOS 包管理器 (Homebrew)",
        "usage": "brew [command] [package]",
        "category": "包管理",
        "examples": [
            "brew install package",
            "brew update",
            "brew search keyword",
            "brew list",
        ],
        "flags": {
            "install": "安装包",
            "uninstall": "卸载包",
            "update": "更新Homebrew",
            "upgrade": "升级已安装的包",
            "search": "搜索包",
            "list": "列出已安装的包",
        },
    },
    "snap": {
        "desc": "Ubuntu Snap 包管理器",
        "usage": "snap [command] [package]",
        "category": "包管理",
        "examples": ["snap install package", "snap list"],
        "flags": {},
    },
    "pip": {
        "desc": "Python 包管理器",
        "usage": "pip [command] [package]",
        "category": "包管理",
        "examples": ["pip install requests", "pip list", "pip freeze > requirements.txt"],
        "flags": {
            "install": "安装包",
            "uninstall": "卸载包",
            "list": "列出已安装包",
            "freeze": "输出依赖列表",
        },
    },
    "npm": {
        "desc": "Node.js 包管理器",
        "usage": "npm [command] [package]",
        "category": "包管理",
        "examples": ["npm install package", "npm run build", "npm init"],
        "flags": {
            "install": "安装包",
            "run": "运行脚本",
            "init": "初始化项目",
            "-g": "全局安装",
        },
    },
    "yarn": {
        "desc": "Node.js 替代包管理器",
        "usage": "yarn [command] [package]",
        "category": "包管理",
        "examples": ["yarn add package", "yarn install"],
        "flags": {},
    },
    "gem": {
        "desc": "Ruby 包管理器",
        "usage": "gem [command] [package]",
        "category": "包管理",
        "examples": ["gem install rails"],
        "flags": {},
    },
    "cargo": {
        "desc": "Rust 包管理器和构建工具",
        "usage": "cargo [command]",
        "category": "包管理",
        "examples": ["cargo build", "cargo run", "cargo test"],
        "flags": {},
    },
    "go": {
        "desc": "Go 语言工具链",
        "usage": "go [command]",
        "category": "包管理",
        "examples": ["go build", "go run main.go", "go mod init"],
        "flags": {},
    },

    # ============================================================
    # Git & Version Control
    # ============================================================
    "git": {
        "desc": "分布式版本控制系统",
        "usage": "git [command] [options]",
        "category": "版本控制",
        "examples": [
            "git clone URL",
            "git add .",
            "git commit -m 'message'",
            "git push",
            "git pull",
            "git status",
            "git log --oneline",
            "git branch",
            "git checkout -b feature",
            "git merge branch",
            "git diff",
            "git stash",
        ],
        "flags": {},
    },

    # ============================================================
    # Docker & Containers
    # ============================================================
    "docker": {
        "desc": "容器管理平台",
        "usage": "docker [command] [options]",
        "category": "容器",
        "examples": [
            "docker ps",
            "docker run -d -p 80:80 nginx",
            "docker build -t myapp .",
            "docker images",
            "docker stop container_id",
            "docker exec -it container bash",
            "docker logs container_id",
        ],
        "flags": {},
    },
    "docker-compose": {
        "desc": "Docker 多容器编排工具",
        "usage": "docker-compose [command]",
        "category": "容器",
        "examples": [
            "docker-compose up -d",
            "docker-compose down",
            "docker-compose logs",
        ],
        "flags": {},
    },
    "kubectl": {
        "desc": "Kubernetes 集群管理命令行工具",
        "usage": "kubectl [command] [type] [name]",
        "category": "容器",
        "examples": [
            "kubectl get pods",
            "kubectl apply -f deploy.yaml",
            "kubectl logs pod-name",
        ],
        "flags": {},
    },

    # ============================================================
    # Service & System Management
    # ============================================================
    "systemctl": {
        "desc": "systemd 系统和服务管理器",
        "usage": "systemctl [command] [service]",
        "category": "系统服务",
        "examples": [
            "systemctl status nginx",
            "systemctl start nginx",
            "systemctl enable nginx",
        ],
        "flags": {},
    },
    "service": {
        "desc": "传统系统服务管理",
        "usage": "service name [command]",
        "category": "系统服务",
        "examples": ["service nginx status", "service nginx restart"],
        "flags": {},
    },
    "journalctl": {
        "desc": "查看 systemd 日志",
        "usage": "journalctl [options]",
        "category": "系统服务",
        "examples": ["journalctl -u nginx", "journalctl -f", "journalctl --since today"],
        "flags": {
            "-u": "指定服务单元",
            "-f": "实时跟踪",
            "--since": "指定开始时间",
        },
    },
    "crontab": {
        "desc": "管理定时任务",
        "usage": "crontab [-e|-l|-r]",
        "category": "系统服务",
        "examples": ["crontab -l", "crontab -e"],
        "flags": {
            "-e": "编辑定时任务",
            "-l": "列出定时任务",
            "-r": "删除所有定时任务",
        },
    },
    "at": {
        "desc": "安排一次性定时任务",
        "usage": "at time",
        "category": "系统服务",
        "examples": ["echo 'backup.sh' | at 2am"],
        "flags": {},
    },
    "shutdown": {
        "desc": "关机或重启系统",
        "usage": "shutdown [options] [time]",
        "category": "系统服务",
        "examples": ["shutdown -h now", "shutdown -r now", "shutdown -h +10"],
        "flags": {
            "-h": "关机",
            "-r": "重启",
        },
    },
    "reboot": {
        "desc": "重启系统",
        "usage": "reboot",
        "category": "系统服务",
        "examples": ["reboot"],
        "flags": {},
    },
    "dmesg": {
        "desc": "显示内核消息缓冲区",
        "usage": "dmesg [options]",
        "category": "系统服务",
        "examples": ["dmesg", "dmesg | tail"],
        "flags": {},
    },

    # ============================================================
    # User Management
    # ============================================================
    "useradd": {
        "desc": "创建新用户",
        "usage": "useradd [options] username",
        "category": "用户管理",
        "examples": ["useradd -m newuser"],
        "flags": {
            "-m": "创建主目录",
            "-s": "指定shell",
            "-G": "指定附加组",
        },
    },
    "userdel": {
        "desc": "删除用户",
        "usage": "userdel [options] username",
        "category": "用户管理",
        "examples": ["userdel -r username"],
        "flags": {
            "-r": "同时删除主目录",
        },
    },
    "usermod": {
        "desc": "修改用户属性",
        "usage": "usermod [options] username",
        "category": "用户管理",
        "examples": ["usermod -aG docker username"],
        "flags": {
            "-aG": "添加到附加组",
            "-s": "修改shell",
        },
    },
    "passwd": {
        "desc": "修改用户密码",
        "usage": "passwd [username]",
        "category": "用户管理",
        "examples": ["passwd", "passwd username"],
        "flags": {},
    },
    "groupadd": {
        "desc": "创建新用户组",
        "usage": "groupadd groupname",
        "category": "用户管理",
        "examples": ["groupadd developers"],
        "flags": {},
    },
    "groups": {
        "desc": "显示用户所属的组",
        "usage": "groups [username]",
        "category": "用户管理",
        "examples": ["groups", "groups root"],
        "flags": {},
    },

    # ============================================================
    # Security & Encryption
    # ============================================================
    "ssh-keygen": {
        "desc": "生成 SSH 密钥对",
        "usage": "ssh-keygen [options]",
        "category": "安全",
        "examples": ["ssh-keygen -t ed25519", "ssh-keygen -t rsa -b 4096"],
        "flags": {
            "-t": "密钥类型",
            "-b": "密钥长度",
            "-f": "输出文件",
        },
    },
    "ssh-copy-id": {
        "desc": "将SSH公钥复制到远程主机",
        "usage": "ssh-copy-id user@host",
        "category": "安全",
        "examples": ["ssh-copy-id user@192.168.1.100"],
        "flags": {},
    },
    "gpg": {
        "desc": "GnuPG 加密和签名工具",
        "usage": "gpg [options] file",
        "category": "安全",
        "examples": ["gpg -c file.txt", "gpg -d file.txt.gpg"],
        "flags": {
            "-c": "对称加密",
            "-d": "解密",
        },
    },
    "openssl": {
        "desc": "SSL/TLS 工具包",
        "usage": "openssl [command] [options]",
        "category": "安全",
        "examples": [
            "openssl rand -base64 32",
            "openssl s_client -connect host:443",
        ],
        "flags": {},
    },
    "md5sum": {
        "desc": "计算文件的 MD5 哈希值",
        "usage": "md5sum file",
        "category": "安全",
        "examples": ["md5sum file.iso"],
        "flags": {},
    },
    "sha256sum": {
        "desc": "计算文件的 SHA-256 哈希值",
        "usage": "sha256sum file",
        "category": "安全",
        "examples": ["sha256sum file.iso"],
        "flags": {},
    },
    "shasum": {
        "desc": "计算文件的 SHA 哈希值（macOS）",
        "usage": "shasum [-a algorithm] file",
        "category": "安全",
        "examples": ["shasum -a 256 file.iso"],
        "flags": {
            "-a": "哈希算法（1, 256, 512）",
        },
    },

    # ============================================================
    # Misc / Utility
    # ============================================================
    "clear": {
        "desc": "清空终端屏幕",
        "usage": "clear",
        "category": "实用工具",
        "examples": ["clear"],
        "flags": {},
    },
    "reset": {
        "desc": "重置终端设置",
        "usage": "reset",
        "category": "实用工具",
        "examples": ["reset"],
        "flags": {},
    },
    "sleep": {
        "desc": "暂停指定秒数",
        "usage": "sleep seconds",
        "category": "实用工具",
        "examples": ["sleep 5", "sleep 0.5"],
        "flags": {},
    },
    "yes": {
        "desc": "重复输出字符串（默认 y）",
        "usage": "yes [string]",
        "category": "实用工具",
        "examples": ["yes | apt install package"],
        "flags": {},
    },
    "true": {
        "desc": "返回成功状态码 (0)",
        "usage": "true",
        "category": "实用工具",
        "examples": ["true"],
        "flags": {},
    },
    "false": {
        "desc": "返回失败状态码 (1)",
        "usage": "false",
        "category": "实用工具",
        "examples": ["false"],
        "flags": {},
    },
    "seq": {
        "desc": "生成数字序列",
        "usage": "seq [first] [increment] last",
        "category": "实用工具",
        "examples": ["seq 1 10", "seq 0 2 20"],
        "flags": {},
    },
    "shuf": {
        "desc": "随机打乱输入行",
        "usage": "shuf [file]",
        "category": "实用工具",
        "examples": ["shuf -n 1 names.txt"],
        "flags": {
            "-n": "输出N行",
        },
    },
    "mktemp": {
        "desc": "创建唯一的临时文件或目录",
        "usage": "mktemp [-d] [template]",
        "category": "实用工具",
        "examples": ["mktemp", "mktemp -d"],
        "flags": {
            "-d": "创建目录",
        },
    },
    "tput": {
        "desc": "控制终端属性（颜色、光标等）",
        "usage": "tput [capability]",
        "category": "实用工具",
        "examples": ["tput cols", "tput lines"],
        "flags": {},
    },
    "source": {
        "desc": "在当前shell中执行脚本",
        "usage": "source file",
        "category": "实用工具",
        "examples": ["source ~/.bashrc", "source .env"],
        "flags": {},
    },
    "eval": {
        "desc": "执行字符串作为命令",
        "usage": "eval command_string",
        "category": "实用工具",
        "examples": ["eval $(ssh-agent)"],
        "flags": {},
    },
    "xdg-open": {
        "desc": "用默认应用打开文件/URL（Linux）",
        "usage": "xdg-open file_or_url",
        "category": "实用工具",
        "examples": ["xdg-open https://google.com", "xdg-open photo.jpg"],
        "flags": {},
    },
    "open": {
        "desc": "用默认应用打开文件/URL（macOS）",
        "usage": "open file_or_url",
        "category": "实用工具",
        "examples": ["open https://google.com", "open -a Safari", "open ."],
        "flags": {
            "-a": "指定应用程序",
        },
    },
    "pbcopy": {
        "desc": "将标准输入复制到剪贴板（macOS）",
        "usage": "command | pbcopy",
        "category": "实用工具",
        "examples": ["echo 'hello' | pbcopy", "cat file.txt | pbcopy"],
        "flags": {},
    },
    "pbpaste": {
        "desc": "将剪贴板内容输出到标准输出（macOS）",
        "usage": "pbpaste",
        "category": "实用工具",
        "examples": ["pbpaste", "pbpaste > file.txt"],
        "flags": {},
    },
    "xclip": {
        "desc": "剪贴板操作工具（Linux）",
        "usage": "xclip [options]",
        "category": "实用工具",
        "examples": ["echo 'text' | xclip -selection clipboard"],
        "flags": {
            "-selection": "指定剪贴板类型",
        },
    },
}
