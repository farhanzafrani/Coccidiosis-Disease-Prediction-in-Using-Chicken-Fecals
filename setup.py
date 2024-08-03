import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "CNN_Classifier"
AUTHOR_USER_NAME = "Muhammad Farhan"
SRC_REPO = "CNN_Classifier"
AUTHOR_EMAIL = "mfarhanzafrani@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/farhanzafrani/Complete_MLOps_Project",
    project_urls={
        "Bug Tracker": "https://github.com/farhanzafrani/Complete_MLOps_Project/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
