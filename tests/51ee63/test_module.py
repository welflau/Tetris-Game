import pytest
from pathlib import Path
import re

class TestSnowflakeEffect:
    """雪花特效集成测试类"""
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效相关的关键元素"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或雪花相关的div
        assert re.search(r'<canvas|<div.*snow|snowflake', content, re.IGNORECASE), \
            "HTML文件中未找到雪花特效相关元素"
        
        # 检查是否包含JavaScript代码或引用
        assert re.search(r'<script|\.js', content, re.IGNORECASE), \
            "HTML文件中未找到JavaScript代码或引用"
        
        # 检查是否包含CSS样式或引用
        assert re.search(r'<style|\.css|style=', content, re.IGNORECASE), \
            "HTML文件中未找到CSS样式或引用"
    
    def test_dev_notes_file_exists_and_valid(self):
        """测试开发文档是否存在且包含有效内容"""
        dev_notes_file = Path("docs/51ee63/19a016/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含markdown格式的内容
        assert re.search(r'#|##|\*|\-|\[.*\]', content), \
            "开发文档不包含有效的markdown格式内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查根目录文件
        root_files = ["index.html"]
        for file_name in root_files:
            file_path = Path(file_name)
            assert file_path.exists(), f"项目根目录缺少必要文件: {file_name}"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists() and docs_dir.is_dir(), "docs目录不存在"
        
        # 检查特定的文档路径
        specific_doc = Path("docs/51ee63/19a016/dev-notes.md")
        assert specific_doc.exists(), "指定的开发文档路径不存在"
    
    def test_html_file_size_and_encoding(self):
        """测试HTML文件大小和编码格式是否合理"""
        html_file = Path("index.html")
        file_size = html_file.stat().st_size
        
        # 文件大小应该大于100字节（基本HTML结构）且小于10MB
        assert 100 < file_size < 10 * 1024 * 1024, \
            f"HTML文件大小异常: {file_size} bytes"
        
        # 尝试以UTF-8编码读取文件
        try:
            content = html_file.read_text(encoding='utf-8')
            assert isinstance(content, str), "HTML文件内容读取失败"
        except UnicodeDecodeError:
            pytest.fail("HTML文件编码格式不是UTF-8或存在编码问题")