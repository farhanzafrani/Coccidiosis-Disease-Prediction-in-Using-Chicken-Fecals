import os
from pathlib import Path
import yaml
from src.logger.logging import Logger
import json
import joblib
from ensure import ensure_annotations
from typing import List, Dict, Union, Any
import base64
from box.exceptions import BoxValueError
from box import ConfigBox


@ensure_annotations
def read_yaml(path_to_file: Path) -> ConfigBox:
    """Read the yaml file and return the contents as configbox
    Args: path_to_file(Path): path of the yaml file

    Raises:
        ValueError: if yaml file does not exist or empty

    Returns:
        ConfigBox: configbox object
    """

    try:
        with open(path_to_file) as file:
            config_dict = yaml.safe_load(file)
            Logger.info("yaml file : {} loaded succesfully.".format(path_to_file))
            return ConfigBox(config_dict)
    except BoxValueError:
        raise ValueError(
            "Could not load yaml file: {} as its empty".format(path_to_file)
        )
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: List, verbose=True):
    """create list of directories

    Args:
        path_to_directories(List[Path]): list of directory paths
        verbose(bool): verbosity flag
    """
    for path in path_to_directories:
        path.mkdir(parents=True, exist_ok=True)
        if verbose:
            Logger.info("Directory : {} created.".format(path))


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data into a file
    Args:
        path: Path to json file
        data: data to be saved
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    Logger.info("Json data saved in : {}.".format(path))


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data from path
    Args:
        path: Path to json file
    Returns:
        ConfigBox: data as object of ConfigBox
    """
    with open(path, "r") as file:
        data = json.load(file)
        return ConfigBox(data)
    Logger.info("json file loaded successfully from:{0}".format(path))


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save data into a binary file
    Args:
        data: data to be saved
        path: path to binary file
    """
    joblib.dump(value=data, filename=path)
    Logger.info("Data saved in binary file : {}.".format(path))


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file data
    Args:
        path: Path to binary file
    Returns:
        Any: object stored in file
    """
    data = joblib.load(path=path)
    Logger.info("Data loaded from binary file : {}.".format(path))
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size of file
    Args:
        path: Path to file
    Returns:
        str: size of file in human readable format
    """
    size = os.path.getsize(path)
    return "{:.2f} {}".format(size / (1024**2), "MB")


@ensure_annotations
def encode_image(image_path: Path):
    """encode image into base64 string
    Args:
        image_path: Path to image file
    Returns:
        str: base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encode_image


@ensure_annotations
def decode_image(image_string, file_name):
    img_data = base64.b64decode(image_string)
    with open(file_name, "wb") as image_file:
        image_file.write(img_data)
    Logger.info("Image decoded successfully from base64 string.")
