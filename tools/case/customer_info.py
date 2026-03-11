#!/usr/bin/env python3
"""
客户信息采集表 - 标准化收集客户案例信息
用法：python3 tools/case/customer_info.py
"""

import argparse
import json
import os
from datetime import datetime

DATA_DIR = os.path.expanduser("~/.openclaw/data/cases")

TEMPLATE = {
    "客户基本信息": {
        "客户名称": "",
        "所属行业": "",
        "企业规模": "（人数/营收）",
        "地理位置": "",
        "联系人及职位": "",
        "联系方式": "",
    },
    "业务背景": {
        "主营业务": "",
        "市场地位": "（行业排名/市场份额）",
        "目标客户群": "",
        "竞争优势": "",
    },
    "痛点与挑战": {
        "核心痛点 1": "",
        "核心痛点 2": "",
        "核心痛点 3": "",
        "痛点影响": "（不解决的后果）",
        "之前尝试过的方案": "",
    },
    "解决方案": {
        "选用产品/服务": "",
        "部署场景": "",
        "使用时长": "",
        "关键功能": "",
        "实施周期": "",
    },
    "成果与价值": {
        "量化指标 1": "（如：效率提升 xx%）",
        "量化指标 2": "（如：成本降低 xx%）",
        "量化指标 3": "（如：收入增长 xx%）",
        "定性收益": "（如：客户满意度提升）",
        "未来规划": "",
    },
    "客户证言": {
        "推荐人姓名": "",
        "推荐人职位": "",
        "证言内容": "",
        "是否可公开": "是/否",
    },
    "传播授权": {
        "是否同意案例传播": "是/否",
        "可传播渠道": "官网/公众号/媒体/全部",
        "是否需要审核": "是/否",
        "限制说明": "",
    },
}

def create_info_form(customer_name=""):
    """创建信息采集表"""
    form = {
        "customer_name": customer_name,
        "created_at": datetime.now().isoformat(),
        "fields": TEMPLATE
    }
    return form

def print_form(form):
    """打印表单"""
    print("\n" + "=" * 70)
    print(f"📋 客户信息采集表 - {form.get('customer_name', '未命名')}")
    print("=" * 70)

    for section, fields in form["fields"].items():
        print(f"\n{section}")
        print("-" * 50)
        for field, placeholder in fields.items():
            if placeholder:
                print(f"  ☐ {field}: {placeholder}")
            else:
                print(f"  ☐ {field}")

    print("\n" + "=" * 70)
    print(f"* 创建时间：{form['created_at']}")
    print(f"* 填写说明：请尽量提供具体数据和事实描述")
    print("=" * 70 + "\n")

def export_markdown(form, output_file):
    """导出为 Markdown"""
    md = [f"# 客户信息采集表 - {form.get('customer_name', '未命名')}\n"]
    md.append(f"\n*创建时间：{form['created_at']}*\n")

    for section, fields in form["fields"].items():
        md.append(f"\n## {section}\n")
        md.append("| 项目 | 内容 |")
        md.append("|------|------|")
        for field, placeholder in fields.items():
            md.append(f"| {field} | {placeholder} |")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='客户信息采集表')
    parser.add_argument('-n', '--name', default='新客户', help='客户名称')
    parser.add_argument('-o', '--output', help='输出文件路径')
    parser.add_argument('--json', action='store_true', help='导出为 JSON')

    args = parser.parse_args()

    form = create_info_form(args.name)
    print_form(form)

    if args.output:
        os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
        if args.json:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(form, f, indent=2, ensure_ascii=False)
        else:
            export_markdown(form, args.output)
        print(f"✅ 已保存到：{args.output}")
