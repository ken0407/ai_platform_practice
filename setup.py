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
                "scikit-learn>=0.23.2,<1.0.0"
                ],
        )

if __name__=="__main__":
    main()
