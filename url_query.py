# from langchain.document_loaders import WebBaseLoader
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.chat_models.openai import ChatOpenAI
# from datetime import datetime
# import dotenv

# dotenv.load_dotenv()

# def web_qa(url_list, query, out_name):
#     openai = ChatOpenAI(
#         model_name="gpt-3.5-turbo",
#         max_tokens=2048
#     )
#     loader_list = []

#     print("printing info from url")
#     for url in url_list:
#         print('loading url: %s' % url)
#         loader_list.append(WebBaseLoader(url))

#     index = VectorstoreIndexCreator().from_loaders(loader_list)
#     ans = index.query(question=query, llm=openai)

#     print("")
#     print(ans)

#     # Change the file extension to '.txt'
#     outfile_name = out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".txt"
#     with open(outfile_name, 'w') as f:
#         f.write(ans)

# url_list = [
#     "https://www.cityofmillvalley.org/758/East-Blithedale-Rehabilitation-Project",
# ]

# prompt = '''
#     Given the context, please provide the following:
#     1. detailed information of what it is (make sure no any point is left )
#     2. give point-wise data available

# '''

# web_qa(url_list, prompt, "summary")



from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models.openai import ChatOpenAI
from datetime import datetime
import dotenv

dotenv.load_dotenv()

import os

def web_qa(url_list, query, out_name, output_dir):
    openai = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        max_tokens=2048
    )
    loader_list = []

    print("printing info from url")
    for url in url_list:
        print('loading url: %s' % url)
        loader_list.append(WebBaseLoader(url))

    index = VectorstoreIndexCreator().from_loaders(loader_list)
    ans = index.query(question=query, llm=openai)

    # print("")
    # print(ans)
    print("url_qury ran succesfully and the output is saved in data folder")

    # Change the file extension to '.txt'
    outfile_name = os.path.join(output_dir, out_name + datetime.now().strftime("%m-%d-%y-%H%M%S") + ".txt")
    with open(outfile_name, 'w') as f:
        f.write(ans)

url_list = [
    "https://www.cityofmillvalley.org/758/East-Blithedale-Rehabilitation-Project",
]

prompt = '''
    Given the context, please provide the following:
    1. detailed information of what it is (make sure no any point is left )
    2. give point-wise data available

'''

output_directory = "data"  

web_qa(url_list, prompt, "summary", output_directory)
