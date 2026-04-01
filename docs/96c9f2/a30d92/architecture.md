# 架构设计 - I型方块类设计与实现

## 架构模式
面向对象模块化架构

## 技术栈

- **language**: JavaScript
- **framework**: 原生HTML5 Canvas

## 模块设计

### Block基类
职责: 定义方块的通用属性和行为，包括位置、颜色、形状数据结构和绘制接口
- constructor(x, y, color)
- draw(ctx, cellSize)
- getShape()
- getPosition()
- setPosition(x, y)
- getColor()

### IBlock类
职责: 继承Block基类，实现I型方块的具体形状定义和特殊绘制逻辑
- constructor(x, y)
- getShape() - 返回I型方块4x1形状矩阵
- draw(ctx, cellSize) - 重写绘制方法实现I型方块样式

### 方块工厂模块
职责: 负责创建不同类型的方块实例，为后续扩展多种方块类型做准备
- createBlock(type, x, y)
- getRandomBlock(x, y)

## 数据流
在现有Canvas渲染循环中集成方块绘制：游戏循环获取当前活动方块 -> 调用方块的draw方法 -> 方块根据自身形状矩阵和位置在Canvas上绘制 -> 渲染完成后等待下一帧

## 关键决策
- 采用继承模式设计Block基类，便于后续扩展T、L、O等其他方块类型
- 方块形状使用二维数组表示，1表示有方块，0表示空白，便于碰撞检测和旋转计算
- 在现有index.html中添加script标签引入方块类，保持单页面架构
- 方块绘制直接集成到现有Canvas渲染系统，不改变现有游戏循环结构
- 预留工厂模式接口，为后续多方块类型扩展提供统一创建入口
