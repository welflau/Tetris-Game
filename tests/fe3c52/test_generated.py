import pytest
from pathlib import Path
import re

class TestOtherModule:
    """测试 other 模块的相关功能"""
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试 index.html 文件是否包含 title 标签"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查是否包含 title 标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML 文件中未找到 title 标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试 index.html 文件的 title 标签内容不为空"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取 title 标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match, "未找到 title 标签"
        title_content = title_match.group(1).strip()
        assert title_content, "title 标签内容为空，这可能是导致页面标题AAA未显示的原因"
        assert len(title_content) > 0, "title 标签内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        # 检查是否包含常见的 markdown 元素
        has_content = any([
            content.strip().startswith('#'),  # 标题
            '##' in content,  # 二级标题
            len(content.split('\n')) > 1  # 多行内容
        ])
        assert has_content, "开发文档似乎没有包含有效的 markdown 内容"
    
    def test_html_basic_structure(self):
        """测试 HTML 文件是否具有基本的 HTML 结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本的 HTML 结构元素
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少 html 开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少 head 标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少 body 标签"
        
        # 检查标签是否正确闭合
        assert '</html>' in content.lower(), "缺少 html 结束标签"
        assert '</head>' in content.lower(), "缺少 head 结束标签"
        assert '</body>' in content.lower(), "缺少 body 结束标签"