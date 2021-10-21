import setuptools

setuptools.setup(
    name="streamlit_widget_tracker",
    version="0.0.1",
    author="Ashish Rai",
    author_email="ashishraics512@gmail.com",
    description="streamlit_widget_tracker helps track the widget values in use",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/PROFESSOR-PENGUIN/streamlit-widget-tracker",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 1.0.0",
    ],
)
