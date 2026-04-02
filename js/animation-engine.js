class SnowflakeAnimationEngine {
    constructor(container) {
        this.container = container;
        this.isRunning = false;
        this.isPaused = false;
        this.animationId = null;
        this.lastTime = 0;
        this.targetFPS = 60;
        this.frameInterval = 1000 / this.targetFPS;
        this.snowflakes = [];
        this.performanceMode = 'auto'; // 'high', 'medium', 'low', 'auto'
        
        // 绑定渲染器和优化器
        this.renderer = new SnowflakeRenderer(container);
        this.optimizer = new AnimationOptimizer();
        
        // 性能监控
        this.frameCount = 0;
        this.lastFPSCheck = 0;
        this.currentFPS = 60;
    }
    
    start() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        this.isPaused = false;
        this.lastTime = performance.now();
        this.animate();
        
        console.log('雪花动画引擎已启动');
    }
    
    stop() {
        if (!this.isRunning) return;
        
        this.isRunning = false;
        this.isPaused = false;
        
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
        
        // 清理所有雪花
        this.snowflakes.forEach(snowflake => {
            this.renderer.removeSnowflake(snowflake.element);
        });
        this.snowflakes = [];
        
        console.log('雪花动画引擎已停止');
    }
    
    pause() {
        if (!this.isRunning || this.isPaused) return;
        
        this.isPaused = true;
        console.log('雪花动画引擎已暂停');
    }
    
    resume() {
        if (!this.isRunning || !this.isPaused) return;
        
        this.isPaused = false;
        this.lastTime = performance.now();
        console.log('雪花动画引擎已恢复');
    }
    
    animate() {
        if (!this.isRunning) return;
        
        const currentTime = performance.now();
        const deltaTime = currentTime - this.lastTime;
        
        // 帧率控制
        if (deltaTime >= this.frameInterval) {
            if (!this.isPaused) {
                this.updateSnowflakes(deltaTime);
                this.render();
                
                // 性能监控
                this.updateFPS(currentTime);
                
                // 自动性能优化
                if (this.performanceMode === 'auto') {
                    this.optimizer.checkPerformance(this.currentFPS);
                    this.optimizer.adjustQuality(this);
                }
            }
            
            this.lastTime = currentTime - (deltaTime % this.frameInterval);
        }
        
        this.animationId = requestAnimationFrame(() => this.animate());
    }
    
    updateSnowflakes(deltaTime) {
        const dt = deltaTime / 1000; // 转换为秒
        
        for (let i = this.snowflakes.length - 1; i >= 0; i--) {
            const snowflake = this.snowflakes[i];
            
            // 更新位置
            snowflake.y += snowflake.speed * dt * 60; // 60fps基准
            snowflake.x += Math.sin(snowflake.y * 0.01 + snowflake.drift) * snowflake.sway * dt * 60;
            
            // 更新旋转
            snowflake.rotation += snowflake.rotationSpeed * dt * 60;
            
            // 边界检查
            if (snowflake.y > window.innerHeight + 50) {
                // 雪花落到底部，移除
                this.renderer.removeSnowflake(snowflake.element);
                this.snowflakes.splice(i, 1);
            } else if (snowflake.x < -50) {
                snowflake.x = window.innerWidth + 50;
            } else if (snowflake.x > window.innerWidth + 50) {
                snowflake.x = -50;
            }
        }
    }
    
    render() {
        this.snowflakes.forEach(snowflake => {
            this.renderer.renderSnowflake(snowflake);
        });
    }
    
    addSnowflake(snowflake) {
        this.snowflakes.push(snowflake);
    }
    
    setPerformanceMode(mode) {
        this.performanceMode = mode;
        
        switch (mode) {
            case 'high':
                this.targetFPS = 60;
                break;
            case 'medium':
                this.targetFPS = 30;
                break;
            case 'low':
                this.targetFPS = 15;
                break;
            case 'auto':
                this.targetFPS = 60;
                break;
        }
        
        this.frameInterval = 1000 / this.targetFPS;
        console.log(`性能模式设置为: ${mode}, 目标FPS: ${this.targetFPS}`);
    }
    
    updateFPS(currentTime) {
        this.frameCount++;
        
        if (currentTime - this.lastFPSCheck >= 1000) {
            this.currentFPS = this.frameCount;
            this.frameCount = 0;
            this.lastFPSCheck = currentTime;
        }
    }
    
    getSnowflakeCount() {
        return this.snowflakes.length;
    }
    
    getCurrentFPS() {
        return this.currentFPS;
    }
}