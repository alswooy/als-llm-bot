from crewai import Crew, Agent, Task
from langchain_ollama import ChatOllama
from openai import OpenAI

llm = ChatOllama( # 어떠한 모델을 사용할지
    model='llama3.1',
    base_url='http://localhost:11434'   

)
# Crew : 러닝크루  => N명 (조직)
# Agnet : 요원 => 1명(조직원)
# Task : 업무(미션)

user_question = input("편하게 질문해주세요 : ")
# 쇼핑몰 (컨셉 : 무신사 서점)
# - 
shopping_agent = Agent( # 고객
    role = '의류 구매 어시던트',
    goal = '고객이 어떤 상황인지 설명을 하면 해당 상황에 맞는 우리 쇼핑몰 제품을 소개합니다.',
    backstory = '당신은 우리 쇼핑몰의 모든 의류 정보를 알고있으며, 의류을 통해 사람들의 상황에 맞는 의류를 소개하는데 전문가 입니다.',
    llm = llm
)
recommand_shop_task = Task( #수행할 요원
    # description = '고객의 상황에 맞는 최고의 추천 도서 제안하기',
    description = user_question,
    expected_output = '고객의 상황에 맞는 5개의 의류를 추천해주고, 해당 의류를 추천한 이유를 알려줘(한국어로 말해줘)',
    agent = shopping_agent,
    output_file='recommand_shop_task.md'
)
review_agent = Agent( # 고객
    role = '의류 리뷰 어시스턴트', #어떤걸 수행할지
    goal = '추천받은 의류들의 쇼핑몰에 대한 리뷰를 제공하고, 해당 의류에 대한 심도있는 평가를 제공합니다.', # 어떠한 행동을 해야하는지
    backstory = '당신은 우리 쇼핑몰의 모든 의류 정보를 알고 있으며, 추천받은 의류에 대한 전문가 수준의 리뷰를 제공합니다.', #두개를 합쳐서 어떠한 말을 해야할지
    llm = llm
)
review_task= Task( #수행할 요원
    # description = '고객의 상황에 맞는 최고의 추천 도서 제안하기',
    description = '고객이 선택한 의류에 대한 리뷰를 제공합니다',
    expected_output = '고객이 선택한 의류에 대한 리뷰를 제공합니다.(한국어로 말해줘))',
    agent = shopping_agent
)


#요원과 미션을 관리
crew = Crew(
    agents = [shopping_agent, review_agent],
    tasks = [recommand_shop_task],
    verbose = True
)

result = crew.kickoff()

print(result)

# RAG : 확장하는 기능 => PDF, DB 