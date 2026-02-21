from llama_index.query_engine import SubQuestionQueryEngine, QueryEngineTool
from llama_index.query_engine.tool_metadata import ToolMetadata

def get_query_engine(index):
    engine = index.as_query_engine()
    query_tool = QueryEngineTool(
        query_engine=engine,
        metadata=ToolMetadata(
            name="FinancialReport",
            description="Provides insights from uploaded financial documents."
        )
    )
    s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=[query_tool])
    return s_engine

def ask_query(engine, query_text):
    response = engine.query(query_text)
    return response.response
