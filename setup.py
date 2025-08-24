from setuptools import setup, find_packages

install_requires = [
    "backports.tarfile==1.2.0",
    "flask==3.1.1",
    "importlib-metadata==8.0.0",
    "jaraco.collections==5.1.0",
    "kafka-python==2.2.15",
    "langchain-community==0.3.27",
    "langchain-mistralai==0.2.11",
    "langchain-openai==0.3.28",
    "tinycss2==1.4.0",
    "tomli==2.0.1",
]

setup(
    name='ds-service',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    include_package_data=True,
)