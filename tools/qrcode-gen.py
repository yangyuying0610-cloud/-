#!/usr/bin/env python3
"""二维码生成器 - 生成二维码图片"""

import argparse

def generate_qr(data, output='qrcode.png'):
    """生成二维码"""
    try:
        import qrcode
    except ImportError:
        print("❌ 需要安装 qrcode 库：pip install qrcode[pil]")
        return False

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    print(f"✅ 二维码已保存到：{output}")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='二维码生成器')
    parser.add_argument('data', help='要编码的内容 (URL、文本等)')
    parser.add_argument('-o', '--output', default='qrcode.png', help='输出文件名 (默认：qrcode.png)')

    args = parser.parse_args()
    generate_qr(args.data, args.output)
