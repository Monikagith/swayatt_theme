from setuptools import setup, find_packages

setup(
    name="swayatt_theme",
    version="0.0.1",
    description="Custom Theme for ERPNext",
    author="Swayatt",
    author_email="sunny@swayatt.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
