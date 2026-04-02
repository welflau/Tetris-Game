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
        assert html_file.exists(), "HTML文件不存在，无法进行内容测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素（通常用于雪花动画）
        assert re.search(r'<canvas', content, re.IGNORECASE), "HTML中未找到canvas元素"
        
        # 检查是否包含JavaScript相关内容
        js_patterns = [
            r'<script',
            r'snowflake|snow|雪花',
            r'animation|animate'
        ]
        
        js_found = any(re.search(pattern, content, re.IGNORECASE) for pattern in js_patterns)
        assert js_found, "HTML中未找到雪花特效相关的JavaScript代码"
    
    def test_dev_notes_file_exists_and_content(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert docs_file.exists(), "开发文档文件不存在"
        assert docs_file.is_file(), "开发文档不是一个有效的文件"
        
        content = docs_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含开发相关的关键词
        dev_keywords = ['开发', '测试', '雪花', 'snowflake', '特效', 'effect']
        keyword_found = any(keyword in content for keyword in dev_keywords)
        assert keyword_found, "开发文档中未找到相关的开发关键词"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查项目根目录
        root_path = Path(".")
        assert root_path.exists(), "项目根目录不存在"
        
        # 检查docs目录结构
        docs_path = Path("docs")
        if docs_path.exists():
            assert docs_path.is_dir(), "docs应该是一个目录"
            
        # 检查是否有基本的web文件
        web_files = ["index.html"]
        for file_name in web_files:
            file_path = Path(file_name)
            if file_path.exists():
                assert file_path.stat().st_size > 0, f"{file_name}文件大小为0"
    
    def test_html_basic_structure(self):
        """测试HTML文件的基本结构是否正确"""
        html_file = Path("index.html")
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过结构测试")
            
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少DOCTYPE声明"
        assert re.search(r'<html', content, re.IGNORECASE), "缺少html标签"
        assert re.search(r'<head', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body', content, re.IGNORECASE), "缺少body标签"
        
        # 检查标题
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            assert len(title) > 0, "页面标题为空"