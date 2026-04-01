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
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML文件中缺少title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件中的title标签内容不为空，验证页面标题AAA显示问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        assert title_match, "未找到title标签"
        
        title_content = title_match.group(1).strip()
        assert title_content, "title标签内容为空，这可能是页面标题未显示的原因"
        
        # 检查是否包含预期的标题内容AAA
        assert "AAA" in title_content, f"页面标题中未包含预期的'AAA'文本，当前标题为: {title_content}"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档dev-notes.md文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含关于页面标题bug的相关说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        # 检查文档是否包含标题相关的内容
        title_keywords = ["标题", "title", "AAA", "显示", "bug"]
        found_keywords = [keyword for keyword in title_keywords if keyword.lower() in content.lower()]
        assert len(found_keywords) > 0, f"开发文档中未找到与页面标题相关的关键词，应包含: {title_keywords}"
    
    def test_html_basic_structure_validity(self):
        """测试HTML文件是否具有基本的HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "HTML文件缺少html开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "HTML文件缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "HTML文件缺少body标签"
        
        # 确保title标签在head部分
        head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.IGNORECASE | re.DOTALL)
        if head_match:
            head_content = head_match.group(1)
            assert re.search(r'<title[^>]*>.*?</title>', head_content, re.IGNORECASE | re.DOTALL), "title标签应该位于head标签内部"