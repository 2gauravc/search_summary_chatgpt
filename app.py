
import config 
import openai 
import sys, getopt
from datetime import datetime

def get_chatgpt_resp(question): 
    openai.api_key = config.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                    {"role":"system","content":"You are a chatbot"},
                    {"role":"system","content":question}]
    )
    result = ''
    for choice in response.choices:
        result+=choice.message.content

    return (result)

def gsearch(pname):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
 
    # Google Search and return 10 links
    query = pname
    search_links = []
    for j in search(query, tld="com", num=10, stop=10, pause=2):
        search_links.append(j)
    return(search_links)
    
    
def chatgpt_prompt(pname, search_links):
    all_links = '\n'.join(map(str,search_links))
    prompt_text = "You are a expert KYC analyst. I need help to identify if there is any adverse news about {}\
       in the following links. \n {}. \n. In the reply include a 20 word summary of the text in each link and if you find any adverse\
           news (Yes or No)".format(pname, all_links)
    return(prompt_text)

def generate_kyc_output(pname, search_links, chat_response):
    rep_txt = ''

    rep_txt += 'Summary of Google Search for {} \n'.format(pname)
    rep_txt += "Report generated on {} \n".format(datetime.now())
    rep_txt += "----------------------------------------------------- \n"

    rep_txt += "Top ten Google Search Links \n"
    rep_txt += '\n'.join(map(str,search_links))
    rep_txt += "----------------------------------------------------- \n"

    rep_txt+= "Summary of searches and adverse news findings \n"
    rep_txt += chat_response 

    return(rep_txt)




def main(argv):
    try:
        opts, args = getopt.getopt(argv,"i:", ["person="])
    except getopt.GetoptError:
            print ('Usage: python app.py --person=<person name>')
            sys.exit(2)
    for opt, arg in opts:
        if opt == '--person':
            pname = arg
    # Google search for the person name and get the first 20 query links 
    search_links = gsearch(pname)

    # Construct the prompt 
    prompt_text = chatgpt_prompt(pname, search_links)

    #get ChatGPT response 
    resp = get_chatgpt_resp(prompt_text)
    
    # Create PDF with links and summary 
    rep_txt= generate_kyc_output(pname, search_links, resp)

    print(rep_txt)


if __name__ == "__main__":
    main(sys.argv[1:])