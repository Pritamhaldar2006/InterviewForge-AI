from pydantic import BaseModel


class AnswerRequest(BaseModel):
    answer: str


class QuestionResponse(BaseModel):
    question: str


class ReportResponse(BaseModel):
    report: dict