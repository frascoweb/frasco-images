from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-images',
    version='0.1',
    url='http://github.com/frascoweb/frasco-images',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Image manipulation for Frasco",
    long_description=desc(),
    py_modules=['frasco_images'],
    platforms='any',
    install_requires=[
        'frasco',
        'Pillow==2.5.1'
    ]
)