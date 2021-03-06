import os
from distutils.core import setup



setup(
    name='DeltaML-commons',  # How you named your package folder (MyLib)
    packages=['commons', 'commons.data', 'commons.decorators', 'commons.encryption', 'commons.model',
              'commons.operations_utils', 'commons.utils', 'commons.model.exceptions', 'commons.web3',
              'commons.web3.resources'],  # Chose the same as "name"
    package_dir={'commons.web3.resources': 'commons/web3/resources'},
    package_data={'commons.web3.resources': ['commons/web3/resources/*.json']},

    data_files=[('commons.web3.resources', ['commons/web3/resources/abi.json'])],
    include_package_data=True,
    version='0.10.17',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Commons resources between DeltaML projects',  # Give a short description about your library
    author='DeltaML',  # Type in your name
    author_email='rojasagustin90@gmail.com',  # Type in your E-Mail
    url='https://github.com/DeltaML/commons',  # Provide either the link to your github or to your website
    download_url='https://github.com/DeltaML/commons/archive/v_01.tar.gz',  # I explain this later on
    keywords=['federated learning', 'machine learning', 'IA'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'numpy',
        'pandas',
        'sklearn',
        'phe',
        'web3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
