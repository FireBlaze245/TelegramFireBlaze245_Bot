import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

async def test_proxy(proxy_url):
    connector = ProxyConnector.from_url(proxy_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            async with session.get('https://httpbin.org/ip', timeout=10) as resp:
                print(f"Статус: {resp.status}")
                if resp.status == 200:
                    print("Ответ:", await resp.json())
                else:
                    print("Тело ответа:", await resp.text())
        except Exception as e:
            print(f"Ошибка: {e}")

# Замените на ваш HTTPS-прокси
# Формат: http://user:pass@host:port (для прокси с авторизацией)
# Или: http://host:port (для открытого прокси)
proxy_url = "http://38.145.208.234:8453"
asyncio.run(test_proxy(proxy_url))
