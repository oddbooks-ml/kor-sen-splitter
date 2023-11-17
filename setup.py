from setuptools import setup

setup(
    name='kor-sen-splitter',
    version='0.0.3',
    description="한국어 문장 분리기",
    url="https://github.com/oddbooks-ml/kor-sen-splitter.git",
    author="jinoan",
    author_email="jinoan89@gmail.com",
    packages=["kor_sen_splitter"],
    install_requires=["kss", "kiwipiepy"]
)