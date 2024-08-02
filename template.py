import os
from pathlib import Path



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
    "src/utils/utils.py",
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
    "experiments/experiments.ipynb"
]

def create_folder_structure(list_of_files):
    for file in list_of_files:
        file_path = Path(file)
        file_dir = file_path.parent
        if not file_dir.exists():
            file_dir.mkdir(parents=True, exist_ok=True)
        if not file_path.exists() or file_path.stat().st_size == 0:
            file_path.touch()


if __name__ == "__main__":
    create_folder_structure(LIST_OF_FILES)