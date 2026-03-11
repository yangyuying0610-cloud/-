#!/usr/bin/env python3
"""
公众号传播数据盘点报告生成器
用法：python3 tools/market/wechat_report.py
"""

import argparse
from datetime import datetime

def generate_report(articles, period=""):
    """生成盘点报告"""

    # 计算汇总数据
    total_views = sum(a.get('views', 0) for a in articles)
    total_likes = sum(a.get('likes', 0) for a in articles)
    total_shares = sum(a.get('shares', 0) for a in articles)
    avg_views = total_views // len(articles) if articles else 0

    # 找出爆文 (阅读>10000)
    viral = [a for a in articles if a.get('views', 0) >= 10000]

    report = f"""# Openclaw 传播效果盘点

**统计周期**: {period or '2026 年第' + str(datetime.now().isocalendar()[1]) + '周'}
**数据来源**: 百度智能云公众号

---

## 📊 核心指标

| 指标 | 数值 |
|------|------|
| 发布文章数 | {len(articles)} 篇 |
| 总阅读量 | {total_views:,} |
| 总点赞数 | {total_likes:,} |
| 总转发数 | {total_shares:,} |
| 平均阅读 | {avg_views:,} |
| 爆文数 (1w+) | {len(viral)} 篇 |

---

## 📝 文章详情

| # | 文章标题 | 日期 | 阅读 | 点赞 | 在看 | 转发 |
|---|----------|------|------|------|------|------|
"""

    for i, a in enumerate(articles, 1):
        report += f"| {i} | {a.get('title', '-')} | {a.get('date', '-')} | {a.get('views', '-'):,} | {a.get('likes', '-')} | {a.get('looks', '-')} | {a.get('shares', '-')} |\n"

    report += f"""
---

## 💡 亮点与洞察

### 表现最好的文章
"""
    if articles:
        best = max(articles, key=lambda x: x.get('views', 0))
        report += f"- **{best.get('title', '-')}** ({best.get('views', 0):,} 阅读)\n"

    report += """
### 亮点
-

### 不足
-

### 建议
-

---

## 📌 下周计划

1.
2.
3.

---

*报告生成时间：{0}*
""".format(datetime.now().strftime('%Y-%m-%d %H:%M'))

    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='公众号传播数据盘点报告生成器')
    parser.add_argument('-p', '--period', help='统计周期 (如：2026 年第 10 周)')
    parser.add_argument('-o', '--output', help='输出文件路径')
    parser.add_argument('--sample', action='store_true', help='生成示例报告')

    args = parser.parse_args()

    # 示例数据
    sample_articles = [
        {"title": "Openclaw 智能助手发布", "date": "2026-03-10", "views": 15800, "likes": 420, "looks": 180, "shares": 95},
        {"title": "百度智能云生态大会回顾", "date": "2026-03-08", "views": 23500, "likes": 680, "looks": 320, "shares": 150},
        {"title": "Openclaw 使用指南", "date": "2026-03-06", "views": 8900, "likes": 210, "looks": 85, "shares": 42},
    ]

    if args.sample:
        articles = sample_articles
    else:
        print("请输入文章数据（JSON 格式，输入空行结束）:")
        import json
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        if lines:
            articles = json.loads('\n'.join(lines))
        else:
            articles = sample_articles

    report = generate_report(articles, args.period or "2026 年第 10 周")

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ 报告已保存到：{args.output}")
    else:
        print(report)
