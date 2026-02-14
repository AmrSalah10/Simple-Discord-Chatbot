import requests

class QuoteService:
    def get_quote(self) -> str:
        try:
            response = requests.get("https://zenquotes.io/api/random")
            response.raise_for_status()
            data = response.json()
            return data[0]['q'] + " - " + data[0]['a']
        except Exception as e:
            print(f"Error fetching quote: {e}")
            return "I couldn't fetch a quote at the moment. Stay strong!"
