import os
import platform
from setuptools import setup, find_packages

install_requires = ['numpy']

if platform.system() == 'Darwin' and platform.processor() == 'arm':
    install_requires.append('tensorflow-macos>=2.0')
    # https://github.com/grpc/grpc/issues/25082
    os.environ['GRPC_PYTHON_BUILD_SYSTEM_OPENSSL'] = '1'
    os.environ['GRPC_PYTHON_BUILD_SYSTEM_ZLIB'] = '1'
else:
    install_requires.append('tensorflow>=2.0')

setup(
    name='keras-tcn',
    version='3.5.0',
    description='Keras TCN',
    author='Philippe Remy',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.7',)
