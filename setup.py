from setuptools import find_namespace_packages, setup


def main():
    setup(
        name='ai_platform_practice',
        version='0.0.1',
        description='Practice package for AI Platform.',
        author='kex5n',
        author_email='kentaro.ishii0407@gmail.com',
        url='https://github.com/ken0407/ai_platform_practice',
        packages=find_namespace_packages(exclude=("tests",)),
        install_requires=[
            "click>=7.1.2,<8.0.0",
            "python-dotenv>=0.14.0,<1.0.0",
            "scikit-learn>=0.23.2,<1.0.0",
            "pandas>=1.1.2,<2.0.0",
            "numpy>=1.19.2,<2.0.0",
        ],
        extras_require={
            "test": [
                "isort<5.0.0",
                "black==19.10b0",
                "mypy",
                "pytest",
                "flake8",
                "pytest-cov",
                "pytest-flake8",
                "pytest-env",
                "pytest-subtests",
                "flake8-isort",
                "flake8-docstrings",
                "freezegun",
            ],
        },
        package_data={
            ".": [
                ".env",
            ]
        }
    )


if __name__ == "__main__":
    main()
