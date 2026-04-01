import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    """前端文件测试类"""
    
    def test_index_html_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试index.html文件是否包含基本的HTML结构元素"""
        index_file = Path("frontend/index.html")
        
        # 确保文件存在
        assert index_file.exists(), "index.html文件不存在"
        
        # 读取文件内容
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少DOCTYPE声明"
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html标签"
        assert re.search(r'<head[^>]*>.*</head>', content, re.IGNORECASE | re.DOTALL), "缺少head标签"
        assert re.search(r'<body[^>]*>.*</body>', content, re.IGNORECASE | re.DOTALL), "缺少body标签"
        
        # 检查页面标题
        assert re.search(r'<title[^>]*>.*</title>', content, re.IGNORECASE | re.DOTALL), "缺少title标签"
    
    def test_index_html_contains_system_integration_content(self):
        """测试index.html文件是否包含系统集成相关的内容元素"""
        index_file = Path("frontend/index.html")
        
        # 确保文件存在
        assert index_file.exists(), "index.html文件不存在"
        
        # 读取文件内容
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否包含系统集成相关关键词（不区分大小写）
        integration_keywords = ['系统', 'system', '集成', 'integration', '优化', 'optimization']
        found_keywords = []
        
        for keyword in integration_keywords:
            if re.search(keyword, content, re.IGNORECASE):
                found_keywords.append(keyword)
        
        assert len(found_keywords) > 0, f"页面内容中未找到系统集成相关关键词，检查的关键词: {integration_keywords}"
        
        # 检查是否有基本的交互元素（按钮、表单、链接等）
        interactive_elements = [
            r'<button[^>]*>',
            r'<input[^>]*>',
            r'<form[^>]*>',
            r'<a[^>]*href',
            r'<div[^>]*class',
            r'<script[^>]*>'
        ]
        
        found_elements = []
        for element_pattern in interactive_elements:
            if re.search(element_pattern, content, re.IGNORECASE):
                found_elements.append(element_pattern)
        
        assert len(found_elements) > 0, "页面缺少基本的交互元素或样式结构"

    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/96c9f2/0b7485/dev-notes.md")
        
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        # 测试文件是否可读
        try:
            content = dev_notes_file.read_text(encoding='utf-8')
            assert len(content.strip()) > 0, "开发文档文件为空"
        except UnicodeDecodeError:
            # 如果UTF-8解码失败，尝试其他编码
            content = dev_notes_file.read_text(encoding='gbk')
            assert len(content.strip()) > 0, "开发文档文件为空"

    def test_dev_notes_contains_documentation_structure(self):
        """测试开发文档是否包含合理的文档结构"""
        dev_notes_file = Path("docs/96c9f2/0b7485/dev-notes.md")
        
        if not dev_notes_file.exists():
            pytest.skip("开发文档文件不存在，跳过结构测试")
        
        try:
            content = dev_notes_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            content = dev_notes_file.read_text(encoding='gbk')
        
        # 检查Markdown文档的基本结构元素
        markdown_elements = [
            r'^#+\s+',  # 标题
            r'```',     # 代码块
            r'\*\*.*\*\*',  # 粗体
            r'\*.*\*',  # 斜体
            r'^\s*[-*+]\s+',  # 列表项
            r'^\s*\d+\.\s+'   # 有序列表
        ]
        
        found_elements = []
        for pattern in markdown_elements:
            if re.search(pattern, content, re.MULTILINE):
                found_elements.append(pattern)
        
        assert len(found_elements) >= 2, f"开发文档缺少基本的Markdown结构元素，找到的元素数量: {len(found_elements)}"