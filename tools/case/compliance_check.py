#!/usr/bin/env python3
"""
合规检查器 - 检查敏感词、数据脱敏
用法：python3 tools/case/compliance_check.py <文件>
"""

import argparse
import re
import os

# 敏感词库（示例，实际使用需完善）
SENSITIVE_WORDS = [
    "第一", "唯一", "最强", "顶级", "国家级", "国际领先",
    "垄断", "独占", "绝对", "100%",
    "机密", "秘密", "内部", "保密",
]

# 需要脱敏的数据模式
PATTERNS = {
    "手机号": r"1[3-9]\d{9}",
    "邮箱": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "身份证": r"\d{17}[\dXx]",
    "银行卡": r"\d{16,19}",
    "IP 地址": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
}

def check_compliance(text):
    """检查合规性"""
    results = {
        "sensitive_words": [],
        "data_leaks": [],
        "suggestions": []
    }

    # 检查敏感词
    for word in SENSITIVE_WORDS:
        if word in text:
            results["sensitive_words"].append(word)

    # 检查数据泄露
    for name, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            results["data_leaks"].append({"type": name, "matches": matches})

    # 生成建议
    if results["sensitive_words"]:
        results["suggestions"].append("⚠️ 发现广告法敏感词，建议修改")
    if results["data_leaks"]:
        results["suggestions"].append("⚠️ 发现可能敏感的数据，请确认是否可公开")

    return results

def mask_data(text):
    """数据脱敏"""
    # 手机号脱敏
    text = re.sub(r"1[3-9]\d{7}(\d{4})", r"1***\1", text)
    # 邮箱脱敏
    text = re.sub(r"([A-Za-z])[\w.-]*@([\w.-]+\.[A-Za-z]{2,})", r"\1***@\2", text)
    # 身份证脱敏
    text = re.sub(r"(\d{6})\d{8}(\d{4})", r"\1********\2", text)
    return text

def print_report(results, file_name=""):
    """打印报告"""
    print("\n" + "=" * 70)
    print(f"✅ 合规检查报告 - {file_name or '输入内容'}")
    print("=" * 70)

    if not results["sensitive_words"] and not results["data_leaks"]:
        print("\n🎉 未发现合规问题，可以发布！\n")
    else:
        if results["sensitive_words"]:
            print(f"\n⚠️  敏感词 ({len(results['sensitive_words'])} 个):")
            for word in results["sensitive_words"]:
                print(f"   • {word}")

        if results["data_leaks"]:
            print(f"\n⚠️  敏感数据 ({len(results['data_leaks'])} 类):")
            for item in results["data_leaks"]:
                print(f"   • {item['type']}: {len(item['matches'])} 处")

        if results["suggestions"]:
            print(f"\n💡 建议:")
            for s in results["suggestions"]:
                print(f"   {s}")

    print("\n" + "=" * 70 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='合规检查器')
    parser.add_argument('file', nargs='?', help='要检查的文件')
    parser.add_argument('-t', '--text', help='要检查的文本')
    parser.add_argument('-m', '--mask', action='store_true', help='自动脱敏')
    parser.add_argument('-o', '--output', help='输出脱敏后的文件')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("请输入要检查的内容 (输入空行结束):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        text = "\n".join(lines)

    results = check_compliance(text)
    print_report(results, args.file or "输入内容")

    if args.mask:
        masked = mask_data(text)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(masked)
            print(f"✅ 脱敏内容已保存到：{args.output}")
        else:
            print("\n📝 脱敏后内容:\n")
            print(masked)
