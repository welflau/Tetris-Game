import pytest
from pathlib import Path
from bs4 import BeautifulSoup
import re

class TestSnowflakeEffectFrontend:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_snowflake_elements(self):
        """测试HTML文件是否包含雪花特效相关的关键元素"""
        html_file = Path("frontend/index.html")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否包含canvas元素（通常用于雪花动画）
        canvas_elements = soup.find_all('canvas')
        script_elements = soup.find_all('script')
        
        # 至少应该有canvas或script标签来实现雪花效果
        assert len(canvas_elements) > 0 or len(script_elements) > 0, "HTML文件缺少雪花特效实现元素"
        
        # 检查内容中是否包含雪花相关关键词
        content_lower = content.lower()
        snowflake_keywords = ['snow', 'flake', '雪花', 'particle', 'animation']
        has_snowflake_keyword = any(keyword in content_lower for keyword in snowflake_keywords)
        assert has_snowflake_keyword, "HTML文件内容中未找到雪花特效相关关键词"
    
    def test_html_performance_optimization_indicators(self):
        """测试HTML文件是否包含性能优化相关的指标和元素"""
        html_file = Path("frontend/index.html")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否有性能优化相关的meta标签
        meta_tags = soup.find_all('meta')
        viewport_meta = any('viewport' in str(meta) for meta in meta_tags)
        
        # 检查是否有requestAnimationFrame或其他性能优化相关代码
        performance_keywords = ['requestanimationframe', 'performance', 'optimize', '优化', 'fps']
        content_lower = content.lower()
        has_performance_code = any(keyword in content_lower for keyword in performance_keywords)
        
        assert viewport_meta or has_performance_code, "HTML文件中未找到性能优化相关的代码或配置"
    
    def test_dev_notes_file_exists_and_valid(self):
        """测试开发文档是否存在且包含有效内容"""
        dev_notes_file = Path("docs/51ee63/16dedc/dev-notes.md")
        
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "开发文档不是一个有效的文件"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档是否为空
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含开发相关关键词
        dev_keywords = ['优化', '性能', 'performance', '雪花', 'snow', '特效', 'effect']
        content_lower = content.lower()
        has_dev_keyword = any(keyword in content_lower for keyword in dev_keywords)
        assert has_dev_keyword, "开发文档中未找到项目相关的关键词"
    
    def test_html_structure_validity(self):
        """测试HTML文件结构的有效性"""
        html_file = Path("frontend/index.html")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        html_tag = soup.find('html')
        head_tag = soup.find('head')
        body_tag = soup.find('body')
        
        assert html_tag is not None, "HTML文件缺少html标签"
        assert head_tag is not None, "HTML文件缺少head标签"
        assert body_tag is not None, "HTML文件缺少body标签"
        
        # 检查title标签
        title_tag = soup.find('title')
        assert title_tag is not None, "HTML文件缺少title标签"
        assert len(title_tag.get_text().strip()) > 0, "title标签内容为空"