from collections.abc import Iterator

class Matrix3:
    def __init__(
        self,
        a11: float,
        a12: float,
        a13: float,
        a21: float,
        a22: float,
        a23: float,
        a31: float,
        a32: float,
        a33: float,
    ) -> None: ...
    # 必要に応じて他のメソッドや属性を追加

class Body: ...  # 詳細は省略

class BodyContainer:
    def __getitem__(self, id: int) -> Body: ...
    def __setitem__(self, id: int, body: Body) -> None: ...
    def __delitem__(self, id: int) -> None: ...
    def append(self, body: Body) -> int: ...
    def remove(self, id: int) -> None: ...
    def __iter__(self) -> Iterator[Body]: ...
    def __len__(self) -> int: ...
    # 必要に応じて他のメソッドや属性を追加

class Omega:
    bodies: BodyContainer
    # 必要に応じて他の属性やメソッドを追加

O: Omega