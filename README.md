# 惊喜库 🎁

> 这里存放各种惊喜。

---

## 📦 工具集合

### 🔧 实用工具

| 工具 | 说明 |
|------|------|
| [password-gen.py](tools/password-gen.py) | 密码生成器 |
| [json-format.py](tools/json-format.py) | JSON 格式化 |
| [qrcode-gen.py](tools/qrcode-gen.py) | 二维码生成器 |
| [url-short.py](tools/url-short.py) | 短链接生成器 |
| [csv2excel.py](tools/csv2excel.py) | CSV 转 Excel |
| [image-compress.py](tools/image-compress.py) | 图片压缩 |

### 📈 市场活动工具（打工人必备）

| 工具 | 说明 |
|------|------|
| [daily_report.py](tools/market/daily_report.py) | 日报/周报生成器 |
| [roi_calculator.py](tools/market/roi_calculator.py) | 活动 ROI 计算器 |
| [title_generator.py](tools/market/title_generator.py) | 爆款标题生成器 |
| [event_checklist.py](tools/market/event_checklist.py) | 活动 Checklist |
| [competitor_tracker.py](tools/market/competitor_tracker.py) | 竞品活动追踪 |

### 📖 客户案例工具（案例制作必备）

| 工具 | 说明 |
|------|------|
| [customer_info.py](tools/case/customer_info.py) | 客户信息采集表 |
| [interview_questions.py](tools/case/interview_questions.py) | 采访提纲生成器 |
| [case_template.py](tools/case/case_template.py) | 案例模板库 |
| [data_viz.py](tools/case/data_viz.py) | 数据可视化生成器 |
| [compliance_check.py](tools/case/compliance_check.py) | 合规检查器 |
| [multi_version.py](tools/case/multi_version.py) | 多版本生成器 |
| [case_value.py](tools/case/case_value.py) | 案例价值评估器 |
| [tracking.py](tools/case/tracking.py) | 传播效果追踪器 |

---

## 🚀 快速开始

### 客户案例工具

```bash
# 客户信息采集表
python3 tools/case/customer_info.py -n "XX 公司"

# 生成采访提纲
python3 tools/case/interview_questions.py "XX 公司" -i 互联网

# 查看案例模板
python3 tools/case/case_template.py -t 标准版

# 数据可视化
python3 tools/case/data_viz.py

# 合规检查
python3 tools/case/compliance_check.py case.md -m

# 多版本生成
python3 tools/case/multi_version.py case.md -v 全部 -o output/

# 案例价值评估
python3 tools/case/case_value.py -i

# 传播效果追踪
python3 tools/case/tracking.py add "XX 公司案例" -c "XX 公司"
python3 tools/case/tracking.py channel "XX 公司案例" 公众号 -u https://xxx
python3 tools/case/tracking.py update "XX 公司案例" 公众号 -v 10000 -l 500
python3 tools/case/tracking.py report
```

### 市场活动工具

```bash
# 生成日报模板
python3 tools/market/daily_report.py -t 日报

# 生成周报模板
python3 tools/market/daily_report.py -t 周报

# 计算活动 ROI
python3 tools/market/roi_calculator.py -i 100000 -r 350000 -b 50000

# 生成爆款标题
python3 tools/market/title_generator.py "生态大会"

# 查看活动 Checklist
python3 tools/market/event_checklist.py

# 追踪竞品活动
python3 tools/market/competitor_tracker.py add 阿里云
python3 tools/market/competitor_tracker.py activity 阿里云 云栖大会 2026-09-20 大会 -l https://xxx
python3 tools/market/competitor_tracker.py list
```

### 日常工具

```bash
# 生成密码
python3 tools/password-gen.py -l 20 -n 5

# JSON 格式化
python3 tools/json-format.py data.json

# 生成二维码
python3 tools/qrcode-gen.py "https://example.com"

# 短链接
python3 tools/url-short.py "https://long-url.com/path"
```

---

## 关于

- 创建者：yangyuying0610-cloud
- 创建日期：2026-03-11
- 持续更新中...

---

*准备好迎接惊喜了吗？* 🎁
