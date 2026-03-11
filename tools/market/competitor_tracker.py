#!/usr/bin/env python3
"""
竞品活动追踪 - 监控友商活动动态
用法：python3 tools/market/competitor_tracker.py
"""

import argparse
import json
from datetime import datetime
import os

DATA_FILE = os.path.expanduser("~/.openclaw/data/competitor_tracking.json")

def load_data():
    """加载数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"competitors": [], "activities": []}

def save_data(data):
    """保存数据"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_competitor(name, industry=""):
    """添加竞品公司"""
    data = load_data()
    data["competitors"].append({
        "name": name,
        "industry": industry,
        "added_at": datetime.now().isoformat()
    })
    save_data(data)
    print(f"✅ 添加竞品：{name}")

def add_activity(competitor, title, date, type_, link="", notes=""):
    """添加活动记录"""
    data = load_data()
    data["activities"].append({
        "competitor": competitor,
        "title": title,
        "date": date,
        "type": type_,
        "link": link,
        "notes": notes,
        "recorded_at": datetime.now().isoformat()
    })
    save_data(data)
    print(f"✅ 添加活动：{competitor} - {title}")

def list_activities(limit=10):
    """列出活动"""
    data = load_data()
    activities = data.get("activities", [])[-limit:]

    print("\n📊 竞品活动追踪\n")
    print("=" * 70)

    for act in reversed(activities):
        print(f"🏢 {act['competitor']}")
        print(f"   📝 {act['title']}")
        print(f"   📅 {act['date']} | 类型：{act['type']}")
        if act.get('link'):
            print(f"   🔗 {act['link']}")
        if act.get('notes'):
            print(f"   📌 {act['notes']}")
        print()

    print("=" * 70)
    print(f"共 {len(activities)} 条记录")

def export_report():
    """导出报告"""
    data = load_data()
    print("\n" + "=" * 70)
    print("📈 竞品活动追踪报告")
    print("=" * 70)

    # 按竞品分组
    by_competitor = {}
    for act in data.get("activities", []):
        c = act["competitor"]
        if c not in by_competitor:
            by_competitor[c] = []
        by_competitor[c].append(act)

    for competitor, acts in by_competitor.items():
        print(f"\n🏢 {competitor} ({len(acts)} 场活动)")
        print("-" * 50)
        for act in acts[-5:]:
            print(f"  • {act['date']} | {act['title']}")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='竞品活动追踪')
    subparsers = parser.add_subparsers(dest='command', help='命令')

    # 添加竞品
    p_add = subparsers.add_parser('add', help='添加竞品')
    p_add.add_argument('name', help='竞品名称')
    p_add.add_argument('-i', '--industry', help='行业')

    # 添加活动
    p_act = subparsers.add_parser('activity', help='添加活动')
    p_act.add_argument('competitor', help='竞品名称')
    p_act.add_argument('title', help='活动标题')
    p_act.add_argument('date', help='活动日期 (YYYY-MM-DD)')
    p_act.add_argument('type', help='活动类型 (大会/发布会/直播/其他)')
    p_act.add_argument('-l', '--link', help='活动链接')
    p_act.add_argument('-n', '--notes', help='备注')

    # 列出
    p_list = subparsers.add_parser('list', help='列出活动')
    p_list.add_argument('-n', '--num', type=int, default=10, help='显示数量')

    # 报告
    p_report = subparsers.add_parser('report', help='导出报告')

    args = parser.parse_args()

    if args.command == 'add':
        add_competitor(args.name, args.industry or "")
    elif args.command == 'activity':
        add_activity(args.competitor, args.title, args.date, args.type, args.link or "", args.notes or "")
    elif args.command == 'list':
        list_activities(args.num)
    elif args.command == 'report':
        export_report()
    else:
        parser.print_help()
        print("\n示例:")
        print("  python3 competitor_tracker.py add 华为云")
        print("  python3 competitor_tracker.py activity 华为云 生态大会 2026-03-20 大会 -l https://xxx")
        print("  python3 competitor_tracker.py list")
        print("  python3 competitor_tracker.py report")
