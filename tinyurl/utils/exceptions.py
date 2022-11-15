__all__ = ['UnauthorizedAccess', 'MissingPermissions', 'ValidationFailed', 'UnexpectedError']


class UnauthorizedAccess(Exception):
	def __init__(self) -> None:
		super().__init__("[401] You are not authorized to use/access this API endpoint or resource. Please check your API token.")


class MissingPermissions(Exception):
	def __init__(self) -> None:
		super().__init__("[405] You do not have permissions to access this resource.")


class ValidationFailed(Exception):
	def __init__(self) -> None:
		super().__init__("[422] Validation failed on one of the properties. please check the errors in the response body.")


class UnexpectedError(Exception):
	def __init__(self) -> None:
		super().__init__("[5XX] There was an unexpected error while processing your request.")