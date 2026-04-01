# 架构设计 - 响应式UI界面设计

## 架构模式
响应式UI组件架构

## 技术栈

- **language**: JavaScript
- **framework**: 原生HTML5/CSS3

## 模块设计

### UIManager
职责: 管理游戏界面状态、信息显示和响应式布局
- updateScore(score)
- updateLevel(level)
- updateLines(lines)
- showNextPiece(piece)
- updateGameStatus(status)
- handleResize()

### ResponsiveLayout
职责: 处理不同屏幕尺寸的布局适配和Canvas尺寸调整
- calculateOptimalSize()
- adjustLayout(screenSize)
- updateCanvasSize(width, height)

### GameControls
职责: 处理游戏控制按钮和键盘输入
- bindKeyboardEvents()
- bindTouchEvents()
- handleGameAction(action)

## 数据流
UIManager接收游戏状态更新 -> 更新界面显示元素 -> ResponsiveLayout监听窗口变化 -> 调整Canvas和布局尺寸 -> GameControls捕获用户输入 -> 触发游戏逻辑回调

## 关键决策
- 在现有index.html基础上完善CSS样式，修复截断的样式代码
- 使用CSS Grid和Flexbox实现响应式布局，支持移动端和桌面端
- 添加游戏信息面板显示分数、等级、消除行数等
- 实现下一个方块预览区域
- 添加游戏控制按钮，支持触屏设备
- 使用CSS媒体查询实现不同屏幕尺寸的适配
- 保持与现有Canvas游戏逻辑的接口兼容性
