from pydantic import BaseModel, Field


class AnswerEvaluation(BaseModel):

    score: float = Field(
        description="Score from 0 to 10."
    )

    feedback: str = Field(
        description="Constructive feedback."
    )

    strengths: list[str] = Field(
        default_factory=list
    )

    improvements: list[str] = Field(
        default_factory=list
    )

    follow_up_required: bool = Field(
        description="True if another question on this topic should be asked."
    )

    follow_up_reason: str = ""