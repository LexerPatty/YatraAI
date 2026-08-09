import asyncio

from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights 

# from mcp_client_test import get_all_tools, tavily_mcp_search
import asyncio

from mcp_client import get_all_tools


from tools.custom_weather_mcp_server import (
    get_current_weather,
    get_forecast,
)


## TAVILY TEST...................................................

# res = tavily_search("Best Hotel in india")
# print(res)

## AVIATIONSTACK TEST....................................................

# res = search_flights("Plan a 4 days Varanasi trip from Kolkata")
# print(res)


## CHECK WEATHER TOOLS.............................................

# city = "Kolkata"
# weather = get_current_weather(city)
# print(weather)
# x
# forecast = get_forecast(city)
# print(forecast)



if __name__ == "__main__":
    asyncio.run(get_all_tools())

    # query = "latest news about AI"
    # result = asyncio.run(tavily_mcp_search(query))