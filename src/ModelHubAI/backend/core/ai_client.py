import httpx

async def get_ai_status():
    # verify the connection to the ai_suite
    async with httpx.AsyncClient() as client:
        response = await client.get("http://ai_suite:8001/status")
        return response.json()