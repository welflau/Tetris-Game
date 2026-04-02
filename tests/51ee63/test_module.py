import pytest
from pathlib import Path
import re

class TestSnowflakeEffectProject:
    """雪花特效技术方案设计项目测试类"""
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("design/index.html")
        assert html_file.exists(), f"HTML文件不存在: {html_file}"
        assert html_file.is_file(), f"路径不是文件: {html_file}"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效相关的关键元素"""
        html_file = Path("design/index.html")
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过内容测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "HTML文件缺少body标签"
        
        # 检查雪花特效相关元素（至少包含其中一项）
        snowflake_indicators = [
            'snowflake',
            'snow',
            'canvas',
            'animation',
            'particle'
        ]
        
        has_snowflake_element = any(indicator in content.lower() for indicator in snowflake_indicators)
        assert has_snowflake_element, "HTML文件中未找到雪花特效相关元素"
    
    def test_dev_notes_file_exists_and_valid(self):
        """测试开发文档是否存在且包含有效内容"""
        dev_notes_file = Path("design/docs/51ee63/b8d19f/dev-notes.md")
        
        assert dev_notes_file.exists(), f"开发文档不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"路径不是文件: {dev_notes_file}"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含技术方案相关内容
        technical_keywords = [
            '技术',
            '方案',
            '设计',
            '实现',
            '雪花',
            'snowflake',
            'canvas',
            'javascript',
            'css',
            'animation'
        ]
        
        has_technical_content = any(keyword in content.lower() for keyword in technical_keywords)
        assert has_technical_content, "开发文档中未找到技术方案相关内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        design_dir = Path("design")
        assert design_dir.exists(), "design目录不存在"
        assert design_dir.is_dir(), "design路径不是目录"
        
        docs_dir = Path("design/docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs路径不是目录"
    
    def test_html_syntax_basic_validation(self):
        """测试HTML文件基本语法有效性"""
        html_file = Path("design/index.html")
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过语法测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 基本语法检查
        open_tags = re.findall(r'<(\w+)[^>]*>', content)
        close_tags = re.findall(r'</(\w+)>', content)
        
        # 检查关键标签是否配对
        critical_tags = ['html', 'head', 'body']
        for tag in critical_tags:
            if tag in open_tags:
                assert tag in close_tags, f"标签 {tag} 没有正确闭合"