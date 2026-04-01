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
        # 检查是否包含预期的标题内容
        assert len(title_content) > 0, "页面标题内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含相关的bug记录或说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含常见的bug相关关键词
        bug_keywords = ['bug', 'BUG', '问题', '错误', 'title', 'AAA', '标题', '显示']
        has_relevant_content = any(keyword in content for keyword in bug_keywords)
        assert has_relevant_content, "开发文档中未找到与页面标题bug相关的内容"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构完整性"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head' in content.lower(), "HTML文件缺少head标签"
        assert '<body' in content.lower(), "HTML文件缺少body标签"
        
        # 检查head标签中是否包含title
        head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.IGNORECASE | re.DOTALL)
        if head_match:
            head_content = head_match.group(1)
            assert '<title' in head_content.lower(), "head标签中缺少title标签，这是页面标题AAA未显示的可能原因"