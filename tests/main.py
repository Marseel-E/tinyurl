import rich

from tinyurl import Client

API_TOKEN = "GuZ9EcshSkhClPXAJfh5shWDkhxv1cXHRumIg14IHeOGjiZZn3oZUjuGgJ0g"
TEST_URL = "https://github.com/Marseel-E"


async def main() -> None:
	async with Client(API_TOKEN) as session:
		url = await session.create(TEST_URL)

	print(url)


if __name__ == '__main__':
	import asyncio

	asyncio.run(main())