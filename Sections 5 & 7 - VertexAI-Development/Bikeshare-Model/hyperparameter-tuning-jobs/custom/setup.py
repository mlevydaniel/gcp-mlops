
import setuptools

setuptools.setup(
    name=bikeshare_model,
    version=0.1,
    install_requires=[
        'cloudml-hypertune==0.1.0.dev6',
        'gcsfs',
        'pandas',
        'numpy',
        'scikit-learn',
        'google-cloud-storage',
        'joblib'
    ],
    packages=setuptools.find_packages()
)