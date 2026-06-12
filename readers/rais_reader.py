"""
Descrição:
    Reader dos datasets da RAIS.

Objetivo:
    Padronizar a leitura dos datasets da RAIS

Responsabilidades:
    - configurar leitura
    - abstrair pandas.read_csv
    - padronizar encoding
    - padronizar separador
    - permitir leitura em chunks
"""

from typing import Iterator
import pandas as pd

class RaisReader:

    def __init__(
        self,
        encoding: str = "latin-1",
        separator: str = ",",
        chunksize: int = 100_000
    ):
        """
        Inicializa reader.

        Args:
            encoding:
                Encoding do dataset.

            separator:
                Separador do CSV.

            chunksize:
                Tamanho dos chunks.
        """

        self.encoding = encoding
        self.separator = separator
        self.chunksize = chunksize

    def configure(
        self, 
        encoding: str,
        separator: str
    ):
        """
        Atualiza parâmetros de leitura.

        Args:
            encoding:
                Novo encoding.

            separator:
                Novo separador.
        """

        if encoding is not None:
            self.encoding = encoding
        
        if separator is not None:
            self.separator = separator

    def read_chunk(
        self,
        filepath: str
    ) -> Iterator[pd.DataFrame]:
        """
        Lê dataset em chunks.

        Args:
            filepath:
                Caminho do dataset.

        Returns:
            Iterator de DataFrames.
        """
        
        reader = pd.read_csv(
            filepath,
            sep=self.separator,
            encoding=self.encoding,
            chunksize=self.chunksize,
            low_memory=False
        )

        return reader
    
    def read(
        self,
        filepath: str
    ) -> Iterator[pd.DataFrame]:
        """
        Itera sobre chunks do dataset.

        Args:
            filepath:
                Caminho do dataset.

        Yields:
            Chunks do dataset.
        """

        for chunk_id, chunk in enumerate(self.read_chunk(filepath)):
            print(
                f"[Chunk {chunk_id}] "
                f"Rows={len(chunk)}"
            )

            yield chunk