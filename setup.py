import sys
from setuptools import setup, find_packages
from pathlib import Path
from subprocess import call
version = 0.1
with Path('README.md').open() as readme:
    readme = readme.read()

setup(
    name='pspy-proxy',
    version=version if isinstance(version, str) else str(version),
    keywords="",  # keywords of your project that separated by comma ","
    description="",  # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.5.0',
    url='https://github.com/purescript-python/installer',
    author='thautawarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": ['pspy-blueprint=pspy_proxy.proxy:main']},
    # above option specifies what commands to install,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd:compiler"]}
    install_requires=['purescripto>=0.7.3', 'requests'],  # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)

print("Installing binaries...")
call([sys.executable, str(Path(__file__).parent / "install_binary.py")])
