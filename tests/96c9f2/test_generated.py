import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    
    def test_index_html_exists(self):
        """测试index.html文件是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html文件不存在"
        assert index_path.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_tetris_elements(self):
        """测试index.html文件是否包含俄罗斯方块游戏相关的关键元素"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查HTML基本结构
        assert '<html' in content.lower(), "缺少HTML标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "缺少head标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "缺少body标签"
        
        # 检查游戏相关元素
        tetris_keywords = ['tetris', '俄罗斯方块', 'block', 'game', 'canvas', 'grid']
        has_tetris_content = any(keyword.lower() in content.lower() for keyword in tetris_keywords)
        assert has_tetris_content, "HTML文件中缺少俄罗斯方块游戏相关内容"
    
    def test_index_html_has_valid_structure(self):
        """测试index.html文件是否具有有效的HTML结构和I型方块相关内容"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查是否有JavaScript或CSS引用（游戏逻辑需要）
        has_script = '<script' in content.lower()
        has_style = '<style' in content.lower() or '<link' in content.lower()
        assert has_script or has_style, "HTML文件缺少样式或脚本引用"
        
        # 检查是否有游戏容器元素
        container_elements = ['<div', '<canvas', '<table']
        has_container = any(element in content.lower() for element in container_elements)
        assert has_container, "HTML文件缺少游戏容器元素"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        notes_path = Path("docs/96c9f2/a30d92/dev-notes.md")
        assert notes_path.exists(), "开发文档文件不存在"
        assert notes_path.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_i_block_content(self):
        """测试开发文档是否包含I型方块相关的设计内容"""
        notes_path = Path("docs/96c9f2/a30d92/dev-notes.md")
        assert notes_path.exists(), "开发文档文件不存在"
        
        content = notes_path.read_text(encoding='utf-8')
        
        # 检查I型方块相关内容
        i_block_keywords = ['I型', 'I-block', 'I方块', '直线', 'tetromino', '方块类']
        has_i_block_content = any(keyword in content for keyword in i_block_keywords)
        assert has_i_block_content, "开发文档中缺少I型方块相关内容"
        
        # 检查是否包含设计相关内容
        design_keywords = ['设计', '实现', '类', 'class', '方法', '属性']
        has_design_content = any(keyword in content for keyword in design_keywords)
        assert has_design_content, "开发文档中缺少设计实现相关内容"