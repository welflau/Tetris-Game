# 架构设计 - 游戏主循环和状态管理

## 架构模式
基于现有Canvas的游戏主循环架构

## 技术栈

- **language**: JavaScript
- **framework**: 原生HTML5 Canvas

## 模块设计

### GameLoop
职责: 管理游戏主循环，控制帧率和游戏状态更新
- start()
- stop()
- pause()
- resume()
- update(deltaTime)
- render()

### GameState
职责: 管理游戏状态（运行、暂停、结束等）和状态转换
- setState(state)
- getState()
- isRunning()
- isPaused()
- isGameOver()

### TimeManager
职责: 处理时间相关逻辑，包括帧率控制和游戏时间计算
- getDeltaTime()
- getFPS()
- getGameTime()

### RenderManager
职责: 统一管理所有渲染操作，确保渲染顺序和性能
- clearCanvas()
- renderGrid()
- renderBlock()
- renderUI()

## 数据流
GameLoop作为核心控制器，每帧调用TimeManager获取时间差值，通过GameState检查当前状态，如果游戏运行中则更新游戏逻辑（方块位置、碰撞检测等），最后通过RenderManager进行统一渲染。状态变化通过GameState管理，支持暂停/恢复/重启等操作。

## 关键决策
- 使用requestAnimationFrame实现60fps流畅动画，确保浏览器优化
- 采用状态机模式管理游戏状态，便于后续扩展更多状态
- 实现时间独立的游戏逻辑，使用deltaTime确保不同设备上一致的游戏速度
- 将渲染逻辑集中管理，为后续添加特效和UI元素做准备
- 在现有Canvas基础上扩展，保持与已有Grid和Block系统的兼容性
