from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol, runtime_checkable


@runtime_checkable
class ProcessingStage(Protocol):
    """Duck typing interface: any class with process() can be a stage."""
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        print("Stage 1: Input validation")
        return {"raw": data, "valid": True}


class TransformStage:
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        print("Stage 2: Transformation")
        data["transformed"] = True
        return data


class OutputStage:
    def process(self, data: Dict[str, Any]) -> str:
        print("Stage 3: Delivery")
        return f"Final result: {data}"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print(f"Processing JSON through {self.pipeline_id}...")
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print(f"Processing CSV through {self.pipeline_id}...")
        for stage in self.stages:
            data = stage.process(data)
        return data


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print(f"Processing Stream through {self.pipeline_id}...")
        for stage in self.stages:
            data = stage.process(data)
        return data


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        for pipe in self.pipelines:
            result = pipe.process(data)
            print(f"Nexus Output: {result}\n")


def main() -> None:
    manager = NexusManager()
    pipe = JSONAdapter("J1")
    pipe.add_stage(InputStage())
    pipe.add_stage(TransformStage())
    pipe.add_stage(OutputStage())
    manager.add_pipeline(pipe)
    manager.process_data({"test": "data"})


if __name__ == "__main__":
    main()
