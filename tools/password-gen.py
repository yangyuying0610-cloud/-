#!/usr/bin/env python3
"""密码生成器 - 生成高强度随机密码"""

import random
import string
import argparse

def generate_password(length=16, use_special=True):
    """生成随机密码"""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # 确保至少有一个大写字母、一个小写字母、一个数字
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]

    # 填充剩余长度
    password += [random.choice(chars) for _ in range(length - 3)]

    # 打乱顺序
    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='生成高强度随机密码')
    parser.add_argument('-l', '--length', type=int, default=16, help='密码长度 (默认：16)')
    parser.add_argument('-n', '--count', type=int, default=1, help='生成数量 (默认：1)')
    parser.add_argument('--no-special', action='store_true', help='不使用特殊字符')

    args = parser.parse_args()

    print(f"\n🔐 生成的密码 ({args.length} 位):\n")
    for i in range(args.count):
        pwd = generate_password(args.length, not args.no_special)
        print(f"  {i+1}. {pwd}")
    print()
