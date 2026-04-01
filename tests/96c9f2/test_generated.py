import pytest
from pathlib import Path
import re

class TestGameCanvasAndGrid:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_canvas_element(self):
        """测试HTML文件是否包含画布元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas标签
        assert '<canvas' in content, "HTML文件中缺少canvas元素"
        
        # 检查canvas是否有id属性
        canvas_pattern = r'<canvas[^>]*id\s*=\s*["\'][^"\']*["\'][^>]*>'
        assert re.search(canvas_pattern, content), "canvas元素缺少id属性"
    
    def test_html_contains_game_related_elements(self):
        """测试HTML文件是否包含游戏相关的关键元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript相关内容
        js_indicators = ['<script', 'javascript', 'canvas', 'grid', 'game']
        found_indicators = [indicator for indicator in js_indicators if indicator.lower() in content.lower()]
        assert len(found_indicators) >= 2, f"HTML文件缺少足够的游戏相关元素，只找到: {found_indicators}"
        
        # 检查HTML基本结构
        assert '<html' in content or '<!DOCTYPE html>' in content, "HTML文件缺少基本的HTML结构"
        assert '<head>' in content or '<body>' in content, "HTML文件缺少head或body标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/96c9f2/2879ba/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_relevant_content(self):
        """测试开发文档是否包含相关的技术内容"""
        dev_notes_file = Path("docs/96c9f2/2879ba/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查是否包含游戏开发相关关键词
        game_keywords = ['canvas', 'grid', 'game', '画布', '网格', '游戏']
        found_keywords = [keyword for keyword in game_keywords if keyword.lower() in content.lower()]
        assert len(found_keywords) >= 1, f"开发文档缺少游戏相关内容，应包含: {game_keywords}"
        
        # 检查文档是否有实际内容（不是空文件）
        assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs")
        
        # 检查主要目录是否存在
        assert frontend_dir.exists(), "frontend目录不存在"
        assert docs_dir.exists(), "docs目录不存在"
        
        # 检查frontend目录下是否有HTML文件
        html_files = list(frontend_dir.glob("*.html"))
        assert len(html_files) >= 1, "frontend目录下没有HTML文件"
        
        # 检查docs目录结构
        dev_notes_path = Path("docs/96c9f2/2879ba")
        assert dev_notes_path.exists(), "文档子目录结构不完整"