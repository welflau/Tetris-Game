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
        """测试index.html文件中的title标签内容不为空（用于检测AAA标题显示问题）"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        assert title_match is not None, "未找到title标签"
        
        title_content = title_match.group(1).strip()
        assert title_content != "", "title标签内容为空"
        assert len(title_content) > 0, "title标签内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档路径不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含相关的bug记录或说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        # 检查是否包含bug相关的关键词
        bug_keywords = ['bug', 'BUG', '问题', '标题', 'title', 'AAA']
        has_bug_info = any(keyword in content for keyword in bug_keywords)
        assert has_bug_info, "开发文档中未找到相关的bug记录或说明"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构完整性"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html开始标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head开始标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body开始标签"
        
        # 检查标签是否正确闭合
        assert '</html>' in content.lower(), "缺少html结束标签"
        assert '</head>' in content.lower(), "缺少head结束标签"
        assert '</body>' in content.lower(), "缺少body结束标签"