import pytest
from pathlib import Path
import re

class TestSnowflakeEffectFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_snowflake_elements(self):
        """测试 index.html 文件是否包含雪花特效相关的关键元素"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否包含基本的HTML结构
        assert '<html' in content.lower(), "缺少 HTML 标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "缺少 head 标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "缺少 body 标签"
        
        # 检查是否包含雪花特效相关的元素或类名
        snowflake_keywords = ['snowflake', 'snow', '雪花', 'particle', 'effect']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML 文件中未找到雪花特效相关内容"
    
    def test_index_html_has_css_and_js_references(self):
        """测试 index.html 文件是否包含 CSS 和 JavaScript 引用，用于实现雪花特效样式和层级处理"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否包含 CSS 引用（内联样式或外部文件）
        has_css = ('<style' in content.lower() or 
                  '<link' in content.lower() and 'stylesheet' in content.lower() or
                  'z-index' in content.lower() or
                  'position' in content.lower())
        assert has_css, "未找到 CSS 样式引用，无法实现雪花特效样式"
        
        # 检查是否包含 JavaScript 引用（内联脚本或外部文件）
        has_js = ('<script' in content.lower())
        assert has_js, "未找到 JavaScript 脚本引用，无法实现雪花特效动画"
    
    def test_dev_notes_file_exists_and_contains_project_info(self):
        """测试开发文档是否存在并包含项目相关信息"""
        dev_notes_file = Path("docs/51ee63/461647/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含项目相关的关键词
        project_keywords = ['雪花', 'snowflake', '特效', 'effect', '层级', 'layer', 'z-index']
        has_project_content = any(keyword in content.lower() for keyword in project_keywords)
        assert has_project_content, "开发文档中未找到项目相关内容"
    
    def test_html_structure_for_layered_effects(self):
        """测试 HTML 结构是否支持层级效果处理"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否有容器元素用于承载雪花特效
        container_patterns = [
            r'<div[^>]*class[^>]*["\'][^"\']*container[^"\']*["\']',
            r'<div[^>]*id[^>]*["\'][^"\']*snow[^"\']*["\']',
            r'<canvas',
            r'<div[^>]*class[^>]*["\'][^"\']*snow[^"\']*["\']'
        ]
        
        has_container = any(re.search(pattern, content, re.IGNORECASE) for pattern in container_patterns)
        assert has_container, "未找到用于承载雪花特效的容器元素"