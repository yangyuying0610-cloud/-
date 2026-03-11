#!/usr/bin/env python3
"""CSV 转 Excel - 转换 CSV 文件为 Excel 格式"""

import argparse
import sys

def csv_to_excel(csv_file, excel_file=None):
    """转换 CSV 为 Excel"""
    try:
        import pandas as pd
    except ImportError:
        print("❌ 需要安装 pandas 和 openpyxl: pip install pandas openpyxl")
        return False

    if excel_file is None:
        excel_file = csv_file.replace('.csv', '.xlsx')

    df = pd.read_csv(csv_file, encoding='utf-8')
    df.to_excel(excel_file, index=False)
    print(f"✅ 已转换：{csv_file} → {excel_file}")
    print(f"   行数：{len(df)}, 列数：{len(df.columns)}")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV 转 Excel')
    parser.add_argument('csv_file', help='输入的 CSV 文件')
    parser.add_argument('-o', '--output', help='输出的 Excel 文件名')

    args = parser.parse_args()
    csv_to_excel(args.csv_file, args.output)
