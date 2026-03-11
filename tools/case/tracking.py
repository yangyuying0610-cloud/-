#!/usr/bin/env python3
"""
传播效果追踪器 - 追踪案例传播数据
用法：python3 tools/case/tracking.py
"""

import argparse
import json
import os
from datetime import datetime

DATA_FILE = os.path.expanduser("~/.openclaw/data/case_tracking.json")

def load_data():
    """加载数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"cases": []}

def save_data(data):
    """保存数据"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_case(name, customer=""):
    """添加案例"""
    data = load_data()
    case = {
        "name": name,
        "customer": customer,
        "created_at": datetime.now().isoformat(),
        "channels": []
    }
    data["cases"].append(case)
    save_data(data)
    print(f"✅ 添加案例：{name}")
    return case

def add_channel(case_name, channel, url="", metrics=None):
    """添加渠道数据"""
    data = load_data()
    for case in data["cases"]:
        if case["name"] == case_name:
            case["channels"].append({
                "channel": channel,
                "url": url,
                "published_at": datetime.now().isoformat(),
                "metrics": metrics or {}
            })
            save_data(data)
            print(f"✅ 添加渠道：{channel}")
            return
    print(f"❌ 未找到案例：{case_name}")

def update_metrics(case_name, channel, metrics):
    """更新数据"""
    data = load_data()
    for case in data["cases"]:
        if case["name"] == case_name:
            for c in case["channels"]:
                if c["channel"] == channel:
                    c["metrics"].update(metrics)
                    c["updated_at"] = datetime.now().isoformat()
                    save_data(data)
                    print(f"✅ 更新数据：{channel}")
                    return
    print(f"❌ 未找到：{case_name} - {channel}")

def list_cases():
    """列出案例"""
    data = load_data()

    print("\n" + "=" * 70)
    print("📊 案例传播效果追踪")
    print("=" * 70)

    for case in data["cases"]:
        print(f"\n📁 {case['name']} ({case.get('customer', '')})")
        print(f"   创建时间：{case['created_at'][:10]}")

        total_views = 0
        total_engagement = 0

        for c in case.get("channels", []):
            m = c.get("metrics", {})
            views = m.get("views", 0)
            engagement = m.get("likes", 0) + m.get("shares", 0) + m.get("comments", 0)

            total_views += views
            total_engagement += engagement

            print(f"   • {c['channel']}: 👁 {views:,} | 👍 {engagement:,}")

        if case.get("channels"):
            print(f"   📊 合计：👁 {total_views:,} | 👍 {total_engagement:,}")

    print("\n" + "=" * 70)
    print(f"共 {len(data['cases'])} 个案例")
    print("=" * 70 + "\n")

def export_report():
    """导出报告"""
    data = load_data()

    print("\n" + "=" * 70)
    print("📈 案例传播效果报告")
    print("=" * 70)

    total_cases = len(data["cases"])
    total_channels = sum(len(c.get("channels", [])) for c in data["cases"])
    total_views = 0
    total_engagement = 0

    for case in data["cases"]:
        for c in case.get("channels", []):
            m = c.get("metrics", {})
            total_views += m.get("views", 0)
            total_engagement += m.get("likes", 0) + m.get("shares", 0) + m.get("comments", 0)

    print(f"\n📊 总览")
    print(f"   案例数：{total_cases}")
    print(f"   渠道数：{total_channels}")
    print(f"   总阅读：{total_views:,}")
    print(f"   总互动：{total_engagement:,}")

    print("\n📁 案例详情")
    print("-" * 70)

    # 按效果排序
    cases_with_data = []
    for case in data["cases"]:
        views = sum(c.get("metrics", {}).get("views", 0) for c in case.get("channels", []))
        engagement = sum(
            c.get("metrics", {}).get("likes", 0) +
            c.get("metrics", {}).get("shares", 0) +
            c.get("metrics", {}).get("comments", 0)
            for c in case.get("channels", [])
        )
        cases_with_data.append((case, views, engagement))

    cases_with_data.sort(key=lambda x: x[1] + x[2], reverse=True)

    for case, views, engagement in cases_with_data:
        print(f"\n{case['name']}")
        print(f"   阅读：{views:,} | 互动：{engagement:,}")

    print("\n" + "=" * 70 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='传播效果追踪器')
    subparsers = parser.add_subparsers(dest='command', help='命令')

    # 添加案例
    p_add = subparsers.add_parser('add', help='添加案例')
    p_add.add_argument('name', help='案例名称')
    p_add.add_argument('-c', '--customer', help='客户名称')

    # 添加渠道
    p_ch = subparsers.add_parser('channel', help='添加渠道')
    p_ch.add_argument('case', help='案例名称')
    p_ch.add_argument('channel', help='渠道名称')
    p_ch.add_argument('-u', '--url', help='链接')

    # 更新数据
    p_up = subparsers.add_parser('update', help='更新数据')
    p_up.add_argument('case', help='案例名称')
    p_up.add_argument('channel', help='渠道名称')
    p_up.add_argument('-v', '--views', type=int, help='阅读量')
    p_up.add_argument('-l', '--likes', type=int, help='点赞数')
    p_up.add_argument('-s', '--shares', type=int, help='转发数')
    p_up.add_argument('-c', '--comments', type=int, help='评论数')

    # 列出
    p_list = subparsers.add_parser('list', help='列出案例')

    # 报告
    p_report = subparsers.add_parser('report', help='导出报告')

    args = parser.parse_args()

    if args.command == 'add':
        add_case(args.name, args.customer or "")
    elif args.command == 'channel':
        add_channel(args.case, args.channel, args.url or "")
    elif args.command == 'update':
        metrics = {}
        if args.views: metrics["views"] = args.views
        if args.likes: metrics["likes"] = args.likes
        if args.shares: metrics["shares"] = args.shares
        if args.comments: metrics["comments"] = args.comments
        update_metrics(args.case, args.channel, metrics)
    elif args.command == 'list':
        list_cases()
    elif args.command == 'report':
        export_report()
    else:
        parser.print_help()
        print("\n示例:")
        print("  python3 tracking.py add 'XX 公司案例' -c 'XX 公司'")
        print("  python3 tracking.py channel 'XX 公司案例' 公众号 -u https://xxx")
        print("  python3 tracking.py update 'XX 公司案例' 公众号 -v 10000 -l 500 -s 200")
        print("  python3 tracking.py list")
        print("  python3 tracking.py report")
