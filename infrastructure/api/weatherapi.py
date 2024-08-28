from typing import Optional

from aiohttp import ClientSession, ClientResponse

from tgbot.config import load_config


config = load_config(".env")

class WeatherApiSession:
    def __init__(self, url: str = config.api.url, api_key: str = config.api.api_key, method: str = config.api.method):
        self.url = url
        self.api_key = api_key
        self.method = method
        self.session: Optional[ClientSession] = None
        
    async def create_session(self) -> ClientSession:
        if self.session is None or self.session.closed:
            self.session = ClientSession()
        
        return self.session
    
    async def close(self) -> None:
        if self.session is not None and not self.session.closed:
            await self.session.close()
    
    
    async def check_response(self, response: ClientResponse):
        match response.status:
            case 200:
                return await response.json()
            
            case 400:
                return False
            
    async def make_request(self, residence):
        session = await self.create_session()
        
        try:
            async with session.get(
                url=f"{config.api.url}{config.api.method}",
                params=dict(key=config.api.api_key, q=residence, days=3, lang="uk")
            ) as resp:
                
                result = await self.check_response(response=resp)
                
                # !!!
                # await self.close()
            
                return result
                
        except Exception as e:
            print(f"Виникла помилка: {e}")
            