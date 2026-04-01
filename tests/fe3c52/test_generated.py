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
        
        # 检查title标签是否存在
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件中缺少title标签"
        
        # 检查title内容是否包含AAA或相关内容
        title_text = title_tag.get_text().strip()
        assert len(title_text) > 0, "页面标题为空"
        
        # 检查是否有h1标签作为页面主标题
        h1_tags = soup.find_all('h1')
        assert len(h1_tags) > 0, "页面缺少h1主标题标签"
    
    def test_index_html_has_basic_structure(self):
        """测试 index.html 文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        html_tag = soup.find('html')
        assert html_tag is not None, "缺少html根标签"
        
        head_tag = soup.find('head')
        assert head_tag is not None, "缺少head标签"
        
        body_tag = soup.find('body')
        assert body_tag is not None, "缺少body标签"
        
        # 检查meta标签
        meta_tags = soup.find_all('meta')
        assert len(meta_tags) > 0, "缺少meta标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "dev-notes.md 文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含markdown格式的标题
        lines = content.split('\n')
        has_markdown_header = any(line.strip().startswith('#') for line in lines)
        assert has_markdown_header, "开发文档缺少markdown格式的标题"
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否正确"""
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个目录"
        
        fe3c52_dir = Path("docs/fe3c52")
        assert fe3c52_dir.exists(), "docs/fe3c52目录不存在"
        assert fe3c52_dir.is_dir(), "docs/fe3c52不是一个目录"
        
        final_dir = Path("docs/fe3c52/3ba7c2")
        assert final_dir.exists(), "docs/fe3c52/3ba7c2目录不存在"
        assert final_dir.is_dir(), "docs/fe3c52/3ba7c2不是一个目录"