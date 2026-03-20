#!/bin/bash
# ─────────────────────────────────────────
# CmdHint 安装脚本
# ─────────────────────────────────────────

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  CmdHint - 命令动态提示工具 安装器  ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════╝${NC}"
echo ""

# 检查 Python
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo -e "${RED}错误: 未找到 Python，请先安装 Python 3.8+${NC}"
    exit 1
fi

echo -e "${YELLOW}使用 Python: $($PYTHON --version)${NC}"

# 安装依赖
echo -e "\n${GREEN}[1/2] 安装依赖 prompt_toolkit ...${NC}"
$PYTHON -m pip install prompt_toolkit>=3.0.0 --quiet

# 安装工具
echo -e "${GREEN}[2/2] 安装 CmdHint ...${NC}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
$PYTHON -m pip install -e "$SCRIPT_DIR" --quiet 2>/dev/null || {
    echo -e "${YELLOW}pip install -e 失败，使用直接运行方式...${NC}"
    
    # 创建启动脚本
    LAUNCH_SCRIPT="$HOME/.local/bin/cmdhint"
    mkdir -p "$HOME/.local/bin"
    cat > "$LAUNCH_SCRIPT" << LAUNCH_EOF
#!/bin/bash
$PYTHON "$SCRIPT_DIR/cmdhint.py"
LAUNCH_EOF
    chmod +x "$LAUNCH_SCRIPT"
    
    # 提示 PATH
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo -e "\n${YELLOW}提示: 请将 ~/.local/bin 加入 PATH:${NC}"
        echo -e "  ${CYAN}echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.zshrc${NC}"
        echo -e "  ${CYAN}source ~/.zshrc${NC}"
    fi
}

echo ""
echo -e "${GREEN}✅ 安装完成！${NC}"
echo ""
echo -e "  使用方法:"
echo -e "    ${CYAN}cmdhint${NC}                   启动交互式提示"
echo -e "    ${CYAN}python3 $(dirname "$0")/cmdhint.py${NC}   直接运行"
echo ""
