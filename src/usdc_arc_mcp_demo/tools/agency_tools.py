def register_tools(mcp):
    @mcp.tool("list_agencies")
    async def list_agencies():
        """Get list of all available government agencies with their slugs and metadata"""
        agencies = [
            {
                "name": "Agency for International Development",
                "slug": "agency-international-development",
            },
            {
                "name": "American Battle Monuments Commission",
                "slug": "american-battle-monuments-commission",
            },
            {
                "name": "Commodity Futures Trading Commission",
                "slug": "commodity-futures-trading-commission",
            },
            {
                "name": "Consumer Financial Protection Bureau",
                "slug": "consumer-financial-protection-bureau",
            },
            {
                "name": "Consumer Product Safety Commission",
                "slug": "consumer-product-safety-commission",
            },
            {
                "name": "Corporation for National and Community Service",
                "slug": "corporation-national-community-service",
            },
            {
                "name": "Defense Nuclear Facilities Safety Board",
                "slug": "defense-nuclear-facilities-safety-board",
            },
            {"name": "Denali Commission", "slug": "denali-commission"},
            {"name": "Department of Agriculture", "slug": "agriculture"},
            {"name": "Department of Commerce", "slug": "commerce"},
            {"name": "Department of Defense", "slug": "defense"},
            {"name": "Department of Education", "slug": "education"},
            {"name": "Department of Energy", "slug": "energy"},
            {
                "name": "Department of Health and Human Services",
                "slug": "health-human-services",
            },
            {"name": "Department of Homeland Security", "slug": "homeland-security"},
            {
                "name": "Department of Housing and Urban Development",
                "slug": "housing-urban-development",
            },
            {"name": "Department of the Interior", "slug": "interior"},
            {"name": "Department of Justice", "slug": "justice"},
            {"name": "Department of Labor", "slug": "labor"},
            {"name": "Department of State", "slug": "state"},
            {"name": "Department of Transportation", "slug": "transportation"},
            {"name": "Department of the Treasury", "slug": "treasury"},
            {"name": "Department of Veterans Affairs", "slug": "veterans-affairs"},
            {
                "name": "Environmental Protection Agency",
                "slug": "environmental-protection-agency",
            },
            {
                "name": "Equal Employment Opportunity Commission",
                "slug": "equal-employment-opportunity-commission",
            },
            {
                "name": "Executive Office of the President",
                "slug": "executive-office-president",
            },
            {
                "name": "Farm Credit Administration",
                "slug": "farm-credit-administration",
            },
            {
                "name": "Federal Bureau of Investigation",
                "slug": "federal-bureau-investigation",
            },
            {
                "name": "Federal Deposit Insurance Corporation",
                "slug": "federal-deposit-insurance-corporation",
            },
            {
                "name": "Federal Election Commission",
                "slug": "federal-election-commission",
            },
            {
                "name": "Federal Energy Regulatory Commission",
                "slug": "federal-energy-regulatory-commission",
            },
            {
                "name": "Federal Housing Finance Agency",
                "slug": "federal-housing-finance-agency",
            },
            {
                "name": "Federal Maritime Commission",
                "slug": "federal-maritime-commission",
            },
            {
                "name": "Federal Mine Safety and Health Review Commission",
                "slug": "federal-mine-safety-health-review-commission",
            },
            {
                "name": "Federal Retirement Thrift Investment Board",
                "slug": "federal-retirement-thrift-investment-board",
            },
            {"name": "Federal Trade Commission", "slug": "federal-trade-commission"},
            {
                "name": "General Services Administration",
                "slug": "general-services-administration",
            },
            {"name": "Inter-American Foundation", "slug": "inter-american-foundation"},
            {
                "name": "International Development Finance Corporation",
                "slug": "international-development-finance-corporation",
            },
            {
                "name": "Merit Systems Protection Board",
                "slug": "merit-systems-protection-board",
            },
            {
                "name": "Millennium Challenge Corporation",
                "slug": "millennium-challenge-corporation",
            },
            {
                "name": "National Aeronautics and Space Administration",
                "slug": "national-aeronautics-space-administration",
            },
            {
                "name": "National Archives and Records Administration",
                "slug": "national-archives-records-administration",
            },
            {
                "name": "National Capital Planning Commission",
                "slug": "national-capital-planning-commission",
            },
            {
                "name": "National Council on Disability",
                "slug": "national-council-disability",
            },
            {
                "name": "National Credit Union Administration",
                "slug": "national-credit-union-administration",
            },
            {
                "name": "National Education Association",
                "slug": "national-education-association",
            },
            {
                "name": "National Endowment For The Humanities",
                "slug": "national-endowment-humanities",
            },
            {
                "name": "National Labor Relations Board",
                "slug": "national-labor-relations-board",
            },
            {"name": "National Mediation Board", "slug": "national-mediation-board"},
            {
                "name": "National Oceanic and Atmospheric Administration",
                "slug": "national-oceanic-atmospheric-administration",
            },
            {"name": "National Park Service", "slug": "national-park-service"},
            {
                "name": "National Reconnaissance Office",
                "slug": "national-reconnaissance-office",
            },
            {
                "name": "National Science Foundation",
                "slug": "national-science-foundation",
            },
            {
                "name": "National Transportation Safety Board",
                "slug": "national-transportation-safety-board",
            },
            {
                "name": "Nuclear Regulatory Commission",
                "slug": "nuclear-regulatory-commission",
            },
            {
                "name": "Nuclear Waste Technical Review Board",
                "slug": "nuclear-waste-technical-review-board",
            },
            {
                "name": "Office of the Director of National Intelligence",
                "slug": "office-director-national-intelligence",
            },
            {"name": "Office of Government Ethics", "slug": "office-government-ethics"},
            {
                "name": "Office of Navajo and Hopi Indian Relocation",
                "slug": "office-navajo-hopi-indian-relocation",
            },
            {
                "name": "Office of Personnel Management",
                "slug": "office-personnel-management",
            },
            {"name": "Peace Corps", "slug": "peace-corps"},
            {
                "name": "Pension Benefit Guaranty Corporation",
                "slug": "pension-benefit-guaranty-corporation",
            },
            {
                "name": "Postal Regulatory Commission",
                "slug": "postal-regulatory-commission",
            },
            {
                "name": "Privacy and Civil Liberties Oversight Board",
                "slug": "privacy-civil-liberties-oversight-board",
            },
            {
                "name": "Public Buildings Reform Board",
                "slug": "public-buildings-reform-board",
            },
            {
                "name": "Securities and Exchange Commission",
                "slug": "securities-exchange-commission",
            },
            {
                "name": "Small Business Adminstration",
                "slug": "small-business-administration",
            },
            {
                "name": "Social Security Administration",
                "slug": "social-security-administration",
            },
            {
                "name": "Special Inspector General for Afghanistan Reconstruction",
                "slug": "special-inspector-general-afghanistan-restoration",
            },
            {
                "name": "Surface Transportation Board",
                "slug": "surface-transportation-board",
            },
            {
                "name": "Tennessee Valley Authority",
                "slug": "tennessee-valley-authority",
            },
            {"name": "Udall Foundation", "slug": "udall-foundation"},
            {"name": "U.S. Access Board", "slug": "access-board"},
            {"name": "U.S. Agency for Global Media", "slug": "agency-global-media"},
            {
                "name": "U.S. Commission on Civil Rights",
                "slug": "commission-civil-rights",
            },
            {"name": "U.S. Courts", "slug": "us-courts"},
            {
                "name": "U.S. International Trade Commission",
                "slug": "international-trade-commission",
            },
            {
                "name": "U.S. Postal Inspection Service",
                "slug": "postal-inspection-service",
            },
            {"name": "U.S. Postal Service", "slug": "postal-service"},
            {
                "name": "U.S. Railroad Retirement Board",
                "slug": "railroad-retirement-board",
            },
            {
                "name": "U.S. Trade and Development Agency",
                "slug": "trade-development-agency",
            },
        ]
        return agencies
