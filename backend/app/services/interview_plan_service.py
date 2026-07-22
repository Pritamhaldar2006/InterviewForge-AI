from app.config.llm import get_llm

from app.services.analysis_services import (
    compare_resume_and_jd,
)

from app.chains.interview_plan_chain import (
    build_interview_plan_chain,
)


def generate_interview_plan():

    analysis = compare_resume_and_jd()

    llm = get_llm()

    chain = build_interview_plan_chain(llm)

    plan = chain.invoke(
        {
            "matching_skills": analysis.matching_skills,
            "missing_skills": analysis.missing_skills,
            "strengths": analysis.strengths,
            "weaknesses": analysis.weaknesses,
            "summary": analysis.summary,
        }
    )

    return plan