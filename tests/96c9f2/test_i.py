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
        assert "<html" in content.lower(), "缺少HTML标签"
        assert "<head>" in content.lower() or "<head " in content.lower(), "缺少head标签"
        assert "<body>" in content.lower() or "<body " in content.lower(), "缺少body标签"
        
        # 检查游戏相关元素
        assert "canvas" in content.lower() or "游戏" in content or "tetris" in content.lower() or "方块" in content, "缺少游戏相关元素"
    
    def test_dev_notes_exists_and_contains_i_block_info(self):
        """测试开发文档是否存在并包含I型方块相关信息"""
        dev_notes_path = Path("docs/96c9f2/a30d92/dev-notes.md")
        assert dev_notes_path.exists(), "开发文档dev-notes.md不存在"
        assert dev_notes_path.is_file(), "dev-notes.md不是一个有效的文件"
        
        content = dev_notes_path.read_text(encoding='utf-8')
        
        # 检查是否包含I型方块相关内容
        i_block_keywords = ["I型", "I形", "I-block", "直线", "方块", "tetris", "俄罗斯方块"]
        has_i_block_content = any(keyword in content for keyword in i_block_keywords)
        assert has_i_block_content, "开发文档中缺少I型方块相关内容"
    
    def test_html_structure_validity(self):
        """测试HTML文件的基本结构完整性"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查HTML标签配对
        html_open = content.lower().count("<html")
        html_close = content.lower().count("</html>")
        assert html_open > 0 and html_close > 0, "HTML标签不完整"
        
        head_open = content.lower().count("<head")
        head_close = content.lower().count("</head>")
        assert head_open > 0 and head_close > 0, "head标签不完整"
        
        body_open = content.lower().count("<body")
        body_close = content.lower().count("</body>")
        assert body_open > 0 and body_close > 0, "body标签不完整"
    
    def test_project_structure_completeness(self):
        """测试项目结构的完整性，确保关键文件都存在"""
        # 检查frontend目录
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个目录"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        
        # 检查具体的文档路径
        specific_doc_dir = Path("docs/96c9f2/a30d92")
        assert specific_doc_dir.exists(), "指定的文档目录路径不存在"
        assert specific_doc_dir.is_dir(), "指定路径不是一个目录"