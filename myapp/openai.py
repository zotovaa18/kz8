import openai
import json
api_key = "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"

def where_to_go(preferences):
    openai.api_key = api_key
    #answer = openai.ChatCompletion.create(
    #    model="gpt-3.5-turbo",
    #    messages=[
     #       {"role": "user", "content": f"{preferences} Where should I go?"}
     #   ]
   # )
   # print(answer.values())
    #answer_json = json.loads(answer.values())
    #answer_text = answer.answer.get('choices')[0].get('message').get('content')
    answer_text = "\n\nBased on your preferences, I would suggest the following destinations:\n\n1. Spain - Spain is an excellent destination for an active trip with its stunning cities like Barcelona, Madrid, Valencia and Seville. This country offers plenty of outdoor activities like hiking and cycling. Spain is known for its warm weather and vibrant culture.\n\n2. Italy - Another great option is Italy. The country is known for its art, cuisine, and rich history. The cities like Rome, Florence, Milan, and Venice have so much to offer such as museums, galleries, landmarks, and piazzas. Italy is known for its mild climate, and during the summertime, you can enjoy the crystal-clear waters of its coasts.\n\n3. Portugal - If you prefer to avoid crowds, Portugal is a great option. The country has many undiscovered villages, picturesque castles, amazing views, and charming cities like Lisbon and Porto. You can further enjoy the country's warm climate and untouched beaches.\n\n4. Croatia - Croatia has made a name for itself over the past few years due to its turquoise waters, historic landmarks, and relaxed vibe. Cities like Split, Dubrovnik, and Zagreb, offer local gourmet cuisine, cultural history, and views on the Adriatic coast.\n\n5. Greece - Greece has been a classic choice from time immemorial. You can tour Athens, the birthplace of democracy, or relax on one of the many islands. Greece has plenty of sunbathing activities, stunning villages, and ancient history to explore."
    print(answer_text)
    return answer_text
