RESTAURANT CHATBOT - Case Study
27 April 2020

Kavita Thekkedath
Srikar Chepuri


When chatbots were first introduced around 1966, they were programmed to respond to a user's questions with simple matching patterns. Today, they possess sophisticated techniques to understand users' questions and deliver useful and relevant responses. For a chatbot, time is never a constraint, if a customer calls even at midnight for an issue resolution, the chatbot is at his service. If the customer is dissatisfied with the resolution and wants a longer conversation, the bot can still handle it.  With businesses looking at reducing hiring and recruitment costs, chatbots can provide significant cost savings by replacing live agents at lower costs. For businesses, good customer service equals brand success. By using chatbots for instant response - even if it is just a plain "thank you" - and providing appropriate timelines for resolution, businesses earn customer goodwill. 

Chatbots assist businesses by providing real-time, accurate responses to low-complexity customer queries, which largely revolve around non-functional product, warranty expiration, etc. Since time is of the essence, chatbots can bypass dependency on repair personnel and directly provide responses to customers and save precious time. Also, customer information is stored in the organizational database, making it easier for chatbots to dig out previous instances of customer problems and offer speedy resolution.

There are two broad types of chatbots:
- generic chatbots
- domain-specific chatbots

Generic chatbots, also called virtual assistants, such as Google Assistant, Amazon’s Alexa, Microsoft’s Cortana or Apple’s Siri, are used to answer generic queries such as dialling a phone number, dropping a message to a contact, booking a calendar slot, fetching results from a web search, etc. These systems have been trained on massive amounts of user data, encyclopedias, conversational dialogues with humans etc.

The other type is the domain-specific, task-oriented chatbot. By domain-specific and task-oriented, we mean that it can handle queries pertaining to a particular domain or type of task. For example, a ‘weather bot’ can only tell weather predictions. It cannot book a table in a restaurant or set up an alarm. Similarly, a restaurant discovery bot can help you find restaurants in several cities, though it might not be able to answer general questions such as "Who is the prime minister of India?".

Problem Statement:
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

We are going to use an open source framework for building conversational bots - RASA.

Building ChatBot using RASA:
RASA - An open source Conversational AI is a set of machine learning tools for developers to create contextual text and voice-based chatbots and assistants.

Apple’s Siri, Amazon’s Alexa etc. are much more than a 'speech-based search engine'. Apart from searching for information (e.g. from Wikipedia, YouTube, Google etc.), they can 'talk' to us in natural language. Conversation, or dialogue, is a very fundamental aspect of human language, and arguably the most interesting challenge in building truly intelligent NLP systems. A step towards building such systems is domain specific, text-based chatbots used by organisations for tasks such as booking hotels, retrieving stock market information, resolving customer queries etc.

Any conversational system has primarily two components –
-	Natural Language Understanding, or NLU
-	A Dialogue Management System which carries out the overall conversation.

In Rasa, these two components are named Rasa NLU and Rasa Core respectively.
Rasa NLU is the tool used for intent classification and entity extraction.
Rasa Core, the dialogue management layer of Rasa, takes structured input in the form of intents and entities (i.e. the output of Rasa NLU) and decides the next actions.

Rasa Installation:

Prerequisites
-	Python 3.7.0
-	Rasa NLU
-	Rasa Core
-	Spacy – en models

Create a Virtual environment: conda create --name rasa

Installation Steps:
1.	Go the Microsoft Visual Studio link: https://visualstudio.microsoft.com/ . 
a.	Select the ‘Visual Studio IDE’ and from the dropdown, select the ‘Community version 2019’:
b.	Install the downloaded file.
c.	Once the Visual Studio is installed, select the Python Development under ‘Web & Cloud’ Environment. Also, on right side (Summary), in optional menu select the ‘Python native development tools’. Click on install
2.	Open anaconda prompt with administrator rights
3.	Activate Virtual environment
a.	>> activate rasa
4.	Install below packages
a.	>>  pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
b.	>>  pip install rasa 
5.	Install rasa-nlu with spacy using 
a.	>> pip install rasa[spacy]
6.	Download spacy model and link it 
a.	>> python -m spacy download en_core_web_md
b.	>> python -m spacy link en_core_web_md en

Packages Installed on our machine:

-	rasa==1.9.5
-	rasa-sdk==1.9.0
-	rasa-x==0.27.5
-	ujson==1.35
-	tensorflow==2.1.0
-	tensorflow-addons==0.9.1
-	tensorflow-estimator==2.1.0
-	tensorflow-hub==0.7.0
-	tensorflow-probability==0.7.0
-	spacy==2.1.9

How to run this chatbot using Anaconda Command Prompt:
1.	Open two anaconda prompts and activate rasa environment in both of them.
2.	In first prompt, execute "rasa run actions"
3.      In Second Anaconda Prompt, execute "rasa shell" and ask what you are looking for here. 
