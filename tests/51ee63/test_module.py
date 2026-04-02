import pytest
from pathlib import Path
import re

class TestSnowflakeEffect:
    """雪花特效集成测试类"""
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效相关的关键元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在，无法进行内容测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素（通常用于雪花动画）
        assert re.search(r'<canvas[^>]*>', content, re.IGNORECASE), "HTML中缺少canvas元素"
        
        # 检查是否包含JavaScript相关内容
        js_patterns = [
            r'<script[^>]*>',
            r'\.js["\']',
            r'snowflake',
            r'snow'
        ]
        
        has_js = any(re.search(pattern, content, re.IGNORECASE) for pattern in js_patterns)
        assert has_js, "HTML中缺少JavaScript相关内容或雪花特效相关代码"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构完整性"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少DOCTYPE声明"
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body标签"
        
        # 检查标签配对
        open_tags = len(re.findall(r'<html[^>]*>', content, re.IGNORECASE))
        close_tags = len(re.findall(r'</html>', content, re.IGNORECASE))
        assert open_tags == close_tags, "html标签未正确闭合"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "开发文档不是一个有效的文件"
        assert docs_file.suffix == '.md', "开发文档不是markdown格式"
    
    def test_dev_notes_content(self):
        """测试开发文档内容是否包含必要信息"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档不存在，无法进行内容测试"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含常见的开发文档关键词
        keywords = ['雪花', 'snowflake', '特效', 'effect', '开发', 'dev', '说明', '文档']
        has_keywords = any(keyword in content for keyword in keywords)
        assert has_keywords, "开发文档缺少相关关键词内容"
    
    def test_project_directory_structure(self):
        """测试项目目录结构的完整性"""
        # 检查根目录文件
        assert Path("index.html").exists(), "根目录缺少index.html"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个目录"
        
        # 检查嵌套目录结构
        nested_dir = Path("docs/51ee63/19a016")
        assert nested_dir.exists(), "嵌套文档目录不存在"
        assert nested_dir.is_dir(), "嵌套路径不是目录"
        
        # 检查开发文档
        dev_notes = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes.exists(), "开发文档不存在于指定路径"