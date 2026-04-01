import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_title_aaa(self):
        """测试 index.html 文件是否包含页面标题AAA"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查title标签是否存在且包含AAA
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件中未找到title标签"
        assert 'AAA' in title_tag.get_text(), "页面标题中未包含'AAA'"
    
    def test_index_html_has_basic_structure(self):
        """测试 index.html 文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "HTML文件缺少html标签"
        assert soup.find('head') is not None, "HTML文件缺少head标签"
        assert soup.find('body') is not None, "HTML文件缺少body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert len(content) > 0, "dev-notes.md 文件内容为空"
        assert content.count('\n') >= 0, "dev-notes.md 文件应包含文档内容"
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否正确"""
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs 目录不存在"
        assert docs_dir.is_dir(), "docs 不是一个有效的目录"
        
        fe3c52_dir = Path("docs/fe3c52")
        assert fe3c52_dir.exists(), "docs/fe3c52 目录不存在"
        assert fe3c52_dir.is_dir(), "docs/fe3c52 不是一个有效的目录"
        
        final_dir = Path("docs/fe3c52/3ba7c2")
        assert final_dir.exists(), "docs/fe3c52/3ba7c2 目录不存在"
        assert final_dir.is_dir(), "docs/fe3c52/3ba7c2 不是一个有效的目录"