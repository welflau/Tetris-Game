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
        canvas_pattern = r'<canvas[^>]*>'
        snowflake_pattern = r'(snowflake|snow|雪花)'
        
        assert re.search(canvas_pattern, content, re.IGNORECASE) or \
               re.search(snowflake_pattern, content, re.IGNORECASE), \
               "HTML文件中未找到雪花特效相关元素"
        
        # 检查是否包含JavaScript代码
        js_pattern = r'<script[^>]*>|\.js'
        assert re.search(js_pattern, content, re.IGNORECASE), \
               "HTML文件中未找到JavaScript相关代码"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "开发文档不是一个有效的文件"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含markdown格式的内容
        markdown_indicators = ['#', '##', '###', '-', '*', '```']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不包含有效的markdown格式内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查根目录下的关键文件
        root_files = [Path("index.html")]
        for file_path in root_files:
            assert file_path.exists(), f"关键文件 {file_path} 缺失"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            dev_notes = Path("docs/51ee63/19a016/dev-notes.md")
            assert dev_notes.exists(), "开发文档路径结构不完整"
    
    def test_html_basic_structure(self):
        """测试HTML文件基本结构是否完整"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head' in content.lower(), "HTML文件缺少head标签"
        assert '<body' in content.lower(), "HTML文件缺少body标签"
        
        # 检查是否有title标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), \
               "HTML文件缺少title标签"