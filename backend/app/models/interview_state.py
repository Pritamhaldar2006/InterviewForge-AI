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

    # Current interview position
    current_topic: int = 0

    current_subtopic: int = 0

    # Adaptive difficulty
    current_difficulty: Difficulty = Difficulty.INTERMEDIATE

    # Follow-up handling
    follow_up_count: int = 0

    max_follow_ups: int = 2

    # Interview history
    history: list[QuestionAnswer] = Field(default_factory=list)

    # Performance tracking
    weak_topics: list[str] = Field(default_factory=list)

    strong_topics: list[str] = Field(default_factory=list)

    completed_topics: list[str] = Field(default_factory=list)

    # Interview status
    interview_completed: bool = False