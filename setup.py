import setuptools

setuptools.setup(
    name="streamlit-widget-tracker",
    version="0.0.1",
    author="Ashish Rai",
    author_email="ashishraics512@gmail.com",
    description="streamlit-widget-tracker helps track the widget values in use",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/PROFESSOR-PENGUIN/streamlit-widget-tracker",
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "repo @ https://github.com/PROFESSOR-PENGUIN/streamlit-text-like/blob/main/template/dist/streamlit_text_like-0.0.1.tar.gz"
    ],
)
