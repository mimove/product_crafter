from resources.domain.repositories import ResourcesRepository

class CreateResource:
    def __init__(self, resource_repository: ResourcesRepository) -> None:
        self._resource_repository = resource_repository
    def execute(self) -> None:
        pass