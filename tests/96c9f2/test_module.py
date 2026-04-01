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
        assert '<canvas' in content.lower(), "HTML文件中缺少canvas元素"
        
        # 检查canvas是否有id属性
        canvas_pattern = r'<canvas[^>]*id\s*=\s*["\'][^"\']*["\'][^>]*>'
        assert re.search(canvas_pattern, content, re.IGNORECASE), "canvas元素缺少id属性"
    
    def test_html_contains_game_related_elements(self):
        """测试HTML文件是否包含游戏相关的关键元素和脚本"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript相关内容
        js_indicators = ['<script', 'javascript', 'function', 'var ', 'let ', 'const ']
        has_js = any(indicator in content.lower() for indicator in js_indicators)
        assert has_js, "HTML文件中缺少JavaScript代码或引用"
        
        # 检查是否包含游戏相关的关键词
        game_keywords = ['game', 'grid', 'canvas', 'draw', 'render']
        has_game_content = any(keyword in content.lower() for keyword in game_keywords)
        assert has_game_content, "HTML文件中缺少游戏相关的关键内容"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/96c9f2/2879ba/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_documentation(self):
        """测试开发文档是否包含有效的文档内容"""
        dev_notes_file = Path("docs/96c9f2/2879ba/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查文件不为空
        assert len(content.strip()) > 0, "开发文档文件为空"
        
        # 检查是否包含Markdown格式的内容
        markdown_indicators = ['#', '##', '###', '*', '-', '```', '**']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档缺少Markdown格式内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查frontend目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个有效的目录"
        
        # 检查docs目录结构存在
        docs_dir = Path("docs/96c9f2/2879ba")
        assert docs_dir.exists(), "文档目录结构不完整"
        assert docs_dir.is_dir(), "文档路径不是一个有效的目录"
        
        # 检查关键文件都存在
        key_files = [
            Path("frontend/index.html"),
            Path("docs/96c9f2/2879ba/dev-notes.md")
        ]
        
        for file_path in key_files:
            assert file_path.exists(), f"关键文件 {file_path} 不存在"