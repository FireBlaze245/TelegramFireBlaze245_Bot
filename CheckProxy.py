import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

class CheckProxy:
    def __init__(self):
        self.proxy_list = [
            "http://185.191.236.162:3128",
            "http://45.10.53.62:81",
            "http://95.213.217.168:52004",
            "http://62.68.48.22:8080",
            "http://31.192.106.135:8010",
            "http://45.12.151.226:2829",
            "http://82.114.228.67:1080",
            "http://188.190.179.172:8989",
            "http://195.19.217.200:3128"
        ]
        self.proxy_url = None
        self.proxy_status = None

    async def test_proxy(self, proxy_url):
        try:
            connector = ProxyConnector.from_url(proxy_url)
            async with aiohttp.ClientSession(connector=connector) as session:
                # Проверяем через Telegram API — более релевантно для бота
                async with session.get(
                    'https://api.telegram.org/bot8226459028:AAEeEZmhYaXZb6O8EWk8jq2blzUVs2-ZjW4/getMe',
                    timeout=aiohttp.ClientTimeout(total=15)
                ) as resp:
                    print(f"Статус для {proxy_url}: {resp.status}")
                    if resp.status == 200:
                        data = await resp.json()
                        if 'ok' in data and data['ok']:
                            print(f"Прокси {proxy_url} успешно прошёл проверку через Telegram API")
                            return True, resp.status
                    else:
                        print(f"Telegram API вернул ошибку: {resp.status}")
                        return False, resp.status
            return False, resp.status
        except asyncio.TimeoutError:
            print(f"Таймаут для прокси {proxy_url}")
            return False, None
        except Exception as e:
            print(f"Ошибка с прокси {proxy_url}: {type(e).__name__}: {e}")
            return False, None

    async def find_working_proxy(self):
        for proxy_url in self.proxy_list:
            success, status = await self.test_proxy(proxy_url)
            if success:
                self.proxy_url = proxy_url
                self.proxy_status = status
                print(f"✅ Рабочий прокси найден: {proxy_url}")
                return self
        # Если ни один прокси не сработал
        self.proxy_status = 400  # Условный код ошибки
        print("❌ Ни один прокси не доступен")
        return self
#