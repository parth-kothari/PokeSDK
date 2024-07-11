from typing import List, TypeVar, Generic

T = TypeVar('T')

# Generic PaginatedList copied from online
class PaginatedList(Generic[T]):
    def __init__(self, count: int, next_url: str, previous_url: str, results: List[T]):
        self.count = count
        self.next_url = next_url
        self.previous_url = previous_url
        self.results = results

    def __len__(self):
        return len(self.results)

    def __getitem__(self, index):
        return self.results[index]

    def __iter__(self):
        return iter(self.results)

    def __repr__(self):
        return f"<PaginatedList(count={self.count}, results={len(self.results)} items)>"
