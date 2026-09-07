from pydantic import BaseModel, Field


class InterviewReport(BaseModel):
    overall_score: float

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    summary: str

    recommendation: str

    hiring_decision: str