from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="dtit.pyCRCLib",
  version="0.0.1",
  author="sunboss_uw",
  author_email="dev@datatellit.com",
  description="This is DTIT CRC library.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/datatellittech/dtit_packages",
  packages=find_namespace_packages(include=['dtit.*']),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=[
      'numpy>=1.14.0'
  ],  
)