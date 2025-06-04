# 教程：演示 SSE 

## 对你的价值
用尽可能短的代码，演示 SSE。   
后端用 FastAPI 的 StreamingResponse    

<!-- 用 [Gemini](https://gemini.google.com/app) 让它直接教你 SSE，  
给你生成一段 FastAPI 的 SSE 代码也可以    -->

## 第一步：运行后端

安装依赖
```
pip install fastapi uvicorn[standard]
```

运行 Python 服务器
```
uvicorn main:app --reload --port 5000
```

在地址栏输入 http://127.0.0.1:5000/stream 并回车。

## 第二步：运行前端
`index.html` 可以用 live server 打开。

安装依赖
```
pnpm install -g live-server
```

运行
```
live-server
```