from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataStream(ABC):
    """Abstract base for sophisticated data streaming."""

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data - must be overridden."""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {
            "id": self.stream_id,
            "type": self.stream_type,
            "count": self.items_processed
        }


class SensorStream(DataStream):
    """Handles environmental data readings."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Sensor data")

    def process_batch(self, data_batch: List[float]) -> str:
        count = len(data_batch)
        avg = sum(data_batch) / count if count else 0.0
        self.items_processed += count
        return (f"Sensor analysis: {count} readings, "
                f"avg: {avg:.1f}°C")


class TransactionStream(DataStream):
    """Handles financial data operations."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Transaction data")

    def process_batch(self, data_batch: List[int]) -> str:
        self.items_processed += len(data_batch)
        net_flow = sum(data_batch)
        return (f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {'+' if net_flow >= 0 else ''}{net_flow} units")


class EventStream(DataStream):
    """Handles system event keywords."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Event data")

    def process_batch(self, data_batch: List[str]) -> str:
        self.items_processed += len(data_batch)
        errors = [e for e in data_batch if "error" in e.lower()]
        return (f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error(s) detected")


class StreamProcessor:
    """Manages multiple streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        for stream in self.streams:
            if stream.stream_id in batches:
                batch = batches[stream.stream_id]
                result = stream.process_batch(batch)
                print(f"- {stream.stream_type}: {result}")


def main() -> None:
    """Self-test for Exercise 1."""
    proc = StreamProcessor()
    proc.add_stream(SensorStream("S1"))
    proc.process_all({"S1": [20.5, 21.0]})


if __name__ == "__main__":
    main()
