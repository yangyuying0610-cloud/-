#!/usr/bin/env python3
"""短链接生成器 - 使用短链接服务"""

import argparse
import urllib.request
import urllib.parse
import json

def shorten_url(url, service='is.gd'):
    """生成短链接"""
    if service == 'is.gd':
        api_url = f"https://is.gd/create.php?format=json&url={urllib.parse.quote(url)}"
        try:
            with urllib.request.urlopen(api_url, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data.get('shorturl', '生成失败')
        except Exception as e:
            return f"错误：{e}"

    elif service == 'tinyurl':
        api_url = f"https://tinyurl.com/api-create.php?url={urllib.parse.quote(url)}"
        try:
            with urllib.request.urlopen(api_url, timeout=10) as response:
                return response.read().decode()
        except Exception as e:
            return f"错误：{e}"

    return "不支持的服务"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='短链接生成器')
    parser.add_argument('url', help='要缩短的 URL')
    parser.add_argument('-s', '--service', choices=['is.gd', 'tinyurl'], default='is.gd', help='短链接服务')

    args = parser.parse_args()

    print(f"\n🔗 原链接：{args.url}")
    short_url = shorten_url(args.url, args.service)
    print(f"📦 短链接：{short_url}\n")
