"""
Descrição:
    Ferramenta de profiling estrutural dos datasets da RAIS.

Objetivo:
    Descobrir automaticamente características estruturais
    dos arquivos da RAIS.

Responsabilidades:
    - detectar colunas
    - detectar tipos inferidos
    - detectar delimitador
    - detectar encoding
    - identificar padrões estruturais
"""

from pathlib import Path
from typing import Dict

import pandas as pd

class RaisSchemaProfiler:
    """
    Responsável pelo profiling estrutural da RAIS.
    """

    DEFAULT_ENCODING = "latin-1"

    POSSIBLE_SEPARATORS = [
        ",",
        ";",
        "\t"
    ]

    def dectect_separator(
        self,
        file_path: str | Path,
        encoding: str = DEFAULT_ENCODING
    ) -> str:
        """
        Detecta separador utilizado no arquivo.

        Args:
            file_path:
                Caminho do arquivo.
            
            encoding:
                Encoding do arquivo.
        
        Returns:
            Separador detectado.
        """

        with open(file_path, "r", encoding=encoding) as file:
            first_line = file.readline()

        separator_counts = {
            separator: first_line.count(separator)
            for separator in self.POSSIBLE_SEPARATORS
        }

        return max(
            separator_counts,
            key=separator_counts.get
        )

    def profile_schema(
        self,
        file_path: str | Path,
        sample_rows: int = 1000
    ) -> Dict:
        """
        Realiza profiling estrutural do arquivo

        Args:
            file_path:
                Caminho do arquivo extraído.

            sample_rows:
                Quantidade de linhas para inferência.
        
        Returns:
            Dicionário contendo informações estruturais.
        """

        file_path = Path(file_path)

        separator = self.dectect_separator(file_path)

        sample = pd.read_csv(
            file_path,
            encoding=self.DEFAULT_ENCODING,
            sep=separator,
            nrows=sample_rows,
            low_memory=False
        )

        profile = {
            "file_name": file_path.name,
            "encoding": self.DEFAULT_ENCODING,
            "separator": separator,
            "n_columns": len(sample.columns),
            "columns": {
                column: str(dtype)
                for column, dtype
                in sample.dtypes.items()
            },
            "sample_rows": sample_rows
        }

        return profile

    