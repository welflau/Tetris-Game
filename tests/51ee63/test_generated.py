import pytest
from pathlib import Path
import re

class TestSnowflakeAnimationFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含雪花动画必需的HTML元素"""
        index_file = Path("frontend/index.html")
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<html" in content.lower(), "缺少 html 标签"
        assert "<head>" in content.lower(), "缺少 head 标签"
        assert "<body>" in content.lower(), "缺少 body 标签"
        
        # 检查雪花动画相关元素
        assert "canvas" in content.lower() or "div" in content.lower(), "缺少用于渲染雪花的容器元素"
        assert "<script" in content.lower(), "缺少 JavaScript 脚本标签"
    
    def test_index_html_contains_animation_keywords(self):
        """测试 index.html 文件包含雪花动画相关的关键词"""
        index_file = Path("frontend/index.html")
        content = index_file.read_text(encoding='utf-8')
        
        # 检查雪花动画相关关键词（不区分大小写）
        content_lower = content.lower()
        animation_keywords = ['snow', 'flake', 'animation', 'canvas', 'requestanimationframe']
        
        found_keywords = [keyword for keyword in animation_keywords if keyword in content_lower]
        assert len(found_keywords) >= 2, f"HTML文件应包含至少2个雪花动画相关关键词，当前找到: {found_keywords}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/51ee63/9cdd70/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        # 测试文件可读性
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档包含项目相关信息"""
        dev_notes_file = Path("docs/51ee63/9cdd70/dev-notes.md")
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查Markdown格式标记
        assert "#" in content, "开发文档应包含Markdown标题格式"
        
        # 检查项目相关关键词
        content_lower = content.lower()
        project_keywords = ['雪花', 'snow', '动画', 'animation', '开发', 'dev']
        
        found_keywords = [keyword for keyword in project_keywords if keyword in content_lower]
        assert len(found_keywords) >= 2, f"开发文档应包含项目相关关键词，当前找到: {found_keywords}"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构的完整性"""
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 不是一个有效的目录"
        
        docs_dir = Path("docs/51ee63/9cdd70")
        assert docs_dir.exists(), "文档目录不存在"
        assert docs_dir.is_dir(), "文档路径不是一个有效的目录"