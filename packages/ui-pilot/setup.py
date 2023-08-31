from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ui-pilot',
    version='0.0.0',
    license='DEL',
    description='navigate any interface with a human-like pilot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ly3xqhl8g9',
    author_email='ly3xqhl8g9@plurid.com',
    classifiers=[
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: User Interfaces',
        'Programming Language :: Python :: 3.11',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'numpy',
        'opencv-python',
        'PIL',
    ],
)
