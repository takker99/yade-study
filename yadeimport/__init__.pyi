from collections.abc import Iterator

class Matrix3:
    """3x3 matrix class for YADE."""  # noqa: PYI021

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

class Body:
    """Represents a physical object (particle) in the YADE simulation.

    See: https://yade-dem.org/doc/yade.wrapper.html#yade.wrapper.Body.
    """  # noqa: PYI021

    dynamic: bool
    """Whether the body is movable by forces."""
    groupMask: int  # noqa: N815
    """Interaction group mask."""
    id: int
    """Unique identifier."""
    material: object
    """Material information."""
    shape: object
    """Shape information."""
    state: object
    """State (position, velocity, etc.)."""

    def intrs(self) -> list:
        """Return a list of all interactions involving this body."""  # noqa: PYI021

class BodyContainer:
    """Container for managing multiple Body instances.

    Provides append, remove, iteration, and access by ID.
    See: https://yade-dem.org/doc/yade.wrapper.html#yade.wrapper.BodyContainer.
    """  # noqa: PYI021

    def __getitem__(self, body_id: int) -> Body:
        """Return the Body with the given ID."""  # noqa: PYI021

    def __setitem__(self, body_id: int, body: Body) -> None:
        """Set the Body for the given ID."""  # noqa: PYI021

    def __delitem__(self, body_id: int) -> None:
        """Delete the Body with the given ID."""  # noqa: PYI021

    def append(self, body: Body) -> int:
        """Add a Body and return its ID."""  # noqa: PYI021

    def remove(self, body_id: int) -> None:
        """Remove the Body with the given ID."""  # noqa: PYI021

    def __iter__(self) -> Iterator[Body]:
        """Return an iterator over all bodies."""  # noqa: PYI021

    def __len__(self) -> int:
        """Return the total number of bodies."""  # noqa: PYI021

class Omega:
    """The main YADE simulation world.

    Manages bodies, materials, engines, interactions, and simulation state.
    Accessed as the global instance 'O'.
    See: https://yade-dem.org/doc/yade.wrapper.html#yade.wrapper.Omega.
    """  # noqa: PYI021

    bodies: BodyContainer
    """Access to all bodies."""

O: Omega
"""Global instance for simulation control

See: https://yade-dem.org/doc/yade.wrapper.html#yade.wrapper.O
"""
