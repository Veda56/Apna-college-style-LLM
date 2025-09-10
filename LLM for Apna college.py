from google import genai

client = genai.Client(api_key="AIzaSyCuBG5nUJYysIc_v-3gH372JRDHiXZYn64")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="what is apna college"
)
print(response.text)
exmples = """
The Apna College YouTube channel is a popular Indian educational platform led by Shradha Khapra, a former Microsoft software engineer and DRDO intern. The channel focuses on coding tutorials, placement preparation, and career guidance,
aiming to make tech education accessible to students across India.
Apna College provides high-quality online education for students across India, focusing on programming, web development, and data structures.

The channel is led by Shradha Khapra, who combines professional experience with practical teaching to make learning easy and engaging.

Apna College offers comprehensive courses for placement preparation, including mock interviews, aptitude tests, and resume guidance.

Its tutorials cover popular programming languages such as Python, Java, and C++, along with frameworks like ReactJS and Node.js.

The platform aims to bridge the gap between college education and real-world technical skills needed in the IT industry.

Apna College videos are designed to be beginner-friendly, yet deep enough to prepare students for competitive coding and technical interviews.

The channel has grown rapidly, reaching millions of students, and focuses on practical knowledge rather than just theory.

Students can access free tutorials on YouTube and also enroll in structured courses like Delta 3.0 and Sigma 9.0 for in-depth learning.

Apna College encourages self-paced learning, enabling students to learn coding, web development, and placement skills anytime, anywhere.

With a combination of coding examples, real-life scenarios, and career tips, Apna College has become a trusted resource for tech aspirants in India.
You are a helpful and knowledgeable chatbot. Answer user questions clearly and accurately. 
User: What's the capital of France?
Bot: The capital of France is Paris.

User: How many continents are there?
Bot: There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia.

Now continue the conversation:
"""