from setuptools import setup, find_packages

# Semantic-Versioning
'''
0.0.1
First digit: Major Version (breaking changes / big update)
Second digit: Minor Version (Non-Breaking Changes / minor updates)
Third digit: Patch Version (bugfix / patch)
'''
VERSION = '0.1.0'
DESCRIPTION = 'A tiny little library, that returns a list of persons out of pre-generated mock-data.'
LONG_DESCRIPTION = 'This library exposes a "PersonGenerator" class, with a method for getting up to 1000 persons, and a method for printing the same ammount to stdout. This is just a small project for learning how to publish packages. Don\'t expect any kind of support.'

# Setting up
setup(
    name="Persinator",
    version=VERSION,
    author="EvilWeasel (Tobias Wehrle)",
    author_email="38261180+EvilWeasel@users.noreply.github.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'persinator': ['data/*']},
    install_requires=[],
    keywords=['python', 'generate', 'persons', 'person', 'mock', 'library'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)