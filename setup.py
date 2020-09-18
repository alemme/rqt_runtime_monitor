import os
from glob import glob
from setuptools import setup

package_name = 'rqt_runtime_monitor'
package_resource = 'runtime_monitor_widget.ui'


setup(
    name=package_name,
    version='0.5.9',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['plugin.xml']),
        ('share/' + package_name, ['package.xml']),
        ('resource/', ['resource/' + package_resource]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Aaron Blasdel',
    maintainer_email='ablasdel@gmail.com',
    description='rqt_runtime_monitor provides a GUI plugin viewing DiagnosticsArray messages.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'runtime_monitor = rqt_runtime_monitor.runtime_monitor:main'
        ],
    },
)