{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1833cb75-6d90-47cf-9a3a-67abc9c3ff8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi! I'm Chatty, your enhanced chatbot.\n",
      "Type 'bye' to exit.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hii\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatty: I'm not sure how to respond to that. Try asking about the time, jokes, or math.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  jokes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatty: Why did the computer go to therapy? Because it had too many bytes.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  can you convert pdf to jpg\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatty: I'm not sure how to respond to that. Try asking about the time, jokes, or math.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  by\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatty: I'm not sure how to respond to that. Try asking about the time, jokes, or math.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  bye\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatty: Goodbye! Have a great day.\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "import random\n",
    "\n",
    "# Joke list\n",
    "jokes = [\n",
    "    \"Why don’t scientists trust atoms? Because they make up everything!\",\n",
    "    \"Why did the computer go to therapy? Because it had too many bytes.\",\n",
    "    \"Why don’t programmers like nature? Too many bugs.\",\n",
    "    \"How do you comfort a JavaScript bug? You console it.\"\n",
    "]\n",
    "\n",
    "print(\"Hi! I'm Chatty, your enhanced chatbot.\")\n",
    "print(\"Type 'bye' to exit.\\n\")\n",
    "\n",
    "while True:\n",
    "    user_input = input(\"You: \").lower()\n",
    "\n",
    "    # Greeting\n",
    "    if user_input in ['hi', 'hello', 'hey']:\n",
    "        hour = datetime.datetime.now().hour\n",
    "        if hour < 12:\n",
    "            greeting = \"Good morning!\"\n",
    "        elif 12 <= hour < 18:\n",
    "            greeting = \"Good afternoon!\"\n",
    "        else:\n",
    "            greeting = \"Good evening!\"\n",
    "        print(f\"Chatty: {greeting} How can I assist you today?\")\n",
    "    \n",
    "    # Name\n",
    "    elif \"your name\" in user_input:\n",
    "        print(\"Chatty: I'm Chatty, your friendly chatbot.\")\n",
    "    \n",
    "    # How are you\n",
    "    elif \"how are you\" in user_input:\n",
    "        print(\"Chatty: I'm great! Just waiting to chat with you.\")\n",
    "\n",
    "    # Date or time\n",
    "    elif \"time\" in user_input or \"date\" in user_input:\n",
    "        now = datetime.datetime.now()\n",
    "        print(f\"Chatty: It's currently {now.strftime('%A, %d %B %Y at %I:%M %p')}.\")\n",
    "\n",
    "    # Tell a joke\n",
    "    elif \"joke\" in user_input:\n",
    "        print(\"Chatty: \" + random.choice(jokes))\n",
    "\n",
    "    # Help\n",
    "    elif \"help\" in user_input:\n",
    "        print(\"Chatty: I can tell jokes, show the time/date, or even solve simple math! Try typing something!\")\n",
    "\n",
    "    # Math (simple eval for arithmetic)\n",
    "    elif any(op in user_input for op in ['+', '-', '*', '/', '**']):\n",
    "        try:\n",
    "            result = eval(user_input)\n",
    "            print(f\"Chatty: The result is {result}\")\n",
    "        except:\n",
    "            print(\"Chatty: Hmm, I couldn't compute that. Please check your math expression.\")\n",
    "    \n",
    "    # Exit\n",
    "    elif \"bye\" in user_input:\n",
    "        print(\"Chatty: Goodbye! Have a great day.\")\n",
    "        break\n",
    "\n",
    "    # Unknown input\n",
    "    else:\n",
    "        print(\"Chatty: I'm not sure how to respond to that. Try asking about the time, jokes, or math.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2a55537-c7bc-4ac2-b39d-dc9ed3918545",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
