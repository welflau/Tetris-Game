import pytest
from pathlib import Path
import re

class TestSnowflakeAnimationFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含雪花动画必需的HTML元素"""
        index_file = Path("frontend/index.html")
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<html" in content.lower(), "缺少 html 标签"
        assert "<head>" in content.lower(), "缺少 head 标签"
        assert "<body>" in content.lower(), "缺少 body 标签"
        
        # 检查雪花动画相关元素
        assert "canvas" in content.lower() or "div" in content.lower(), "缺少动画容器元素"
        assert "script" in content.lower() or ".js" in content, "缺少JavaScript脚本引用"
    
    def test_index_html_contains_snowflake_animation_keywords(self):
        """测试 index.html 文件包含雪花动画相关的关键词或样式"""
        index_file = Path("frontend/index.html")
        content = index_file.read_text(encoding='utf-8')
        
        # 检查雪花动画相关关键词（不区分大小写）
        snowflake_keywords = [
            "snow", "snowflake", "animation", "canvas", 
            "particle", "winter", "flake", "falling"
        ]
        
        content_lower = content.lower()
        found_keywords = [keyword for keyword in snowflake_keywords if keyword in content_lower]
        
        assert len(found_keywords) > 0, f"HTML文件中未找到雪花动画相关关键词，期望包含: {snowflake_keywords}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/51ee63/9cdd70/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        # 测试文件是否可读且不为空
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_dev_notes_contains_project_documentation(self):
        """测试开发文档包含项目相关的文档内容"""
        dev_notes_file = Path("docs/51ee63/9cdd70/dev-notes.md")
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查Markdown格式标识
        markdown_indicators = ["#", "##", "###", "*", "-", "`"]
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不是有效的Markdown格式"
        
        # 检查项目相关关键词
        project_keywords = [
            "雪花", "动画", "snowflake", "animation", "frontend", 
            "开发", "功能", "实现", "设计"
        ]
        
        content_lower = content.lower()
        found_keywords = [keyword for keyword in project_keywords if keyword.lower() in content_lower]
        
        assert len(found_keywords) > 0, f"开发文档中未找到项目相关关键词，期望包含: {project_keywords}"