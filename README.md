# Voice Assistant Program

## __Overview__
This program is a voice-based assistant that can perform a variety of tasks such as searching Wikipedia, opening websites, and telling the current time. It utilizes Python libraries like `pyttsx3` for text-to-speech functionality, `speech_recognition` for speech-to-text conversion, and `wikipedia` for searching Wikipedia. The assistant responds to voice commands and executes actions accordingly.

## __Features__
- **Voice Interaction:** The program listens for voice commands and responds using text-to-speech (TTS).
- **Greeting Based on Time:** The assistant greets the user based on the time of day (morning, afternoon, evening).
- **Wikipedia Search:** You can ask the assistant to search Wikipedia and get a brief summary of the topic.
- **Website Navigation:** Commands like "open YouTube", "open Google", or "open Instagram" will launch the respective websites in a web browser.
- **Time Information:** The assistant can tell you the current time when asked.
- **Continuous Listening:** The program continuously listens for commands and performs the corresponding action until the user says "quit".

## __Technologies Used__
- `pyttsx3`: For text-to-speech conversion.
- `speech_recognition`: For converting speech to text.
- `wikipedia`: For fetching data from Wikipedia.
- `webbrowser`: For opening websites in the default web browser.
- `datetime`: To fetch the current time and greet the user accordingly.

## __How to Use__
1. Run the program.
2. The assistant will greet you based on the time of day.
3. Speak commands like:
   - `"Search Wikipedia for [topic]"`
   - `"Open YouTube"`
   - `"What is the time?"`
4. The assistant will perform the task and speak the results.
5. To exit, simply say `"quit"`.

