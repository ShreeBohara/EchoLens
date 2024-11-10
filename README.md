## Inspiration
Our core inspiration stemmed from the desire to make the web more inclusive, especially for visually impaired users, and to provide a solution that could enhance their browsing experience.

## What it does
Screen readers typically overlook images when navigating for visually impaired users. Our extension analyzes these images and provides a voiceover description to ensure accessibility.

## How we built it
Our solution is a Chrome extension designed to make images on websites more accessible to people who are visually impaired. When a user clicks on an image (such as a chart or graph) on any web page, our extension captures the image’s source using JavaScript and sends it to a backend Flask server. This server uses the Llama 3.2 Vision model to analyze the image, generating a detailed summary describing the image’s type, labels, and key content in a way that a person can understand without seeing it.

This text summary is then converted into audio using Google Text-to-Speech (gTTS), creating an MP3 file of the description. The Flask server sends this audio back to the extension, where JavaScript triggers playback, allowing the user to hear the description directly. To improve the experience, the extension highlights the selected image with a custom border and provides audio feedback, helping them confirm their selection. The user can also pause the audio playback by pressing the Escape or Space key, and the selection styling will be removed.

## Challenges we ran into
* **Brainstorming and Research:** Identifying pain points for differently-abled users on websites and applications, required gathering insights from diverse user groups to address a wide range of accessibility needs
* **Choosing the Right Model:** Selecting the appropriate image-to-text model for our use case was difficult, as we had to consider factors like time complexity, CPU requirements, and cost.
*  **Crafting the Right Prompt:**
Crafting an accurate prompt – This was a testing part of the process, because getting precise results from the model is a cornerstone of the project

## Accomplishments that we're proud of
* We decided to focus on a single disability—visual impairment—and identified pain points for visually impaired users by testing with various screen readers
* We implemented models from scratch, tested various available open-source models, and chose the most apt ones:
    * Image-to-Text: GPT-2, Molmo, Hugging Face (Microsoft Tesseract OCR, Donut, BLIP, CLIP), Groq (Llama-3.2-11b-vision-preview, Llama-3.2-90b-vision-preview)
    * Text-to-Speech: pyttsx3, gTTS
* Crafting an accurate prompt – We formulated a prompt for the model in such a way that it would give correct results, including but not limited to the chart type, axes, scales, and chart description. We refined and tested multiple prompts and fine-tuned the model further by adjusting temperature and maximum token value parameters
* Grammatically improving Speech Response – We worked to enhance the model's speech response by adjusting parameters such as speaking rate and volume, ensuring the response sounded as natural as possible, with precise punctuation delivery

## What we learned
*We realized the importance of making digital media more accessible for differently-abled individuals, helping them gain independence and feel included
* We discovered multiple open-source websites, repositories, and APIs which enhanced our technical skills
 * Time Management played a crucial aspect as we had 24 hours and Collaboration helped us deliver our idea

## What's next for Untitled
* **Integrating EchoLens with Assistive Technologies:** Seamlessly incorporating EchoLens with screen readers, voice assistants, and other assistive technologies.
* **Ensuring Compatibility for Total Vision Loss:** Adapting EchoLens to be fully accessible for individuals with total vision loss.
* **Expanding Platform Compatibility:** Extending EchoLens compatibility to all devices for broader accessibility.
* **Multi-Language Support for EchoLens:** Enabling EchoLens to support multiple languages, ensuring inclusivity for diverse users.
