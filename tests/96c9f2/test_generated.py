import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    """测试前端文件和文档的存在性和内容"""
    
    def test_index_html_exists(self):
        """测试 index.html 文件是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), f"index.html 文件不存在: {index_path}"
        assert index_path.is_file(), f"index.html 不是一个文件: {index_path}"
    
    def test_index_html_contains_game_elements(self):
        """测试 index.html 文件是否包含游戏相关的关键元素"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<html" in content.lower(), "HTML文件缺少html标签"
        assert "<head>" in content.lower() or "<head " in content.lower(), "HTML文件缺少head标签"
        assert "<body>" in content.lower() or "<body " in content.lower(), "HTML文件缺少body标签"
        
        # 检查游戏相关元素
        game_keywords = ["game", "canvas", "script", "start", "play"]
        found_keywords = [keyword for keyword in game_keywords if keyword in content.lower()]
        assert len(found_keywords) >= 2, f"HTML文件应包含至少2个游戏相关关键词，找到: {found_keywords}"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        doc_path = Path("docs/96c9f2/131609/dev-notes.md")
        
        assert doc_path.exists(), f"开发文档不存在: {doc_path}"
        assert doc_path.is_file(), f"开发文档不是一个文件: {doc_path}"
        
        content = doc_path.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含开发相关内容
        dev_keywords = ["游戏", "状态", "循环", "管理", "开发", "设计", "功能"]
        found_keywords = [keyword for keyword in dev_keywords if keyword in content]
        assert len(found_keywords) >= 2, f"开发文档应包含至少2个开发相关关键词，找到: {found_keywords}"

class TestGameStateManagement:
    """测试游戏状态管理相关功能"""
    
    def test_html_contains_state_management_structure(self):
        """测试HTML文件是否包含状态管理相关的结构"""
        index_path = Path("frontend/index.html")
        
        if not index_path.exists():
            pytest.skip("index.html 文件不存在，跳过状态管理测试")
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript相关内容（用于状态管理）
        js_indicators = ["<script", "javascript", "function", "var ", "let ", "const "]
        has_js = any(indicator in content.lower() for indicator in js_indicators)
        
        if has_js:
            # 如果有JavaScript，检查可能的状态管理相关内容
            state_keywords = ["state", "status", "game", "update", "render", "loop"]
            found_state_keywords = [keyword for keyword in state_keywords if keyword in content.lower()]
            assert len(found_state_keywords) >= 1, f"应包含状态管理相关关键词，找到: {found_state_keywords}"
        else:
            # 如果没有JavaScript，至少应该有基本的游戏容器
            container_keywords = ["canvas", "div", "container", "game"]
            found_containers = [keyword for keyword in container_keywords if keyword in content.lower()]
            assert len(found_containers) >= 1, f"应包含游戏容器元素，找到: {found_containers}"

class TestProjectStructure:
    """测试项目结构的完整性"""
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否合理"""
        frontend_dir = Path("frontend")
        
        if frontend_dir.exists():
            assert frontend_dir.is_dir(), "frontend 应该是一个目录"
            
            # 检查是否有HTML文件
            html_files = list(frontend_dir.glob("*.html"))
            assert len(html_files) >= 1, f"frontend目录应包含至少一个HTML文件，找到: {html_files}"
        else:
            # 如果frontend目录不存在，检查当前目录是否有index.html
            index_path = Path("index.html")
            assert index_path.exists(), "既没有frontend目录，当前目录也没有index.html文件"