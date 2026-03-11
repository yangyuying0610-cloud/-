#!/usr/bin/env python3
"""
日报/周报生成器 - 自动汇总工作产出
用法：python3 tools/market/daily_report.py
"""

import argparse
from datetime import datetime

def generate_report(report_type="日报"):
    """生成工作报告模板"""

    today = datetime.now().strftime("%Y-%m-%d")

    if report_type == "日报":
        template = f"""# 工作日报 - {today}

## ✅ 今日完成

### 项目进展
| 项目 | 进度 | 状态 |
|------|------|------|
| [项目名] | [xx]% | 🟢 正常 |

### 内容产出
- [ ] 文案：
- [ ] 设计：
- [ ] 其他：

### 数据汇总
- 公众号：阅读 [x] | 点赞 [x] | 转发 [x]
- 视频号：播放 [x] | 点赞 [x]
- 其他渠道：[数据]

## 📅 明日计划
1.
2.
3.

## ⚠️ 需要支持
- [无/具体事项]

---
*生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""
    else:  # 周报
        template = f"""# 工作周报 - {today}

## 📊 本周核心数据

### 传播数据
| 渠道 | 内容数 | 总阅读 | 互动数 | 环比 |
|------|--------|--------|--------|------|
| 公众号 | | | | |
| 视频号 | | | | |
| 其他媒体 | | | | |

### 活动进展
| 活动名称 | 阶段 | 进度 | 预计完成 |
|----------|------|------|----------|
| [活动 A] | 策划 | 80% | MM-DD |

## ✅ 本周完成

### 重点项目
1. **项目 A** - 完成情况说明
2. **项目 B** - 完成情况说明

### 内容产出
- 公众号文章 [x] 篇
- 社交媒体内容 [x] 条
- 其他物料 [x] 份

## 📈 亮点与不足

### 亮点
-

### 不足
-

## 📅 下周计划

### 重点工作
1.
2.
3.

### 需要协调
-

---
*生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""

    return template

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='工作报告生成器')
    parser.add_argument('-t', '--type', choices=['日报', '周报'], default='日报', help='报告类型')
    parser.add_argument('-o', '--output', help='输出文件路径')

    args = parser.parse_args()

    report = generate_report(args.type)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ 报告已保存到：{args.output}")
    else:
        print(report)
