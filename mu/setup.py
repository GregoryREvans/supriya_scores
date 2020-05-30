import setuptools


install_requires = ["supriya"]

keywords = [
    "supriya",
    "music composition",
    "audio synthesis",
    "supercollider",
]

if __name__ == "__main__":
    setuptools.setup(
        author="Gregory Rowland Evans",
        author_email="gregoryrowlandevans@gmail.com",
        install_requires=install_requires,
        keywords=", ".join(keywords),
        name="mu",
        packages=["mu"],
        platforms="Any",
        url="https://github.com/GregoryREvans/mu",
    )
