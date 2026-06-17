"""
Descrição:
    Selecionador de datasets válidos da RAIS.

Objetivo:
    Filtrar arquivos relevantes para profiling, 
    ingestão e processamento da RAIS.

Responsabilidades:
    - remover arquivos de documentação
    - remover arquivos inválidos
    - selecionar datasets específicos
    - organizar datasets por categoria
"""

from typing import List, Dict

class RaisDatasetSelector:
    """
    Responsável pela seleção de datasets válidos da RAIS.
    """

    def select_valid_datasets(
        self,
        parsed_files: List[Dict]
    ) -> List[Dict]:
        """
        Seleciona datasets válidos para processamento.
        
        Args:
            parsed_files:
                Lista de arquivos parseados.
        
        Returns:
            Lista contendo apenas datasets válidos.
        """

        valid_datasets = []

        for file_info in parsed_files:
            dataset_type = file_info.get("dataset_type")

            if dataset_type == "documentation":
                continue

            if dataset_type == "unknown":
                continue

            valid_datasets.append(file_info)
        
        valid_datasets = [file_info
                          for file_info in valid_datasets
                          if file_info.get("special_category") is None]
        
        return valid_datasets
    
    def select_by_dataset_type(
        self,
        parsed_files: List[Dict],
        dataset_type: str
    ) -> List[Dict]:
        """
        Filtra datasets por tipo.

        Args:
            parsed_files:
                Lista de arquivos parseados.

            dataset_type:
                Tipo desejado:
                - vinculo
                - estabelecimento
        
        Returns:
            Lista filtrada.
        """

        return [
            file_info
            for file_info in parsed_files
            if file_info.get("dataset_type") 
            == dataset_type
        ]
    
    def select_by_schema_generation(
        self,
        parsed_files: List[Dict],
        schema_generation: str
    ) -> List[Dict]:
        """
        Filtra datasets por geração de schema.

        Args:
            parsed_files:
                Lista de arquivos parseados.
            
                schema_generation:
                    Geração desejada:
                    - legacy
                    - regionalized
        
        Returns:
            Lista filtrada.
        """

        return [
            file_info
            for file_info in parsed_files
            if file_info.get("schema_generation")
            == schema_generation
        ]