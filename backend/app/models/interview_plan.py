from pydantic import BaseModel, Field


class InterviewSubTopic(BaseModel):
    name: str
    difficulty: str


class InterviewTopic(BaseModel):
    skill: str

    subtopics: list[InterviewSubTopic] = Field(default_factory=list)


class InterviewPlan(BaseModel):
    topics: list[InterviewTopic] = Field(default_factory=list)