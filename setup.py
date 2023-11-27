import setuptools

with open ('README.md' , "r",encoding ="utf-8") as f:
    long_description = f.read() ## to publish as pypi package or local package

__version__ =  "0.0.0"

REPO_NAME ="TEXTSUMMARIZER"
AUTHOR = "SubramanyaNayak"
SRC_repo = 'textsummarizer'
AUTHOR_EMAIL = 'subramanyanayak3@gmail.com'



setuptools.setup(
    name=SRC_repo,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

