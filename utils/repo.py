from src.infra.repository.QuerySourceRepository import CSVQuerySourceRepository

repository = CSVQuerySourceRepository()

print(repository.get_source_data(file_name="pdi_chunks"))