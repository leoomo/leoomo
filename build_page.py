#!/usr/bin/env python3
"""
Personal Tech Card Website Generator
Generates static HTML from configuration data.
Upgraded version with enhanced visual design.
"""

# Configuration data based on spec.md
PERSONAL_INFO = {
    "name": "Hua Zeng",
    "title": "Python Developer",
    "initials": "HZ",
    "age": 42,
    "experience": "19 years",
    "python_experience": "9 years",
    "location": "Hangzhou",
    "email": "leoomo@gmail.com",
    "bio": """9 years Python full-stack developer with expertise in RPA automation and AI/LLM application development.
Former TCM (Traditional Chinese Medicine) moxibustion practitioner, transitioned to tech with unique cross-domain thinking.
Led tax RPA solution design, developed AI products including Hua Xin AI RAG System and Smart Fishing Assistant.
Strong communication and project management skills.""",
    "skills": {
        "AI/LLM": ["LangChain", "RAG", "LLM Apps"],
        "Backend": ["Django", "Flask", "FastAPI", "SQLAlchemy"],
        "RPA": ["Selenium", "Playwright", "XPath"],
        "Frontend": ["React", "TypeScript", "Vue.js", "ECharts"],
        "Database": ["PostgreSQL", "MySQL"],
        "DevOps": ["Ansible", "Redis", "Celery", "GitHub Actions"]
    },
    "projects": [
        {
            "name": "Hua Xin AI RAG System",
            "description": "AI-powered knowledge retrieval and RAG Q&A system",
            "tech": "LangChain, RAG, Claude Code",
            "url": "https://github.com/leoomo/hua_news_ai_rag",
            "featured": True
        },
        {
            "name": "Smart Fishing Assistant",
            "description": "AI fishing advisor with weather analysis and gear comparison",
            "tech": "FastAPI, React, LangChain, WeChat Mini Program",
            "url": None,
            "featured": False
        },
        {
            "name": "Tax RPA Automation",
            "description": "Tax RPA automation solutions for 36 provinces/cities",
            "tech": "Python, Selenium, Playwright",
            "url": None,
            "featured": False
        },
        {
            "name": "Employee Performance System",
            "description": "Performance evaluation and data analytics platform",
            "tech": "Django, Vue.js, MySQL",
            "url": None,
            "featured": False
        },
        {
            "name": "CI/CD Platform",
            "description": "Automated deployment platform supporting 157 projects",
            "tech": "Ansible, Redis, Django",
            "url": None,
            "featured": False
        }
    ],
    "work_experience": [
        {
            "company": "Nuonuo.com",
            "position": "RPA Lead Developer",
            "period": "2017.06-2025.04",
            "highlights": ["Tax RPA development", "Team leadership", "Cross-department collaboration"],
            "icon": "N"
        },
        {
            "company": "Smart Fishing Assistant",
            "position": "Full-stack Developer",
            "period": "2025.10-Present",
            "highlights": ["AI assistant development", "LangChain applications"],
            "icon": "SF"
        },
        {
            "company": "Shanghai Shinju Network",
            "position": "Test Development Engineer",
            "period": "2016.06-2017.06",
            "highlights": ["Performance testing", "Test tool development"],
            "icon": "SJ"
        },
        {
            "company": "Beijing Infomedia Technology",
            "position": "Software Test Development Engineer",
            "period": "2007.03-2014.06",
            "highlights": ["Software testing", "Software training", "QA processes"],
            "icon": "BI"
        },
        {
            "company": "Yuanhecaotang (TCM)",
            "position": "TCM Moxibustion Therapist",
            "period": "2014.06-2016.06",
            "highlights": ["TCM therapy", "Healthcare"],
            "icon": "YH"
        }
    ],
    "education": {
        "school": "Hubei Normal University",
        "major": "Environmental Engineering",
        "period": "2001-2005"
    },
    "social": {
        "github": "https://github.com/leoomo",
        "email": "leoomo@gmail.com"
    }
}

# Skill category colors
SKILL_COLORS = {
    "AI/LLM": "#10B981",
    "Backend": "#3B82F6",
    "RPA": "#F59E0B",
    "Frontend": "#8B5CF6",
    "Database": "#EC4899",
    "DevOps": "#06B6D4"
}


