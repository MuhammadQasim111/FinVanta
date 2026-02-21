from pydantic import BaseModel, Field

class FiscalYearHighlights(BaseModel):
    performance: str = Field(..., description="Key financial metrics")
    major_events: str = Field(..., description="Strategic or major events")
    challenges: str = Field(..., description="Key challenges faced")

def parse_insights(raw_response):
    # For simplicity, splitting by headings
    lines = raw_response.split("\n")
    insights = {
        "Fiscal Year Highlights": "\n".join(lines[:3]),
        "Strategy & Future Outlook": "\n".join(lines[3:6]),
        "Risk Management": "\n".join(lines[6:9]),
        "Innovation & R&D": "\n".join(lines[9:12])
    }
    return insights
