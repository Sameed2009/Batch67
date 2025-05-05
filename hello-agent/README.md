open terminal in administrator mode


1.  uv init --package hello-agent
2.  uv venv
3.  .venv\Scripts\activate
4.  uv run hello-agent      ===> and result is Hello from hello-agent!
5.  code .
6.  Add file .env outside src folder
7.  .env & Save             ===>add line at last in gitignore file
8.  geneate api key from google ai studio
9.  and add in .env file
10. uv add openai-agents        ===>Add openai-agents 
11. add new file in src folder agent_hello.py
12. press ctrl+shift+p key
13. Select interpreter and the select Python (Recommended)
14. import classes in agent_hello.py
15. define model openai and use gemini open ai key
16. define agent using model
16. create a function of my_first_agnet
17. add a while loop unti user type exit to close the agent
18. get result of user input using runner and run_sync method
19. display the result on screen
20. Loop start untill user type Exit