"""Implement a circular buffer."""


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""

    def __init__(self, message):
        """Initialize the exception message."""

        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""

    def __init__(self, message):
        """Initialize the exception message."""

        super().__init__(message)


class CircularBuffer:
    """Represent a fixed-capacity circular buffer."""

    def __init__(self, capacity):
        """Initialize the buffer with a fixed capacity."""

        self.capacity = capacity
        self.buffer = []

    def read(self):
        """Remove and return the oldest item."""

        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.pop(0)

    def write(self, data):
        """Add an item if the buffer has available space."""

        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data):
        """Add an item, replacing the oldest if the buffer is full."""

        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)

        self.buffer.append(data)

    def clear(self):
        """Remove all items from the buffer."""

        self.buffer.clear()