"""Idea Generator: output hypotheses, never market facts."""
def generate(patterns):
    return [{"problem_key": p["problem_key"],
             "solution_hypothesis": "Design a small service or tool that reduces this documented friction.",
             "evidence_class": "hypothesis", "customer_demand_proven": False,
             "next_validation": "Interview affected people and seek independent evidence of alternatives and payment."}
            for p in patterns]
