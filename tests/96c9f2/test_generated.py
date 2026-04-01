import pytest
from pathlib import Path
import os
import re

class TestDocumentationAndDelivery:
    
    def test_feature_js_file_exists(self):
        """测试功能模块JavaScript文件是否存在"""
        project_root = Path(__file__).parent.parent
        feature_file = project_root / "src" / "feature_3161.js"
        assert feature_file.exists(), f"功能文件 {feature_file} 不存在"
        assert feature_file.is_file(), f"{feature_file} 不是一个有效的文件"
    
    def test_feature_js_contains_valid_content(self):
        """测试JavaScript功能文件包含有效的代码内容"""
        project_root = Path(__file__).parent.parent
        feature_file = project_root / "src" / "feature_3161.js"
        
        if feature_file.exists():
            content = feature_file.read_text(encoding='utf-8')
            # 检查是否包含JavaScript基本语法元素
            assert len(content.strip()) > 0, "JavaScript文件内容为空"
            # 检查是否包含函数定义或变量声明等基本代码结构
            js_patterns = [
                r'function\s+\w+',  # 函数定义
                r'const\s+\w+',     # const声明
                r'let\s+\w+',       # let声明
                r'var\s+\w+',       # var声明
                r'=>\s*{',          # 箭头函数
                r'export\s+',       # 导出语句
            ]
            has_js_syntax = any(re.search(pattern, content) for pattern in js_patterns)
            assert has_js_syntax, "JavaScript文件缺少基本的代码结构"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在且包含必要的项目信息"""
        project_root = Path(__file__).parent.parent
        doc_file = project_root / "docs" / "96c9f2" / "bd2934" / "dev-notes.md"
        
        assert doc_file.exists(), f"开发文档 {doc_file} 不存在"
        assert doc_file.is_file(), f"{doc_file} 不是一个有效的文件"
        
        content = doc_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查文档是否包含常见的开发文档关键词
        doc_keywords = ['功能', '实现', '说明', '文档', '项目', 'feature', 'implementation', 'documentation']
        content_lower = content.lower()
        has_relevant_content = any(keyword in content_lower for keyword in doc_keywords)
        assert has_relevant_content, "开发文档缺少相关的项目说明内容"
    
    def test_project_structure_integrity(self):
        """测试项目目录结构的完整性"""
        project_root = Path(__file__).parent.parent
        
        # 检查关键目录是否存在
        src_dir = project_root / "src"
        docs_dir = project_root / "docs"
        
        assert src_dir.exists() and src_dir.is_dir(), "src目录不存在"
        assert docs_dir.exists() and docs_dir.is_dir(), "docs目录不存在"
        
        # 检查src目录下是否有文件
        src_files = list(src_dir.glob("*"))
        assert len(src_files) > 0, "src目录为空"
        
        # 检查docs目录结构
        docs_subdirs = list(docs_dir.glob("*"))
        assert len(docs_subdirs) > 0, "docs目录为空"
    
    def test_file_encoding_and_readability(self):
        """测试文件编码正确性和可读性"""
        project_root = Path(__file__).parent.parent
        files_to_check = [
            project_root / "src" / "feature_3161.js",
            project_root / "docs" / "96c9f2" / "bd2934" / "dev-notes.md"
        ]
        
        for file_path in files_to_check:
            if file_path.exists():
                try:
                    # 尝试用UTF-8编码读取文件
                    content = file_path.read_text(encoding='utf-8')
                    assert isinstance(content, str), f"文件 {file_path} 读取后不是字符串类型"
                    # 检查文件大小合理性（不为空且不超过10MB）
                    file_size = file_path.stat().st_size
                    assert 0 < file_size < 10 * 1024 * 1024, f"文件 {file_path} 大小异常"
                except UnicodeDecodeError:
                    pytest.fail(f"文件 {file_path} 编码格式不正确，无法用UTF-8解码")