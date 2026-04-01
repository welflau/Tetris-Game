import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    """前端文件功能测试和兼容性验证"""
    
    def test_index_html_exists_and_structure(self):
        """测试index.html文件存在且包含基本HTML结构元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<!DOCTYPE html>" in content or "<html" in content, "缺少HTML文档声明或html标签"
        assert "<head>" in content, "缺少head标签"
        assert "<body>" in content, "缺少body标签"
        assert "<title>" in content, "缺少title标签"
        
        # 检查内容不为空
        assert len(content.strip()) > 100, "HTML文件内容过少，可能不完整"
    
    def test_test_report_html_contains_test_elements(self):
        """测试test-report.html包含测试报告相关的关键元素"""
        report_file = Path("test-report.html")
        assert report_file.exists(), "test-report.html文件不存在"
        
        content = report_file.read_text(encoding='utf-8')
        
        # 检查测试报告相关关键词
        test_keywords = ["test", "report", "result", "pass", "fail", "测试", "报告", "结果"]
        found_keywords = [keyword for keyword in test_keywords if keyword.lower() in content.lower()]
        assert len(found_keywords) >= 2, f"测试报告文件缺少相关关键词，仅找到: {found_keywords}"
        
        # 检查是否包含表格或列表结构（常见的报告格式）
        has_table = "<table" in content or "<tr" in content or "<td" in content
        has_list = "<ul" in content or "<ol" in content or "<li" in content
        has_div_structure = content.count("<div") >= 3
        
        assert has_table or has_list or has_div_structure, "测试报告文件缺少结构化内容展示元素"
    
    def test_dev_notes_markdown_format_and_content(self):
        """测试开发文档markdown文件格式正确且包含有效内容"""
        docs_file = Path("docs/fe3c52/315926/dev-notes.md")
        assert docs_file.exists(), "开发文档dev-notes.md文件不存在"
        
        content = docs_file.read_text(encoding='utf-8')
        
        # 检查markdown基本格式元素
        has_headers = bool(re.search(r'^#+\s+.+', content, re.MULTILINE))
        has_content = len(content.strip()) > 50
        
        assert has_headers, "开发文档缺少markdown标题格式"
        assert has_content, "开发文档内容过少"
        
        # 检查是否包含开发相关关键词
        dev_keywords = ["开发", "功能", "测试", "兼容", "版本", "更新", "修复", "feature", "bug", "fix", "update"]
        found_dev_keywords = [keyword for keyword in dev_keywords if keyword.lower() in content.lower()]
        assert len(found_dev_keywords) >= 2, f"开发文档缺少开发相关内容，仅找到关键词: {found_dev_keywords}"
    
    def test_html_files_encoding_compatibility(self):
        """测试HTML文件编码兼容性，确保能正确读取中文内容"""
        html_files = [Path("index.html"), Path("test-report.html")]
        
        for html_file in html_files:
            if html_file.exists():
                # 测试UTF-8编码读取
                try:
                    content_utf8 = html_file.read_text(encoding='utf-8')
                    assert len(content_utf8) > 0, f"{html_file.name} UTF-8编码读取失败"
                except UnicodeDecodeError:
                    pytest.fail(f"{html_file.name} 不支持UTF-8编码")
                
                # 检查charset声明
                if "charset" in content_utf8.lower():
                    assert "utf-8" in content_utf8.lower(), f"{html_file.name} 字符集声明不是UTF-8"
    
    def test_project_structure_completeness(self):
        """测试项目结构完整性，验证所有必需文件都存在"""
        required_files = [
            Path("index.html"),
            Path("test-report.html"),
            Path("docs/fe3c52/315926/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"项目缺少必需文件: {missing_files}"
        
        # 检查docs目录结构
        docs_dir = Path("docs/fe3c52/315926")
        assert docs_dir.exists() and docs_dir.is_dir(), "文档目录结构不完整"