# 架构设计 - 雪花特效样式和层级处理

## 架构模式
增量式CSS样式扩展

## 技术栈

- **language**: CSS3
- **framework**: 原生CSS + HTML

## 模块设计

### 雪花CSS样式系统
职责: 完善雪花元素的视觉样式，包括颜色、大小、透明度等变体样式
- .snowflake基础样式类
- .snowflake.type-*颜色变体类
- .snowflake.size-*大小变体类
- .snowflake.opacity-*透明度变体类

### 层级管理系统
职责: 确保雪花背景层级正确，不影响游戏界面交互
- #snowflake-container容器样式
- z-index层级控制
- pointer-events交互控制

### 响应式适配
职责: 确保雪花效果在不同屏幕尺寸下正常显示
- @media查询规则
- viewport相对单位
- 动态字体大小调整

## 数据流
CSS样式类通过类名组合应用到雪花DOM元素上，通过z-index控制层级关系，使用CSS变量和媒体查询实现响应式效果，样式优先级确保不覆盖游戏界面样式

## 关键决策
- 在现有index.html的<style>标签中补充完整的雪花样式定义
- 使用z-index: -1确保雪花层级在游戏界面之下
- 通过pointer-events: none确保雪花不影响用户交互
- 使用CSS类组合方式实现雪花样式变体的灵活组合
- 采用相对单位(em, vh, vw)确保响应式效果
- 使用will-change: transform优化动画性能
