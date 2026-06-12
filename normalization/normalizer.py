"""
Normalização dos schemas históricos da RAIS.

Objetivo:
    Converter diferentes versões da RAIS para um schema canônico
"""

import pandas as pd

from .column_mapping import VINCULOS_VARS, VINCULOS_RENAME, ESTAB_VARS, ESTAB_RENAME

class RaisNormalizer:
    def normalize(
        self,
        chunk: pd.DataFrame,
        dataset_type: str
    ) -> pd.DataFrame:
        """
        Normaliza nomes de colunas.

        Args:
            chunk: Dataframe original

            datset_type: vinculo/estabelecimento

        Returns:
            DataFrame normalizado
        """

        if dataset_type == "vinculo":
            mapping = VINCULOS_RENAME
            canonical_columns = VINCULOS_VARS

        elif dataset_type == "estabelecimento":
            mapping = ESTAB_RENAME
            canonical_columns = ESTAB_VARS

        else:
            raise ValueError(f"dataset_type inválido: {dataset_type}")
        
        chunk = chunk.rename(columns=mapping)

        for column in canonical_columns:
            if column not in chunk.columns:
                chunk[column] = None
        
        return chunk