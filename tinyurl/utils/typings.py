__all__ = ['CreateData', 'UpdateData', 'CreateData', 'DeleteData', 'ArchiveData', 'StatusData', 'SharingData']

from typing import TypedDict


class ResponseData(TypedDict):
	data: dict
	code: int
	errors: list[str]

class AnalyticsData(TypedDict):
	enabled: bool
	public: bool

class CreateData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str
	url: str

class UpdateData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str

class ChangeData(TypedDict):
	url: str

class DeleteData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str
	url: str

class ArchiveData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str

class StatusData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str

class SharingData(TypedDict):
	domain: str
	alias: str
	deleted: bool
	archived: bool
	tags: list[str]
	analytics: AnalyticsData
	tiny_url: str