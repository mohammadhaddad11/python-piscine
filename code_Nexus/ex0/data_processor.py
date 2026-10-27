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


if __name__ == "__main__":
    mynum = NumericProcessor()
    mystr = TextProcessor()
    mylog = LogProcessor()

    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    print("Trying to validate input '42': ", end="")
    print(mynum.validate(42))
    print("Trying to validate input 'Hello': ", end="")
    print(mynum.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        mynum.ingest("foo")
    except ValueError as exc:
        print(f"Got exception: {exc}")

    print("Processing data: [1, 2, 3, 4, 5]")
    mynum.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for _ in range(3):
        result = mynum.output()
        print(f"Numeric value {result[0]}: {result[1]}")

    print("Testing Text Processor...")
    print("Trying to validate input '42': ", end="")
    print(mystr.validate(42))

    print("Processing data: ['Hello', 'Nexus', 'World']")
    mystr.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    result = mystr.output()
    print(f"Text value {result[0]}: {result[1]}")

    print("Testing Log Processor...")
    print("Trying to validate input 'Hello': ", end="")
    print(mylog.validate("Hello"))

    logs = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]

    print("Processing data:", logs)
    mylog.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        result = mylog.output()
        print(f"Log entry {result[0]}: {result[1]}")
