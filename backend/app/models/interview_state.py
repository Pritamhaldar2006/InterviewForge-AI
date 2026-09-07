from enum import Enum

from pydantic import BaseModel, Field

from app.models.jd_analysis import JDAnalysis
from app.models.interview_plan import InterviewPlan


class Difficulty(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class QuestionAnswer(BaseModel):
    skill: str
    subtopic: str

    difficulty: str

    question: str
    answer: str = ""

    score: float = 0.0
    feedback: str = ""

    strengths: list[str] = Field(default_factory=list)
    improvements: list[str] = Field(default_factory=list)

    follow_up: bool = False


class InterviewState(BaseModel):
    analysis: JDAnalysis
    plan: InterviewPlan

    current_topic: int = 0
    current_question: int = 0

    current_difficulty: str = "Beginner"

    follow_up_count: int = 0
    max_follow_ups: int = 2

    history: list[QuestionAnswer] = Field(default_factory=list)

    weak_topics: list[str] = Field(default_factory=list)
    strong_topics: list[str] = Field(default_factory=list)

    interview_completed: bool = False