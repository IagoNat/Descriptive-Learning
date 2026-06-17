"""
Descrição:
    Parser responsável por interpretar semanticamente
    os nomes dos arquivos da RAIS.

Objetivo:
    Converter nomes de arquivos da RAIS em metadados
    estruturados para uso interno do pipeline.

Observações:
    A RAIS possui múltiplas gerações históricas de
    nomenclatura e organização dos arquivos.

    Gerações identificadas:

    - legacy_uf_based (1985-2017)
    - regionalized (2018+)
"""

import re
from pathlib import Path

class RaisFilenameParser:
    """
    Parser para nomes de arquivos da RAIS.
    """

    UF_CODES = {
        "AC", "AL", "AM", "AP",
        "BA", "CE", "DF", "ES",
        "GO", "MA", "MG", "MS",
        "MT", "PA", "PB", "PE",
        "PI", "PR", "RJ", "RN",
        "RO", "RR", "RS", "SC",
        "SE", "SP", "TO"
    }

    REGION_GROUPS = {
        "SUL": ["RS", "SC", "PR"],

        "NORTE": [
            "AC", "AM", "AP", "PA",
            "RO", "RR", "TO"
        ],

        "NORDESTE": [
            "AL", "BA", "CE",
            "MA", "PB", "PE",
            "PI", "RN", "SE"
        ],

        "CENTRO_OESTE": [
            "DF", "GO", "MS", "MT"
        ],

        "MG_ES_RJ": [
            "MG", "ES", "RJ"
        ],

        "SP": ["SP"]
    }

    def parse(self, filename: str) -> dict:
        """
        Interpreta um nome de arquivo da RAIS.

        Args:
            filename:
                Nome do arquivo.

        Returns:
            Dicionário com metadados estruturados.
        """

        path = Path(filename)

        parsed = {
            "filename": path.name,
            "stem": path.stem,
            "extension": path.suffix.replace(".", "").lower(),
            "dataset": "rais",
            "dataset_type": None,
            "schema_generation": None,
            "regions": [],
            "special_categoty": None
        }

        stem = path.stem.upper()

        # DOCUMENTAÇÃO
        if path.suffix.lower() in [".txt", ".htm", ".html"]:
            parsed["dataset_type"] = "documentation"
            return parsed
        
        # REGIONALIZADO (2018+)
        if stem.startswith("RAIS_VINC_PUB"):
            parsed["dataset_type"] = "vinculo"
            parsed["schema_generation"] = "regionalized"

            for region_name, ufs in self.REGION_GROUPS.items():
                if region_name in stem:
                    parsed["regions"] = ufs
                    break

            if "NI" in stem:
                parsed["special_category"] = "not_identified"
            
            return parsed

        if stem.startswith("RAIS_ESTAB_PUB"):
            parsed["dataset_type"] = "estabelecimento"
            parsed["schema_generation"] = "regionalized"

            return parsed
        
        # LEGACY ESTAB
        if re.match(r"(?i)^ESTB\d{4}$", stem):
            parsed["dataset_type"] = "estabelecimento"
            parsed["schema_generation"] = "legacy"

            return parsed
        
        # LEGACY IGNORADOS
        if "IGNOR" in stem:
            parsed["dataset_type"] = "vinculo"
            parsed["schema_generation"] = "legacy"
            parsed["special_category"] = "ignored"

            return parsed

        # LEGACY BASE-UF
        uf = stem[:2]

        if uf in self.UF_CODES:
            parsed["schema_generation"] = "legacy"
            parsed["dataset_type"] = "vinculo"
            parsed["regions"] = [uf]

            return parsed
        
        # UNKNOWN
        parsed["dataset_type"] = "unknown"

        return parsed