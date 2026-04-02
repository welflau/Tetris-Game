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
        
        # 检查是否包含canvas元素或雪花相关的div
        assert re.search(r'<canvas|<div.*snow|snow.*>', content, re.IGNORECASE), \
            "HTML文件中未找到canvas元素或雪花相关容器"
        
        # 检查是否包含JavaScript代码或引用
        assert re.search(r'<script|\.js', content, re.IGNORECASE), \
            "HTML文件中未找到JavaScript代码或引用"
        
        # 检查是否包含CSS样式或引用
        assert re.search(r'<style|\.css|style=', content, re.IGNORECASE), \
            "HTML文件中未找到CSS样式或引用"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "开发文档不是一个有效的文件"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含markdown格式的内容
        markdown_indicators = ['#', '##', '###', '*', '-', '`', '```']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不包含有效的markdown格式内容"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构有效性"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head' in content.lower(), "HTML文件缺少head标签"
        assert '<body' in content.lower(), "HTML文件缺少body标签"
        
        # 检查标签配对（简单检查）
        html_count = content.lower().count('<html')
        html_close_count = content.lower().count('</html>')
        assert html_count == html_close_count, "HTML标签未正确闭合"
    
    def test_project_file_structure(self):
        """测试项目文件结构的完整性"""
        # 检查主要文件是否存在
        required_files = [
            Path("index.html"),
            Path("docs/51ee63/19a016/dev-notes.md")
        ]
        
        for file_path in required_files:
            assert file_path.exists(), f"必需的文件 {file_path} 不存在"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs应该是一个目录"
            
        # 检查是否有其他可能的资源文件
        current_dir = Path(".")
        js_files = list(current_dir.glob("*.js"))
        css_files = list(current_dir.glob("*.css"))
        
        # 如果存在JS或CSS文件，验证它们是有效文件
        for js_file in js_files:
            assert js_file.stat().st_size > 0, f"JavaScript文件 {js_file} 为空"
            
        for css_file in css_files:
            assert css_file.stat().st_size > 0, f"CSS文件 {css_file} 为空"