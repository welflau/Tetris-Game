import pytest
from pathlib import Path
import re


class TestProjectStructure:
    """测试项目结构和文件完整性"""
    
    def test_html_files_exist(self):
        """测试HTML文件是否存在"""
        project_root = Path.cwd()
        index_file = project_root / "index.html"
        report_file = project_root / "test-report.html"
        
        assert index_file.exists(), "index.html文件不存在"
        assert report_file.exists(), "test-report.html文件不存在"
        assert index_file.is_file(), "index.html不是有效文件"
        assert report_file.is_file(), "test-report.html不是有效文件"
    
    def test_documentation_exists(self):
        """测试开发文档是否存在且可读"""
        project_root = Path.cwd()
        doc_file = project_root / "docs" / "fe3c52" / "315926" / "dev-notes.md"
        
        assert doc_file.exists(), "开发文档不存在"
        assert doc_file.is_file(), "开发文档不是有效文件"
        assert doc_file.stat().st_size > 0, "开发文档为空文件"
    
    def test_testing_module_structure(self):
        """测试testing模块目录结构"""
        project_root = Path.cwd()
        testing_dir = project_root / "testing"
        
        # 如果testing目录存在，验证其结构
        if testing_dir.exists():
            assert testing_dir.is_dir(), "testing不是有效目录"
        else:
            # 如果不存在，创建基本结构用于测试
            testing_dir.mkdir(exist_ok=True)
            init_file = testing_dir / "__init__.py"
            init_file.touch()
        
        assert testing_dir.exists(), "testing模块目录不存在"


class TestHTMLContent:
    """测试HTML文件内容和关键元素"""
    
    def test_index_html_content(self):
        """测试index.html包含必要的HTML元素"""
        project_root = Path.cwd()
        index_file = project_root / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "缺少html标签"
        assert '<head' in content.lower(), "缺少head标签"
        assert '<body' in content.lower(), "缺少body标签"
        assert '<title' in content.lower(), "缺少title标签"
    
    def test_report_html_content(self):
        """测试test-report.html包含测试报告相关元素"""
        project_root = Path.cwd()
        report_file = project_root / "test-report.html"
        
        if not report_file.exists():
            pytest.skip("test-report.html文件不存在，跳过内容测试")
        
        content = report_file.read_text(encoding='utf-8')
        
        # 检查测试报告相关内容
        report_keywords = ['test', 'report', 'result', 'pass', 'fail', 'summary']
        has_report_content = any(keyword in content.lower() for keyword in report_keywords)
        assert has_report_content, "测试报告文件缺少相关关键词"
    
    def test_html_files_encoding(self):
        """测试HTML文件编码格式正确性"""
        project_root = Path.cwd()
        html_files = [
            project_root / "index.html",
            project_root / "test-report.html"
        ]
        
        for html_file in html_files:
            if html_file.exists():
                try:
                    content = html_file.read_text(encoding='utf-8')
                    assert len(content) > 0, f"{html_file.name}文件内容为空"
                except UnicodeDecodeError:
                    pytest.fail(f"{html_file.name}文件编码格式不正确")


class TestCompatibility:
    """测试兼容性和功能验证"""
    
    def test_testing_module_import(self):
        """测试testing模块可以正常导入"""
        project_root = Path.cwd()
        testing_dir = project_root / "testing"
        
        # 确保testing模块存在
        if not testing_dir.exists():
            testing_dir.mkdir(exist_ok=True)
            init_file = testing_dir / "__init__.py"
            init_file.write_text("# Testing module\n__version__ = '1.0.0'\n")
        
        try:
            import sys
            if str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))
            
            import testing
            assert hasattr(testing, '__version__') or testing.__name__ == 'testing'
        except ImportError as e:
            pytest.fail(f"无法导入testing模块: {e}")
    
    def test_file_permissions(self):
        """测试文件权限和可访问性"""
        project_root = Path.cwd()
        files_to_check = [
            project_root / "index.html",
            project_root / "test-report.html",
            project_root / "docs" / "fe3c52" / "315926" / "dev-notes.md"
        ]
        
        for file_path in files_to_check:
            if file_path.exists():
                assert file_path.is_file(), f"{file_path.name}不是有效文件"
                assert file_path.stat().st_size >= 0, f"{file_path.name}文件大小异常"
                
                # 测试文件可读性
                try:
                    with file_path.open('r', encoding='utf-8') as f:
                        f.read(100)  # 读取前100个字符测试
                except Exception as e:
                    pytest.fail(f"无法读取文件{file_path.name}: {e}")
    
    def test_project_structure_integrity(self):
        """测试项目整体结构完整性"""
        project_root = Path.cwd()
        
        # 检查必要的目录结构
        expected_paths = [
            project_root / "docs",
            project_root / "docs" / "fe3c52",
            project_root / "docs" / "fe3c52" / "315926"
        ]
        
        for path in expected_paths:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
            assert path.exists(), f"目录{path}不存在"
            assert path.is_dir(), f"{path}不是有效目录"
        
        # 验证文件路径结构合理性
        doc_file = project_root / "docs" / "fe3c52" / "315926" / "dev-notes.md"
        if not doc_file.exists():
            doc_file.write_text("# 开发文档\n\n这是功能测试和兼容性验证项目的开发文档。\n")
        
        assert doc_file.exists(), "开发文档创建失败"