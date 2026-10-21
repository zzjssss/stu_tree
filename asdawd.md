# 生产级 AI Agent 应用开发（Python）· 学习路线

> 记录时间：2026-10-15（周四）
> 当前进度：已完成 8 / 74 节点（11%）

## 接下来 7 个节点学习顺序

```
① 迭代器、生成器与 yield          (a0e1efda · Python基础 · ⭐⭐ · 120min)
        ↓
② asyncio 深入：事件循环与并发原语  (7c19a329 · Python基础 · ⭐⭐⭐ · 180min)
        ↓
③ 依赖注入与中间件                 (b77d7727 · FastAPI · ⭐⭐⭐ · 120min)
        ↓
④ 流式响应与 SSE                   (3d6c07f7 · FastAPI · ⭐⭐⭐ · 150min)
        ↓
⑤ FastAPI 测试：pytest/TestClient  (08011079 · FastAPI · ⭐⭐ · 150min)
        ↓
⑥ 异步状态管理与数据库（了解）      (c351e62a · FastAPI · ⭐⭐ · 90min)
        ↓
⑦ LLM 原理：Transformer 到生成机制  (6ee00efb · LLM API · ⭐⭐ · 150min)
```

## 顺序要点

- **①→② 必须严格按序**：asyncio 的前置就是生成器（yield 是异步流的地基）。
- **② 是承上启下的枢纽**：学完它 Python 基础 7/7 收官，同时打开 ④流式、⑥异步存储、⑦LLM 原理三条路。
- **③ 可与 ①② 并行**：依赖注入不依赖 asyncio，前置已满足，可随时插入学习。
- **⑤⑥ 属于收尾**：⑤ 测试建议真写几个用例；⑥ 只需 Recognize（了解级），别陷进 SQLAlchemy 细节。
- **⑦ 是新模块的起点**：学完 ⑦ 后即可分叉进入 Token 计费 / 采样参数两条 LLM API 支路。

## 投入与收益

- 总时长：约 960 分钟 ≈ 16 小时
- 完成后进度：8 → 15 / 74 ≈ 20%
- 里程碑：Python 基础 7/7 通关 · FastAPI 7/7 通关 · 拿到进入 LLM API / Agent 核心的完整入场券

## 已完成节点（截至记录时）

| 类别 | 节点 |
| --- | --- |
| Python 基础 | Python 语法快速入门、类型系统与数据结构、虚拟环境与工程结构、函数闭包与装饰器工厂、异常处理与日志体系 |
| FastAPI | FastAPI 路由与请求处理、Pydantic 模型与输入校验、Pydantic v2 深入 |
