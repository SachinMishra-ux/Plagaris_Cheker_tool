#!/bin/bash
pip install rapidocr-onnxruntime

wget -N https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

# Clean up the zip file
rm chromedriver_linux64.zip

# Remove the LICENSE.chromedriver file
rm -f LICENSE.chromedriver
