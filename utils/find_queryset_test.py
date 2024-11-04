from src.synthesize.query.usecases.FindQuerySet import FindQuerySet, InputFindQuerySetDto
from src.infra.repository.JSONRepository import JSONRepository

repository = JSONRepository()
usecase = FindQuerySet(repository=repository)

input = InputFindQuerySetDto(
    id="cc1565d3-a0d2-435c-a52e-f3be9fdfbe75"
)
data = usecase.execute(input)

print(data)