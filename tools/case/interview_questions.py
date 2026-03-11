#!/usr/bin/env python3
"""
采访提纲生成器 - 根据行业自动生成采访问题
用法：python3 tools/case/interview_questions.py "客户名称" -i 行业
"""

import argparse

QUESTIONS_BY_INDUSTRY = {
    "通用": [
        "请简单介绍一下贵公司的业务和主要服务对象？",
        "在合作之前，贵司面临的最大挑战是什么？",
        "为什么选择了我们作为合作伙伴？",
        "合作过程中，哪些功能/服务让您印象最深刻？",
        "合作后取得了哪些可量化的成果？",
        "您如何评价我们的产品和服务？",
        "未来还有哪些合作计划？",
        "您会向同行推荐我们吗？为什么？",
    ],
    "互联网": [
        "贵司的业务规模和技术架构是怎样的？",
        "在技术选型时最关注哪些因素？",
        "合作后系统性能/稳定性提升了多少？",
        "对业务增长有什么直接帮助？",
        "技术团队的使用体验如何？",
    ],
    "制造业": [
        "贵司的生产规模和产品线是怎样的？",
        "数字化转型过程中遇到的主要困难？",
        "合作后生产效率提升了多少？",
        "质量管控/成本方面有什么改善？",
        "一线员工的使用反馈如何？",
    ],
    "金融": [
        "贵司的业务类型和监管要求？",
        "在合规和安全方面有哪些考量？",
        "合作后风险控制能力如何提升？",
        "客户体验有什么改善？",
        "对业务创新有什么帮助？",
    ],
    "零售": [
        "贵司的渠道布局和销售规模？",
        "在客户运营方面遇到哪些挑战？",
        "合作后转化率/复购率提升了多少？",
        "全渠道运营效率如何？",
        "消费者体验有什么变化？",
    ],
    "医疗": [
        "贵司的医疗服务类型和覆盖范围？",
        "在合规和数据安全方面的要求？",
        "合作后诊疗效率/患者体验如何提升？",
        "对医疗质量有什么帮助？",
        "医护人员的使用反馈？",
    ],
    "教育": [
        "贵机构的学员规模和教学模式？",
        "在教学管理方面的痛点？",
        "合作后教学效率/学员满意度如何？",
        "对招生/运营有什么帮助？",
        "老师和学员的反馈？",
    ],
    "政务": [
        "贵部门的服务范围和职能？",
        "在数字化服务方面的目标？",
        "合作后办事效率/群众满意度如何？",
        "数据安全如何保障？",
        "对政务服务创新有什么帮助？",
    ],
}

def generate_questions(industry="通用", custom_topics=None):
    """生成采访提纲"""
    questions = QUESTIONS_BY_INDUSTRY.get(industry, QUESTIONS_BY_INDUSTRY["通用"])

    # 追加通用问题
    if industry != "通用":
        questions += ["", "--- 通用问题 ---", ""] + QUESTIONS_BY_INDUSTRY["通用"][:3]

    return questions

def print_questions(questions, customer_name=""):
    """打印采访提纲"""
    print("\n" + "=" * 70)
    print(f"🎤 客户采访提纲 - {customer_name}")
    print(f"   行业：{industry}")
    print("=" * 70)

    for q in questions:
        if q.startswith("---"):
            print(f"\n{q}\n")
        else:
            print(f"  ☐ {q}")

    print("\n" + "=" * 70)
    print("💡 采访提示:")
    print("  • 采访时长建议：45-60 分钟")
    print("  • 优先采访对象：项目负责人/业务负责人/一线用户")
    print("  • 务必获取：具体数据、对比效果、客户原话")
    print("=" * 70 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='采访提纲生成器')
    parser.add_argument('customer', help='客户名称')
    parser.add_argument('-i', '--industry', default='通用',
                       choices=['通用', '互联网', '制造业', '金融', '零售', '医疗', '教育', '政务'],
                       help='所属行业')
    parser.add_argument('-o', '--output', help='输出文件')

    args = parser.parse_args()
    industry = args.industry

    questions = generate_questions(industry)
    print_questions(questions, args.customer)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"# 客户采访提纲 - {args.customer}\n\n")
            f.write(f"行业：{industry}\n\n")
            for q in questions:
                f.write(f"- {q}\n")
        print(f"✅ 已保存到：{args.output}")
