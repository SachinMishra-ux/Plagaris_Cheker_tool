# Plagiarism checker tool

## Local Project Setup:

- Clone the project to desktop

#### chromedriver setup

- This project requires a `chromedriver` and the version needs to match with your chrome browser.
- So first check your chrome browser version by doing the below step:
![alt text](./assets/chrome_version.png)

- Once you identify the chrome version, go to this link [Link to download chromedriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) find the version of the chromedriver that matches your chrome browser version.

- Make sure you are downloading the `chromedriver` and not `chrome or chrome-headless-shell`
- ![alt text](./assets/different_things.png)
- It will download the zip file, extract the zip file and copy paste the `chromedriver` to the `local_deriver` folder.
- [Watch this video for more information](./assets/chrome_version.png)

### Environment Setup

#### Either

1. Run the following command in your terminal to setup the environment:
   - ```bash setup.sh```
2. To activate virtual environment:
   - ```conda activate ./plagiarism```
3. Within the `src` folder you will see a file called `constanats.py`and within the the file you need to change the value of `image_folder` = `"/Users/sachinmishra/Desktop/plagarism_checker/extracted_images"` according to your system path.

 - example, if you have your path like this: `/Users/swaroop/Desktop/plagarism_checker/extracted_images` so just replace the `image_folder` with `"/Users/swaroop/Desktop/plagarism_checker/extracted_images"`

#### OR
  
1. create virtual environment: ```conda create -p plagarism python==3.10 -y```
2. check your environment ```conda env list```
3. You will see something like this: `/Users/sachinmishra/Desktop/Testing/plagarism_checker/plagarism`
4. activate virtual environment : ```conda activate {full_path_of_virtual_environment} ```
5. download all the dependencies: ```pip install -r requirements.txt```
6. 3. Within the `src` folder you will see a file called `constanats.py`and within the the file you need to change the value of `image_folder` = `"/Users/sachinmishra/Desktop/plagarism_checker/extracted_images"` according to your system path.

 - example, if you have your path like this: `/Users/swaroop/Desktop/plagarism_checker/extracted_images` so just replace the `image_folder` with `"/Users/swaroop/Desktop/plagarism_checker/extracted_images"`


## To run the application:
``` streamlit run main.py```

### Chromedriver execuation error resolution
 
- Once You run the application and if you see a prompt regarding `chromedriver not executable` or something related to access of the chromedriver then you can use the below step to fix it.
![alt text](./assets/image.png)


### For any Query

- In case of any query/issue reach out to Sachin via slack or email: sachin.mishra@datasociety.com

