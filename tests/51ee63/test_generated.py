import pytest
from pathlib import Path
import re

class TestSnowflakeDesignProject:
    """雪花视觉素材准备项目测试类"""
    
    @pytest.fixture
    def project_root(self):
        """获取项目根目录"""
        return Path(__file__).parent
    
    def test_html_file_exists(self, project_root):
        """测试HTML文件是否存在"""
        html_file = project_root / "design" / "index.html"
        assert html_file.exists(), f"HTML文件不存在: {html_file}"
        assert html_file.is_file(), f"路径不是文件: {html_file}"
    
    def test_html_content_structure(self, project_root):
        """测试HTML文件内容包含必要的雪花设计元素"""
        html_file = project_root / "design" / "index.html"
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过内容测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower(), "HTML文件缺少body标签"
        
        # 检查雪花相关元素
        snowflake_keywords = ['snowflake', '雪花', 'snow', 'crystal', '晶体']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML内容中未找到雪花相关关键词"
    
    def test_dev_notes_documentation(self, project_root):
        """测试开发文档是否存在且包含有效内容"""
        dev_notes_file = project_root / "docs" / "51ee63" / "327d7d" / "dev-notes.md"
        
        assert dev_notes_file.exists(), f"开发文档不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"路径不是文件: {dev_notes_file}"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含开发相关内容
        dev_keywords = ['开发', 'development', '设计', 'design', '雪花', 'snowflake', '素材', 'material']
        has_dev_content = any(keyword in content.lower() for keyword in dev_keywords)
        assert has_dev_content, "开发文档中未找到相关开发内容"
    
    def test_project_structure_integrity(self, project_root):
        """测试项目目录结构完整性"""
        design_dir = project_root / "design"
        docs_dir = project_root / "docs"
        
        assert design_dir.exists(), "design目录不存在"
        assert design_dir.is_dir(), "design路径不是目录"
        
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs路径不是目录"
        
        # 检查docs子目录结构
        docs_subdir = docs_dir / "51ee63" / "327d7d"
        assert docs_subdir.exists(), "docs子目录结构不完整"
        assert docs_subdir.is_dir(), "docs子目录路径不是目录"
    
    def test_html_file_encoding_and_format(self, project_root):
        """测试HTML文件编码和格式正确性"""
        html_file = project_root / "design" / "index.html"
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过编码测试")
        
        try:
            content = html_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            pytest.fail("HTML文件编码不是UTF-8或存在编码问题")
        
        # 检查HTML文档类型声明
        has_doctype = content.strip().lower().startswith('<!doctype') or '<html' in content.lower()
        assert has_doctype, "HTML文件缺少文档类型声明"
        
        # 检查是否有基本的meta标签
        meta_pattern = r'<meta[^>]*charset[^>]*>'
        has_charset = re.search(meta_pattern, content, re.IGNORECASE)
        if not has_charset:
            # 如果没有charset meta标签，至少应该有其他meta标签
            has_meta = '<meta' in content.lower()
            assert has_meta or len(content) < 200, "HTML文件建议包含字符集声明"