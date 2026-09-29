"""
Mock database for Milan & Mandap (Agentic Matrimony & Wedding OS).
Contains rich profiles, verified trust credentials, dealbreaker parameters,
and wedding catalog (venues, caterers, photographers, decor packages).
"""

CANDIDATES_DATABASE = [
    {
        "id": "cand_001",
        "name": "Dr. Ananya Sharma",
        "age": 28,
        "height": "5'7\"",
        "profession": "Pediatric Surgeon at Premier University Hospital",
        "location": "San Francisco, CA (willing to relocate to NYC/Boston)",
        "lifestyle": "Vegetarian, marathon runner, loves weekend pottery, values intellectual curiosity",
        "values": {
            "family_involvement": "High - values weekly family dinners and festival gatherings",
            "finances": "Balanced saver/investor, zero consumer debt, values philanthropy",
            "relocation": "Flexible for major metro healthcare hubs",
            "conflict_style": "Calm, analytical, prefers cooling-off period before debrief"
        },
        "dealbreakers": [
            "Smoking/tobacco use",
            "Unwillingness to share equal parenting responsibilities",
            "High gambling or undisciplined debt"
        ],
        "family_preferences": {
            "community": "Open-minded North/Pan-Indian cultural roots",
            "horoscope_importance": "Moderate/Family preference",
            "diet": "Vegetarian or flexitarian preferred"
        },
        "trust_score": 98,
        "verification_badges": ["Workplace Verified (MD)", "Government KYC Verified", "AI Liveness Video Verified"],
        "photo_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500"
    },
    {
        "id": "cand_002",
        "name": "Rohan Mehta",
        "age": 30,
        "height": "5'11\"",
        "profession": "AI Research Scientist & Tech Co-founder",
        "location": "New York, NY",
        "lifestyle": "Eggetarian, jazz enthusiast, avid hiker, passionate about sustainable tech",
        "values": {
            "family_involvement": "Moderate - deeply respects parents, maintains healthy boundaries",
            "finances": "Aggressive equity investor, frugal daily lifestyle, loves experiential travel",
            "relocation": "East Coast or remote-friendly hubs",
            "conflict_style": "Direct, transparent, solution-focused with open communication"
        },
        "dealbreakers": [
            "Dishonesty or lack of transparency",
            "Disrespect towards independent career pursuits",
            "Strict non-negotiable horoscope dependence"
        ],
        "family_preferences": {
            "community": "Progressive Pan-Indian",
            "horoscope_importance": "Low / Optional",
            "diet": "Vegetarian / Eggetarian"
        },
        "trust_score": 96,
        "verification_badges": ["Workplace Verified", "Govt ID Verified", "LinkedIn Verified"],
        "photo_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500"
    },
    {
        "id": "cand_003",
        "name": "Pooja Varma",
        "age": 29,
        "height": "5'5\"",
        "profession": "Senior Environmental Architect",
        "location": "Austin, TX (Remote)",
        "lifestyle": "Vegan, animal rescue volunteer, classical dancer (Bharatanatyam), minimalist",
        "values": {
            "family_involvement": "High - close-knit family bond, warm and welcoming",
            "finances": "Sustainable living, budget conscious, values home equity",
            "relocation": "Open to Western and Southern US",
            "conflict_style": "Empathetic listener, seeks harmony and mutual understanding"
        },
        "dealbreakers": [
            "Cruelty to animals / anti-pets",
            "Heavy alcohol or substance abuse",
            "Controlling or non-collaborative partnership mindset"
        ],
        "family_preferences": {
            "community": "South/West Indian progressive roots",
            "horoscope_importance": "Moderate",
            "diet": "Strict Vegetarian / Vegan"
        },
        "trust_score": 99,
        "verification_badges": ["Workplace Verified", "KYC Liveness Verified", "Credit Tier Verified (780+)"],
        "photo_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500"
    }
]

WEDDING_CATALOG = {
    "venues": [
        {
            "id": "ven_01",
            "name": "The Oberoi Udaivilas Heritage Palace",
            "location": "Udaipur, Rajasthan",
            "capacity": "200 - 450 guests",
            "price_per_night": 25000,
            "currency": "USD",
            "inclusions": ["Lake view courtyards", "Grand ballroom", "Bridal suites", "24/7 Butler"],
            "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=500",
            "escrow_supported": True,
            "rating": 4.9
        },
        {
            "id": "ven_02",
            "name": "Napa Valley Vista Vineyards Estate",
            "location": "St. Helena, Napa Valley, CA",
            "capacity": "100 - 250 guests",
            "price_per_night": 18000,
            "currency": "USD",
            "inclusions": ["Outdoor vineyard lawn", "Barrel room reception", "Sommelier service"],
            "image_url": "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?w=500",
            "escrow_supported": True,
            "rating": 4.8
        },
        {
            "id": "ven_03",
            "name": "Taj Falaknuma Palace",
            "location": "Hyderabad, Telangana",
            "capacity": "150 - 350 guests",
            "price_per_night": 22000,
            "currency": "USD",
            "inclusions": ["101-seat dining hall", "Royal horse-drawn carriage", "Palace gardens"],
            "image_url": "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=500",
            "escrow_supported": True,
            "rating": 4.95
        }
    ],
    "vendors": [
        {
            "id": "v_photo_01",
            "name": "House On The Clouds (Cinematic Photography & Film)",
            "category": "Photography & Cinema",
            "base_rate": 6500,
            "currency": "USD",
            "deliverables": ["3-day coverage", "2 cinematic teasers", "Full wedding documentary", "AI facial photo distribution"],
            "rating": 5.0,
            "escrow_milestones": ["20% Booking", "50% On-Event", "30% Upon Raw Deliverables Delivery"]
        },
        {
            "id": "v_decor_01",
            "name": "Altair Floral & Scenography Design",
            "category": "Decor & Ambiance",
            "base_rate": 14000,
            "currency": "USD",
            "deliverables": ["Bespoke floral Mandap", "Sangeet LED stage", "Mehendi bohemian setup", "Sustainable materials"],
            "rating": 4.9,
            "escrow_milestones": ["30% Booking", "50% Day-Before Setup", "20% Post-Event Sign-off"]
        },
        {
            "id": "v_cater_01",
            "name": "Spice Route Global Gourmet Curations",
            "category": "Catering & Culinary Arts",
            "rate_per_plate": 85,
            "currency": "USD",
            "deliverables": ["Live fusion counters (Indo-Mexican, Awadhi Dum)", "Craft mocktail/cocktail bars", "Artisanal dessert stations"],
            "rating": 4.85,
            "escrow_milestones": ["25% Deposit", "50% Week-Prior Confirmation", "25% Day-Of Inspection"]
        }
    ]
}
