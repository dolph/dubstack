from setuptools import setup, find_packages

setup(name='dubstack',
      version='1.0',
      description="Dubstep karaoke service for OpenStack",
      author='OpenStack, LLC.',
      author_email='openstack@lists.launchpad.net',
      url='http://www.openstack.org',
      packages=find_packages(exclude=['test', 'bin']),
      scripts=['bin/dubstack', 'bin/dubstack-manage'],
      zip_safe=False,
      install_requires=['setuptools'],
      )
