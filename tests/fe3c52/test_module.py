import pytest
from pathlib import Path
import re

class TestDesignModule:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("design/index.html")
        assert html_file.exists(), f"HTML文件不存在: {html_file}"
        assert html_file.is_file(), f"路径不是文件: {html_file}"
    
    def test_html_contains_title_elements(self):
        """测试HTML文件是否包含标题相关的关键元素"""
        html_file = Path("design/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含标题标签
        title_tags = re.findall(r'<h[1-6][^>]*>.*?</h[1-6]>', content, re.IGNORECASE | re.DOTALL)
        assert len(title_tags) > 0, "HTML文件中未找到标题标签(h1-h6)"
        
        # 检查是否包含CSS样式相关内容
        has_style = '<style>' in content or 'class=' in content or '.css' in content
        assert has_style, "HTML文件中未找到样式相关内容"
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "HTML文件缺少body标签"
    
    def test_dev_notes_file_exists_and_content(self):
        """测试开发文档是否存在并包含相关内容"""
        notes_file = Path("design/docs/fe3c52/12a146/dev-notes.md")
        assert notes_file.exists(), f"开发文档不存在: {notes_file}"
        assert notes_file.is_file(), f"路径不是文件: {notes_file}"
        
        content = notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含标题样式相关关键词
        keywords = ['标题', '样式', 'title', 'style', 'design', 'h1', 'h2', 'h3', 'css']
        has_relevant_content = any(keyword.lower() in content.lower() for keyword in keywords)
        assert has_relevant_content, "开发文档中未找到与标题样式相关的内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        design_dir = Path("design")
        assert design_dir.exists(), "design目录不存在"
        assert design_dir.is_dir(), "design不是目录"
        
        docs_dir = Path("design/docs")
        assert docs_dir.exists(), "docs目录不存在"
        
        # 检查文档目录结构
        fe3c52_dir = Path("design/docs/fe3c52")
        assert fe3c52_dir.exists(), "fe3c52目录不存在"
        
        dev_notes_dir = Path("design/docs/fe3c52/12a146")
        assert dev_notes_dir.exists(), "12a146目录不存在"
    
    def test_html_title_styling_features(self):
        """测试HTML文件中标题样式功能特性"""
        html_file = Path("design/index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否有多级标题
        h1_count = len(re.findall(r'<h1[^>]*>.*?</h1>', content, re.IGNORECASE | re.DOTALL))
        h2_count = len(re.findall(r'<h2[^>]*>.*?</h2>', content, re.IGNORECASE | re.DOTALL))
        h3_count = len(re.findall(r'<h3[^>]*>.*?</h3>', content, re.IGNORECASE | re.DOTALL))
        
        total_headings = h1_count + h2_count + h3_count
        assert total_headings >= 2, "应该包含至少2个不同级别的标题来展示样式方案"
        
        # 检查是否有样式定义
        style_definitions = re.findall(r'(font-size|color|font-weight|margin|padding|text-align)', content, re.IGNORECASE)
        assert len(style_definitions) > 0, "HTML文件中应包含标题样式定义"