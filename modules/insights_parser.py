# modules/insights_parser.py
from typing import Type
from pydantic import BaseModel, Field
from llama_index.core.query_engine import BaseQueryEngine  # ✅ correct base class
from langchain_core.prompts import PromptTemplate           # ✅ updated path
from langchain_core.output_parsers import PydanticOutputParser  # ✅ updated path


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


def parse_insights(engine: BaseQueryEngine, section: str, pydantic_model: Type[BaseModel]):
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
