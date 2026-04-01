import pytest
from pathlib import Path
import re

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试 index.html 文件是否包含 title 标签元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查是否包含 title 标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML 文件中未找到 title 标签"
    
    def test_index_html_title_contains_aaa(self):
        """测试 index.html 文件的 title 标签是否包含 AAA 文本内容"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取 title 标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match, "HTML 文件中未找到 title 标签"
        title_content = title_match.group(1).strip()
        assert "AAA" in title_content, f"页面标题 '{title_content}' 中未包含 'AAA' 文本"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_html_basic_structure(self):
        """测试 HTML 文件是否包含基本的 HTML 结构元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本的 HTML 结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "HTML 文件缺少 html 标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "HTML 文件缺少 head 标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "HTML 文件缺少 body 标签"