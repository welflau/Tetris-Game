import pytest
from pathlib import Path
import re

class TestProjectStructure:
    """测试项目结构和文件存在性"""
    
    def test_index_html_exists(self):
        """测试 index.html 文件是否存在"""
        index_path = Path("index.html")
        assert index_path.exists(), "index.html 文件不存在"
        assert index_path.is_file(), "index.html 不是一个有效的文件"
    
    def test_dev_notes_exists(self):
        """测试开发文档是否存在"""
        docs_path = Path("docs/96c9f2/66f076/dev-notes.md")
        assert docs_path.exists(), "dev-notes.md 文件不存在"
        assert docs_path.is_file(), "dev-notes.md 不是一个有效的文件"
    
    def test_testing_module_directory(self):
        """测试 testing 模块目录是否存在"""
        testing_path = Path("testing")
        if testing_path.exists():
            assert testing_path.is_dir(), "testing 应该是一个目录"

class TestHTMLContent:
    """测试 HTML 文件内容"""
    
    def test_index_html_basic_structure(self):
        """测试 index.html 包含基本的 HTML 结构元素"""
        index_path = Path("index.html")
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查基本 HTML 标签
        assert '<html' in content.lower(), "HTML 文件应包含 <html> 标签"
        assert '<head' in content.lower(), "HTML 文件应包含 <head> 标签"
        assert '<body' in content.lower(), "HTML 文件应包含 <body> 标签"
    
    def test_index_html_title_exists(self):
        """测试 index.html 包含标题元素"""
        index_path = Path("index.html")
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过标题测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查是否有标题相关标签
        has_title = '<title' in content.lower()
        has_h1 = '<h1' in content.lower()
        has_h2 = '<h2' in content.lower()
        
        assert has_title or has_h1 or has_h2, "HTML 文件应包含标题元素（title、h1 或 h2）"
    
    def test_index_html_testing_related_content(self):
        """测试 index.html 包含与测试相关的内容"""
        index_path = Path("index.html")
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过测试相关内容检查")
        
        content = index_path.read_text(encoding='utf-8')
        content_lower = content.lower()
        
        # 检查是否包含测试相关关键词
        testing_keywords = ['test', 'testing', '测试', 'debug', '调试', 'pytest']
        has_testing_content = any(keyword in content_lower for keyword in testing_keywords)
        
        assert has_testing_content, "HTML 文件应包含与测试或调试相关的内容"

class TestDocumentationContent:
    """测试文档内容"""
    
    def test_dev_notes_markdown_format(self):
        """测试开发文档是否为有效的 Markdown 格式"""
        docs_path = Path("docs/96c9f2/66f076/dev-notes.md")
        if not docs_path.exists():
            pytest.skip("dev-notes.md 文件不存在，跳过格式测试")
        
        content = docs_path.read_text(encoding='utf-8')
        
        # 检查 Markdown 常见元素
        has_headers = bool(re.search(r'^#+\s', content, re.MULTILINE))
        has_content = len(content.strip()) > 0
        
        assert has_content, "开发文档不应为空"
        # Markdown 文件通常包含标题，但不强制要求
        if not has_headers:
            # 至少应该有一些文本内容
            assert len(content.strip()) > 10, "开发文档内容过少"
    
    def test_dev_notes_contains_development_info(self):
        """测试开发文档包含开发相关信息"""
        docs_path = Path("docs/96c9f2/66f076/dev-notes.md")
        if not docs_path.exists():
            pytest.skip("dev-notes.md 文件不存在，跳过内容检查")
        
        content = docs_path.read_text(encoding='utf-8')
        content_lower = content.lower()
        
        # 检查开发相关关键词
        dev_keywords = [
            'dev', 'development', '开发', 'note', 'notes', '笔记',
            'test', 'testing', '测试', 'debug', '调试', 'feature', '功能'
        ]
        
        keyword_count = sum(1 for keyword in dev_keywords if keyword in content_lower)
        assert keyword_count >= 1, "开发文档应包含至少一个开发相关的关键词"

class TestProjectConfiguration:
    """测试项目配置和结构"""
    
    def test_project_root_structure(self):
        """测试项目根目录结构合理性"""
        root_path = Path(".")
        
        # 检查是否存在常见的项目文件
        common_files = ["index.html"]
        existing_files = [f for f in common_files if (root_path / f).exists()]
        
        assert len(existing_files) > 0, "项目根目录应包含至少一个主要文件"
    
    def test_docs_directory_structure(self):
        """测试文档目录结构"""
        docs_base = Path("docs")
        if docs_base.exists():
            assert docs_base.is_dir(), "docs 应该是一个目录"
            
            # 检查是否有文档文件
            doc_files = list(docs_base.rglob("*.md"))
            if len(doc_files) > 0:
                assert any(f.name == "dev-notes.md" for f in doc_files), "应包含 dev-notes.md 文档"
    
    def test_file_encoding_compatibility(self):
        """测试文件编码兼容性"""
        files_to_check = [
            Path("index.html"),
            Path("docs/96c9f2/66f076/dev-notes.md")
        ]
        
        for file_path in files_to_check:
            if file_path.exists():
                try:
                    content = file_path.read_text(encoding='utf-8')
                    assert isinstance(content, str), f"{file_path} 文件读取后应为字符串类型"
                    assert len(content) >= 0, f"{file_path} 文件内容长度应为非负数"
                except UnicodeDecodeError:
                    pytest.fail(f"{file_path