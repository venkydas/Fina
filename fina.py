from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name='web_search_agent',
    role='search the web for information',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True

)

fina = Agent(
    name='financial_analyst',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, fina],
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    instructions=["Use the web search agent to find information and the financial analyst to analyze the data."],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize the stock price, analyst recommendations, and stock fundamentals for Apple Inc. (AAPL).")