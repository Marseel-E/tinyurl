from __future__ import annotations

"""
MIT License

Copyright (c) 2022 Marseel-E

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = []

__title__ = 'tinyurl'
__author__ = 'Marseel Eeso'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present Marseel Eeso'
__version__ = '0.1.0'
# __path__ = __import__('pkgutil').extend_path(__path__, __name__)

import aiohttp

from datetime import datetime

from .utils import *

API_BASE = "https://api.tinyurl.com/"
EXPIRES_AT_FORMAT = "%Y-%m-%d %H:%M:%S"


class Client:
	def __init__(self, token: str) -> None:
		self.token: str = token
		self.session: aiohttp.ClientSession | None = None

	async def __aenter__(self) -> "Client":
		self.session = aiohttp.ClientSession()

		return self

	async def close_session(self) -> None:
		if self.session is not None:
			await self.session.close()

	async def __aexit__(self, *args) -> None:
		await self.close_session()

	@staticmethod
	async def _check_response(response_code: int) -> None:
		# 200/0 - success
		if response_code == 0:
			return

		# 401/1 - unauthorized accesss
		if response_code == 1:
			raise UnauthorizedAccess()
		
		# 405/4 - no perms
		if response_code == 4:
			raise MissingPermissions()

		# 422/5 - validation failed
		if response_code == 5:
			raise ValidationFailed()
		
		# 5XX/7 - unexpected error
		if response_code == 7:
			raise UnexpectedError()


	async def create(self, url: str, domain: str | None = "tinyurl.com", alias: str | None = "", tags: list[str] | None = None, expires_at: datetime | None = None) -> str:
		data = {
			"url": url,
			"domain": domain,
			"alias": alias,
			"tags": ','.join(tags) if tags != None else "",
			"expires_at": expires_at.strftime(EXPIRES_AT_FORMAT) if expires_at != None else ""
		}

		if self.session is None:
			self.session = aiohttp.ClientSession()

		async with self.session.post(API_BASE + "create", data=data, params={'api_token': self.token}) as raw_response:
			response = await raw_response.json()

		await self._check_response(response['code'])

		return response['data']['tiny_url']


	async def _patch(self, endpoint: str, data: dict) -> dict:
		if self.session is None:
			self.session = aiohttp.ClientSession()

		async with self.session.post(API_BASE + endpoint, data=data, params={'api_token': self.token}) as raw_response:
			response = await raw_response.json()

		await self._check_response(response['code'])

		return response['data']

	async def update(self, alias: str, new_alias: str, domain: str | None = "tinyurl.com", new_domain: str | None = "tinyurl.com", new_stats: bool = True, new_tags: list[str] | None = None, new_expires_at: datetime | None = None) -> dict:
		data = {
			"domain": domain,
			"alias": alias,
			"new_domain": new_domain,
			"new_alias": new_alias,
			"new_stats": str(new_stats).lower(),
			"new_tags": ', '.join(new_tags) if new_tags != None else "",
			"new_expires_at": new_expires_at.strftime(EXPIRES_AT_FORMAT) if new_expires_at != None else ""
		}

		response = await self._patch('update', data)

		return response