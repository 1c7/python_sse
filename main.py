'''
有 2 个 Endpoint
1. /stream 返回一个流式响应，每隔 0.5 秒发送一个数据块
2. /sse_stream 返回一个 SSE 流式响应，每隔 0.2 秒发送一个数据块

'''
import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware # 用于处理跨域请求（开发时常见）

app = FastAPI()

# 添加 CORS 中间件，允许所有来源（在生产环境中应更严格）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"], # 允许所有 HTTP 方法
    allow_headers=["*"], # 允许所有 HTTP 请求头
)


async def fake_data_streamer():
    for i in range(10):
        yield f"data: data chunk {i}\n\n" # SSE 格式要求
        await asyncio.sleep(0.5) # 模拟数据生成耗时

@app.get("/stream")
async def stream_data():
    return StreamingResponse(fake_data_streamer(), 
                             media_type="text/event-stream")



# 要发送的长字符串
LONG_STRING = "这是一段将会被一个字一个字发送到前端的示例文本... Hello from FastAPI SSE! "

async def event_generator(request: Request):
    """
    异步生成器，逐字发送字符串
    """
    for char in LONG_STRING:
        # 检查客户端是否仍然连接
        if await request.is_disconnected():
            print("客户端断开连接")
            break
        # SSE 消息格式: "data: <your_data>\n\n"
        yield f"data: {char}\n\n"
        await asyncio.sleep(0.2) # 模拟一些处理时间或网络延迟，让效果更明显
    # （可选）发送一个特殊的结束事件
    yield "event: end\ndata: Transmission Complete\n\n"
    print("字符串发送完毕")


@app.get("/sse_stream")
async def sse_stream_endpoint(request: Request):
    """
    SSE 端点，返回一个流式响应
    """
    return StreamingResponse(event_generator(request), media_type="text/event-stream")

# 用于直接运行 (uvicorn main:app --reload)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)