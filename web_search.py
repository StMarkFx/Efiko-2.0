from duckduckgo_search import DDGS
from typing import List, Optional

class WebSearchTool:
    def __init__(self, max_results: int = 3):
        self.max_results = max_results
        self.ddgs = DDGS()

    def search(self, query: str) -> List[dict]:
        """
        Perform a web search using DuckDuckGo
        
        Args:
            query (str): Search query
            
        Returns:
            List[dict]: List of search results with 'title', 'link', and 'snippet' keys
        """
        try:
            results = list(self.ddgs.text(query, max_results=self.max_results))
            formatted_results = [
                {
                    'title': result['title'],
                    'link': result['link'],
                    'snippet': result['body']
                }
                for result in results
            ]
            return formatted_results
        except Exception as e:
            print(f"Search error: {str(e)}")
            return []
