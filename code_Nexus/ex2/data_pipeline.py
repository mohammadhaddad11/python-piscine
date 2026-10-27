from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def output_pipeline(self, nb: int, plugin: 'ExportPlugin') -> None:
        for proc in self.processors:
            res = []
            rng = min(nb, len(proc.data))

            for _ in range(rng):
                res.append(proc.output())

            if res:
                plugin.process_output(res)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(
                f"{proc.__class__.__name__}: total {proc.counter} "
                f"items processed, remaining {len(proc.data)} on processor"
            )


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        res = []
        for i in data:
            res.append(i[1])
        print("CSV Output:")
        print(','.join(res))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        res = []
        for i in data:
            res.append(f'"item_{i[0]}": "{i[1]}"')
        print("JSON Output:")
        print('{' + ', '.join(res) + '}')


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("\nRegistering Processors\n")
    data_stream.register_processor(num)
    data_stream.register_processor(txt)
    data_stream.register_processor(log)

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

    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("\nSend another batch of data:", second_batch)
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)
    data_stream.print_processors_stats()
