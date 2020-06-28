import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTikTokAPI",
    packages=setuptools.find_packages(),
    version="0.0.2",
    license='MIT',
    author="Avilash Kumar",
    author_email="avilashkumar4@gmail.com",
    description="Unofficial TikTok API wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avilash/TikTokAPI",
    download_url='https://github.com/avilash/TikTokAPI/tarball/master',
    keywords=['tiktok', 'python', 'api', 'tiktok-api', 'tiktok api'],
    install_requires=[
        'requests',
        'pyppeteer',
        "pyppeteer_stealth"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    include_package_data=True
)
