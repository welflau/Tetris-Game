import pytest
from pathlib import Path
from bs4 import BeautifulSoup
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
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否包含canvas元素或雪花相关的div
        canvas_elements = soup.find_all('canvas')
        snowflake_divs = soup.find_all('div', class_=re.compile(r'snow|flake', re.I))
        
        assert len(canvas_elements) > 0 or len(snowflake_divs) > 0, "HTML中未找到雪花特效相关元素"
        
        # 检查是否包含JavaScript代码
        script_tags = soup.find_all('script')
        has_snowflake_js = False
        
        for script in script_tags:
            if script.string and any(keyword in script.string.lower() for keyword in ['snow', 'flake', 'particle']):
                has_snowflake_js = True
                break
        
        assert has_snowflake_js or len(script_tags) > 0, "HTML中未找到JavaScript代码"
    
    def test_html_structure_validity(self):
        """测试HTML文件结构的有效性"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "缺少html标签"
        assert soup.find('head') is not None, "缺少head标签"
        assert soup.find('body') is not None, "缺少body标签"
        
        # 检查title标签
        title = soup.find('title')
        assert title is not None, "缺少title标签"
        assert len(title.get_text().strip()) > 0, "title标签内容为空"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
    
    def test_dev_notes_content_structure(self):
        """测试开发文档内容结构是否合理"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档是否包含基本内容
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含Markdown标题
        has_headers = bool(re.search(r'^#+\s+.+', content, re.MULTILINE))
        assert has_headers, "开发文档缺少Markdown标题结构"
        
        # 检查是否包含雪花特效相关内容
        snowflake_keywords = ['雪花', 'snow', 'flake', '特效', 'effect', '动画', 'animation']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "开发文档中未找到雪花特效相关内容"
    
    def test_project_file_structure(self):
        """测试项目文件结构的完整性"""
        # 检查根目录文件
        root_files = ['index.html']
        for file_name in root_files:
            file_path = Path(file_name)
            assert file_path.exists(), f"项目根目录缺少必要文件: {file_name}"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs应该是一个目录"
            
            # 检查嵌套目录结构
            nested_dir = Path("docs/51ee63/19a016")
            if nested_dir.exists():
                assert nested_dir.is_dir(), "嵌套目录结构不正确"
                
                dev_notes = nested_dir / "dev-notes.md"
                assert dev_notes.exists(), "开发文档文件路径不正确"