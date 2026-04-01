# 架构设计 - 方块下落动画系统

## 架构模式
基于现有Canvas架构的增量扩展

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生HTML5 Canvas API

## 模块设计

### AnimationController
职责: 管理游戏主循环、帧率控制和渲染调度
- start()
- stop()
- pause()
- resume()
- setFPS(fps)

### FallSystem
职责: 控制方块下落逻辑、速度调节和下落定时器
- startFalling()
- stopFalling()
- setFallSpeed(speed)
- forceDrop()

### GameLoop
职责: 协调游戏状态更新和渲染，集成现有Grid和Block系统
- update(deltaTime)
- render()
- handleGameState()

### TimeManager
职责: 管理游戏时间、增量时间计算和速度控制
- getDeltaTime()
- updateTime()
- getGameTime()

## 数据流
AnimationController使用requestAnimationFrame驱动主循环 -> TimeManager计算deltaTime -> GameLoop.update()更新方块位置 -> FallSystem检查下落条件并移动方块 -> Grid系统验证位置合法性 -> GameLoop.render()重绘Canvas -> 循环继续直到方块着陆

## 关键决策
- 使用requestAnimationFrame替代setInterval确保60fps流畅动画
- 采用基于时间的下落系统而非固定帧数，支持动态速度调节
- 保持现有Grid和Block类不变，通过新增系统模块实现下落功能
- 实现可配置的下落速度，为后续难度系统预留接口
- 添加游戏暂停/恢复功能，提升用户体验
