from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='simple_spearmint_v2',
    version='1.0.0',
    description='Thin and improved wrapper class around spearmint',
    author='Federico Parroni',
    author_email='federicoparroni.95@gmail.com',
    url='https://github.com/keyblade95/simple_spearmint',
    packages=['simple_spearmint_v2'],
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers"
    ],
    keywords='bayesian hyperparameter optimization',
    license='MIT',
    install_requires=[
        'spearmint',
        'numpy',
    ],
)
