class CustomAPIError(Exception):
    def __init__(self, message, status_code, error_code=None):
        self.message = str(message)
        self.status_code = status_code
        self.error_code = error_code or f"ERR_{status_code}"
        super().__init__(self.message)