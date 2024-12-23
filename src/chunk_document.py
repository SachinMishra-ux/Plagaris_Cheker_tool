from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.text_clean_helper import clean_string


def no_of_searches(file_path):
    """
    Extracts, processes, and cleans text from a PDF file to determine the number of relevant search queries.

    Args:
        file_path (str): The file path to the PDF document to be processed.

    Returns:
        list: A list of cleaned text chunks representing the search queries to be made.

    Functionality:
        1. Loads the PDF file using the `PyPDFLoader` class.
        2. Counts and prints the total number of pages in the PDF.
        3. Splits the document into smaller chunks using a `RecursiveCharacterTextSplitter` 
           with specified chunk size and overlap.
        4. Cleans each chunk of text by:
            - Filtering out content that includes specific unwanted phrases (e.g., "Albert Einstein", "Ⓒ", 
              "Knowledge check", etc.).
            - Cleaning the remaining text using a `clean_string` function (assumed to be predefined).
        5. Prints and returns the number of valid queries generated.
    """
    queries = []
    # load Fulfillment_report_slides.pdf from `data` folder to Colab
    loaders = PyPDFLoader(file_path, extract_images=True)
    docs = loaders.load()
    #loaders = PyPDFLoader(file_path, extract_images=True)
    #docs= loaders.load_and_split()
    # No of pages in doc
    print('Numbers of pages:',len(docs))

    # Document splitting
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 170,
        chunk_overlap = 15
    )
    splits = text_splitter.split_documents(docs)
    
    
    # Clean each document chunk (split)
    for document in splits:
        # Skip the iteration if any of the unwanted phrases are in the document content
        if any(phrase in document.page_content for phrase in ['Albert Einstein', 'Ⓒ', 'Congratulations', 'Knowledge check','Module completion','import','# Importing necessary modules','print','pip']):
            continue  # Skip this iteration
    
        # Clean the text and append to queries
        cleaned_text = clean_string(document.page_content)
        queries.append(cleaned_text)

    print("No of searches to make:", len(queries))
    return queries

