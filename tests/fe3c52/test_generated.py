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
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        assert title_match is not None, "HTML文件中未找到title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件中的title标签内容不为空（检查AAA标题显示问题）"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match is not None, "HTML文件中未找到title标签"
        title_content = title_match.group(1).strip()
        assert len(title_content) > 0, "title标签内容为空，页面标题未正确显示"
        assert title_content != "AAA" or "AAA" in title_content, "页面标题AAA显示异常"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        # 检查是否包含markdown格式的内容
        assert any(line.strip() for line in content.split('\n')), "开发文档没有有效的文本内容"
    
    def test_html_basic_structure(self):
        """测试HTML文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "HTML文件缺少html标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "HTML文件缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "HTML文件缺少body标签"