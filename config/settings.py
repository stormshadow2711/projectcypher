class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            # Add configuration settings here
            cls._instance.settings = {
                "max_password_length": 20,
                "min_password_length": 8,
                "charsets": {
                    "lowercase": "abcdefghijklmnopqrstuvwxyz",
                    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "digits": "0123456789",
                    "special": "!@#$%^&*()-_+="
                }
            }
        return cls._instance

    def get_setting(self, key):
        return self._instance.settings.get(key, None)
