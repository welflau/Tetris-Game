import pytest
from pathlib import Path
import re

class TestFrontendModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path(__file__).parent / "frontend"
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在: {index_file}"
        assert index_file.is_file(), f"index.html 不是一个文件: {index_file}"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含必要的 HTML 元素"""
        frontend_dir = Path(__file__).parent / "frontend"
        index_file = frontend_dir / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本 HTML 结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少 DOCTYPE 声明"
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少 html 标签"
        assert re.search(r'<head[^>]*>.*</head>', content, re.IGNORECASE | re.DOTALL), "缺少 head 标签"
        assert re.search(r'<body[^>]*>.*</body>', content, re.IGNORECASE | re.DOTALL), "缺少 body 标签"
        
        # 检查基本元信息
        assert re.search(r'<title[^>]*>.*</title>', content, re.IGNORECASE | re.DOTALL), "缺少 title 标签"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        docs_dir = Path(__file__).parent / "docs" / "96c9f2" / "d49040"
        dev_notes_file = docs_dir / "dev-notes.md"
        
        assert dev_notes_file.exists(), f"开发文档文件不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"开发文档不是一个文件: {dev_notes_file}"
        
        # 测试文件是否可读
        try:
            content = dev_notes_file.read_text(encoding='utf-8')
            assert len(content.strip()) > 0, "开发文档文件内容为空"
        except UnicodeDecodeError:
            # 如果 UTF-8 解码失败，尝试其他编码
            content = dev_notes_file.read_text(encoding='gbk')
            assert len(content.strip()) > 0, "开发文档文件内容为空"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否合理"""
        frontend_dir = Path(__file__).parent / "frontend"
        
        # 检查前端目录是否存在
        if not frontend_dir.exists():
            pytest.skip("frontend 目录不存在，跳过目录结构测试")
        
        assert frontend_dir.is_dir(), "frontend 应该是一个目录"
        
        # 检查是否包含基本的前端文件
        files_in_frontend = list(frontend_dir.iterdir())
        assert len(files_in_frontend) > 0, "frontend 目录不应该为空"
        
        # 检查 index.html 是否在正确位置
        index_file = frontend_dir / "index.html"
        if index_file.exists():
            assert index_file.parent == frontend_dir, "index.html 应该在 frontend 目录下"
    
    def test_project_documentation_structure(self):
        """测试项目文档目录结构是否正确"""
        base_dir = Path(__file__).parent
        docs_path = base_dir / "docs" / "96c9f2" / "d49040"
        
        # 检查文档目录路径是否存在
        if not docs_path.exists():
            pytest.skip("文档目录不存在，跳过文档结构测试")
        
        assert docs_path.is_dir(), "文档路径应该是一个目录"
        
        # 检查开发文档是否存在
        dev_notes = docs_path / "dev-notes.md"
        if dev_notes.exists():
            assert dev_notes.suffix == '.md', "开发文档应该是 Markdown 格式"
            
            # 检查文档内容是否包含项目相关信息
            content = dev_notes.read_text(encoding='utf-8')
            # 简单检查是否包含一些常见的项目文档关键词
            keywords = ['项目', 'project', '架构', 'architecture', '环境', 'environment', '搭建', 'setup']
            has_project_content = any(keyword in content.lower() for keyword in keywords)
            assert has_project_content, "开发文档应该包含项目相关内容"