import pytest
from pathlib import Path
import re

class TestSnowflakeEffectFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在于 {frontend_dir} 目录中"
        assert index_file.is_file(), "index.html 应该是一个文件而不是目录"
    
    def test_index_html_contains_snowflake_elements(self):
        """测试 index.html 是否包含雪花特效相关的关键元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        # 确保文件存在
        assert index_file.exists(), "index.html 文件不存在"
        
        # 读取文件内容
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<html" in content.lower(), "HTML文件应包含html标签"
        assert "<head>" in content.lower() or "<head " in content.lower(), "HTML文件应包含head标签"
        assert "<body>" in content.lower() or "<body " in content.lower(), "HTML文件应包含body标签"
        
        # 检查雪花特效相关元素（可能的关键词）
        snowflake_keywords = ["snow", "flake", "snowflake", "雪花", "canvas", "animation"]
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML文件应包含雪花特效相关的内容"
    
    def test_index_html_has_valid_structure(self):
        """测试 index.html 是否具有有效的HTML结构和用户体验优化元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查DOCTYPE声明
        assert "<!doctype" in content.lower() or "<!DOCTYPE" in content, "HTML文件应包含DOCTYPE声明"
        
        # 检查meta标签（用户体验优化相关）
        meta_patterns = [
            r'<meta\s+[^>]*viewport[^>]*>',  # viewport meta标签
            r'<meta\s+[^>]*charset[^>]*>',   # charset meta标签
        ]
        
        has_viewport = bool(re.search(meta_patterns[0], content, re.IGNORECASE))
        has_charset = bool(re.search(meta_patterns[1], content, re.IGNORECASE))
        
        # 至少应该有其中一个meta标签来优化用户体验
        assert has_viewport or has_charset, "HTML文件应包含viewport或charset等用户体验优化的meta标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在"""
        docs_path = Path("docs/51ee63/8261e0/dev-notes.md")
        assert docs_path.exists(), f"开发文档不存在于 {docs_path}"
        assert docs_path.is_file(), "dev-notes.md 应该是一个文件"
        assert docs_path.suffix == ".md", "开发文档应该是markdown格式"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息"""
        docs_path = Path("docs/51ee63/8261e0/dev-notes.md")
        
        if not docs_path.exists():
            pytest.skip("开发文档文件不存在，跳过内容测试")
        
        content = docs_path.read_text(encoding='utf-8')
        
        # 检查文档是否包含项目相关关键词
        project_keywords = ["雪花", "特效", "用户体验", "优化", "frontend", "snowflake", "effect"]
        has_project_content = any(keyword in content for keyword in project_keywords)
        
        assert len(content.strip()) > 0, "开发文档不应为空"
        assert has_project_content, "开发文档应包含项目相关的内容描述"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查frontend目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录应该存在"
        assert frontend_dir.is_dir(), "frontend 应该是一个目录"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs 应该是一个目录"
            
        # 检查关键文件
        key_files = [
            Path("frontend/index.html"),
            Path("docs/51ee63/8261e0/dev-notes.md")
        ]
        
        existing_files = [f for f in key_files if f.exists()]
        assert len(existing_files) > 0, "至少应该存在一个关键项目文件"