echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.10"
conda create --prefix ./plagiarism python=3.10 -y
echo [$(date)]: "activate plagiarism"
source activate ./plagiarism
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"