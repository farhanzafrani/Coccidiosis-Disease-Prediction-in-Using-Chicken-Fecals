import os
from pathlib import Path
from src.logger.logging import Logger


LIST_OF_FILES = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "src/logger/logging.py",
    "src/exceptions/exceptions.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
    "experiments/experiments.ipynb",
    "config/config.yml",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "params.yml",
]


def create_folder_structure(list_of_files):
    for file in list_of_files:
        file_path = Path(file)
        file_dir = file_path.parent
        if not file_dir.exists():
            Logger.info(f"Creating directory {file_dir} for file {file_path}")
            file_dir.mkdir(parents=True, exist_ok=True)
        else:
            Logger.info(f"Directory {file_dir} already exists")
        if not file_path.exists() or file_path.stat().st_size == 0:
            file_path.touch()
        else:
            Logger.info(f"File {file_path} already exists")


if __name__ == "__main__":
    create_folder_structure(LIST_OF_FILES)
