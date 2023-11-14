class ApiError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code
        self.error_messages = {
            0: "Recognition succeeded",
            1001: "No recognition",
            2000: "Recording error (device may not have permission)",
            2001: "Init failed or request timeout",
            2002: "Metadata parse error",
            2004: "Unable to generate fingerprint",
            2005: "Timeout",
            3000: "Recognition service error（http error 500）",
            3003: "Limit exceeded, please upgrade your account",
            3006: "Invalid arguments",
            3014: "Invalid signature",
            3015: "QpS limit exceeded, please upgrade your account",

        }

    def __str__(self):
        if self.error_code in self.error_messages:
            return f"API Error {self.error_code}: {self.error_messages[self.error_code]}"
        else:
            return f"Unknown API Error Code: {self.error_code}"
