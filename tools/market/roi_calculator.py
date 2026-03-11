#!/usr/bin/env python3
"""
活动 ROI 计算器 - 投入产出比分析
用法：python3 tools/market/roi_calculator.py
"""

import argparse
import json

def calculate_roi(investment, returns, brand_value=0):
    """计算 ROI"""
    total_returns = returns + brand_value
    roi = ((total_returns - investment) / investment * 100) if investment > 0 else 0
    return {
        'investment': investment,
        'direct_returns': returns,
        'brand_value': brand_value,
        'total_returns': total_returns,
        'roi': roi,
        'profit': total_returns - investment
    }

def print_report(data):
    """打印报告"""
    print("\n" + "="*50)
    print("📊 活动 ROI 分析报告")
    print("="*50)
    print(f"\n💰 投入成本：¥{data['investment']:,.2f}")
    print(f"\n📈 直接收益：¥{data['direct_returns']:,.2f}")
    print(f"🌟 品牌价值：¥{data['brand_value']:,.2f} (估算)")
    print(f"\n💎 总收益：¥{data['total_returns']:,.2f}")
    print(f"\n📊 ROI: {data['roi']:.1f}%")
    print(f"💵 净利润：¥{data['profit']:,.2f}")

    # 评级
    if data['roi'] >= 300:
        rating = "🏆 优秀"
    elif data['roi'] >= 100:
        rating = "✅ 良好"
    elif data['roi'] >= 0:
        rating = "⚠️ 一般"
    else:
        rating = "❌ 亏损"
    print(f"\n🎯 评级：{rating}")
    print("="*50 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='活动 ROI 计算器')
    parser.add_argument('-i', '--investment', type=float, required=True, help='投入成本')
    parser.add_argument('-r', '--returns', type=float, default=0, help='直接收益')
    parser.add_argument('-b', '--brand', type=float, default=0, help='品牌价值 (估算)')
    parser.add_argument('-o', '--output', help='输出 JSON 文件')

    args = parser.parse_args()

    result = calculate_roi(args.investment, args.returns, args.brand)
    print_report(result)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"📁 已保存到：{args.output}")
