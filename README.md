# 教程：理解 Python FastAPI 的 StreamingResponse 以及前端 SSE 是怎么回事

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
`index.html` 可以用随便一个 live server 打开。

