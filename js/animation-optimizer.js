class AnimationOptimizer {
    constructor() {
        this.performanceHistory = [];
        this.maxHistoryLength = 60; // 保存60帧的性能数据
        this.lowFPSThreshold = 30;
        this.highFPSThreshold = 55;
        this.optimizationLevel = 0; // 0-3，优化等级
        this.lastOptimization = 0;
        this.optimizationCooldown = 2000; // 2秒冷却时间
        
        // 性能监控
        this.isRAFEnabled = true;
        this.throttleLevel = 0;
        
        // 设备性能检测
        this.devicePerformance = this.detectDevicePerformance();
    }
    
    checkPerformance(currentFPS) {
        // 记录性能历史
        this.performanceHistory.push({
            fps: currentFPS,
            timestamp: performance.now()
        });
        
        // 保持历史记录长度
        if (this.performanceHistory.length > this.maxHistoryLength) {
            this.performanceHistory.shift();
        }
        
        // 计算平均FPS
        const avgFPS = this.getAverageFPS();
        
        // 性能分析
        const performanceStatus = this.analyzePerformance(avgFPS);
        
        return {
            currentFPS,
            averageFPS: avgFPS,
            status: performanceStatus,
            optimizationLevel: this.optimizationLevel
        };
    }
    
    adjustQuality(animationEngine) {
        const now = performance.now();
        
        // 冷却时间检查
        if (now - this.lastOptimization < this.optimizationCooldown) {
            return;
        }
        
        const avgFPS = this.getAverageFPS();
        
        if (avgFPS < this.lowFPSThreshold && this.optimizationLevel < 3) {
            // 性能不足，提高优化等级
            this.optimizationLevel++;
            this.applyOptimization(animationEngine, this.optimizationLevel);
            this.lastOptimization = now;
            
            console.log(`性能优化等级提升至: ${this.optimizationLevel}`);
        } else if (avgFPS > this.highFPSThreshold && this.optimizationLevel > 0) {
            // 性能充足，降低优化等级
            this.optimizationLevel--;
            this.applyOptimization(animationEngine, this.optimizationLevel);
            this.lastOptimization = now;
            
            console.log(`性能优化等级降低至: ${this.optimizationLevel}`);
        }
    }
    
    applyOptimization(animationEngine, level) {
        switch (level) {
            case 0: // 无优化
                this.throttleLevel = 0;
                animationEngine.targetFPS = 60;
                break;
                
            case 1: // 轻度优化
                this.throttleLevel = 1;
                animationEngine.targetFPS = 45;
                break;
                
            case 2: // 中度优化
                this.throttleLevel = 2;
                animationEngine.targetFPS = 30;
                break;
                
            case 3: // 重度优化
                this.throttleLevel = 3;
                animationEngine.targetFPS = 20;
                break;
        }
        
        animationEngine.frameInterval = 1000 / animationEngine.targetFPS;
    }
    
    enableRAF() {
        this.isRAFEnabled = true;
    }
    
    disableRAF() {
        this.isRAFEnabled = false;
    }
    
    throttleAnimation() {
        return this.throttleLevel;
    }
    
    getOptimalSnowflakeCount() {
        const baseCount = this.devicePerformance.baseSnowflakeCount;
        const reductionFactor = this.optimizationLevel * 0.25;
        
        return Math.max(10, Math.floor(baseCount * (1 - reductionFactor)));
    }
    
    getAverageFPS() {
        if (this.performanceHistory.length === 0) return 60;
        
        const sum = this.performanceHistory.reduce((acc, record) => acc + record.fps, 0);
        return sum / this.performanceHistory.length;
    }
    
    analyzePerformance(avgFPS) {
        if (avgFPS >= this.highFPSThreshold) {
            return 'excellent';
        } else if (avgFPS >= this.lowFPSThreshold) {
            return 'good';
        } else if (avgFPS >= 20) {
            return 'poor';
        } else {
            return 'critical';
        }
    }
    
    detectDevicePerformance() {
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
        
        let performanceScore = 100;
        let baseSnowflakeCount = 100;
        
        // 检测硬件加速支持
        if (!gl) {
            performanceScore -= 30;
            baseSnowflakeCount = 50;
        }
        
        // 检测设备内存
        if (navigator.deviceMemory) {
            if (navigator.deviceMemory < 2) {
                performanceScore -= 20;
                baseSnowflakeCount = Math.min(baseSnowflakeCount, 30);
            } else if (navigator.deviceMemory < 4) {
                performanceScore -= 10;
                baseSnowflakeCount = Math.min(baseSnowflakeCount, 60);
            }
        }
        
        // 检测CPU核心数
        if (navigator.hardwareConcurrency) {
            if (navigator.hardwareConcurrency < 2) {
                performanceScore -= 15;
                baseSnowflakeCount = Math.min(baseSnowflakeCount, 40);
            } else if (navigator.hardwareConcurrency < 4) {
                performanceScore -= 5;
            }
        }
        
        // 检测移动设备
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        if (isMobile) {
            performanceScore -= 20;
            baseSnowflakeCount = Math.min(baseSnowflakeCount, 40);
        }
        
        return {
            score: performanceScore,
            baseSnowflakeCount,
            hasWebGL: !!gl,
            isMobile,
            deviceMemory: navigator.deviceMemory || 'unknown',
            hardwareConcurrency: navigator.hardwareConcurrency || 'unknown'
        };
    }
    
    // 获取优化建议
    getOptimizationSuggestions() {
        const suggestions = [];
        
        if (this.optimizationLevel > 0) {
            suggestions.push('当前正在进行性能优化');
        }
        
        if (!this.devicePerformance.hasWebGL) {
            suggestions.push('建议使用支持WebGL的浏览器以获得更好性能');
        }
        
        if (this.devicePerformance.isMobile) {
            suggestions.push('移动设备建议使用低性能模式');
        }
        
        if (this.getAverageFPS() < this.lowFPSThreshold) {
            suggestions.push('当前性能较低，建议关闭其他应用程序');
        }
        
        return suggestions;
    }
    
    // 重置优化状态
    reset() {
        this.performanceHistory = [];
        this.optimizationLevel = 0;
        this.throttleLevel = 0;
        this.lastOptimization = 0;
    }
    
    // 获取性能报告
    getPerformanceReport() {
        return {
            averageFPS: this.getAverageFPS(),
            optimizationLevel: this.optimizationLevel,
            devicePerformance: this.devicePerformance,
            suggestions: this.getOptimizationSuggestions(),
            performanceHistory: this.performanceHistory.slice(-10) // 最近10帧数据
        };
    }
}