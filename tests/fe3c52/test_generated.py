import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_title_aaa(self):
        """测试index.html文件是否包含标题AAA"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查title标签是否存在
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件中缺少title标签"
        
        # 检查title内容是否包含AAA
        title_text = title_tag.get_text().strip()
        assert 'AAA' in title_text, f"页面标题'{title_text}'中未包含'AAA'"
    
    def test_index_html_has_basic_structure(self):
        """测试index.html文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "缺少html标签"
        assert soup.find('head') is not None, "缺少head标签"
        assert soup.find('body') is not None, "缺少body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert len(content) > 0, "开发文档内容为空"
        assert content.count('\n') >= 0, "文档应该包含文本内容"