from dataclasses import dataclass, field


@dataclass
class Stack:
    stack: list = field(default_factory=list)

    def add(self, new_element: type) -> None:
        self.stack.append(new_element)

    def pop(self) -> None:
        self.stack.remove(self.stack[-1])

    def print(self) -> None:
        for element in self.stack:
            print(element)