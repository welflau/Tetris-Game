import pytest
from pathlib import Path
import re

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试index.html文件是否包含title标签元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查是否包含title标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML文件中未找到title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件中的title标签内容不为空，解决标题AAA未显示的问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match, "HTML文件中未找到title标签"
        title_content = title_match.group(1).strip()
        assert title_content, "title标签内容为空，这可能是导致页面标题AAA未显示的原因"
        assert len(title_content) > 0, "title标签内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档路径不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含关于页面标题问题的说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        # 检查文档是否包含标题相关的内容
        title_keywords = ['标题', 'title', 'AAA', '显示']
        has_title_content = any(keyword in content for keyword in title_keywords)
        assert has_title_content, "开发文档中未找到与页面标题相关的内容"
    
    def test_html_basic_structure_validity(self):
        """测试HTML文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "HTML文件缺少html开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "HTML文件缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "HTML文件缺少body标签"