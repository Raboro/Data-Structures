from dataclasses import dataclass, field


@dataclass
class Queue:
    queue: list = field(default_factory=list)

    def add(self, new_element: type) -> None:
        self.queue.append(new_element)

    def pop(self) -> None:
        self.queue.remove(self.queue[0])
    
    def print(self) -> None:
        for element in self.queue:
            print(element)