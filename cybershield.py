# CyberShield: Security Incident Risk Analyzer

def calculate_risk(impact, likelihood):
    return impact * likelihood


def classify_risk(score):
    if score >= 20:
        return "CRITICAL"
    elif score >= 12:
        return "HIGH"
    elif score >= 6:
        return "MEDIUM"
    else:
        return "LOW"


def recommend_action(level):
    actions = {
        "CRITICAL": "Isolate affected systems and investigate immediately.",
        "HIGH": "Investigate urgently and apply security controls.",
        "MEDIUM": "Review the incident and strengthen protections.",
        "LOW": "Monitor the system for suspicious activity."
    }
    return actions[level]


def main():
    print("=" * 40)
    print(" CYBERSHIELD: INCIDENT RISK ANALYZER")
    print("=" * 40)

    incident = input("Enter incident name: ")

    print("\nImpact: 1 (Low) to 5 (Severe)")
    impact = int(input("Enter impact level: "))

    print("\nLikelihood: 1 (Rare) to 5 (Very Likely)")
    likelihood = int(input("Enter likelihood level: "))

    if not (1 <= impact <= 5 and 1 <= likelihood <= 5):
        print("Invalid input! Values must be between 1 and 5.")
        return

    score = calculate_risk(impact, likelihood)
    level = classify_risk(score)

    print("\n" + "-" * 40)
    print("INCIDENT REPORT")
    print("-" * 40)
    print("Incident:", incident)
    print("Risk Score:", score, "/ 25")
    print("Risk Level:", level)
    print("Recommended Action:", recommend_action(level))
    print("-" * 40)


if __name__ == "__main__":
    main()