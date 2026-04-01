import pytest
from pathlib import Path
import re

class TestFallingBlocksAnimationSystem:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_canvas_element(self):
        """测试HTML文件是否包含用于动画渲染的canvas元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        # 检查是否包含canvas标签
        assert '<canvas' in content, "HTML文件中缺少canvas元素"
        # 检查是否包含JavaScript相关内容
        assert any(keyword in content.lower() for keyword in ['script', 'javascript']), "HTML文件中缺少JavaScript代码"
    
    def test_html_contains_animation_keywords(self):
        """测试HTML文件是否包含方块下落动画相关的关键词和元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8').lower()
        # 检查动画相关关键词
        animation_keywords = ['block', 'fall', 'drop', 'animation', 'move', 'gravity']
        found_keywords = [keyword for keyword in animation_keywords if keyword in content]
        assert len(found_keywords) > 0, f"HTML文件中未找到动画相关关键词，期望包含: {animation_keywords}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/96c9f2/725714/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        # 测试文件是否可读
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content) > 0, "开发文档文件为空"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构是否有效"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        # 检查基本HTML结构
        assert '<html' in content.lower(), "缺少html标签"
        assert '<head' in content.lower(), "缺少head标签"
        assert '<body' in content.lower(), "缺少body标签"
        
        # 检查标签配对（简单检查）
        html_tags = re.findall(r'<(/?)(\w+)', content.lower())
        open_tags = [tag for is_close, tag in html_tags if not is_close and tag in ['html', 'head', 'body']]
        close_tags = [tag for is_close, tag in html_tags if is_close and tag in ['html', 'head', 'body']]
        assert len(open_tags) == len(close_tags), "HTML标签未正确闭合"