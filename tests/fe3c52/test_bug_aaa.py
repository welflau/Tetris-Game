import pytest
from pathlib import Path
import re

class TestOtherModule:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        assert index_file.is_file(), "index.html不是一个有效的文件"
    
    def test_index_html_contains_title_element(self):
        """测试index.html文件是否包含title标签元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 检查是否包含title标签
        title_pattern = r'<title[^>]*>.*?</title>'
        assert re.search(title_pattern, content, re.IGNORECASE | re.DOTALL), "HTML文件中缺少title标签"
    
    def test_index_html_title_content_not_empty(self):
        """测试index.html文件中的title标签内容不为空，验证AAA标题显示问题"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        # 提取title标签内容
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        assert title_match is not None, "未找到title标签"
        
        title_content = title_match.group(1).strip()
        assert len(title_content) > 0, "title标签内容为空，这可能是导致页面标题AAA未显示的原因"
        # 检查是否包含预期的标题内容
        assert "AAA" in title_content or len(title_content) > 2, "title内容可能不正确，应该包含有意义的标题而不是占位符"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档文件是否包含有效内容"""
        dev_notes_file = Path("docs/fe3c52/3ba7c2/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        # 检查是否包含markdown格式的内容
        assert any(marker in content for marker in ['#', '##', '###', '-', '*', '```']), "文档内容不符合markdown格式规范"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性，确保相关文件都存在"""
        required_files = [
            Path("index.html"),
            Path("docs/fe3c52/3ba7c2/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"以下必需文件缺失: {', '.join(missing_files)}"