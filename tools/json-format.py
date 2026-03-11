#!/usr/bin/env python3
"""JSON 格式化 - 美化和验证 JSON 数据"""

import json
import sys
import argparse

def format_json(input_file=None, compact=False):
    """格式化 JSON"""
    if input_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        print("请输入 JSON (输入空行结束):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        data = json.loads('\n'.join(lines))

    if compact:
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    else:
        return json.dumps(data, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON 格式化工具')
    parser.add_argument('file', nargs='?', help='输入的 JSON 文件')
    parser.add_argument('-c', '--compact', action='store_true', help='压缩输出')
    parser.add_argument('-o', '--output', help='输出文件')

    args = parser.parse_args()

    try:
        result = format_json(args.file, args.compact)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✅ 已保存到：{args.output}")
        else:
            print(result)
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误：{e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ 文件不存在：{args.file}")
        sys.exit(1)
