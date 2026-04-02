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
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或雪花相关的div
        assert re.search(r'<canvas|<div.*snow|snowflake', content, re.IGNORECASE), \
            "HTML文件中未找到雪花特效相关的DOM元素"
        
        # 检查是否包含JavaScript代码或引用
        assert re.search(r'<script|\.js', content, re.IGNORECASE), \
            "HTML文件中未找到JavaScript代码或引用"
    
    def test_html_structure_validity(self):
        """测试HTML文件结构的有效性"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE html|<html', content, re.IGNORECASE), \
            "HTML文件缺少DOCTYPE声明或html标签"
        
        assert re.search(r'<head>', content, re.IGNORECASE), \
            "HTML文件缺少head标签"
        
        assert re.search(r'<body>', content, re.IGNORECASE), \
            "HTML文件缺少body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查是否包含雪花特效相关的描述
        assert re.search(r'雪花|snow|特效|effect', content, re.IGNORECASE), \
            "开发文档中未找到雪花特效相关的描述"
        
        # 检查文档长度是否合理
        assert len(content.strip()) > 50, "开发文档内容过于简短"
    
    def test_project_file_structure(self):
        """测试项目文件结构的完整性"""
        # 检查根目录下的HTML文件
        assert Path("index.html").exists(), "缺少主页HTML文件"
        
        # 检查文档目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs应该是一个目录"
        
        # 检查开发文档的目录结构
        dev_notes_parent = Path("docs/51ee63/19a016")
        if dev_notes_parent.exists():
            assert dev_notes_parent.is_dir(), "开发文档的父目录结构不正确"