import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestOtherModule:
    """测试 other 模块的相关功能"""
    
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
    
    def test_index_html_title_content_not_empty(self):
        """测试 index.html 文件的 title 标签内容不为空（检查标题AAA显示问题）"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        title_element = soup.find('title')
        assert title_element is not None, "HTML 文件中缺少 title 标签"
        
        title_text = title_element.get_text().strip()
        assert title_text != "", "页面标题内容为空，可能导致标题AAA未显示的问题"
        assert len(title_text) > 0, "页面标题长度为0，标题未正确设置"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert content != "", "开发文档内容为空"
        assert len(content) > 10, "开发文档内容过短，可能不是有效的文档"
    
    def test_html_basic_structure(self):
        """测试 HTML 文件是否具有基本的 HTML 结构"""
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