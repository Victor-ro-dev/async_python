import asyncio
import httpx

async def fetch_get(client, pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    print(f"Fetching {url}")
    response = await client.get(url)
    print(f"Response received for {url}")
    data = response.json()

    name = data["name"]
    id = data["id"]
    habilities = data["moves"][0]["move"]["name"]
    print(f"{name} has id {id} and its first move is {habilities}")
    

async def main():
    async with httpx.AsyncClient() as client:
        print("Fetching pokemons")
        await asyncio.gather(
            fetch_get(client, "charmander"),
            fetch_get(client, "bulbasaur"),
            fetch_get(client, "squirtle")
        )
        print("Pokemons fetched")

asyncio.run(main())