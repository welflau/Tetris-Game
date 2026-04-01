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
        """测试index.html文件中是否包含标题AAA相关元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查title标签是否存在
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件中缺少title标签"
        
        # 检查是否包含AAA标题
        title_text = title_tag.get_text().strip()
        assert 'AAA' in title_text or title_text == 'AAA', f"页面标题应包含'AAA'，实际标题为: {title_text}"
    
    def test_index_html_basic_structure(self):
        """测试index.html文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        html_tag = soup.find('html')
        assert html_tag is not None, "HTML文件缺少html标签"
        
        head_tag = soup.find('head')
        assert head_tag is not None, "HTML文件缺少head标签"
        
        body_tag = soup.find('body')
        assert body_tag is not None, "HTML文件缺少body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_content_not_empty(self):
        """测试开发文档文件内容不为空"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert len(content) > 0, "dev-notes.md文件内容为空"
        assert content != "", "开发文档应包含实际内容"