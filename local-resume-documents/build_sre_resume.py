"""Build the SRE-focused one-page resume from verified career details."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, HRFlowable, KeepTogether,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "Chhotu_Kumar_SRE_Resume_Oct_2026.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor("#172626")
MUTED = colors.HexColor("#526360")
ACCENT = colors.HexColor("#B9512B")
RULE = colors.HexColor("#D7DED8")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=INK, alignment=TA_CENTER, spaceAfter=3),
    "title": ParagraphStyle("title", fontName="Helvetica", fontSize=11, leading=14, textColor=MUTED, alignment=TA_CENTER, spaceAfter=6),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, leading=12.5, textColor=INK, alignment=TA_CENTER, spaceAfter=10),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=10.3, leading=13, textColor=ACCENT, spaceBefore=13, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, leading=13.2, textColor=INK, spaceAfter=4),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.1, leading=12.4, leftIndent=12, firstLineIndent=-9, textColor=INK, spaceAfter=4),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.6, leading=13, textColor=INK, spaceBefore=5, spaceAfter=3),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8.8, leading=12, textColor=MUTED, spaceAfter=2),
}


def para(text, style="body"):
    return Paragraph(text, styles[style])


def bullet(text):
    return para("&#8226; " + text, "bullet")


story = [
    para("Chhotu Kumar", "name"),
    para("Software Developer | Infrastructure Automation &amp; Reliability", "title"),
    para(
        'Gurugram, Haryana  |  +91 73196 40608  |  '
        '<link href="mailto:chhotu22@navgurukul.org" color="#172626">chhotu22@navgurukul.org</link><br/>'
        '<link href="https://github.com/ck-surya" color="#172626">github.com/ck-surya</link>  |  '
        '<link href="https://www.linkedin.com/in/chhotu-kumar-148b5324b/" color="#172626">linkedin.com/in/chhotu-kumar-148b5324b</link>',
        "contact",
    ),
    HRFlowable(width="100%", thickness=0.7, color=RULE),
    para("PROFILE", "section"),
    para(
        "Software developer with 4+ years of experience across backend systems and infrastructure automation. "
        "Built Docker based services for contest operations, automated Ubuntu provisioning and deployment with Bash "
        "and Ansible, and supported Linux troubleshooting. Hands-on with AWS storage, Hetzner-to-AWS media migration "
        "using rclone, and Firebase phone verification and notifications."
    ),
    para("TECHNICAL SKILLS", "section"),
    para("<b>Infrastructure:</b> Linux / Ubuntu, Docker, Docker Compose, Bash, Ansible, Git, Traefik"),
    para("<b>Cloud and monitoring:</b> AWS storage, Hetzner, rclone, Firebase, Prometheus / Grafana configuration"),
    para("<b>Development:</b> Python, JavaScript, TypeScript, Node.js, NestJS, Frappe, MySQL"),
    para("EXPERIENCE", "section"),
    para("Justuju | Software Developer | Sep 2024 - Present", "role"),
    bullet("Built and containerized Docker based services supporting software delivery and contest operations."),
    bullet("Automated Ubuntu provisioning, system configuration, and repeatable deployments for ICPC contest environments using Bash and Ansible."),
    bullet("Implemented network restriction proxies and internal monitoring workflows; troubleshot Linux based services during operations."),
    bullet("Migrated CCL media uploads from Hetzner to AWS storage with rclone."),
    para("NavGurukul | Software &amp; Internal Tools Developer | Sep 2022 - Aug 2024", "role"),
    bullet("Developed Python and JavaScript workflows on Frappe, including data models and automated triggers."),
    bullet("Built Google Apps Script tracking and reporting workflows for more than 100 active users."),
    bullet("Created technical curriculum problems and led development workshops for more than 50 junior developers."),
    para("SELECTED PROJECTS", "section"),
    para('<link href="https://github.com/ck-surya/domjudge-docker-setup" color="#172626"><b>DOMjudge Docker Setup</b></link> | Docker, Bash, cloud-init, Prometheus, Grafana', "role"),
    bullet("Created a Docker Compose service stack and provisioning scripts for DOMjudge, plus status and diagnostic tooling and monitoring configuration."),
    para("<b>KBGV Learning Platform</b> | NestJS, MySQL, Docker, Firebase", "role"),
    bullet("Designed modular REST APIs and role based access; integrated Firebase services and containerized the backend."),
    para("EDUCATION", "section"),
    para("HE High School Araria | Class 10, 81% | 2021", "small"),
]


class ResumeDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(str(filename), pagesize=A4, leftMargin=46, rightMargin=46, topMargin=36, bottomMargin=34)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="resume", frames=frame))


ResumeDoc(OUTPUT).build(story)
print(OUTPUT)
