from app.prompts.jd_match_prompt import jd_match_prompt
from app.models.jd_analysis import JDAnalysis


def build_jd_match_chain(llm):

    structured_llm = llm.with_structured_output(
        JDAnalysis
    )

    chain = (

        jd_match_prompt

        | structured_llm

    )

    return chain