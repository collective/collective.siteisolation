from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='kuleuven.siteisolation',
      version=version,
      description="Isolate objects in a Zope root from each other",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='ICTS KULeuven',
      author_email='jfroche@affinitic.be',
      url='http://svn.plone.org/svn/collective/collective.siteisolation',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
            test=['zope.testing']),
      install_requires=[
          'setuptools',
          'zope.component',
          'plone.memoize',
          'zope.interface'])