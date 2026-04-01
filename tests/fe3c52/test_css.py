import pytest
from pathlib import Path
import re

class TestTitleCSSStyles:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), f"HTML文件不存在: {html_file}"
        assert html_file.is_file(), f"路径不是文件: {html_file}"
    
    def test_html_contains_title_elements(self):
        """测试HTML文件是否包含标题相关元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含标题标签
        title_tags = ['<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<title']
        has_title_tag = any(tag in content.lower() for tag in title_tags)
        assert has_title_tag, "HTML文件中未找到标题标签"
        
        # 检查是否包含CSS样式引用
        has_css = any(pattern in content.lower() for pattern in ['<style', 'stylesheet', '.css'])
        assert has_css, "HTML文件中未找到CSS样式引用"
    
    def test_html_title_css_classes_or_styles(self):
        """测试HTML文件中标题元素是否包含CSS类名或样式"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 使用正则表达式查找标题标签
        title_pattern = r'<h[1-6][^>]*>'
        title_matches = re.findall(title_pattern, content, re.IGNORECASE)
        
        if title_matches:
            # 检查标题标签是否包含class或style属性
            has_styling = any(
                'class=' in match.lower() or 'style=' in match.lower() 
                for match in title_matches
            )
            assert has_styling, "标题元素缺少CSS类名或样式属性"
        else:
            # 如果没有h标签，检查是否有CSS样式定义
            css_title_selectors = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']
            has_title_css = any(selector in content.lower() for selector in css_title_selectors)
            assert has_title_css, "未找到标题相关的CSS样式定义"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        notes_file = Path("docs/fe3c52/93f04c/dev-notes.md")
        assert notes_file.exists(), f"开发文档文件不存在: {notes_file}"
        assert notes_file.is_file(), f"路径不是文件: {notes_file}"
    
    def test_dev_notes_contains_css_documentation(self):
        """测试开发文档是否包含CSS样式相关内容"""
        notes_file = Path("docs/fe3c52/93f04c/dev-notes.md")
        if notes_file.exists():
            content = notes_file.read_text(encoding='utf-8')
            
            # 检查是否包含CSS或样式相关关键词
            css_keywords = ['css', '样式', 'style', '标题', 'title', 'h1', 'h2', 'h3']
            has_css_content = any(keyword in content.lower() for keyword in css_keywords)
            assert has_css_content, "开发文档中未找到CSS样式相关内容"