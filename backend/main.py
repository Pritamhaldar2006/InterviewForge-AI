from app.services.interview_service import start_interview


def main():

    analysis = start_interview()

    print("\n========== MATCHING SKILLS ==========")
    print(analysis.matching_skills)

    print("\n========== MISSING SKILLS ==========")
    print(analysis.missing_skills)

    print("\n========== STRENGTHS ==========")
    print(analysis.strengths)

    print("\n========== WEAKNESSES ==========")
    print(analysis.weaknesses)

    print("\n========== SUMMARY ==========")
    print(analysis.summary)


if __name__ == "__main__":
    main()