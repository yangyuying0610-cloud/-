#!/usr/bin/env python3
"""图片压缩 - 压缩图片文件大小"""

import argparse
import os

def compress_image(input_file, output_file=None, quality=85, max_size=None):
    """压缩图片"""
    try:
        from PIL import Image
    except ImportError:
        print("❌ 需要安装 Pillow: pip install Pillow")
        return False

    if output_file is None:
        name, ext = os.path.splitext(input_file)
        output_file = f"{name}_compressed{ext}"

    img = Image.open(input_file)

    # 调整大小
    if max_size:
        img.thumbnail((max_size, max_size))

    # 保存压缩
    if img.mode in ('RGBA', 'LA'):
        img = img.convert('RGB')

    img.save(output_file, optimize=True, quality=quality)

    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    ratio = (1 - compressed_size / original_size) * 100

    print(f"✅ 已压缩：{input_file}")
    print(f"   输出：{output_file}")
    print(f"   原始：{original_size / 1024:.1f} KB")
    print(f"   压缩后：{compressed_size / 1024:.1f} KB")
    print(f"   压缩率：{ratio:.1f}%")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='图片压缩工具')
    parser.add_argument('input', help='输入图片文件')
    parser.add_argument('-o', '--output', help='输出文件名')
    parser.add_argument('-q', '--quality', type=int, default=80, help='质量 (1-100, 默认：80)')
    parser.add_argument('-s', '--size', type=int, help='最大边长 (像素)')

    args = parser.parse_args()
    compress_image(args.input, args.output, args.quality, args.size)
