#!/usr/bin/env python3
"""
数据可视化生成器 - 把案例成果数据转为图表
用法：python3 tools/case/data_viz.py
"""

import argparse
import json

def generate_chart_data(metrics):
    """生成图表数据配置"""
    charts = []

    # 柱状图 - 对比型
    if len(metrics) >= 2:
        charts.append({
            "type": "bar",
            "title": "核心指标对比",
            "data": metrics
        })

    # 饼图 - 占比型
    total = sum(m.get("value", 0) for m in metrics)
    if total > 0:
        charts.append({
            "type": "pie",
            "title": "指标占比",
            "data": [{"name": m["name"], "value": m.get("value", 0)} for m in metrics]
        })

    return charts

def print_mermaid(metrics):
    """打印 Mermaid 图表代码"""
    print("\n📊 Mermaid 柱状图代码:\n")
    print("```mermaid")
    print("xychart-beta")
    print('    title "成果数据对比"')
    print('    x-axis ["' + '", "'.join(m["name"] for m in metrics) + '"]')
    print("    y-axis \"提升幅度 (%)\" 0 --> " + str(max(m.get("value", 0) for m in metrics) * 1.2))
    print("    bar [" + ", ".join(str(m.get("value", 0)) for m in metrics) + "]")
    print("```\n")

def print_markdown_table(metrics):
    """打印 Markdown 表格"""
    print("\n📊 成果数据表:\n")
    print("| 指标 | 数值 | 说明 |")
    print("|------|------|------|")
    for m in metrics:
        print(f"| {m['name']} | {m.get('value', '-')} | {m.get('desc', '')} |")
    print()

def generate_echarts(metrics):
    """生成 ECharts 配置"""
    config = {
        "title": {"text": "案例成果数据"},
        "tooltip": {},
        "xAxis": {
            "data": [m["name"] for m in metrics]
        },
        "yAxis": {},
        "series": [{
            "type": "bar",
            "data": [m.get("value", 0) for m in metrics],
            "itemStyle": {"color": "#5470c6"}
        }]
    }
    return json.dumps(config, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='数据可视化生成器')
    parser.add_argument('-d', '--data', type=str, help='数据 JSON 字符串')
    parser.add_argument('-o', '--output', help='输出文件')
    parser.add_argument('--echarts', action='store_true', help='输出 ECharts 配置')

    args = parser.parse_args()

    # 示例数据
    default_metrics = [
        {"name": "效率提升", "value": 150, "desc": "工作效率提升 150%"},
        {"name": "成本降低", "value": 45, "desc": "运营成本降低 45%"},
        {"name": "收入增长", "value": 80, "desc": "业务收入增长 80%"},
        {"name": "客户满意度", "value": 95, "desc": "满意度达到 95%"},
    ]

    if args.data:
        metrics = json.loads(args.data)
    else:
        metrics = default_metrics

    print_markdown_table(metrics)
    print_mermaid(metrics)

    if args.echarts:
        print("\n📊 ECharts 配置:\n")
        print(generate_echarts(metrics))

    if args.output:
        output = {
            "metrics": metrics,
            "mermaid": "见上方",
            "echarts": generate_echarts(metrics)
        }
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"✅ 已保存到：{args.output}")
