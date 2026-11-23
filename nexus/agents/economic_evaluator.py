"""Economic Evaluator: report gaps; do not fabricate estimates."""
def evaluate(ideas):
    return [{**idea, "known_costs": [], "unknown_costs": ["development", "distribution", "support", "fees"],
             "verified_revenue": None, "willingness_to_pay": "unknown", "profitability_status": "not_established",
             "required_validation": ["identify reachable buyers", "test willingness to pay",
                                     "price delivery and support", "compare existing alternatives"]}
            for idea in ideas]
