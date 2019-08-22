from setuptools import setup

setup(name='NNet_Core',
      version='1.0',
      description='Tool for brain extraction',
      url='https://github.com/GUR9000/Deep_MRI_brain_extraction',
      python_requires='>=3.5',
      license='MIT',
      zip_safe=False,
      install_requires=[
      'numpy',
      'theano',
      'nibabel',
      'h5py'
      ],
      scripts=['NNet_core/deep3Dpredict.py','NNet_core/deep3Dtrain.py'],
      packages=['NNet_Core'],
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Operating System :: Unix'
      ]
      )

