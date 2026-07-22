from pydantic import BaseModel, Field


class InterviewTopic(BaseModel):
    skill: str
    difficulty: str
    questions: int


class InterviewPlan(BaseModel):
    topics: list[InterviewTopic]