import setuptools

setuptools.setup(
    name="saicinpainting",
    packages=setuptools.find_packages(),
    package_data={'models': ['models/ade20k/color150.mat']},
    include_package_data=True,
)
