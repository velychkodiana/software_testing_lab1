# errors.py

class LabInputError(Exception):
    """Base exception for lab input errors."""
    pass


class RangeError(LabInputError):
    pass


class FormatError(LabInputError):
    pass


class GeometryError(LabInputError):
    pass