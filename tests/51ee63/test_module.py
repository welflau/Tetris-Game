import pytest
from pathlib import Path
import re

class TestSnowflakeGeneratorFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在于 {frontend_dir} 目录中"
        assert index_file.is_file(), "index.html 应该是一个文件而不是目录"
    
    def test_index_html_contains_snowflake_elements(self):
        """测试 index.html 是否包含雪花生成器相关的关键元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件应包含html标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "HTML文件应包含head标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "HTML文件应包含body标签"
        
        # 检查雪花生成器相关元素
        snowflake_keywords = ['snowflake', '雪花', 'generator', '生成器', 'id']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML文件应包含雪花生成器相关的关键词"
    
    def test_index_html_has_interactive_elements(self):
        """测试 index.html 是否包含交互元素用于雪花ID生成"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含按钮或输入框等交互元素
        interactive_elements = [
            r'<button[^>]*>',
            r'<input[^>]*>',
            r'<div[^>]*id[^>]*>',
            r'onclick\s*=',
            r'<script[^>]*>'
        ]
        
        has_interactive = any(re.search(pattern, content, re.IGNORECASE) for pattern in interactive_elements)
        assert has_interactive, "HTML文件应包含按钮、输入框或脚本等交互元素"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档是否存在且可读"""
        docs_path = Path("docs/51ee63/cfce01/dev-notes.md")
        assert docs_path.exists(), f"开发文档不存在于 {docs_path}"
        assert docs_path.is_file(), "dev-notes.md 应该是一个文件"
        
        # 测试文件是否可读且不为空
        with open(docs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert len(content.strip()) > 0, "开发文档不应为空"
        assert any(keyword in content.lower() for keyword in ['snowflake', '雪花', 'frontend', '前端']), \
            "开发文档应包含项目相关内容"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否合理"""
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录应该存在"
        assert frontend_dir.is_dir(), "frontend 应该是一个目录"
        
        # 检查是否有其他常见的前端文件
        files_in_frontend = list(frontend_dir.iterdir())
        assert len(files_in_frontend) > 0, "frontend 目录不应为空"
        
        # 检查 index.html 是否在文件列表中
        html_files = [f for f in files_in_frontend if f.suffix == '.html']
        assert len(html_files) >= 1, "frontend 目录应至少包含一个HTML文件"