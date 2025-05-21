from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import time

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 请求头
)

async def fake_data_streamer():
    for i in range(10):
        yield f"data: data chunk {i}\n\n" # SSE 格式要求
        await asyncio.sleep(0.5) # 模拟数据生成耗时

@app.get("/stream")
async def stream_data():
    return StreamingResponse(fake_data_streamer(), 
                             media_type="text/event-stream")