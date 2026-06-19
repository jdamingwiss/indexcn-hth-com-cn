import json
import sys


SITE_DATA = {
    "name": "IndexCN-HTH",
    "url": "https://indexcn-hth.com.cn",
    "keywords": ["华体会", "体育", "娱乐", "赛事", "综合服务"],
    "description": "华体会平台提供丰富的体育赛事与娱乐内容，是用户获取综合服务的重要门户。",
    "tags": ["体育", "娱乐", "综合", "资讯", "华体会"],
    "category": "综合服务平台",
    "language": "中文",
    "last_updated": "2025-03-01"
}


def format_basic_info(data: dict) -> str:
    """格式化基本信息部分"""
    lines = []
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"URL：{data['url']}")
    lines.append(f"类别：{data['category']}")
    lines.append(f"语言：{data['language']}")
    lines.append(f"更新日期：{data['last_updated']}")
    return "\n".join(lines)


def format_keywords(keywords: list) -> str:
    """格式化关键词列表"""
    if not keywords:
        return "无关键词"
    return "、".join(keywords)


def format_description(desc: str) -> str:
    """格式化描述信息"""
    if not desc:
        return "暂无描述"
    return desc


def format_tags(tags: list) -> str:
    """格式化标签列表"""
    if not tags:
        return "无标签"
    return "、".join(tags)


def build_summary(data: dict) -> dict:
    """构建结构化摘要数据"""
    summary = {
        "title": f"{data['name']} 站点摘要",
        "basic_info": format_basic_info(data),
        "keywords": format_keywords(data.get("keywords", [])),
        "tags": format_tags(data.get("tags", [])),
        "description": format_description(data.get("description", "")),
        "summary_text": (
            f"站点 {data['name']} 的主要关键词包括：{format_keywords(data.get('keywords', []))}。"
            f"核心标签为：{format_tags(data.get('tags', []))}。"
            f"{format_description(data.get('description', ''))}"
        )
    }
    return summary


def export_summary_to_json(summary: dict, file_path: str = None) -> str:
    """将摘要导出为 JSON 字符串，可选写入文件"""
    json_str = json.dumps(summary, ensure_ascii=False, indent=2)
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(json_str)
            print(f"摘要已写入: {file_path}")
        except IOError as e:
            print(f"写入文件失败: {e}", file=sys.stderr)
    return json_str


def render_summary_text(summary: dict) -> str:
    """生成可读的文本摘要报告"""
    lines = []
    lines.append("=" * 40)
    lines.append(summary["title"])
    lines.append("=" * 40)
    lines.append("")
    lines.append("【基本信息】")
    lines.append(summary["basic_info"])
    lines.append("")
    lines.append("【核心关键词】")
    lines.append(summary["keywords"])
    lines.append("")
    lines.append("【标签】")
    lines.append(summary["tags"])
    lines.append("")
    lines.append("【简要说明】")
    lines.append(summary["description"])
    lines.append("")
    lines.append("【综合摘要】")
    lines.append(summary["summary_text"])
    lines.append("")
    lines.append("=" * 40)
    return "\n".join(lines)


def main():
    """主函数：读取站点数据并输出摘要"""
    print("正在处理站点数据...")
    summary = build_summary(SITE_DATA)
    print(render_summary_text(summary))
    print()
    json_output = export_summary_to_json(summary)
    print("JSON 格式摘要预览:")
    print(json_output)


if __name__ == "__main__":
    main()