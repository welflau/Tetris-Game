import pytest
from pathlib import Path
import re

class TestSnowflakeEffectIntegration:
    
    def test_html_file_exists(self):
        """测试雪花特效的HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效的关键元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在，无法进行内容测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素（通常用于雪花动画）
        assert re.search(r'<canvas|canvas', content, re.IGNORECASE), "HTML中缺少canvas元素"
        
        # 检查是否包含JavaScript相关内容
        assert re.search(r'<script|\.js|javascript', content, re.IGNORECASE), "HTML中缺少JavaScript相关内容"
        
        # 检查是否包含雪花相关的关键词
        snowflake_keywords = ['snow', 'flake', '雪花', 'particle', 'animation']
        has_snowflake_keyword = any(keyword.lower() in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_keyword, "HTML内容中缺少雪花特效相关关键词"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档dev-notes.md不存在"
        assert docs_file.is_file(), "dev-notes.md不是一个有效的文件"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含Markdown格式的内容
        markdown_indicators = ['#', '##', '###', '*', '-', '```']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不包含有效的Markdown格式内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查根目录下的HTML文件
        assert Path("index.html").exists(), "项目根目录缺少index.html"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个有效的目录"
        
        # 检查嵌套的文档目录结构
        nested_dir = Path("docs/51ee63/19a016")
        assert nested_dir.exists(), "嵌套的文档目录结构不完整"
        assert nested_dir.is_dir(), "嵌套路径不是有效目录"
    
    def test_html_file_size_reasonable(self):
        """测试HTML文件大小是否合理（不为空且不过大）"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        file_size = html_file.stat().st_size
        assert file_size > 0, "HTML文件为空"
        assert file_size < 10 * 1024 * 1024, "HTML文件过大（超过10MB）"  # 10MB限制
        
        # 检查文件内容行数是否合理
        content = html_file.read_text(encoding='utf-8')
        lines = content.split('\n')
        assert len(lines) > 5, "HTML文件内容过少，可能不完整"