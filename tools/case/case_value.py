#!/usr/bin/env python3
"""
案例价值评估器 - 评估案例传播价值
用法：python3 tools/case/case_value.py
"""

import argparse
import json
from datetime import datetime

CRITERIA = [
    {"name": "客户知名度", "weight": 3, "options": [
        (1, "一般企业"),
        (3, "行业知名"),
        (5, "头部/标杆"),
    ]},
    {"name": "成果显著度", "weight": 3, "options": [
        (1, "有改善"),
        (3, "明显提升"),
        (5, "突破性成果"),
    ]},
    {"name": "行业代表性", "weight": 2, "options": [
        (1, "普通场景"),
        (3, "典型场景"),
        (5, "创新场景"),
    ]},
    {"name": "数据完整性", "weight": 2, "options": [
        (1, "定性描述"),
        (3, "部分量化"),
        (5, "完整数据"),
    ]},
    {"name": "客户配合度", "weight": 2, "options": [
        (1, "仅内部使用"),
        (3, "可官网发布"),
        (5, "可联合传播"),
    ]},
]

def evaluate(scores):
    """评估案例价值"""
    total_score = 0
    total_weight = 0

    details = []
    for i, score in enumerate(scores.values()):
        weight = CRITERIA[i]["weight"]
        total_score += score * weight
        total_weight += weight
        details.append({
            "criteria": CRITERIA[i]["name"],
            "score": score,
            "weight": weight,
            "weighted": score * weight
        })

    max_score = 5 * total_weight
    percentage = (total_score / max_score) * 100

    # 评级
    if percentage >= 80:
        level = "🏆 S 级 - 优先传播"
    elif percentage >= 60:
        level = "✅ A 级 - 重点传播"
    elif percentage >= 40:
        level = "📊 B 级 - 常规传播"
    else:
        level = "⚠️ C 级 - 内部参考"

    return {
        "total_score": total_score,
        "max_score": max_score,
        "percentage": percentage,
        "level": level,
        "details": details
    }

def print_evaluation(result):
    """打印评估结果"""
    print("\n" + "=" * 70)
    print("📊 案例价值评估报告")
    print("=" * 70)

    print(f"\n总分：{result['total_score']} / {result['max_score']} ({result['percentage']:.1f}%)")
    print(f"\n评级：{result['level']}")

    print("\n评分详情:")
    print("-" * 50)
    print(f"{'维度':<12} {'得分':<8} {'权重':<8} {'加权':<8}")
    print("-" * 50)
    for d in result["details"]:
        print(f"{d['criteria']:<12} {d['score']:<8} {d['weight']:<8} {d['weighted']:<8}")

    print("\n" + "=" * 70)
    print("\n💡 建议:")
    if result['percentage'] >= 80:
        print("  • 安排头部媒体发布")
        print("  • 制作多种传播素材")
        print("  • 纳入销售工具包")
    elif result['percentage'] >= 60:
        print("  • 官网/公众号发布")
        print("  • 补充更多数据")
    elif result['percentage'] >= 40:
        print("  • 可作为参考案例")
        print("  • 挖掘更多亮点")
    else:
        print("  • 暂不适合对外传播")
        print("  • 可作为内部学习材料")
    print("=" * 70 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='案例价值评估器')
    parser.add_argument('-s', '--scores', help='评分 JSON 字符串')
    parser.add_argument('-i', '--interactive', action='store_true', help='交互模式')
    parser.add_argument('-o', '--output', help='输出 JSON 文件')

    args = parser.parse_args()

    if args.interactive:
        print("\n📊 案例价值评估\n")
        scores = {}
        for c in CRITERIA:
            print(f"{c['name']} (权重 x{c['weight']}):")
            for score, desc in c['options']:
                print(f"  {score} 分 - {desc}")
            s = int(input("  评分："))
            scores[c['name']] = s
            print()
    elif args.scores:
        scores = json.loads(args.scores)
    else:
        # 默认示例
        print("\n📊 案例价值评估（示例）\n")
        scores = {
            "客户知名度": 4,
            "成果显著度": 5,
            "行业代表性": 3,
            "数据完整性": 4,
            "客户配合度": 5,
        }

    result = evaluate(scores)
    print_evaluation(result)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump({
                "evaluated_at": datetime.now().isoformat(),
                "scores": scores,
                "result": result
            }, f, indent=2, ensure_ascii=False)
        print(f"✅ 已保存到：{args.output}")
