import pytest
from pathlib import Path
import os
import re

class TestFeature3161:
    """测试 feature_3161.js 功能模块"""
    
    def test_feature_3161_file_exists(self):
        """测试 feature_3161.js 文件是否存在"""
        feature_file = Path("src/feature_3161.js")
        assert feature_file.exists(), f"功能文件 {feature_file} 不存在"
        assert feature_file.is_file(), f"{feature_file} 不是一个有效的文件"
    
    def test_feature_3161_contains_function_definition(self):
        """测试 feature_3161.js 文件包含函数定义"""
        feature_file = Path("src/feature_3161.js")
        if feature_file.exists():
            content = feature_file.read_text(encoding='utf-8')
            # 检查是否包含函数定义关键字
            function_patterns = [
                r'function\s+\w+',  # function functionName
                r'const\s+\w+\s*=\s*\(',  # const funcName = (
                r'let\s+\w+\s*=\s*\(',    # let funcName = (
                r'var\s+\w+\s*=\s*\(',    # var funcName = (
                r'\w+\s*:\s*function',     # objMethod: function
                r'=>'                      # arrow function
            ]
            has_function = any(re.search(pattern, content) for pattern in function_patterns)
            assert has_function, "JavaScript文件应该包含至少一个函数定义"
        else:
            pytest.skip("功能文件不存在，跳过内容测试")
    
    def test_feature_3161_has_valid_javascript_syntax(self):
        """测试 feature_3161.js 文件包含有效的JavaScript语法元素"""
        feature_file = Path("src/feature_3161.js")
        if feature_file.exists():
            content = feature_file.read_text(encoding='utf-8')
            # 检查基本的JavaScript语法元素
            js_elements = [
                r'[{}\[\]();]',  # 基本的JavaScript符号
                r'(var|let|const|function|if|for|while|return)',  # JavaScript关键字
            ]
            has_js_syntax = any(re.search(pattern, content) for pattern in js_elements)
            assert has_js_syntax, "文件应该包含有效的JavaScript语法元素"
            
            # 检查文件不为空
            assert len(content.strip()) > 0, "JavaScript文件不应该为空"
        else:
            pytest.skip("功能文件不存在，跳过语法测试")

class TestDevNotes:
    """测试开发文档功能"""
    
    def test_dev_notes_file_exists(self):
        """测试开发笔记文档文件是否存在"""
        doc_file = Path("docs/96c9f2/bd2934/dev-notes.md")
        assert doc_file.exists(), f"开发文档 {doc_file} 不存在"
        assert doc_file.is_file(), f"{doc_file} 不是一个有效的文件"
    
    def test_dev_notes_contains_markdown_content(self):
        """测试开发笔记包含有效的Markdown内容"""
        doc_file = Path("docs/96c9f2/bd2934/dev-notes.md")
        if doc_file.exists():
            content = doc_file.read_text(encoding='utf-8')
            # 检查Markdown格式元素
            markdown_patterns = [
                r'^#{1,6}\s+.+',  # 标题
                r'^\*\s+.+',      # 无序列表
                r'^\d+\.\s+.+',   # 有序列表
                r'\*\*.+\*\*',    # 粗体
                r'`.+`',          # 行内代码
                r'```',           # 代码块
                r'\[.+\]\(.+\)'   # 链接
            ]
            has_markdown = any(re.search(pattern, content, re.MULTILINE) for pattern in markdown_patterns)
            assert has_markdown or len(content.strip()) > 0, "开发文档应该包含Markdown格式内容或至少有文本内容"
        else:
            pytest.skip("开发文档不存在，跳过内容测试")
    
    def test_dev_notes_has_meaningful_content(self):
        """测试开发笔记包含有意义的内容"""
        doc_file = Path("docs/96c9f2/bd2934/dev-notes.md")
        if doc_file.exists():
            content = doc_file.read_text(encoding='utf-8')
            # 检查文档长度和内容质量
            assert len(content.strip()) > 10, "开发文档应该包含足够的内容"
            
            # 检查是否包含开发相关的关键词
            dev_keywords = [
                '开发', '功能', '实现', '测试', '部署', '配置',
                'development', 'feature', 'implementation', 'test', 
                'deploy', 'config', 'TODO', 'NOTE', 'BUG', 'FIX'
            ]
            content_lower = content.lower()
            has_dev_content = any(keyword.lower() in content_lower for keyword in dev_keywords)
            
            # 如果没有开发关键词，至少应该有基本的文档结构
            if not has_dev_content:
                assert len(content.split('\n')) > 3, "文档应该包含开发相关内容或具有基本的文档结构"
        else:
            pytest.skip("开发文档不存在，跳过内容质量测试")

class TestProjectStructure:
    """测试项目整体结构"""
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否合理"""
        src_dir = Path("src")
        docs_dir = Path("docs")
        
        # 检查主要目录存在
        directories_exist = []
        if src_dir.exists():
            directories_exist.append("src")
        if docs_dir.exists():
            directories_exist.append("docs")
            
        assert len(directories_exist) > 0, "项目应该至少包含 src 或 docs 目录之一"
    
    def test_file_extensions_are_correct(self):
        """测试文件扩展名是否正确"""
        feature_file = Path("src/feature_3161.js")
        doc_file = Path("docs/96c9f2/bd2934/dev-notes.md")
        
        if feature_file.exists():
            assert feature_file.suffix == '.js', "功能文件应该是 .js 扩展名"
            
        if doc_file.exists():
            assert doc_file.suffix == '.md', "文档文件应该是 .md 扩展名"
    
    def test_files_are_readable(self):
        """测试文件是否可读且编码正确"""
        files_to_check = [
            Path("src/feature_3161.js"),
            Path("docs/96c9f2/bd2934/dev-notes.md")
        ]
        
        readable_files = 0
        for file_path