def generate_html(info: dict) -> str:
    """Generate the complete HTML document."""

    # Build skills section
    skills_html = ""
    for category, skills in info["skills"].items():
        color = SKILL_COLORS.get(category, "#6B7280")
        tags = "".join(
            f'<span class="skill-tag" style="--tag-color: {color}">{skill}</span>'
            for skill in skills
        )
        skills_html += f'''
        <div class="skill-group fade-in" style="--delay: {list(info['skills'].keys()).index(category) * 0.1}s">
            <div class="skill-label">{category}</div>
            <div class="skill-tags">{tags}</div>
        </div>'''

    # Build projects section
    projects_html = ""
    for i, project in enumerate(info["projects"]):
        is_featured = project.get("featured", False)
        card_class = "project-card featured" if is_featured else "project-card"
        icon = chr(65 + i)  # A, B, C, D, E

        card_content = f'''
            <div class="project-icon">{icon}</div>
            <div class="project-content">
                <h3 class="project-name">{project['name']}</h3>
                <p class="project-desc">{project['description']}</p>
                <span class="project-tech">{project['tech']}</span>
            </div>'''

        if project["url"]:
            projects_html += f'<a href="{project["url"]}" class="{card_class} fade-in" style="--delay: {i * 0.1}s" target="_blank">{card_content}</a>'
        else:
            projects_html += f'<div class="{card_class} fade-in" style="--delay: {i * 0.1}s">{card_content}</div>'

    # Sort work experience by start date (descending)
    def parse_period(period):
        """Parse period string like '2017.06-2025.04' or '2025.10-Present' to sortable tuple."""
        if period == "Present":
            return (9999, 99)
        start = period.split("-")[0]
        parts = start.split(".")
        return (int(parts[0]), int(parts[1]))

    sorted_experience = sorted(info["work_experience"], key=lambda x: parse_period(x["period"]), reverse=True)

    # Build work experience section with timeline
    experience_html = ""
    for i, job in enumerate(sorted_experience):
        highlights = "".join(f"<li>{h}</li>" for h in job["highlights"])
        icon = job.get("icon", "J")
        experience_html += f'''
        <div class="timeline-item fade-in" style="--delay: {i * 0.1}s">
            <div class="timeline-dot"></div>
            <div class="timeline-line"></div>
            <div class="job-card">
                <div class="job-header">
                    <div class="company-info">
                        <div class="company-icon">{icon}</div>
                        <div>
                            <span class="company">{job['company']}</span>
                            <span class="period">{job['period']}</span>
                        </div>
                    </div>
                </div>
                <p class="position">{job['position']}</p>
                <ul class="highlights">{highlights}</ul>
            </div>
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{info['name']} - {info['title']}</title>
  <meta name="description" content="{info['experience']} Python developer with expertise in RPA automation and AI/LLM applications">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #0D9488;
      --primary-dark: #0F766E;
      --primary-light: #14B8A6;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text-primary: #1E293B;
      --text-secondary: #64748B;
      --text-muted: #94A3B8;
      --accent: #0D9488;
      --gradient-start: #0D9488;
      --gradient-end: #6366F1;
      --border: #E2E8F0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 12px rgba(13,148,136,0.12);
      --shadow-lg: 0 8px 30px rgba(13,148,136,0.18);
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg);
      color: var(--text-primary);
      line-height: 1.6;
      min-height: 100vh;
    }}

    /* Background decoration */
    .bg-decoration {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: -1;
      overflow: hidden;
    }}

    .bg-decoration::before {{
      content: '';
      position: absolute;
      top: -20%;
      right: -10%;
      width: 60%;
      height: 80%;
      background: linear-gradient(135deg, rgba(13,148,136,0.08) 0%, rgba(99,102,241,0.06) 100%);
      border-radius: 50%;
      filter: blur(60px);
      animation: float 20s ease-in-out infinite;
    }}

    .bg-decoration::after {{
      content: '';
      position: absolute;
      bottom: -30%;
      left: -15%;
      width: 50%;
      height: 70%;
      background: linear-gradient(135deg, rgba(99,102,241,0.06) 0%, rgba(13,148,136,0.08) 100%);
      border-radius: 50%;
      filter: blur(60px);
      animation: float 25s ease-in-out infinite reverse;
    }}

    @keyframes float {{
      0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
      33% {{ transform: translate(30px, -30px) rotate(5deg); }}
      66% {{ transform: translate(-20px, 20px) rotate(-5deg); }}
    }}

    /* Animations */
    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    @keyframes scaleIn {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .fade-in {{
      animation: fadeInUp 0.6s ease-out backwards;
      animation-delay: var(--delay, 0s);
    }}

    .container {{
      max-width: 800px;
      margin: 0 auto;
      padding: 48px 24px;
    }}

    /* Header */
    .header {{
      text-align: center;
      padding: 56px 32px;
      margin-bottom: 40px;
      position: relative;
    }}

    .avatar-container {{
      position: relative;
      width: 120px;
      height: 120px;
      margin: 0 auto 24px;
    }}

    .avatar {{
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 36px;
      font-weight: 700;
      color: white;
      box-shadow: var(--shadow-lg);
      animation: scaleIn 0.5s ease-out;
      position: relative;
      z-index: 1;
    }}

    .avatar-ring {{
      position: absolute;
      top: -4px;
      left: -4px;
      right: -4px;
      bottom: -4px;
      border-radius: 50%;
      border: 3px solid transparent;
      background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end)) border-box;
      -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: pulse 3s ease-in-out infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.6; transform: scale(1.02); }}
    }}

    .name {{
      font-size: 48px;
      font-weight: 700;
      background: linear-gradient(135deg, var(--text-primary), var(--primary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
      animation: fadeInUp 0.6s ease-out 0.1s backwards;
    }}

    .title {{
      font-size: 22px;
      font-weight: 500;
      color: var(--primary);
      margin-bottom: 16px;
      animation: fadeInUp 0.6s ease-out 0.2s backwards;
    }}

    .meta {{
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 20px;
      animation: fadeInUp 0.6s ease-out 0.3s backwards;
    }}

    .meta-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 14px;
      font-weight: 500;
      color: var(--text-secondary);
      padding: 6px 14px;
      background: var(--card-bg);
      border-radius: 20px;
      box-shadow: var(--shadow-sm);
    }}

    .meta-item svg {{
      width: 16px;
      height: 16px;
      color: var(--primary);
    }}

    .bio {{
      font-size: 16px;
      color: var(--text-secondary);
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.8;
      animation: fadeInUp 0.6s ease-out 0.4s backwards;
    }}

    /* Sections */
    section {{
      margin-bottom: 48px;
    }}

    .section-title {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.15em;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .section-title::after {{
      content: '';
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, var(--border), transparent);
    }}

    /* Skills */
    .skills {{
      background: var(--card-bg);
      border-radius: 20px;
      padding: 32px;
      box-shadow: var(--shadow-sm);
    }}

    .skill-group {{
      margin-bottom: 20px;
    }}

    .skill-group:last-child {{
      margin-bottom: 0;
    }}

    .skill-label {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 10px;
    }}

    .skill-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .skill-tag {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 500;
      padding: 8px 16px;
      border-radius: 8px;
      background: color-mix(in srgb, var(--tag-color) 12%, transparent);
      color: var(--tag-color);
      border: 1px solid color-mix(in srgb, var(--tag-color) 25%, transparent);
      transition: all 0.25s ease;
      cursor: default;
    }}

    .skill-tag:hover {{
      background: color-mix(in srgb, var(--tag-color) 20%, transparent);
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 4px 12px color-mix(in srgb, var(--tag-color) 30%, transparent);
    }}

    /* Projects */
    .projects-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }}

    .project-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      text-decoration: none;
      color: inherit;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      gap: 16px;
      position: relative;
      overflow: hidden;
    }}

    .project-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--primary), var(--gradient-end));
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 0.3s ease;
    }}

    .project-card:hover {{
      border-color: var(--primary);
      box-shadow: var(--shadow-lg);
      transform: translateY(-4px);
    }}

    .project-card:hover::before {{
      transform: scaleX(1);
    }}

    .project-card.featured {{
      grid-column: span 2;
      background: linear-gradient(135deg, rgba(13,148,136,0.04), rgba(99,102,241,0.04));
      border-color: rgba(13,148,136,0.2);
    }}

    .project-card.featured::before {{
      background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
    }}

    .project-icon {{
      width: 48px;
      height: 48px;
      min-width: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 700;
      color: white;
    }}

    .project-card.featured .project-icon {{
      width: 56px;
      height: 56px;
      min-width: 56px;
      font-size: 22px;
    }}

    .project-content {{
      flex: 1;
    }}

    .project-name {{
      font-size: 17px;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 6px;
    }}

    .project-card.featured .project-name {{
      font-size: 20px;
    }}

    .project-desc {{
      font-size: 14px;
      color: var(--text-secondary);
      margin-bottom: 12px;
      line-height: 1.5;
    }}

    .project-tech {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--text-muted);
    }}

    /* Experience - Timeline */
    .timeline {{
      position: relative;
      padding-left: 32px;
    }}

    .timeline-item {{
      position: relative;
      padding-bottom: 28px;
    }}

    .timeline-item:last-child {{
      padding-bottom: 0;
    }}

    .timeline-item:last-child .timeline-line {{
      display: none;
    }}

    .timeline-dot {{
      position: absolute;
      left: -32px;
      top: 6px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--primary);
      border: 3px solid var(--bg);
      box-shadow: 0 0 0 2px var(--primary);
    }}

    .timeline-line {{
      position: absolute;
      left: -26px;
      top: 20px;
      width: 2px;
      height: calc(100% + 8px);
      background: linear-gradient(180deg, var(--primary), var(--border));
    }}

    .job-card {{
      background: var(--card-bg);
      border-radius: 16px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
      transition: all 0.3s ease;
    }}

    .job-card:hover {{
      box-shadow: var(--shadow-md);
      transform: translateX(4px);
    }}

    .job-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 8px;
    }}

    .company-info {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .company-icon {{
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: 700;
      color: white;
    }}

    .company {{
      font-size: 16px;
      font-weight: 600;
      color: var(--text-primary);
      display: block;
    }}

    .period {{
      font-size: 13px;
      color: var(--text-muted);
      display: block;
      margin-top: 2px;
    }}

    .position {{
      font-size: 14px;
      font-weight: 500;
      color: var(--primary);
      margin-bottom: 12px;
    }}

    .highlights {{
      list-style: none;
      padding-left: 0;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .highlights li {{
      font-size: 13px;
      color: var(--text-secondary);
      padding: 4px 12px;
      background: var(--bg);
      border-radius: 6px;
    }}

    /* Education */
    .education-card {{
      background: var(--card-bg);
      border-radius: 16px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      gap: 20px;
      transition: all 0.3s ease;
    }}

    .education-card:hover {{
      box-shadow: var(--shadow-md);
    }}

    .edu-icon {{
      width: 56px;
      height: 56px;
      border-radius: 14px;
      background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .edu-icon svg {{
      width: 28px;
      height: 28px;
      color: white;
    }}

    .edu-info {{
      flex: 1;
    }}

    .school {{
      font-size: 17px;
      font-weight: 600;
      color: var(--text-primary);
    }}

    .major {{
      font-size: 14px;
      color: var(--text-secondary);
      margin-top: 4px;
    }}

    .edu-period {{
      font-size: 14px;
      font-weight: 500;
      color: var(--primary);
      padding: 6px 14px;
      background: rgba(13,148,136,0.1);
      border-radius: 20px;
    }}

    /* Contact */
    .contact {{
      background: linear-gradient(135deg, var(--primary), var(--primary-dark));
      border-radius: 24px;
      padding: 40px;
      text-align: center;
      color: white;
      position: relative;
      overflow: hidden;
    }}

    .contact::before {{
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 60%;
      height: 200%;
      background: rgba(255,255,255,0.05);
      border-radius: 50%;
      transform: rotate(15deg);
    }}

    .contact-title {{
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 8px;
      position: relative;
    }}

    .contact-subtitle {{
      font-size: 15px;
      opacity: 0.9;
      margin-bottom: 28px;
      position: relative;
    }}

    .contact-links {{
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      position: relative;
    }}

    .contact-link {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 15px;
      font-weight: 500;
      color: white;
      text-decoration: none;
      padding: 14px 24px;
      background: rgba(255,255,255,0.15);
      border-radius: 12px;
      transition: all 0.3s ease;
      backdrop-filter: blur(10px);
    }}

    .contact-link:hover {{
      background: rgba(255,255,255,0.25);
      transform: translateY(-2px);
    }}

    .contact-link svg {{
      width: 20px;
      height: 20px;
    }}

    /* Scroll animations */
    .scroll-animate {{
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.6s ease-out;
    }}

    .scroll-animate.visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Footer */
    .footer {{
      text-align: center;
      padding: 32px 0;
      color: var(--text-muted);
      font-size: 13px;
    }}

    .footer a {{
      color: var(--primary);
      text-decoration: none;
    }}

    .footer a:hover {{
      text-decoration: underline;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .container {{
        padding: 32px 16px;
      }}

      .name {{
        font-size: 36px;
      }}

      .title {{
        font-size: 18px;
      }}

      .meta {{
        gap: 8px;
      }}

      .meta-item {{
        font-size: 13px;
        padding: 5px 10px;
      }}

      .projects-grid {{
        grid-template-columns: 1fr;
      }}

      .project-card.featured {{
        grid-column: span 1;
      }}

      .education-card {{
        flex-direction: column;
        text-align: center;
      }}

      .edu-period {{
        width: fit-content;
      }}

      .contact {{
        padding: 32px 20px;
      }}

      .contact-links {{
        flex-direction: column;
      }}

      .contact-link {{
        width: 100%;
        justify-content: center;
      }}
    }}
  </style>
</head>
<body>
  <!-- Background decoration -->
  <div class="bg-decoration"></div>

  <main class="container">
    <!-- Header -->
    <header class="header">
      <div class="avatar-container">
        <div class="avatar-ring"></div>
        <div class="avatar">{info['initials']}</div>
      </div>
      <h1 class="name">{info['name']}</h1>
      <p class="title">{info['title']}</p>
      <div class="meta">
        <span class="meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          {info['experience']} total
        </span>
        <span class="meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
          {info['python_experience']} Python
        </span>
        <span class="meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          {info['location']}
        </span>
      </div>
      <p class="bio">{info['bio'].strip().replace(chr(10), ' ')}</p>
    </header>

    <!-- Skills -->
    <section class="skills scroll-animate">
      <h2 class="section-title">Skills</h2>
      {skills_html}
    </section>

    <!-- Projects -->
    <section class="projects scroll-animate">
      <h2 class="section-title">Projects</h2>
      <div class="projects-grid">
        {projects_html}
      </div>
    </section>

    <!-- Work Experience -->
    <section class="experience scroll-animate">
      <h2 class="section-title">Work Experience</h2>
      <div class="timeline">
        {experience_html}
      </div>
    </section>

    <!-- Education -->
    <section class="education scroll-animate">
      <h2 class="section-title">Education</h2>
      <div class="education-card">
        <div class="edu-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
        </div>
        <div class="edu-info">
          <div class="school">{info['education']['school']}</div>
          <div class="major">{info['education']['major']}</div>
        </div>
        <div class="edu-period">{info['education']['period']}</div>
      </div>
    </section>

    <!-- Contact -->
    <section class="contact scroll-animate">
      <h2 class="contact-title">Let's Connect</h2>
      <p class="contact-subtitle">Feel free to reach out for collaboration or just to say hi!</p>
      <div class="contact-links">
        <a href="{info['social']['github']}" class="contact-link" target="_blank">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          GitHub
        </a>
        <a href="mailto:{info['social']['email']}" class="contact-link">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          Email
        </a>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <p>Built with passion &middot; <a href="https://github.com/leoomo" target="_blank">View on GitHub</a></p>
    </footer>
  </main>

  <script>
    // Scroll animations with Intersection Observer
    const observerOptions = {{
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    }};

    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('visible');
        }}
      }});
    }}, observerOptions);

    document.querySelectorAll('.scroll-animate').forEach(el => {{
      observer.observe(el);
    }});
  </script>
</body>
</html>'''

    return html


def main():
    """Main function to generate the HTML page."""
    html = generate_html(PERSONAL_INFO)

    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {output_path}")


if __name__ == "__main__":
    main()
