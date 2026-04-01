import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestFrontendHTMLStructure:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试index.html文件是否包含标题元素"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否包含title标签
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件中缺少<title>标签"
        
        # 检查title标签是否有内容
        assert title_tag.get_text().strip() != "", "title标签内容为空"
    
    def test_index_html_has_proper_html_structure(self):
        """测试index.html文件是否具有正确的HTML基本结构"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        html_tag = soup.find('html')
        assert html_tag is not None, "HTML文件缺少<html>标签"
        
        head_tag = soup.find('head')
        assert head_tag is not None, "HTML文件缺少<head>标签"
        
        body_tag = soup.find('body')
        assert body_tag is not None, "HTML文件缺少<body>标签"
        
        # 确保title标签在head标签内
        title_in_head = head_tag.find('title')
        assert title_in_head is not None, "title标签应该位于head标签内"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/2e9404/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含相关内容"""
        dev_notes_file = Path("docs/fe3c52/2e9404/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        
        # 检查是否包含与HTML标题相关的关键词
        content_lower = content.lower()
        title_keywords = ['title', '标题', 'html', 'head']
        has_relevant_content = any(keyword in content_lower for keyword in title_keywords)
        assert has_relevant_content, "开发文档应包含与HTML标题相关的内容"