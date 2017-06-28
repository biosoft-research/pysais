from setuptools import setup, find_packages, Extension
try:
    from Cython.Build import cythonize
except:
    print('Cython is required to install PySAIS')
    raise
try:
    import numpy as np
except:
    print('numpy is required to install PySAIS')
    raise

glibc_fix = False

compile_args = ['-O3', '-fomit-frame-pointer']
if glibc_fix:
    compile_args.append('-DGLIBC_FIX')

extensions = [Extension('PySAIS._sais32',
                        sources=['PySAIS/_sais32.pyx', 'PySAIS/sais32.c'],
                        extra_compile_args=compile_args),
              Extension('PySAIS._sais64',
                        sources=['PySAIS/_sais64.pyx', 'PySAIS/sais64.c'],
                        extra_compile_args=compile_args)]


setup(
    name='PySAIS',
    version='1.0.0',
    ext_modules=cythonize(extensions, include_path=[np.get_include()]),
    include_dirs=[np.get_include()],
    packages=find_packages(),
    install_requires=['Cython', 'numpy'],
    license='MIT'  # Wrapped library is under MIT license.
)
