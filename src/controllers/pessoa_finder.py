from src.models.repositories.pessoas_repository import PessoasRepository

class PessoaFinder:
    def __init__(self):
        self.pessoa_repository = PessoasRepository()

    async def find_by_id(self, id) -> dict:
        return self.pessoa_repository.find_by_id(id)

    async def find_all(self) -> dict:
        pessoas = await self.pessoa_repository.get_all_people()
        if pessoas == []:
            raise Exception("No people found")
        
        formatted_pessoas = []
        for pessoa in pessoas:
            formatted_pessoas.append({
                "id": pessoa.id,
                "name": pessoa.name
            })

        return {
            "type": "Pessoa",
            "count": len(formatted_pessoas),
            "attributes": formatted_pessoas
        }