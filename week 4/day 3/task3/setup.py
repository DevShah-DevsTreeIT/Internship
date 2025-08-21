from setuptools import setup, find_packages

setup(
    name='my-first-package-username',  # Must be unique on TestPyPI
    version='0.1.0',
    author='Your Name',
    author_email='you@example.com',
    description='A simple greeting package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_first_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
