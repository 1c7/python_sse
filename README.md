# 教程：演示 SSE 

## 对你有什么价值
用尽可能简短的代码，演示 SSE 在前后端是怎么写代码的。   
后端用 FastAPI 的 StreamingResponse    

用 [Gemini](https://gemini.google.com/app) 让它直接教你 SSE，  
给你生成一段 FastAPI 的 SSE 代码也可以   


## 安装依赖
```
pip install fastapi uvicorn[standard]
```

## 运行 Python 服务器
```
uvicorn main:app --reload --port 5000
```

在地址栏输入 http://127.0.0.1:5000/stream 并回车。

## 前端 SSE
`index.html` 可以用 live server 打开。

```
pnpm install -g live-server
```

```
live-server
```