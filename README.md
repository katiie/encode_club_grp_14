# encode_club_grp_14
Repository for Group 14 Encode Bootcamp

# Chef GPT
A customer AI-powered system to assist you with cooking and baking. The model can:
- Provide dish name given a list of ingredients
- Generate recipe for requested dish
- Offer improvement and feeback on existing recipes

# Installation and Setups
1) Create/retrieve an OpenAI API key from your [Playground account](https://platform.openai.com/settings/profile?tab=api-keys).
2) Ensure that you have [python](https://www.python.org/downloads/) installed on your laptop
3) Ensure that you have pip installed on your laptop

# Running the Application

### Step 1: Add your API key as an command variable
 ```bash
   # Linux/MacOS/Bash on Windows
   export OPENAI_API_KEY="your-api-key-here"
   ```

   ```bash
   # Windows Command Prompt
   set OPENAI_API_KEY=your-api-key-here
   ```

   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your-api-key-here"
   ```

 ### Step 2: Check if you have the variable set up correctly by running the following command on your terminal:

   ```bash
   # Linux/MacOS/Bash on Windows
   echo $OPENAI_API_KEY
   ```

   ```bash
   # Windows Command Prompt
   echo %OPENAI_API_KEY%
   ```

   ```bash
   # Windows PowerShell
   echo $env:OPENAI_API_KEY
   ```

 ### Step 3: To check if the key is set up correctly without revealing your key on your terminal, you can display it partially by running the following command:

   ```bash
   # Linux/MacOS/Git Bash on Windows
   echo ${OPENAI_API_KEY:0:3}...
   ```

   ```bash
   # Windows Command Prompt
   echo %OPENAI_API_KEY:~0,3%...
   ```

   ```bash
   # Windows PowerShell
   echo ($env:OPENAI_API_KEY).Substring(0,3) + "..."
   ```

### Step 4: Final Check

 Check if you have `sk-...` and not just `...`

### Step 5: Run the script
 ```bash
 # Linux/MacOS/Git Bash on Windows
 # Windows Command Prompt
 # Windows PowerShell

 # if you have python

 python "[Name Of File].py"

 # if you have python3

 python3 "[Name Of File].py"
 ```

> For more instructions on how to complete this in different Operational Systems, go to <https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key>

Now you're ready to start cooking with Chef GPT! 🍽️