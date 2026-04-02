class SnowflakeRenderer {
    constructor(container) {
        this.container = container;
        this.elementPool = []; // 元素池，用于复用DOM元素
        this.maxPoolSize = 100;
    }
    
    renderSnowflake(snowflake) {
        if (!snowflake.element) {
            snowflake.element = this.createSnowflakeElement(snowflake);
        }
        
        this.updatePosition(snowflake.element, snowflake.x, snowflake.y);
        this.updateOpacity(snowflake.element, snowflake.opacity);
        this.updateScale(snowflake.element, snowflake.size);
        this.updateRotation(snowflake.element, snowflake.rotation);
    }
    
    createSnowflakeElement(snowflake) {
        let element;
        
        // 尝试从元素池获取
        if (this.elementPool.length > 0) {
            element = this.elementPool.pop();
        } else {
            element = document.createElement('div');
            element.className = 'snowflake';
            this.container.appendChild(element);
        }
        
        // 设置雪花样式
        element.style.cssText = `
            position: absolute;
            pointer-events: none;
            user-select: none;
            will-change: transform;
            color: ${snowflake.color};
            font-size: ${snowflake.size}px;
            z-index: ${snowflake.zIndex};
        `;
        
        // 设置雪花字符
        element.textContent = snowflake.character;
        
        return element;
    }
    
    updatePosition(element, x, y) {
        if (!element) return;
        
        // 使用transform而不是left/top，性能更好
        element.style.transform = `translate3d(${x}px, ${y}px, 0) rotate(${element._rotation || 0}deg) scale(${element._scale || 1})`;
    }
    
    updateOpacity(element, opacity) {
        if (!element) return;
        
        element.style.opacity = opacity;
    }
    
    updateScale(element, scale) {
        if (!element) return;
        
        element._scale = scale;
        // 更新transform
        const currentTransform = element.style.transform;
        const scaleRegex = /scale\([^)]*\)/;
        
        if (scaleRegex.test(currentTransform)) {
            element.style.transform = currentTransform.replace(scaleRegex, `scale(${scale})`);
        } else {
            element.style.transform += ` scale(${scale})`;
        }
    }
    
    updateRotation(element, rotation) {
        if (!element) return;
        
        element._rotation = rotation;
        // 更新transform
        const currentTransform = element.style.transform;
        const rotateRegex = /rotate\([^)]*\)/;
        
        if (rotateRegex.test(currentTransform)) {
            element.style.transform = currentTransform.replace(rotateRegex, `rotate(${rotation}deg)`);
        } else {
            element.style.transform += ` rotate(${rotation}deg)`;
        }
    }
    
    removeSnowflake(element) {
        if (!element) return;
        
        // 将元素放回池中复用
        if (this.elementPool.length < this.maxPoolSize) {
            element.style.display = 'none';
            this.elementPool.push(element);
        } else {
            // 池满了，直接移除
            if (element.parentNode) {
                element.parentNode.removeChild(element);
            }
        }
    }
    
    // 批量渲染优化
    batchRender(snowflakes) {
        // 使用DocumentFragment进行批量DOM操作
        const fragment = document.createDocumentFragment();
        const updates = [];
        
        snowflakes.forEach(snowflake => {
            if (!snowflake.element) {
                snowflake.element = this.createSnowflakeElement(snowflake);
                fragment.appendChild(snowflake.element);
            }
            
            updates.push(() => {
                this.updatePosition(snowflake.element, snowflake.x, snowflake.y);
                this.updateOpacity(snowflake.element, snowflake.opacity);
                this.updateScale(snowflake.element, snowflake.size);
                this.updateRotation(snowflake.element, snowflake.rotation);
            });
        });
        
        // 批量添加新元素
        if (fragment.children.length > 0) {
            this.container.appendChild(fragment);
        }
        
        // 批量更新样式
        requestAnimationFrame(() => {
            updates.forEach(update => update());
        });
    }
    
    // 清理所有雪花
    clear() {
        const snowflakes = this.container.querySelectorAll('.snowflake');
        snowflakes.forEach(element => {
            this.removeSnowflake(element);
        });
    }
    
    // 获取渲染统计信息
    getRenderStats() {
        return {
            activeElements: this.container.querySelectorAll('.snowflake').length,
            pooledElements: this.elementPool.length,
            totalElements: this.container.querySelectorAll('.snowflake').length + this.elementPool.length
        };
    }
}