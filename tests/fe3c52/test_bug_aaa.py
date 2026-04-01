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
        """测试index.html文件中的title标签内容不为空（针对AAA未显示的bug）"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_pattern = r'<title[^>]*>(.*?)</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        
        assert title_match, "未找到title标签"
        title_content = title_match.group(1).strip()
        assert title_content, "title标签内容为空，页面标题未正确设置"
        assert len(title_content) > 0, "title内容长度为0"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_bug_documentation(self):
        """测试开发文档是否包含相关bug记录或说明"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        # 检查是否包含bug相关关键词
        bug_keywords = ['bug', 'BUG', '标题', 'title', 'AAA', '显示', '问题']
        has_bug_info = any(keyword in content for keyword in bug_keywords)
        assert has_bug_info, "开发文档中未找到相关bug信息记录"
    
    def test_html_structure_validity(self):
        """测试HTML文件基本结构的有效性"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head' in content.lower(), "HTML文件缺少head标签"
        assert '<body' in content.lower(), "HTML文件缺少body标签"
        
        # 检查title标签是否在head标签内
        head_pattern = r'<head[^>]*>(.*?)</head>'
        head_match = re.search(head_pattern, content, re.IGNORECASE | re.DOTALL)
        if head_match:
            head_content = head_match.group(1)
            assert '<title' in head_content.lower(), "title标签应该位于head标签内"