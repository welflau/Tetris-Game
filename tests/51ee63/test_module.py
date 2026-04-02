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
        """测试HTML文件是否包含雪花特效相关的关键元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在，无法进行内容测试"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或雪花相关的关键词
        snowflake_keywords = [
            'snowflake', 'snow', 'canvas', 'animation', 
            '雪花', '雪', '特效', 'effect'
        ]
        
        has_snowflake_content = any(keyword.lower() in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML文件中未找到雪花特效相关的关键元素"
        
        # 检查基本HTML结构
        assert '<html' in content.lower() or '<!doctype html>' in content.lower(), "HTML文件缺少基本HTML结构"
    
    def test_html_has_valid_structure(self):
        """测试HTML文件是否具有有效的基本结构"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查HTML标签配对
        html_tags = ['html', 'head', 'body']
        for tag in html_tags:
            open_tag_pattern = f'<{tag}[^>]*>'
            close_tag_pattern = f'</{tag}>'
            
            open_matches = len(re.findall(open_tag_pattern, content, re.IGNORECASE))
            close_matches = len(re.findall(close_tag_pattern, content, re.IGNORECASE))
            
            if open_matches > 0:  # 如果存在开标签，则必须有对应的闭标签
                assert close_matches > 0, f"HTML文件中{tag}标签未正确闭合"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档是否包含有效内容"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在，无法进行内容测试"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
        
        # 检查是否包含开发相关的关键词
        dev_keywords = [
            '开发', '测试', '功能', '实现', '说明', 
            'development', 'test', 'feature', 'implementation'
        ]
        
        has_dev_content = any(keyword.lower() in content.lower() for keyword in dev_keywords)
        assert has_dev_content, "开发文档中未找到相关的开发说明内容"
    
    def test_project_structure_integrity(self):
        """测试项目整体结构的完整性"""
        # 检查主要文件是否都存在
        required_files = [
            Path("index.html"),
            Path("docs/51ee63/19a016/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"以下必需文件缺失: {', '.join(missing_files)}"
        
        # 检查docs目录结构
        docs_dir = Path("docs/51ee63/19a016")
        assert docs_dir.exists(), "文档目录结构不完整"
        assert docs_dir.is_dir(), "docs路径应该是一个目录"