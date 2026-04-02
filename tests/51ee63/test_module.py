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
        
        # 检查是否包含基本的HTML结构
        assert "<html" in content.lower(), "HTML文件应包含html标签"
        assert "<head>" in content.lower() or "<head " in content.lower(), "HTML文件应包含head标签"
        assert "<body>" in content.lower() or "<body " in content.lower(), "HTML文件应包含body标签"
        
        # 检查是否包含雪花特效相关元素（canvas、JavaScript或CSS动画相关）
        snowflake_indicators = [
            "snow", "snowflake", "canvas", "animation", 
            "particle", "effect", "flake"
        ]
        
        content_lower = content.lower()
        has_snowflake_element = any(indicator in content_lower for indicator in snowflake_indicators)
        assert has_snowflake_element, f"HTML文件应包含雪花特效相关元素，如: {', '.join(snowflake_indicators)}"
    
    def test_index_html_has_valid_structure(self):
        """测试 index.html 是否具有有效的HTML结构和用户体验优化元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        content_lower = content.lower()
        
        # 检查DOCTYPE声明
        assert "<!doctype" in content_lower, "HTML文件应包含DOCTYPE声明"
        
        # 检查是否包含viewport meta标签（移动端优化）
        viewport_pattern = r'<meta[^>]*name=["\']viewport["\'][^>]*>'
        has_viewport = bool(re.search(viewport_pattern, content, re.IGNORECASE))
        
        # 检查是否包含charset声明
        charset_pattern = r'<meta[^>]*charset[^>]*>'
        has_charset = bool(re.search(charset_pattern, content, re.IGNORECASE))
        
        # 检查是否包含title标签
        has_title = "<title>" in content_lower
        
        # 用户体验优化检查：至少应该有charset和title
        assert has_charset or has_title, "HTML文件应包含基本的用户体验优化元素（charset声明或title标签）"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档是否存在且可读取"""
        docs_path = Path("docs/51ee63/8261e0/dev-notes.md")
        
        assert docs_path.exists(), f"开发文档不存在于路径: {docs_path}"
        assert docs_path.is_file(), "dev-notes.md 应该是一个文件"
        
        # 尝试读取文件内容
        try:
            content = docs_path.read_text(encoding='utf-8')
            assert len(content.strip()) > 0, "开发文档不应为空"
        except UnicodeDecodeError:
            # 如果UTF-8解码失败，尝试其他编码
            content = docs_path.read_text(encoding='gbk')
            assert len(content.strip()) > 0, "开发文档不应为空"
    
    def test_dev_notes_contains_relevant_content(self):
        """测试开发文档是否包含项目相关内容"""
        docs_path = Path("docs/51ee63/8261e0/dev-notes.md")
        
        assert docs_path.exists(), "开发文档不存在"
        
        try:
            content = docs_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            content = docs_path.read_text(encoding='gbk')
        
        content_lower = content.lower()
        
        # 检查是否包含项目相关关键词
        project_keywords = [
            "雪花", "snow", "特效", "effect", "优化", "optimization",
            "用户体验", "user experience", "ux", "frontend", "前端"
        ]
        
        has_relevant_content = any(keyword in content_lower for keyword in project_keywords)
        assert has_relevant_content, f"开发文档应包含项目相关内容，如: {', '.join(project_keywords)}"