import pytest
from pathlib import Path
import re

class TestSnowflakeEffectFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html 文件不存在"
        assert index_path.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_snowflake_elements(self):
        """测试 index.html 文件是否包含雪花特效相关的关键元素"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "缺少 HTML 标签"
        assert '<head>' in content.lower() or '<head ' in content.lower(), "缺少 head 标签"
        assert '<body>' in content.lower() or '<body ' in content.lower(), "缺少 body 标签"
        
        # 检查雪花特效相关元素
        snowflake_keywords = ['snow', 'flake', 'canvas', 'animation', 'particle']
        has_snowflake_content = any(keyword in content.lower() for keyword in snowflake_keywords)
        assert has_snowflake_content, "HTML 文件中未找到雪花特效相关内容"
    
    def test_index_html_has_performance_optimization_features(self):
        """测试 index.html 文件是否包含性能优化相关的特性"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过性能优化测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查性能优化相关特性
        performance_indicators = [
            'requestanimationframe',  # 动画优化
            'canvas',  # Canvas 渲染
            'transform',  # CSS 变换优化
            'will-change',  # CSS 性能提示
            'defer',  # 脚本延迟加载
            'async'  # 异步加载
        ]
        
        performance_score = sum(1 for indicator in performance_indicators 
                              if indicator in content.lower())
        
        assert performance_score >= 1, f"未找到足够的性能优化特性，当前得分: {performance_score}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_path = Path("docs/51ee63/16dedc/dev-notes.md")
        
        assert dev_notes_path.exists(), "开发文档文件不存在"
        assert dev_notes_path.is_file(), "开发文档不是一个有效的文件"
        
        # 测试文件是否可读
        try:
            content = dev_notes_path.read_text(encoding='utf-8')
            assert len(content.strip()) > 0, "开发文档文件为空"
        except UnicodeDecodeError:
            # 如果UTF-8解码失败，尝试其他编码
            content = dev_notes_path.read_text(encoding='gbk')
            assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_dev_notes_contains_project_information(self):
        """测试开发文档是否包含项目相关信息"""
        dev_notes_path = Path("docs/51ee63/16dedc/dev-notes.md")
        
        if not dev_notes_path.exists():
            pytest.skip("开发文档文件不存在，跳过内容测试")
        
        try:
            content = dev_notes_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            content = dev_notes_path.read_text(encoding='gbk')
        
        # 检查是否包含项目相关关键词
        project_keywords = ['雪花', 'snow', '特效', 'effect', '性能', 'performance', '优化', 'optimization']
        has_project_content = any(keyword in content.lower() for keyword in project_keywords)
        
        assert has_project_content, "开发文档中未找到项目相关内容"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否合理"""
        frontend_path = Path("frontend")
        
        assert frontend_path.exists(), "frontend 目录不存在"
        assert frontend_path.is_dir(), "frontend 不是一个目录"
        
        # 检查是否有基本的前端文件
        expected_files = ["index.html"]
        existing_files = []
        
        for file_name in expected_files:
            file_path = frontend_path / file_name
            if file_path.exists():
                existing_files.append(file_name)
        
        assert len(existing_files) > 0, f"frontend 目录中缺少基本文件，期望: {expected_files}"