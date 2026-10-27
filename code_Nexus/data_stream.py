from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.counter = 0
        self.data: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise ValueError("No data to output")
        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            )

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.data.append((self.counter, str(item)))
                self.counter += 1
        else:
            self.data.append((self.counter, str(data)))
            self.counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.data.append((self.counter, item))
                self.counter += 1
        else:
            self.data.append((self.counter, data))
            self.counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                data.keys() == {"log_level", "log_message"}
                and isinstance(data["log_level"], str)
                and isinstance(data["log_message"], str)
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and item.keys() == {"log_level", "log_message"}
                and isinstance(item["log_level"], str)
                and isinstance(item["log_message"], str)
                for item in data
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                log_entry = f"{item['log_level']}: {item['log_message']}"
                self.data.append((self.counter, log_entry))
                self.counter += 1
        else:
            log_entry = f"{data['log_level']}: {data['log_message']}"
            self.data.append((self.counter, log_entry))
            self.counter += 1


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for i in stream:
            processed = False

            for proc in self.processors:
                if proc.validate(i):
                    try:
                        proc.ingest(i)
                        processed = True
                        break
                    except ValueError as e:
                        print(f"Error processing item {i}: {e}")

            if not processed:
                print(f"DataStream error-Can't process element in stream: {i}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(
                f"{proc.__class__.__name__}: total {proc.counter} "
                f"items processed, remaining {len(proc.data)} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()

    data_stream.print_processors_stats()

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(num)

    print("Send first batch of data on stream:", first_batch)
    data_stream.process_stream(first_batch)

    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(txt)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(first_batch)

    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors:")
    print("Numeric 3, Text 2, Log 1")

    for _ in range(3):
        num.output()

    for _ in range(2):
        txt.output()

    for _ in range(1):
        log.output()

    data_stream.print_processors_stats()
