import pytest
from pathlib import Path
import re

class TestSnowflakeEffect:
    
    def test_html_file_exists(self):
        """测试雪花特效的HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效的关键元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或雪花相关的div
        assert any(keyword in content.lower() for keyword in ['canvas', 'snowflake', 'snow']), \
            "HTML文件中未找到雪花特效相关元素"
        
        # 检查是否包含JavaScript代码
        assert '<script' in content or '.js' in content, \
            "HTML文件中未找到JavaScript引用"
        
        # 检查基本HTML结构
        assert '<html' in content and '</html>' in content, \
            "HTML文件缺少基本的html标签结构"
    
    def test_html_has_valid_structure(self):
        """测试HTML文件是否具有有效的文档结构"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查DOCTYPE声明
        assert '<!doctype' in content.lower() or '<!DOCTYPE' in content, \
            "HTML文件缺少DOCTYPE声明"
        
        # 检查head和body标签
        assert '<head' in content and '</head>' in content, \
            "HTML文件缺少head标签"
        assert '<body' in content and '</body>' in content, \
            "HTML文件缺少body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "开发文档不是一个有效的文件"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查根目录下的主要文件
        assert Path("index.html").exists(), "缺少主HTML文件"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs应该是一个目录"
        
        # 检查是否有CSS或JS文件（可能在子目录中）
        root_path = Path(".")
        has_css = any(root_path.rglob("*.css"))
        has_js = any(root_path.rglob("*.js"))
        
        assert has_css or has_js or "style" in Path("index.html").read_text(encoding='utf-8').lower(), \
            "项目中未找到样式文件或内联样式"