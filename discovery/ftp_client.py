"""
Descrição:
    Cliente FTP genérico para acesso aos microdados governamentais.

Objetivo:
    Fornecer operações básicas de:
    - conexão
    - navegação
    - listagem
    - download

Observações:
    O FTP do Ministério do Trabalho utiliza encoding latin-1.
"""

import ftplib
from pathlib import Path

class FTPClient:
    def __init__(self, host: str, encoding: str = "latin-1"):
        """
        Inicializa cliente FTP.

        Args:
            host:
                Endereço do servidor FTP.

            encoding:
                Encoding utilizado pelo servidor FTP.
        """

        self.host = host
        self.encoding = encoding
        self.ftp = None

    def connect(self):
        """
        Estabelece conexão com o servidor FTP.
        """

        self.ftp = ftplib.FTP(
            self.host,
            encoding=self.encoding
        )

        self.ftp.login()
    
    def disconnect(self):
        """
        Encerra conexão como o servidor FTP.
        """

        if self.ftp is not None:
            self.ftp.quit()

    def list_directory(self, remote_path: str):
        """
        Lista arquivos e diretórios de um caminho remoto.

        Args:
            remote_path:
                Caminho remoto no FTP.

        Returns:
            Lista de arquivos/diretórios encontrados.
        """

        self.ftp.cwd(remote_path)

        return self.ftp.nlst()

    def download_file(
        self, 
        remote_file: str,
        local_path: str | Path
    ):
        """
        Realiza download de um arquivo do FTP.

        Args:
            remote_file:
                Nome/caminho do arquivo remoto.

            local_path:
                Caminho local onde o arquivo será salvo.
        """

        local_path = Path(local_path)

        local_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(local_path, "wb") as file:
            self.ftp.retrbinary(
                f"RETR {remote_file}",
                file.write
            )

    def file_exists(
        self,
        remote_path: str
    ) -> bool:
        """
        Verifica se um arquivo existe no servidor FTP.

        Args:
            remote_path:
                Caminho remoto do arquivo.

        Returns:
            True se existir, False caso contrário.
        """

        try:
            self.ftp.size(remote_path)
            return True
        except:
            return False