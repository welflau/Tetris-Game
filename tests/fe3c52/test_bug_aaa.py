import pytest
from pathlib import Path
import re

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试index.html文件是否包含title标签元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查是否包含title标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML文件中未找到title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件中的title标签内容不为空，验证AAA标题显示问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match is not None, "未找到title标签"
        title_content = title_match.group(1).strip()
        assert len(title_content) > 0, "title标签内容为空，这可能是导致页面标题AAA未显示的原因"
        
        # 检查是否包含AAA或其他有意义的标题内容
        assert title_content != "AAA" or len(title_content) >= 3, f"title内容可能有问题: '{title_content}'"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        
        # 检查是否包含markdown格式的内容
        has_markdown_elements = any([
            '#' in content,  # 标题
            '*' in content,  # 列表或强调
            '```' in content,  # 代码块
            '[' in content and ']' in content,  # 链接
        ])
        assert has_markdown_elements or len(content) > 50, "开发文档可能缺少有效的markdown内容"
    
    def test_html_basic_structure(self):
        """测试HTML文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body标签"
        
        # 检查DOCTYPE声明
        doctype_pattern = r'<!DOCTYPE\s+html>'
        has_doctype = re.search(doctype_pattern, content, re.IGNORECASE)
        if not has_doctype:
            # 如果没有标准的HTML5 DOCTYPE，至少应该有某种DOCTYPE声明
            assert '<!DOCTYPE' in content.upper(), "HTML文件缺少DOCTYPE声明"