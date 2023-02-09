import setuptools


def load_requirements():
    requirements_file_name = "requirements.txt"
    requires = []
    with open(requirements_file_name) as f:
        for line in f:
            if line:
                requires.append(line.strip())
    return requires


setuptools.setup(
    name="saicinpainting",
    packages=setuptools.find_packages(),
    install_requires=load_requirements(),
)
