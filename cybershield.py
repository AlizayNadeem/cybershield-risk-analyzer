# CyberShield: Security Incident Risk Analyzer


def calculate_risk(impact: int, likelihood: int) -> int:
    """Calculate a risk score based on impact and likelihood."""
    if not isinstance(impact, int) or not isinstance(likelihood, int):
        raise TypeError("Impact and likelihood must be integers.")
    if not (1 <= impact <= 5 and 1 <= likelihood <= 5):
        raise ValueError("Impact and likelihood must each be between 1 and 5.")
    return impact * likelihood


def classify_risk(score: int) -> str:
    """Convert a numerical score into a risk category."""
    if score >= 20:
        return "CRITICAL"
    if score >= 12:
        return "HIGH"
    if score >= 6:
        return "MEDIUM"
    return "LOW"


def recommend_action(level: str) -> str:
    """Return the recommended response for a given risk level."""
    actions = {
        "CRITICAL": "Isolate affected systems and investigate immediately.",
        "HIGH": "Investigate urgently and apply security controls.",
        "MEDIUM": "Review the incident and strengthen protections.",
        "LOW": "Monitor the system for suspicious activity.",
    }
    return actions.get(level, "No specific action defined.")


def read_valid_int(prompt: str, minimum: int = 1, maximum: int = 5) -> int:
    """Prompt the user until a valid integer within range is entered."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a whole number between {minimum} and {maximum}.")
            continue

        if not (minimum <= value <= maximum):
            print(f"Value must be between {minimum} and {maximum}.")
            continue

        return value


def main():
    print("=" * 40)
    print(" CYBERSHIELD: INCIDENT RISK ANALYZER")
    print("=" * 40)

    incident = input("Enter incident name: ").strip()
    if not incident:
        incident = "Unnamed Incident"

    print("\nImpact: 1 (Low) to 5 (Severe)")
    impact = read_valid_int("Enter impact level: ")

    print("\nLikelihood: 1 (Rare) to 5 (Very Likely)")
    likelihood = read_valid_int("Enter likelihood level: ")

    score = calculate_risk(impact, likelihood)
    level = classify_risk(score)

    print("\n" + "-" * 40)
    print("INCIDENT REPORT")
    print("-" * 40)
    print(f"Incident: {incident}")
    print(f"Risk Score: {score} / 25")
    print(f"Risk Level: {level}")
    print(f"Recommended Action: {recommend_action(level)}")
    print("-" * 40)


if __name__ == "__main__":
    main()