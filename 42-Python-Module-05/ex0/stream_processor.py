from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """Abstract base class for all Nexus processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting (can be overridden)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Handles numeric lists for calculation."""

    def validate(self, data: Any) -> bool:
        """Validate if data is a list of numbers."""
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: List[Union[int, float]]) -> str:
        if not self.validate(data):
            return "Invalid numeric data"

        count = len(data)
        total = sum(data)
        avg = total / count if count else 0.0

        return (f"Processed {count} numeric values, "
                f"sum={total}, avg={avg}")


class TextProcessor(DataProcessor):
    """Analyzes strings for character and word counts."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        if not self.validate(data):
            return "Invalid text data"
        words = len(data.split())
        chars = len(data)
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    """Identifies alerts in log strings."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: str) -> str:
        if not self.validate(data):
            return "Invalid log data"
        level = data.split(":")[0]
        message = data.split(":", 1)[1].strip()
        return f"[{level}] {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Overriding the default format for logs."""
        return result


def main() -> None:
    """Diagnostic suite to verify polymorphic constructs."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors = [
        (NumericProcessor(), [1, 2, 3, 4, 5], "Numeric Processor"),
        (TextProcessor(), "Hello Nexus World", "Text Processor"),
        (LogProcessor(), "ERROR: Connection timeout", "Log Processor")
    ]

    for proc, data, name in processors:
        print(f"Initializing {name}...")
        print(f"Processing data: {repr(data)}")
        if proc.validate(data):
            print("Validation: Data verified")
            result = proc.process(data)
            print(proc.format_output(result))
        print("-" * 20)

    print("=== Polymorphic Processing Demo ===")
    mixed_data = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Nexus ready"),
        (LogProcessor(), "INFO: System ready")
    ]

    for i, (proc, data) in enumerate(mixed_data, 1):
        print(f"Result {i}: {proc.process(data)}")


if __name__ == "__main__":
    main()
