import asyncio

from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights 

from mcp_client_test import get_all_tools, tavily_mcp_search
import asyncio

# res = tavily_search("Best Hotel in india")
# print(res)


# res = search_flights("Plan a 4 days Varanasi trip from Kolkata")
# print(res)


if __name__ == "__main__":
    # asyncio.run(get_all_tools())

    query = "latest news about AI"
    result = asyncio.run(tavily_mcp_search(query))