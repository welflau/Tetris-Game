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
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_bug_info(self):
        """测试开发文档是否包含相关的 bug 信息"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档是否包含相关关键词
        keywords = ["标题", "AAA", "显示", "BUG", "bug"]
        found_keywords = [keyword for keyword in keywords if keyword in content]
        assert len(found_keywords) > 0, f"开发文档中未找到相关关键词: {keywords}"