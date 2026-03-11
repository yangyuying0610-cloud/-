#!/usr/bin/env python3
"""
活动 Checklist - 活动前中后任务清单
用法：python3 tools/market/event_checklist.py
"""

import argparse
import json
from datetime import datetime

CHECKLIST = {
    "活动前": [
        "✅ 确定活动目标和主题",
        "✅ 制定预算方案",
        "✅ 选定活动日期和场地",
        "✅ 确认嘉宾/演讲者名单",
        "✅ 设计活动视觉 (主 KV/物料)",
        "✅ 搭建报名页面",
        "✅ 准备宣传内容 (推文/海报)",
        "✅ 联系媒体合作",
        "✅ 采购礼品/物料",
        "✅ 确认搭建商和供应商",
        "✅ 制定活动流程脚本",
        "✅ 准备主持人串词",
        "✅ 确认摄影摄像",
        "✅ 准备签到表和胸牌",
        "✅ 彩排演练",
    ],
    "活动中": [
        "✅ 现场签到管理",
        "✅ 设备调试 (音响/投影)",
        "✅ 控制活动节奏",
        "✅ 拍照/录像记录",
        "✅ 互动环节执行",
        "✅ 突发情况处理",
        "✅ 直播推流监控",
        "✅ 社交媒体实时播报",
    ],
    "活动后": [
        "✅ 整理活动照片/视频",
        "✅ 撰写活动回顾推文",
        "✅ 收集参与者反馈",
        "✅ 统计活动数据 (报名/到场/互动)",
        "✅ 媒体发稿跟进",
        "✅ 费用结算",
        "✅ 复盘报告",
        "✅ 感谢信发送",
        "✅ 素材归档",
    ],
}

def print_checklist(phase=None):
    """打印清单"""
    output = []
    output.append(f"\n📋 活动 Checklist")
    output.append("=" * 50)

    for p, items in CHECKLIST.items():
        if phase and p != phase:
            continue
        output.append(f"\n{p}\n")
        for item in items:
            output.append(f"  ☐ {item[2:]}")  # 去掉原有 emoji

    output.append("\n" + "=" * 50)
    output.append(f"*生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(output)

def export_json(output_file):
    """导出为 JSON"""
    data = {
        "generated_at": datetime.now().isoformat(),
        "checklist": CHECKLIST
    }
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='活动 Checklist')
    parser.add_argument('-p', '--phase', choices=['活动前', '活动中', '活动后'], help='阶段')
    parser.add_argument('-o', '--output', help='输出文件')
    parser.add_argument('--json', action='store_true', help='导出为 JSON')

    args = parser.parse_args()

    result = print_checklist(args.phase)
    print(result)

    if args.output:
        if args.json:
            export_json(args.output)
        else:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
        print(f"✅ 已保存到：{args.output}")
