#!/usr/bin/env python3
"""
多版本生成器 - 一份内容多场景复用
用法：python3 tools/case/multi_version.py <案例文件>
"""

import argparse
import re

def extract_sections(content):
    """提取案例各部分"""
    sections = {}
    current_section = "title"
    current_content = []

    for line in content.split('\n'):
        if line.startswith('# '):
            sections['title'] = line[2:].strip()
        elif line.startswith('## '):
            if current_section != "title":
                sections[current_section] = '\n'.join(current_content)
            current_section = line[3:].strip()
            current_content = []
        else:
            current_content.append(line)

    if current_content:
        sections[current_section] = '\n'.join(current_content)

    return sections

def generate_versions(sections):
    """生成各版本"""
    versions = {}

    # 公众号版本
    versions["公众号"] = f"""
# {sections.get('title', '客户案例')}

{sections.get('面临的挑战', '')}

{sections.get('解决方案', '')}

{sections.get('成果与价值', '')}

{sections.get('客户证言', '')}

---
💡 点击了解更多
"""

    # 官网版本
    versions["官网"] = f"""
{sections.get('title', '客户案例')}

## 客户概况
{sections.get('客户概况', '')}

## 挑战与方案
{sections.get('面临的挑战', '')}
{sections.get('解决方案', '')}

## 成果展示
{sections.get('成果与价值', '')}

{sections.get('客户证言', '')}
"""

    # 销售版（内部）
    versions["销售版"] = f"""
【内部参考】{sections.get('title', '客户案例')}

🎯 客户画像
{sections.get('客户概况', '')}

💡 核心痛点
{sections.get('面临的挑战', '')}

✅ 解决方案亮点
{sections.get('解决方案', '')}

📊 可量化成果
{sections.get('成果与价值', '')}

💬 客户原话
{sections.get('客户证言', '')}

📌 销售话术建议
- 强调客户行业地位
- 突出量化成果
- 使用客户证言
"""

    # 社交媒体版
    versions["社交媒体"] = f"""
🎯 {sections.get('title', '客户案例')}

📊 核心数字
{sections.get('成果与价值', '成果显著')[:200]}

💬 "{sections.get('客户证言', '客户高度认可')[:100]}"

#客户案例 #成功案例
"""

    # 一图流版
    versions["一图流"] = f"""
【{sections.get('title', '客户案例')}】

3 个关键词：
• 关键词 1
• 关键词 2
• 关键词 3

核心成果：
• 成果 1
• 成果 2
• 成果 3

客户说：
"{sections.get('客户证言', '')[:50]}..."
"""

    return versions

def print_versions(versions):
    """打印各版本"""
    for name, content in versions.items():
        print(f"\n{'='*70}")
        print(f"📱 {name} 版本")
        print('='*70)
        print(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='多版本生成器')
    parser.add_argument('file', help='案例 Markdown 文件')
    parser.add_argument('-v', '--version', choices=['公众号', '官网', '销售版', '社交媒体', '一图流', '全部'],
                       default='全部', help='输出版本')
    parser.add_argument('-o', '--output', help='输出目录')

    args = parser.parse_args()

    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = extract_sections(content)
    all_versions = generate_versions(sections)

    if args.version == '全部':
        print_versions(all_versions)
    else:
        print(f"\n📱 {args.version} 版本\n")
        print('='*70)
        print(all_versions[args.version])

    if args.output:
        import os
        os.makedirs(args.output, exist_ok=True)
        if args.version == '全部':
            for name, content in all_versions.items():
                path = os.path.join(args.output, f"{name}.md")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ 已保存：{path}")
        else:
            path = os.path.join(args.output, f"{args.version}.md")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(all_versions[args.version])
            print(f"✅ 已保存：{path}")
