from pydantic import BaseModel, Field


class JDAnalysis(BaseModel):

    matching_skills: list[str] = Field(
        description="Skills that match the job description."
    )

    missing_skills: list[str] = Field(
        description="Skills missing from the resume."
    )

    strengths: list[str] = Field(
        description="Candidate strengths."
    )

    weaknesses: list[str] = Field(
        description="Candidate weaknesses."
    )

    summary: str = Field(
        description="Overall evaluation."
    )