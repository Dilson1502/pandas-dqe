from dataclasses import dataclass


@dataclass
class SampleInput:
    id: type = int
    name: type = str
    age: type = int

    @property
    def schema(self):
        """Returns the schema as a dictionary of field names and their expected types."""
        return {field: getattr(self, field) for field in self.__annotations__}


@dataclass
class SampleOutput:
    user_id: type = int
    full_name: type = str
    age_in_10_years: type = float

    @property
    def schema(self):
        """Returns the schema as a dictionary of field names and their expected types."""
        return {field: getattr(self, field) for field in self.__annotations__}
