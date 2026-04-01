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
        """测试HTML文件是否包含canvas元素用于动画渲染"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        # 检查是否包含canvas标签
        assert '<canvas' in content.lower(), "HTML文件中缺少canvas元素"
        # 检查是否包含JavaScript相关内容
        assert any(keyword in content.lower() for keyword in ['<script', 'javascript']), "HTML文件中缺少JavaScript代码"
    
    def test_html_contains_animation_keywords(self):
        """测试HTML文件是否包含方块下落动画相关的关键词"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8').lower()
        animation_keywords = ['block', 'fall', 'drop', 'animate', 'game', 'tetris']
        
        # 至少包含一个动画相关关键词
        found_keywords = [keyword for keyword in animation_keywords if keyword in content]
        assert len(found_keywords) > 0, f"HTML文件中未找到动画相关关键词，期望包含: {animation_keywords}"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/96c9f2/725714/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.suffix == '.md', "开发文档不是markdown格式"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息"""
        dev_notes_file = Path("docs/96c9f2/725714/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        # 检查文档是否有实际内容
        assert len(content.strip()) > 0, "开发文档为空"
        # 检查是否包含markdown标题格式
        assert re.search(r'^#+\s+', content, re.MULTILINE), "开发文档缺少markdown标题格式"