import aiohttp
import asyncio
import json

news = [{"title": "Article 1", "text": "Suspendisse venenatis accumsan metus, vitae tempor nunc porta sit amet. Vestibulum hendrerit velit non sem ullamcorper egestas. In turpis ligula, porttitor quis justo a, bibendum suscipit sapien. Nunc commodo dui augue, ac maximus libero viverra quis. Fusce vestibulum velit nec felis tincidunt condimentum. Vestibulum feugiat, arcu quis porta gravida, nisi enim placerat ante, in vulputate est justo a orci. Sed ac tellus dolor. "}, {"title": "Article 2", "text": "Etiam ut massa nisi. Praesent eget augue eget neque fringilla pharetra. Nullam sapien orci, ornare ut tortor in, commodo facilisis elit. Donec sit amet massa quis dolor malesuada convallis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras vestibulum orci in orci posuere dapibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus nec placerat elit. Fusce venenatis lorem nec vehicula tincidunt. "},
        {"title": "Article 3", "text": "Sed nisi sapien, fringilla vel ligula ut, ultrices egestas justo. Donec volutpat dolor non posuere egestas. Curabitur quis enim est. Cras in condimentum turpis. Maecenas et magna non odio scelerisque hendrerit at dapibus augue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut in auctor neque. Etiam eget velit consequat, dapibus ligula sed, condimentum orci. Praesent congue varius nunc. Nullam auctor pretium neque id laoreet. "}]
news = json.dumps(news)


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/news', data={"news": news}) as resp:
            print("connected to server")
            print(resp.status)
            print(await resp.text())
    print('disconnected')


asyncio.run(main())
