import pytest
from pathlib import Path
import re

class TestSnowflakeEffect:
    """雪花特效集成测试类"""
    
    def test_index_html_exists(self):
        """测试 index.html 文件是否存在"""
        index_path = Path("index.html")
        assert index_path.exists(), "index.html 文件不存在"
        assert index_path.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_snowflake_elements(self):
        """测试 index.html 文件是否包含雪花特效相关的关键元素"""
        index_path = Path("index.html")
        assert index_path.exists(), "index.html 文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查HTML基本结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "HTML文件缺少body标签"
        
        # 检查雪花特效相关元素（可能的关键词）
        snowflake_keywords = ['snow', 'flake', '雪花', 'canvas', 'animation', 'particle']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML文件中未找到雪花特效相关内容"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在且包含有效内容"""
        docs_path = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_path.exists(), "开发文档 dev-notes.md 不存在"
        assert docs_path.is_file(), "dev-notes.md 不是一个有效的文件"
        
        content = docs_path.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含常见的文档结构元素
        doc_indicators = ['#', '##', '###', '- ', '* ', '1.', 'TODO', 'NOTE', '注意', '说明']
        has_doc_structure = any(indicator in content for indicator in doc_indicators)
        assert has_doc_structure, "开发文档缺少基本的文档结构标记"
    
    def test_html_canvas_or_script_elements(self):
        """测试 HTML 文件是否包含用于雪花特效的 canvas 或 script 元素"""
        index_path = Path("index.html")
        assert index_path.exists(), "index.html 文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或script标签
        has_canvas = '<canvas' in content.lower()
        has_script = '<script' in content.lower()
        has_js_file = '.js' in content.lower()
        
        assert has_canvas or has_script or has_js_file, "HTML文件中未找到用于实现雪花特效的canvas或script元素"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
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
            assert docs_dir.is_dir(), "docs 应该是一个目录"
    
    def test_html_file_encoding_and_structure(self):
        """测试 HTML 文件编码和基本结构的有效性"""
        index_path = Path("index.html")
        assert index_path.exists(), "index.html 文件不存在"
        
        # 测试文件可以正确读取（编码测试）
        try:
            content = index_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                content = index_path.read_text(encoding='gbk')
            except UnicodeDecodeError:
                pytest.fail("HTML文件编码无法识别，既不是UTF-8也不是GBK")
        
        # 检查HTML文档类型声明
        has_doctype = '<!doctype' in content.lower() or '<!DOCTYPE' in content
        if not has_doctype:
            # 如果没有doctype，至少应该有基本的HTML结构
            assert '<html' in content.lower(), "HTML文件缺少基本的HTML标签结构"