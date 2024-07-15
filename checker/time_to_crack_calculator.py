from .base_strategy import PasswordStrategy
from config.settings import Settings

class TimeToCrackCalculator(PasswordStrategy):
    def evaluate(self, password: str) -> str:
        settings = Settings()
        charsets = settings.get_setting("charsets")
        
        possible_chars = sum(len(charset) for charset in charsets.values())
        combinations = possible_chars ** len(password)
        
        # Assume 1 billion attempts per second (modern GPU)
        attempts_per_second = 1_000_000_000
        seconds = combinations / attempts_per_second
        
        return self.convert_seconds_to_human_readable(seconds)
    
    def convert_seconds_to_human_readable(self, seconds: int) -> str:
        intervals = (
            ('years', 365 * 24 * 60 * 60),
            ('months', 30 * 24 * 60 * 60),
            ('days', 24 * 60 * 60),
            ('hours', 60 * 60),
            ('minutes', 60),
            ('seconds', 1),
        )
        
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                result.append(f"{value} {name}")
        return ', '.join(result)
