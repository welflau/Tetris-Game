import pytest
from pathlib import Path
import re

class TestDesignTitleStyleProject:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_title_elements(self):
        """测试HTML文件是否包含标题相关的关键元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在，无法进行内容测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含HTML基本结构
        assert "<html" in content.lower(), "HTML文件缺少html标签"
        assert "<head>" in content.lower(), "HTML文件缺少head标签"
        assert "<body>" in content.lower(), "HTML文件缺少body标签"
        
        # 检查是否包含标题元素
        title_elements = ["<h1", "<h2", "<h3", "<title>"]
        has_title_element = any(element in content.lower() for element in title_elements)
        assert has_title_element, "HTML文件中没有找到标题相关元素(h1, h2, h3, title)"
    
    def test_html_contains_style_definitions(self):
        """测试HTML文件是否包含样式定义或样式引用"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在，无法进行样式测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含CSS样式定义或引用
        style_indicators = [
            "<style>",
            "stylesheet",
            ".css",
            "font-",
            "color:",
            "text-align",
            "font-size"
        ]
        
        has_style = any(indicator in content.lower() for indicator in style_indicators)
        assert has_style, "HTML文件中没有找到样式定义或样式相关内容"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        docs_file = Path("docs/fe3c52/12a146/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "dev-notes.md不是一个有效的文件"
        assert docs_file.suffix == ".md", "开发文档不是markdown格式"
    
    def test_dev_notes_contains_design_content(self):
        """测试开发文档是否包含设计相关内容"""
        docs_file = Path("docs/fe3c52/12a146/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在，无法进行内容测试"
        
        content = docs_file.read_text(encoding='utf-8')
        
        # 检查是否包含设计相关关键词
        design_keywords = [
            "标题", "样式", "设计", "title", "style", "design",
            "字体", "颜色", "布局", "font", "color", "layout"
        ]
        
        found_keywords = [keyword for keyword in design_keywords if keyword in content.lower()]
        assert len(found_keywords) > 0, f"开发文档中没有找到设计相关关键词，期望包含: {design_keywords}"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查项目根目录文件
        assert Path("index.html").exists(), "缺少主HTML文件"
        
        # 检查文档目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个目录"
        
        # 检查嵌套目录结构
        nested_dir = Path("docs/fe3c52/12a146")
        assert nested_dir.exists(), "嵌套文档目录结构不完整"
        assert nested_dir.is_dir(), "嵌套路径不是目录"
        
        # 检查开发文档
        dev_notes = Path("docs/fe3c52/12a146/dev-notes.md")
        assert dev_notes.exists(), "开发文档文件缺失"