#!/usr/bin/env python3
"""
爆款标题生成器 - 一键生成多个标题变体
用法：python3 tools/market/title_generator.py "原标题"
"""

import argparse
import random

TITLE_TEMPLATES = [
    # 数字型
    "这{}个{}，{}%的人都不知道",
    "{}个{}技巧，让你{}",
    "关于{}，你一定要知道的{}件事",

    # 疑问型
    "为什么{}？答案出乎意料",
    "{}到底值不值得{}？",
    "如何实现{}？看这篇就够了",

    # 对比型
    "同样是{}，为什么{}能{}？",
    "{}vs{}，谁更胜一筹？",
    "从{}到{}，我经历了什么",

    # 情绪型
    "太{}了！{}必看",
    "终于{}了！{}",
    "后悔没有早点{}",

    # 独家型
    "首次公开：{}",
    "内部资料：{}",
    "独家揭秘：{}",

    # 紧迫型
    "最后{}天！{}",
    "限时{}，{}",
    "错过等{}！{}",
]

PATTERNS = [
    "🔥 {}",
    "💡 {}",
    "📢 {}",
    "✨ {}",
    "🎯 {}",
    "👉 {}",
    "❗ {}",
    "📊 {}",
    "🚀 {}",
    "💰 {}",
]

def generate_titles(topic, keywords=None):
    """生成标题变体"""
    titles = []

    # 基础变体
    for template in TITLE_TEMPLATES[:6]:
        try:
            title = template.format(
                random.choice([3, 5, 7, 10]),
                topic,
                random.choice([80, 90, 95, 99])
            )
            titles.append(title)
        except:
            pass

    # 添加 emoji 前缀
    emoji_titles = [t.format(random.choice(["🔥", "💡", "📢", "✨"])) + t for t in titles[:5]]

    # 组合型
    combo_titles = [
        f"【必看】{topic} 的完整攻略",
        f"建议收藏 | {topic} 一文讲清楚",
        f"深度解读 | {topic} 背后的逻辑",
        f"干货满满 | {topic} 实操指南",
        f"重磅发布 | {topic} 来了",
    ]

    all_titles = titles + combo_titles

    # 去重
    unique_titles = list(dict.fromkeys(all_titles))

    return unique_titles[:15]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='爆款标题生成器')
    parser.add_argument('topic', help='主题/关键词')
    parser.add_argument('-n', '--count', type=int, default=10, help='生成数量')
    parser.add_argument('-o', '--output', help='输出文件')

    args = parser.parse_args()

    titles = generate_titles(args.topic)

    print(f"\n🎯 主题：{args.topic}")
    print(f"\n📝 生成的标题 ({len(titles)} 个):\n")

    for i, title in enumerate(titles, 1):
        print(f"  {i:2d}. {title}")

    print()

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for i, title in enumerate(titles, 1):
                f.write(f"{i}. {title}\n")
        print(f"✅ 已保存到：{args.output}")
