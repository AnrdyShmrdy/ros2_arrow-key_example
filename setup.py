from setuptools import setup

package_name = 'keyboard_pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andyp',
    maintainer_email='andy.ponce@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'publisher = keyboard_pub_sub.keyboard_publisher:main',
        	'subscriber = keyboard_pub_sub.keyboard_subscriber:main'
        ],
    },
)