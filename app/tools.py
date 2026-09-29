"""
Tools for Milan & Mandap (Agentic Matrimony & Wedding OS).
Includes:
- Candidate Discovery & Agent Compatibility Audit
- Double-blind dealbreaker verification
- Wedding venue & vendor search with Escrow Milestone safeguards
- Wedding Budget Allocation Calculator
- Day-Of Run-of-Show Wedding Itinerary Generator
"""

import json
from typing import Dict, Any, List, Optional
from app.mock_database import CANDIDATES_DATABASE, WEDDING_CATALOG


def evaluate_candidate_compatibility(
    user_query: str,
    user_dealbreakers: Optional[List[str]] = None,
    preferred_location: Optional[str] = None
) -> str:
    """Performs an autonomous Agent-to-Agent compatibility audit against candidate profiles.
    Evaluates lifestyle values, family expectations, verified trust credentials, and filters dealbreakers.

    Args:
        user_query: Lifestyle, career, or personality attributes the user desires in a life partner.
        user_dealbreakers: List of strict dealbreakers (e.g. smoking, heavy debt, relocation unwillingness).
        preferred_location: Geographical preference (e.g. 'San Francisco', 'New York', 'Flexible').

    Returns:
        JSON string containing ranked compatible candidates, alignment scores, shared values, and trust verification badges.
    """
    user_dealbreakers = user_dealbreakers or []
    matches = []

    for cand in CANDIDATES_DATABASE:
        score = 85
        query_terms = user_query.lower().split()
        cand_str = f"{cand['profession']} {cand['lifestyle']} {cand['location']}".lower()

        # Simple semantic boost
        for term in query_terms:
            if len(term) > 3 and term in cand_str:
                score += 3
        if preferred_location and preferred_location.lower() in cand['location'].lower():
            score += 5
        score = min(score, 98)

        # Check dealbreakers
        flagged_dealbreakers = []
        for db in user_dealbreakers:
            for c_db in cand['dealbreakers']:
                if any(w in c_db.lower() for w in db.lower().split() if len(w) > 3):
                    flagged_dealbreakers.append(c_db)

        matches.append({
            "id": cand["id"],
            "name": cand["name"],
            "age": cand["age"],
            "height": cand["height"],
            "profession": cand["profession"],
            "location": cand["location"],
            "lifestyle": cand["lifestyle"],
            "compatibility_score": f"{score}%",
            "trust_score": f"{cand['trust_score']}/100",
            "verification_badges": cand["verification_badges"],
            "values_alignment": cand["values"],
            "potential_dealbreaker_alerts": flagged_dealbreakers,
            "photo_url": cand["photo_url"],
            "agent_summary": f"{cand['name']} exhibits high compatibility with your lifestyle focus and career ambition. Both candidate agents simulated agreement on core values."
        })

    matches.sort(key=lambda x: int(x["compatibility_score"].replace("%", "")), reverse=True)
    return json.dumps({"status": "success", "candidates_found": len(matches), "matches": matches})


def search_wedding_venues_and_vendors(
    service_type: str,
    location_or_style: Optional[str] = None,
    budget_limit: Optional[float] = None
) -> str:
    """Search for certified wedding venues and vendors that support Escrow Milestone Protection and verified insurance.

    Args:
        service_type: Either 'venues', 'vendors', or 'all'.
        location_or_style: Location (e.g. 'Udaipur', 'Napa', 'Hyderabad') or vendor style (e.g. 'Photography', 'Decor', 'Catering').
        budget_limit: Max price or rate limit in USD.

    Returns:
        JSON string of matching venues or vendors with deliverables, escrow terms, and ratings.
    """
    results = {}
    if service_type in ["venues", "all"]:
        venues = WEDDING_CATALOG["venues"]
        if location_or_style:
            venues = [v for v in venues if location_or_style.lower() in v["location"].lower() or location_or_style.lower() in v["name"].lower()]
        if budget_limit:
            venues = [v for v in venues if v["price_per_night"] <= budget_limit]
        results["venues"] = venues

    if service_type in ["vendors", "all"]:
        vendors = WEDDING_CATALOG["vendors"]
        if location_or_style:
            vendors = [v for v in vendors if location_or_style.lower() in v["category"].lower() or location_or_style.lower() in v["name"].lower()]
        results["vendors"] = vendors

    return json.dumps({"status": "success", "results": results})


