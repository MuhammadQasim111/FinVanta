# modules/query_engine.py
from llama_index import QueryEngineTool, SubQuestionQueryEngine

def get_query_engine(index):
    engine = index.as_query_engine()
    query_engine_tools = [
        QueryEngineTool(
            query_engine=engine,
            metadata={
                "name": "Annual Report",
                "description": "Provides insights from company reports",
            },
        )
    ]
    s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=query_engine_tools)
    return s_engine

def ask_query(engine, query):
    return engine.query(query).response
