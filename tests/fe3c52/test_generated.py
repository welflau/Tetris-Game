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
        """测试index.html文件的title标签内容不为空，验证页面标题AAA显示问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        assert title_match, "未找到title标签"
        
        title_content = title_match.group(1).strip()
        assert title_content, "title标签内容为空，这可能是页面标题AAA未显示的原因"
        # 检查是否包含预期的标题内容AAA
        assert "AAA" in title_content, "页面标题中未包含预期的'AAA'文本"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档dev-notes.md文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含相关的bug记录或说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档dev-notes.md文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert content.strip(), "开发文档内容为空"
        # 检查是否包含与标题相关的关键词
        keywords = ["标题", "title", "AAA", "显示", "页面"]
        has_relevant_content = any(keyword in content for keyword in keywords)
        assert has_relevant_content, "开发文档中未找到与页面标题相关的内容记录"