import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    """前端文件功能测试和兼容性验证"""
    
    def test_index_html_exists_and_valid(self):
        """测试index.html文件是否存在且包含基本HTML结构"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        assert content.strip(), "index.html文件内容为空"
        
        # 验证基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body标签"
        
        # 验证关键元素
        assert '<title>' in content.lower(), "缺少title标签"
    
    def test_test_report_html_structure(self):
        """测试test-report.html文件结构和测试报告相关元素"""
        report_file = Path("test-report.html")
        assert report_file.exists(), "test-report.html文件不存在"
        
        content = report_file.read_text(encoding='utf-8')
        assert content.strip(), "test-report.html文件内容为空"
        
        # 验证测试报告相关关键词
        report_keywords = ['test', 'report', 'result', 'pass', 'fail', 'summary']
        content_lower = content.lower()
        
        keyword_found = any(keyword in content_lower for keyword in report_keywords)
        assert keyword_found, f"测试报告文件应包含以下关键词之一: {report_keywords}"
        
        # 验证HTML基本结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "测试报告缺少html标签"
    
    def test_dev_notes_documentation(self):
        """测试开发文档是否存在且包含有效内容"""
        docs_file = Path("docs/fe3c52/315926/dev-notes.md")
        assert docs_file.exists(), "开发文档dev-notes.md不存在"
        
        content = docs_file.read_text(encoding='utf-8')
        assert content.strip(), "开发文档内容为空"
        
        # 验证Markdown文档特征
        markdown_indicators = ['#', '##', '###', '-', '*', '```', '**', '__']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "文档应包含Markdown格式标记"
        
        # 验证文档长度合理性
        assert len(content) > 50, "开发文档内容过短，应包含更详细的说明"
    
    def test_html_files_encoding_compatibility(self):
        """测试HTML文件编码兼容性和字符集声明"""
        html_files = [Path("index.html"), Path("test-report.html")]
        
        for html_file in html_files:
            if html_file.exists():
                # 测试UTF-8编码读取
                try:
                    content = html_file.read_text(encoding='utf-8')
                    assert content, f"{html_file.name}使用UTF-8编码读取失败"
                except UnicodeDecodeError:
                    pytest.fail(f"{html_file.name}不是有效的UTF-8编码文件")
                
                # 检查字符集声明
                charset_patterns = [
                    r'<meta[^>]+charset[^>]*utf-8[^>]*>',
                    r'<meta[^>]+content[^>]*charset=utf-8[^>]*>'
                ]
                
                has_charset = any(
                    re.search(pattern, content, re.IGNORECASE) 
                    for pattern in charset_patterns
                )
                
                if not has_charset:
                    print(f"警告: {html_file.name}建议添加UTF-8字符集声明以提高兼容性")
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性和文件组织"""
        # 验证核心文件存在
        core_files = [
            Path("index.html"),
            Path("test-report.html"),
            Path("docs/fe3c52/315926/dev-notes.md")
        ]
        
        existing_files = [f for f in core_files if f.exists()]
        assert len(existing_files) >= 2, f"项目核心文件缺失，现有文件: {[str(f) for f in existing_files]}"
        
        # 验证目录结构
        docs_dir = Path("docs/fe3c52/315926")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs/fe3c52/315926应该是目录"
            
            # 检查目录权限
            assert docs_dir.stat().st_mode & 0o444, "文档目录应具有读取权限"