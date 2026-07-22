from pydantic import BaseModel, Field

from app.models.jd_analysis import JDAnalysis
from app.models.interview_plan import InterviewPlan


class QuestionAnswer(BaseModel):
    question: str
    answer: str = ""
    score: float = 0
    feedback: str = ""


class InterviewState(BaseModel):

    analysis: JDAnalysis

    plan: InterviewPlan

    current_topic: int = 0

    current_question: int = 0

    history: list[QuestionAnswer] = Field(default_factory=list)

    weak_topics: list[str] = Field(default_factory=list)

    strong_topics: list[str] = Field(default_factory=list)

    interview_completed: bool = False