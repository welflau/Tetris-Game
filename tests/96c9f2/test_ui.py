import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    
    def test_index_html_exists(self):
        """测试index.html文件是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html文件不存在"
        assert index_path.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试index.html文件包含响应式UI的基本HTML元素"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html文件不存在，跳过内容测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少DOCTYPE声明"
        assert '<html' in content.lower(), "缺少html标签"
        assert '<head>' in content.lower(), "缺少head标签"
        assert '<body>' in content.lower(), "缺少body标签"
        
        # 检查响应式设计相关元素
        viewport_pattern = r'<meta\s+name=["\']viewport["\'].*content=["\'][^"\']*width=device-width[^"\']*["\']'
        assert re.search(viewport_pattern, content, re.IGNORECASE), "缺少响应式viewport meta标签"
    
    def test_index_html_contains_ui_components(self):
        """测试index.html文件包含UI界面组件"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html文件不存在，跳过UI组件测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查常见的UI组件标签
        ui_elements = ['div', 'button', 'input', 'form', 'nav', 'header', 'footer', 'section', 'article']
        found_elements = []
        
        for element in ui_elements:
            if f'<{element}' in content.lower():
                found_elements.append(element)
        
        assert len(found_elements) >= 2, f"HTML文件应包含至少2个UI组件标签，当前找到: {found_elements}"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_path = Path("docs/96c9f2/258e56/dev-notes.md")
        assert dev_notes_path.exists(), "开发文档文件不存在"
        assert dev_notes_path.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_documentation(self):
        """测试开发文档包含有效的文档内容"""
        dev_notes_path = Path("docs/96c9f2/258e56/dev-notes.md")
        
        if not dev_notes_path.exists():
            pytest.skip("dev-notes.md文件不存在，跳过文档内容测试")
        
        content = dev_notes_path.read_text(encoding='utf-8')
        
        # 检查文档不为空
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含Markdown格式的内容
        markdown_indicators = ['#', '##', '###', '*', '-', '```', '**', '__']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        
        assert has_markdown, "文档应包含Markdown格式的内容"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构的完整性"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs/96c9f2/258e56")
        
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个有效的目录"
        
        assert docs_dir.exists(), "docs目录结构不完整"
        assert docs_dir.is_dir(), "docs路径不是一个有效的目录"
        
        # 检查目录中是否有文件
        frontend_files = list(frontend_dir.glob("*"))
        assert len(frontend_files) > 0, "frontend目录为空"