if __name__ == "__main__":
    queries= no_of_searches("./data/test1.pdf")
    print(type(queries))
    print(queries)

    #my_list= ['Intro to classi\x00cation - Logistic regression - 1\nOne should look for what is and not what he thinks should be. (Albert Einstein)DAT\nSOCI', 'Logistic regression: Topic introduction\nIn this part of the course, we will cover the following concepts:\nLogistic regression use cases and theory behind it\nData transformation necessary for logistic regression\nImplementation of logistic regression on a dataset', 'Implementation of logistic regression on a dataset\nModel performance evaluation and tuning\nLogistic regression-1 1', 'Quick Activity\nSuppose we want to predict whether a person will purchase a certain car or not\nWhat nume rical data might be relevant for making this prediction?\nWhat additional qualitative or categorical data might be relevant?', 'What additional qualitative or categorical data might be relevant?\nHow migh t you handle variables like marital status, education level, or gender?\nLogistic regression-1 2', 'Module completion checklist\nObjectives Complete\nDetermine when to use logistic regression for classi\x00cation and transformation of target\nvariable\nSummarize the process and the math behind logistic regression\nLogistic regression-1 3', 'Logistic regression\nLogistic regression is a supervised machine learning method used for classi\x00cation\nThe target or dependent variable is binary\nYes or no\nThis or that\n1 or 0\nThe outputs are numerical probabilities that different observations will be in the desired', '1 or 0\nThe outputs are numerical probabilities that different observations will be in the desired\nclass (y = 1), rather than category labels\nLogistic regression-1 4', 'What logistic regression looks like\nThe “logis tic” in logistic regression comes from the logit function (a.k.a. sigmoid\nfunction)\nThe mod el solves for coef\x00cients to create a curve maximizing the likelihood of correct\nclassi\x00cation\nLogistic regression-1 5', 'What logistic regression looks like (cont’d)\nThe mod el’s performance can be changed by adjusting the cut-off probability where\nthe curve bends, with no need to re-run the model with new parameters\nNote that we convert the target variable to binary values or either 0 or 1 depending on', 'Note that we convert the target variable to binary values or either 0 or 1 depending on\nthis cut-off or threshold\nSource\nLogistic regression-1 6Logisticregressioncurve\ncosts:0.401\n1.0\nx\nxXXx\n0.8\ny\n0.6\n0.4\n0.2\n0\nXXXX\nX\nx\nX\n-150\n-100\n-50\n0\n50\n100\n150\n200\nX', 'Logistic regression: process\nLogistic regression-1 7Step 1:\nStep 2:\nStep 3:\nStep 4:\nConvert target\nLogistic regression\nUseROC curve\n&AUC\nCheck performance on\nvariable to 1/0\non training data\nto pick threshold\ntest data\nTruePositive Rate\nAct+\nAct-\nPred +\nPred-\nFalsePositiveRate\nX', 'Converting catego rical to binary variable\nThere are two main ways to prepare the target variable:\nFirst method: translate an existing binary variable (i.e., any categorical variable\nwith 2 classes) into 1 and 0\nLogistic regression-1 81\nB\nB\nB\nA\nB\n3\nA\nA\nA\nB\n2\nB\nB\nA\nA\n5\n2\n3\n4\nx', 'Converting continuous to binary variable\nSecond method: convert a continuous  numeric variable into a binary one\nWe can do this by using a threshold and labeling observations that are higher than\nthat threshold as 1 and 0 otherwise', 'that threshold as 1 and 0 otherwise\nIf the median for the example below was 1 0 0, then any point below the median is\ncoded as 0, and any point above is 1\nLogistic regression-1 9Charge\nCharge\n193.89\n1\n0\n0\n39.99\n0\n201.65\n1\n117.9\n1\n200.88\n1\n79.99\n0', 'Module completion checklist\nObjectives Complete\nDetermine when to use logistic regression for classi\x00cation and transformation of target\nvariable✔\nSummarize the process and the math behind logistic regression\nLogistic regression-1 10', 'Linear regression line\nFor data points , we have \nor \nThe function that “\x00ts” the points is a\nsimple line Logistic regression curve\nFor the same data points , \nor \nThe function that “\x00ts” the data points is\na sigmoid Linear vs.\xa0logistic regression\n,..., x1 xn y=0\ny=1\n=ax+b ŷ\xa0,..., x1 xny=0\ny=1', 'a sigmoid Linear vs.\xa0logistic regression\n,..., x1 xn y=0\ny=1\n=ax+b ŷ\xa0,..., x1 xny=0\ny=1\np(y=1)=exp(ax+b)\n1+exp(ax+b)\nLogistic regression-1 11', 'Logistic regression: function\nFor every value of , we \x00nd  (i.e., probability of success) or probability that \nTo solve for , logis tic regression uses an expression called a sigmoid function:\nAlthough it may look a little scary, we can see a very familiar equation inside of the\nparentheses:', 'parentheses: \nThis is virtually identical to x p y=1\np\np=exp(ax+b)\n1+exp(ax+b)\nax+b\ny=mx+b\nLogistic regression-1 12', 'Logistic regression: the odds ratio\nThrough some algebraic transformations that are beyond the scope of this course, we\ncan change this equation…\ninto a loga rithmic expression\nSince p is the probability of success, 1 - p is the probability of failure', 'Since p is the probability of success, 1 - p is the probability of failure\nThe ratio  is called the odds ratio - it tells us the odds of having a successful\noutcome with respect to the opposite\nKnowing this provides useful insight into interpreting the resulting coef\x00cientsp=exp(ax+b)\n1+exp(ax+b)', '1+exp(ax+b)\nlogit(p)=log( )p\n1−p\n( )p\n1−p\nLogistic regression-1 13', 'Logistic regression: coef\x00cients\nIn linear regression, the coef\x00cients in the equation can easily be interpreted\nAn increase in  will result in an increase in  and vice versa\nHowever, in logistic regression, the simplest way to interpret a positive coef\x00cient is\nwith an increase in likelihood', 'with an increase in likelihood\nA larger value of  increases the likelihood that ax+b\nx y\nx y=1\nLogistic regression-1 14', 'Knowledge check\nLink: https://forms.gle/NucjSoLP9z4RDwiDA\nLogistic regression-1 15', 'Module completion checklist\nObjectives Complete\nDetermine when to use logistic regression for classi\x00cation and transformation of target\nvariable✔\nSummarize the process and the math behind logistic regression ✔\nLogistic regression-1 16', 'Congratulations on completing this module!\nLogistic regression-1 17']