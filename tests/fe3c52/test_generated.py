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
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML文件中缺少title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件的title标签内容不为空，解决标题AAA未显示的问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        assert title_match, "未找到title标签"
        
        title_content = title_match.group(1).strip()
        assert title_content, "title标签内容为空，这可能是导致页面标题AAA未显示的原因"
        assert len(title_content) > 0, "title标签内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_html_basic_structure(self):
        """测试HTML文件是否包含基本的HTML结构元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body标签"
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否正确"""
        # 检查docs目录结构
        docs_dir = Path("docs")
        fe3c52_dir = Path("docs/fe3c52")
        target_dir = Path("docs/fe3c52/3ba7c2")
        
        assert docs_dir.exists() and docs_dir.is_dir(), "docs目录不存在"
        assert fe3c52_dir.exists() and fe3c52_dir.is_dir(), "docs/fe3c52目录不存在"
        assert target_dir.exists() and target_dir.is_dir(), "docs/fe3c52/3ba7c2目录不存在"