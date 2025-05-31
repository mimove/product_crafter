from resources.application.create_resource import CreateResource
from resources.domain.models import Resource
from resources.domain.repositories import ResourcesRepository

class FakeResourceRepository(ResourcesRepository):
    def __init__(self) -> None:
        self._resources = []

    def save(self, resource: Resource) -> None: 
        self._resources.append(resource)

    def all(self) -> list[Resource]:
        return list(self._resources)
    

class TestCreateResource:
    def test_creates_resource(self) -> None:
        resource_repository = FakeResourceRepository()

        CreateResource(resource_repository).execute()

        assert len(resource_repository.all()) == 1

    