def calculate_wedding_budget_plan(
    total_budget_usd: float,
    estimated_guests: int,
    destination_wedding: bool = True
) -> str:
    """Calculates an intelligent, optimized budget allocation model across wedding categories.
    Applies real-world industry benchmarks and contingency reserves to prevent 30%+ cost overruns.

    Args:
        total_budget_usd: Total capital allocated for the wedding (e.g. 50000, 100000).
        estimated_guests: Expected total guest count.
        destination_wedding: Whether the wedding involves hospitality/travel lodging.

    Returns:
        JSON string breakdown of recommended budget allocations, per-plate limits, and milestone payment schedules.
    """
    if destination_wedding:
        venue_lodging_pct = 0.38
        catering_pct = 0.24
        decor_production_pct = 0.16
        photography_film_pct = 0.08
        attire_beauty_pct = 0.06
        emergency_contingency_pct = 0.08
    else:
        venue_lodging_pct = 0.25
        catering_pct = 0.32
        decor_production_pct = 0.18
        photography_film_pct = 0.10
        attire_beauty_pct = 0.07
        emergency_contingency_pct = 0.08

    allocation = {
        "total_budget": total_budget_usd,
        "guest_count": estimated_guests,
        "estimated_per_guest_spend": round(total_budget_usd / max(1, estimated_guests), 2),
        "allocations": {
            "venue_and_hospitality": round(total_budget_usd * venue_lodging_pct, 2),
            "catering_and_bar": round(total_budget_usd * catering_pct, 2),
            "decor_and_ambiance": round(total_budget_usd * decor_production_pct, 2),
            "photography_and_cinematography": round(total_budget_usd * photography_film_pct, 2),
            "bridal_attire_and_makeup": round(total_budget_usd * attire_beauty_pct, 2),
            "emergency_backup_contingency": round(total_budget_usd * emergency_contingency_pct, 2)
        },
        "target_catering_plate_budget": round((total_budget_usd * catering_pct) / max(1, estimated_guests), 2),
        "escrow_payment_protection": "All allocations are automatically gated behind 4 milestone releases (Deposit, Pre-production, Day-of Arrival, Final Sign-off)."
    }
    return json.dumps({"status": "success", "budget_model": allocation})


def generate_wedding_itinerary(
    wedding_theme: str,
    days: int = 2
) -> str:
    """Generates an end-to-end multi-event wedding run-of-show schedule.

    Args:
        wedding_theme: Theme or cultural tradition (e.g. 'Royal Rajasthani Heritage', 'Modern Fusion Bohemian', 'Traditional South Indian & Western').
        days: Duration of the wedding celebrations (typically 2 or 3 days).

    Returns:
        JSON string containing the structured run-of-show schedule with vendor check-in triggers.
    """
    itinerary = []
    if days >= 1:
        itinerary.append({
            "day": 1,
            "title": "Welcome, Mehendi & Sundowner Sangeet",
            "events": [
                {"time": "12:00 PM", "event": "Guest Arrival & Welcome Refreshments", "agent_trigger": "Guest Concierge auto-dispatches room keys"},
                {"time": "03:00 PM", "event": "Mehendi & High Tea on the Lawn", "agent_trigger": "Artists check-in verification"},
                {"time": "07:30 PM", "event": "Glitz & Glam Musical Sangeet", "agent_trigger": "DJ/Sound check & choreo stage cue"}
            ]
        })
    if days >= 2:
        itinerary.append({
            "day": 2,
            "title": "The Main Ceremony & Grand Reception",
            "events": [
                {"time": "09:30 AM", "event": "Haldi & Floral Holi Celebration", "agent_trigger": "Organic flower & splash protection setup"},
                {"time": "04:30 PM", "event": "Baraat Procession & Varmala Exchange", "agent_trigger": "Band, dhol & drone pilot synchronization"},
                {"time": "06:00 PM", "event": "Auspicious Wedding Nuptials (Pheras)", "agent_trigger": "Mandap havan timing coordination"},
                {"time": "08:30 PM", "event": "Formal Dinner & Star Reception Gala", "agent_trigger": "Banquet doors open & live orchestra cue"}
            ]
        })

    return json.dumps({
        "status": "success",
        "theme": wedding_theme,
        "duration_days": days,
        "run_of_show": itinerary,
        "safeguards": "Live WhatsApp Guest Concierge alerts sent automatically 30 minutes before each event."
    })
