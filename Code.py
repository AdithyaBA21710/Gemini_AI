from google import genai

client = genai.Client(api_key="AIzaSyCi2wtoHEej5bBHYH34pi9MyTrjHWyQMcc")

text="Akasa Air, on Friday, announced its partnership with Adani Airport Holdings Limited (AAHL), and is set to begin commercial flight operations from the upcoming Navi Mumbai International Airport (NMIA). This decision follows a week after IndiGo’s announcement to launch flights from NMIA."

response = client.models.generate_content(model="gemini-2.0-flash",contents="Improve this passage, give me just one answer: "+text,)

print(response.text)
