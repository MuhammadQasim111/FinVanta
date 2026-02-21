# modules/query_engine.py
from llama_index.core.tools import QueryEngineTool, ToolMetadata  # âœ… correct paths
from llama_index.core.query_engine import SubQuestionQueryEngine


def get_query_engine(index):
    engine = index.as_query_engine()

    tools = [
        QueryEngineTool(
            query_engine=engine,
            metadata=ToolMetadata(  # âœ… must use ToolMetadata object, not a plain dict
                name="Annual_Report",  # no spaces allowed in tool names
                description="Provides insights from company annual reports",
            ),
        )
    ]

    s_engine = SubQuestionQueryEngine.from_defaults(query_engine_tools=tools)
    return s_engine


def ask_query(engine, query):
    response = engine.query(query)
    return response.response
