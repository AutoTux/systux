import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "systux", "version.py")) as fp:
    exec(fp.read())

setup(name = "systux",
      version = __version__,  # noqa: F821
      author = "Juan Bindez, Collin",
      author_email = "juanbindez780@gmail.com",
      packages = ["systux"],
      package_data = {"": ["LICENSE"],},
      url = "https://github.com/AutoTux/systux",
      license = "GPLv2 license",
      entry_points = {
        "console_scripts": [
          "systux = systux.cli:main"],},
      classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python",
            "Topic :: Internet",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Terminals",
            "Topic :: Utilities",
        ],
      description = ("Python 3 library for automation in Linux."),
      include_package_data = True,
      long_description_content_type = "text/markdown",
      long_description = long_description,
      zip_safe = True,
      python_requires = ">=3.7",
      project_urls = {
        "Bug Reports": "https://github.com/AutoTux/systux/issues",
        "Read the Docs": "https://github.com/AutoTux/systux/tree/main/docs/user",
      },
      keywords = ["Linux", "download", "automations", "system",],)