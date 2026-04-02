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
        snowflake_keywords = ['snow', 'flake', 'canvas', 'animation', '雪花']
        has_snowflake_content = any(keyword.lower() in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML文件中未找到雪花特效相关的关键元素"
        
        # 检查是否包含基本的HTML结构
        assert '<html' in content.lower() or '<!doctype html>' in content.lower(), "HTML文件缺少基本的HTML结构"
    
    def test_dev_notes_file_exists_and_valid(self):
        """测试开发文档是否存在且包含有效内容"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
        
        # 检查是否包含markdown格式的内容
        markdown_indicators = ['#', '##', '###', '*', '-', '```']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不包含markdown格式的内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个有效的目录"
        
        # 检查嵌套目录结构
        nested_dir = Path("docs/51ee63/19a016")
        assert nested_dir.exists(), "嵌套的文档目录结构不完整"
        assert nested_dir.is_dir(), "嵌套路径不是有效目录"
    
    def test_html_script_and_style_elements(self):
        """测试HTML文件是否包含必要的脚本和样式元素"""
        html_file = Path("index.html")
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过脚本和样式测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript相关内容（内联或外部）
        has_javascript = ('<script' in content.lower() or 
                         'javascript' in content.lower() or
                         '.js' in content.lower())
        
        # 检查是否包含CSS相关内容（内联或外部）
        has_css = ('<style' in content.lower() or 
                  'stylesheet' in content.lower() or
                  '.css' in content.lower())
        
        # 雪花特效通常需要JavaScript和CSS
        assert has_javascript or has_css, "HTML文件中未找到JavaScript或CSS相关内容，雪花特效可能无法正常工作"