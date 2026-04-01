# 架构设计 - 碰撞检测系统

## 架构模式
基于现有Canvas游戏架构的碰撞检测扩展

## 技术栈

- **language**: JavaScript
- **framework**: 原生HTML5 Canvas

## 模块设计

### CollisionDetector
职责: 处理所有碰撞检测逻辑，包括边界检测、底部检测和方块间碰撞
- checkBoundaryCollision(piece, grid)
- checkBottomCollision(piece, grid)
- checkLeftRightCollision(piece, grid, direction)
- isValidPosition(piece, grid, offsetX, offsetY)

### GameGrid
职责: 扩展现有网格系统，添加占用状态管理和碰撞检测支持
- isCellOccupied(x, y)
- setCellOccupied(x, y, value)
- isPositionValid(x, y)
- placePiece(piece)

### Piece
职责: 扩展现有方块类，添加位置验证和碰撞响应方法
- canMoveTo(newX, newY, grid)
- tryMove(direction, grid)
- lockInPlace(grid)
- getOccupiedCells()

### GameEngine
职责: 修改现有游戏引擎，集成碰撞检测到游戏循环中
- updatePieceMovement()
- handleCollisions()
- processGameTick()

## 数据流
游戏循环中，方块尝试移动时先调用CollisionDetector检查目标位置是否合法，GameGrid提供占用状态查询，如果检测到碰撞则阻止移动或触发锁定逻辑，最终更新Canvas渲染

## 关键决策
- 采用预测性碰撞检测，在移动前验证目标位置合法性
- 将碰撞检测逻辑封装为独立模块，便于后续扩展多种方块类型
- 在现有Canvas渲染基础上添加碰撞状态可视化调试功能
- 保持与现有游戏循环的兼容性，通过扩展而非重写实现功能
- 使用网格坐标系进行碰撞计算，避免像素级检测的性能问题
