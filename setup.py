import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TikTokAPI-Python",
    version="0.0.1",
    license='MIT',
    author="Avilash Kumar",
    author_email="avilash.k@greyorange.sg",
    description="Unofficial TikTok API wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avilash/TikTokAPI",
    download_url='https://github.com/avilash/TikTokAPI/tarball/master',
    keywords=['tiktok', 'python3', 'api', 'unofficial', 'tiktok-api', 'tiktok api'],
    install_requires=[
        'requests',
        'pyppeteer',
        "pyppeteer_stealth"
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
