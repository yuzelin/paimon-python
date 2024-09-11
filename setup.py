################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import fnmatch
import java_based_implementation.util.setup_utils
import os
import shutil

from setuptools import Command, setup


class CleanCommand(Command):
    description = 'Clean up temporary files and directories of last build.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        directories_to_delete = ['build', 'dist', '*.egg-info']

        for directory in directories_to_delete:
            if '*' in directory:
                for matched_dir in filter(lambda x: fnmatch.fnmatch(x, directory), os.listdir('.')):
                    if os.path.isdir(matched_dir):
                        shutil.rmtree(matched_dir)
            else:
                if os.path.exists(directory):
                    shutil.rmtree(directory)


try:
    PACKAGES = [
        'paimon_python_api',
        'java_based_implementation',
        'java_based_implementation.util'
    ]

    PACKAGE_DATA = {
        'java_based_implementation': java_based_implementation.util.setup_utils.get_package_data()
    }

    install_requires = [
        'py4j==0.10.9.7',
        'python-dateutil>=2.8.0,<3',
        'pytz>=2018.3',
        'numpy>=1.22.4',
        'pandas>=1.3.0',
        'pyarrow>=5.0.0'
    ]

    setup(
        name='paimon_python',
        version='0.9.0.dev1',
        packages=PACKAGES,
        include_package_data=True,
        package_data=PACKAGE_DATA,
        cmdclass={'clean': CleanCommand},
        install_requires=install_requires,
        description='Apache Paimon Python API',
        author='Apache Software Foundation',
        author_email='dev@paimon.apache.org',
        url='https://paimon.apache.org',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11'],
        python_requires='>=3.8'
    )
finally:
    java_based_implementation.util.setup_utils.clean()
