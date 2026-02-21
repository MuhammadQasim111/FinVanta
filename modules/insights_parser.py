# modules/insights_parser.py
from pydantic import BaseModel, Field
from llama_index import QueryEngine

# Define structured insight classes
class FiscalYearHighlights(BaseModel):
    performance_highlights: str = Field(..., description="Key metrics over the fiscal year.")
    major_events: str = Field(..., description="Significant events, acquisitions, or strategic shifts.")
    challenges_encountered: str = Field(..., description="Challenges the company faced.")

class StrategyOutlookFutureDirection(BaseModel):
    strategic_initiatives: str = Field(..., description="Company's growth strategies.")
    market_outlook: str = Field(..., description="Insights on market and competition.")

class RiskManagement(BaseModel):
    risk_factors: str = Field(..., description="Primary risks acknowledged by company.")
    risk_mitigation: str = Field(..., description="Strategies for managing these risks.")

class InnovationRnD(BaseModel):
    r_and_d_activities: str = Field(..., description="Overview of R&D focus.")
    innovation_focus: str = Field(..., description="New technologies or patents.")

# Function to parse insights
def parse_insights(engine: QueryEngine, section: str, pydantic_model: BaseModel):
    from langchain.prompts import PromptTemplate
    from langchain.output_parsers import PydanticOutputParser

    parser = PydanticOutputParser(pydantic_object=pydantic_model)

    prompt_template = """
    You are tasked with generating insights for {section} from the company's annual report.

    Output format:
    {output_format}

    Use bullet points. Use $ for money values. If info is missing, write: 'No information available.'
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["section"],
        partial_variables={"output_format": parser.get_format_instructions()}
    )

    formatted_input = prompt.format(section=section)
    response = engine.query(formatted_input)
    return parser.parse(response.response)
