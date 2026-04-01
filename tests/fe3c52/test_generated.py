import pytest
from pathlib import Path
from bs4 import BeautifulSoup

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
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        title_element = soup.find('title')
        assert title_element is not None, "HTML 文件中缺少 title 标签"
    
    def test_index_html_title_displays_aaa(self):
        """测试 index.html 文件的标题是否正确显示 AAA"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        title_element = soup.find('title')
        assert title_element is not None, "HTML 文件中缺少 title 标签"
        
        title_text = title_element.get_text().strip()
        assert "AAA" in title_text, f"页面标题 '{title_text}' 中未包含 'AAA'"
    
    def test_dev_notes_markdown_file_exists(self):
        """测试开发文档 markdown 文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_html_has_basic_structure(self):
        """测试 HTML 文件是否具有基本的页面结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本的 HTML 结构元素
        html_element = soup.find('html')
        head_element = soup.find('head')
        body_element = soup.find('body')
        
        assert html_element is not None, "HTML 文件缺少 html 标签"
        assert head_element is not None, "HTML 文件缺少 head 标签"
        assert body_element is not None, "HTML 文件缺少 body 标签"