from dataclasses import dataclass
from resources.domain.models import Resource
from resources.domain.repositories import ResourcesRepository


@dataclass
class CreateResourceCommand:
    resource_url: str

class CreateResource:
    def __init__(self, resource_repository: ResourcesRepository) -> None:
        self._resource_repository = resource_repository

    def execute(self, command: CreateResourceCommand) -> None:
        resource = Resource.create(resource_url=command.resource_url)
        self._resource_repository.save(resource)