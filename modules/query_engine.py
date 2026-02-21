# modules/query_engine.py
from llama_index.query_engine import QueryEngineTool, SubQuestionQueryEngine

def get_query_engine(index):
    engine = index.as_query_engine()
    tools = [
        QueryEngineTool(
            query_engine=engine,
            metadata={
                "name": "Annual Report",
                "description": "Provides insights from company reports",
            },
        )
    ]
    s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=tools)
    return s_engine

def ask_query(engine, query):
    return engine.query(query).response
