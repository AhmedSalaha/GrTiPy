from setuptools import setup
from GrTiPy import __version__


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='GrTiPy',
      version=__version__,
      description='General Relativity toolbox in python',
      long_description=readme(),
      url='',
      author='Ahmed Salah',
      author_email='asalah3020@gmail.com',
      maintainer='Ahmed Salah',
      maintainer_email='asalah3020@gmail.com',
      license='BSD',
      packages=['GrTiPy'],
      include_package_data=True,
      install_requires=["sympy >= 0.7.3"],
      platforms='any',
      zip_safe=False,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Education',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
      ])
