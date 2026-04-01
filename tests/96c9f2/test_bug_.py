import pytest
from pathlib import Path
import re

class TestTetrisProject:
    
    def test_html_file_exists(self):
        """测试俄罗斯方块游戏的HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_game_elements(self):
        """测试HTML文件是否包含俄罗斯方块游戏的关键元素"""
        html_file = Path("index.html")
        if html_file.exists():
            content = html_file.read_text(encoding='utf-8')
            
            # 检查是否包含游戏相关的关键词
            game_keywords = ['tetris', 'block', 'game', 'canvas', 'score']
            found_keywords = []
            
            for keyword in game_keywords:
                if keyword.lower() in content.lower():
                    found_keywords.append(keyword)
            
            assert len(found_keywords) > 0, f"HTML文件中未找到游戏相关关键词: {game_keywords}"
            
            # 检查基本HTML结构
            assert '<html' in content.lower() or '<!doctype html>' in content.lower(), "缺少HTML文档声明"
            assert '<body' in content.lower(), "缺少body标签"
    
    def test_html_has_javascript_for_block_movement(self):
        """测试HTML文件是否包含处理砖块下落的JavaScript代码"""
        html_file = Path("index.html")
        if html_file.exists():
            content = html_file.read_text(encoding='utf-8')
            
            # 检查是否包含JavaScript相关标签或代码
            js_indicators = ['<script', 'function', 'setInterval', 'setTimeout']
            has_js = any(indicator.lower() in content.lower() for indicator in js_indicators)
            
            assert has_js, "HTML文件中未找到JavaScript代码，可能导致砖块无法下落"
            
            # 检查是否有可能的游戏循环或动画相关代码
            animation_keywords = ['interval', 'timeout', 'animation', 'update', 'move', 'fall', 'drop']
            has_animation = any(keyword.lower() in content.lower() for keyword in animation_keywords)
            
            assert has_animation, "未找到可能的动画或游戏循环代码，这可能是砖块无法下落的原因"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在"""
        docs_file = Path("docs/96c9f2/f26a85/dev-notes.md")
        assert docs_file.exists(), "开发文档dev-notes.md不存在"
        assert docs_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_bug_information(self):
        """测试开发文档是否包含关于砖块下落bug的相关信息"""
        docs_file = Path("docs/96c9f2/f26a85/dev-notes.md")
        if docs_file.exists():
            content = docs_file.read_text(encoding='utf-8')
            
            # 检查是否包含bug相关的关键词
            bug_keywords = ['bug', '问题', 'issue', '下落', 'fall', 'drop', '砖块', 'block', 'tetris']
            found_keywords = []
            
            for keyword in bug_keywords:
                if keyword.lower() in content.lower():
                    found_keywords.append(keyword)
            
            assert len(found_keywords) > 0, f"开发文档中未找到bug相关信息: {bug_keywords}"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性，确保关键文件都存在"""
        required_files = [
            Path("index.html"),
            Path("docs/96c9f2/f26a85/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"以下必需文件缺失: {missing_files}"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs应该是一个目录"