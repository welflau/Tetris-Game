import pytest
from pathlib import Path
import re

class TestCollisionDetectionFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含碰撞检测系统的关键HTML元素"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "缺少 html 标签"
        assert '<head>' in content.lower(), "缺少 head 标签"
        assert '<body>' in content.lower(), "缺少 body 标签"
        
        # 检查碰撞检测相关元素
        collision_keywords = ['collision', '碰撞', 'detection', '检测']
        has_collision_keyword = any(keyword in content.lower() for keyword in collision_keywords)
        assert has_collision_keyword, "页面内容中缺少碰撞检测相关关键词"
        
        # 检查是否包含canvas或svg等图形元素（碰撞检测通常需要可视化）
        graphics_elements = ['<canvas', '<svg', 'canvas', 'svg']
        has_graphics = any(element in content.lower() for element in graphics_elements)
        assert has_graphics, "页面缺少用于碰撞检测可视化的图形元素"
    
    def test_index_html_has_valid_structure(self):
        """测试 index.html 文件具有有效的HTML结构和碰撞检测功能相关的脚本"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript（碰撞检测逻辑通常需要JS）
        has_script = '<script' in content.lower() or '.js' in content.lower()
        assert has_script, "页面缺少JavaScript脚本，无法实现碰撞检测功能"
        
        # 检查是否有交互元素（按钮、输入框等）
        interactive_elements = ['<button', '<input', 'onclick', 'onmousemove', 'addEventListener']
        has_interaction = any(element in content.lower() for element in interactive_elements)
        assert has_interaction, "页面缺少交互元素，无法进行碰撞检测操作"
        
        # 检查文件大小合理性（不能为空，也不应该过大）
        file_size = index_file.stat().st_size
        assert file_size > 100, "HTML文件内容过少，可能不完整"
        assert file_size < 1024 * 1024, "HTML文件过大，可能包含不必要的内容"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在且包含有用信息"""
        dev_notes_file = Path("docs/96c9f2/cffe2c/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查文档是否包含开发相关信息
        dev_keywords = ['开发', '实现', 'implementation', 'development', 'api', '接口', '算法', 'algorithm']
        has_dev_content = any(keyword in content.lower() for keyword in dev_keywords)
        assert has_dev_content, "开发文档缺少开发相关内容"
        
        # 检查文档长度合理性
        assert len(content.strip()) > 50, "开发文档内容过少"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs")
        
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 不是一个目录"
        
        assert docs_dir.exists(), "docs 目录不存在"
        assert docs_dir.is_dir(), "docs 不是一个目录"
        
        # 检查关键文件都存在
        required_files = [
            Path("frontend/index.html"),
            Path("docs/96c9f2/cffe2c/dev-notes.md")
        ]
        
        for file_path in required_files:
            assert file_path.exists(), f"必需的文件 {file_path} 不存在"