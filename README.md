# Objective 

This code automates a part of the customer KYC process in a bank. Given a person's name it: 
1. Fetches the top 'n' links based on a google search of the name 
2. Constructs a prompt for ChatGPT with the links and the person's name. The prompt asks ChatGPT to summarise the content of the links and opine whether there is any adverse news against the individual 
3. Creates a summary report of the findings 

This should help improve productivity of the KCY analyst. Instead of manually searching and clicking through individual links, analysts can peruse the summary.


# Getting Started with this code 

### Install the packages in requirements.txt 

```
pip3 install -r requirements.txt
```

### Create the config file 

Create a file in the repo home called config.py. Feed in your Open AI API code like this:

OPENAI_API_KEY='your_api_key'

# Running the code 

Run the code with :

```python3 app.py --person='Brian Lara' 

The report will be printed on the screen. 
