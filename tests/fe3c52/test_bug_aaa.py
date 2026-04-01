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
        """测试 index.html 文件是否包含标题AAA相关内容"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查页面是否有title标签
        title_tag = soup.find('title')
        assert title_tag is not None, "页面缺少title标签"
        
        # 检查title内容或页面中是否包含AAA
        title_text = title_tag.get_text() if title_tag else ""
        page_text = soup.get_text()
        
        assert "AAA" in title_text or "AAA" in page_text, "页面标题或内容中未找到AAA"
    
    def test_index_html_has_basic_structure(self):
        """测试 index.html 文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
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
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_bug_info(self):
        """测试开发文档是否包含BUG相关信息"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档中是否包含BUG相关关键词
        keywords = ["BUG", "bug", "标题", "AAA", "显示", "页面"]
        found_keywords = [keyword for keyword in keywords if keyword in content]
        
        assert len(found_keywords) > 0, f"开发文档中未找到相关关键词: {keywords}"
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否正确"""
        # 检查根目录文件
        assert Path("index.html").exists(), "根目录缺少index.html文件"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists() and docs_dir.is_dir(), "docs目录不存在"
        
        fe3c52_dir = Path("docs/fe3c52")
        assert fe3c52_dir.exists() and fe3c52_dir.is_dir(), "docs/fe3c52目录不存在"
        
        final_dir = Path("docs/fe3c52/3ba7c2")
        assert final_dir.exists() and final_dir.is_dir(), "docs/fe3c52/3ba7c2目录不存在"
        
        dev_notes = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes.exists() and dev_notes.is_file(), "dev-notes.md文件不存在"