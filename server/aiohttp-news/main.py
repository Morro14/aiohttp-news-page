import aiohttp
from aiohttp import web
import asyncio
import json

news_service = []
news_update = False


async def on_shutdown(app: web.Application):
    for ws in app["sockets"]:
        await ws.close()


async def async_iter(ws, t):
    global news_update
    try:
        while True:
            await asyncio.sleep(t)
            print(id(ws))
            if news_update:
                news_data = {'news': news_service[0]}
                await ws.send_json(data=news_data)
                news_update = False
            else:
                await ws.send_json(data={'ping': 'ping'})
    except ConnectionResetError:
        return
            


async def ws_handler(request):
    global news_update
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    request.app["sockets"].append(ws)
    user_connected = await ws.receive()
    print(request.app["sockets"])
    print(user_connected.data)
    print('sending news')
    
    if len(news_service) != 0:
        news_data = {'news': news_service[0]}
        news_update = False
    else:
        news_data = 'no news yet'
    await ws.send_json(data=news_data)
    
    print('news sent')
    await async_iter(ws, 3)
    await ws.close()
    request.app["sockets"].remove(ws)
    print(f'socket {id(ws)} removed')



async def post_handler(request: web.Request):
    global news_update
    data = await request.post()
    news_ = data.get("news")
    news_ = json.loads(news_)
    news_service.append(news_)
    news_update = True
    return web.Response(body="ok")


app = web.Application()
app.add_routes([web.get('/ws', ws_handler)])
app.add_routes([web.post('/news', post_handler)])

app["sockets"] = []
app.on_shutdown.append(on_shutdown)
web.run_app(app)
