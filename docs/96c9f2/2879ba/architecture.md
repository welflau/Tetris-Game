# 架构设计 - 游戏画布和网格系统实现

## 架构模式
基于Canvas的模块化架构

## 技术栈

- **language**: JavaScript
- **framework**: 原生HTML5 Canvas

## 模块设计

### GameCanvas
职责: 管理Canvas元素的创建、尺寸设置和基础渲染上下文
- init()
- resize()
- getContext()
- clear()

### GridSystem
职责: 实现10x20网格系统，提供坐标转换和网格绘制功能
- drawGrid()
- gridToPixel()
- pixelToGrid()
- isValidPosition()

### GameRenderer
职责: 统一管理所有渲染操作，包括网格、方块和UI元素的绘制
- render()
- renderGrid()
- renderBlock()
- renderUI()

### GameState
职责: 管理游戏状态数据，包括网格状态、当前方块位置等
- getGrid()
- setCell()
- getCell()
- reset()

## 数据流
GameCanvas初始化Canvas元素 -> GridSystem计算网格尺寸和坐标映射 -> GameState维护网格状态数据 -> GameRenderer统一渲染所有元素到Canvas -> 响应式监听器处理窗口变化并重新计算尺寸

## 关键决策
- 在现有index.html的gameCanvas元素基础上扩展，保持现有样式结构
- 采用10x20标准俄罗斯方块网格规格，每个格子30px大小
- 使用二维数组表示网格状态，0表示空格，非0表示已占用
- 实现坐标转换函数，支持网格坐标与像素坐标互转
- 添加响应式支持，根据屏幕大小动态调整Canvas尺寸
- 网格线使用半透明白色绘制，提供清晰的视觉引导
