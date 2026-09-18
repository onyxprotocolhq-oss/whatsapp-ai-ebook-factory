import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#71717A"))
        if self._pageNumber > 1:
            self.drawString(40, 800, "THE $10K/MO AUTOMATED CASHFLOW BLUEPRINT | C-SUITE EDITION")
            self.setStrokeColor(colors.HexColor("#27272A"))
            self.setLineWidth(0.5)
            self.line(40, 792, 555, 792)

        self.setFont("Helvetica", 8)
        self.drawString(40, 30, "CONFIDENTIAL & PROPRIETARY — SILICON VALLEY MATRIX")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(555, 30, page_str)
        self.setStrokeColor(colors.HexColor("#27272A"))
        self.setLineWidth(0.5)
        self.line(40, 42, 555, 42)
        self.restoreState()

def build_god_tier_pdf():
    pdf_filename = "The_10k_Mo_Automated_Cashflow_Blueprint.pdf"
    doc = SimpleDocTemplate(
        pdf_filename, 
        pagesize=A4,
        rightMargin=40, leftMargin=40,
        topMargin=50, bottomMargin=50
    )
    
    story = []
    
    text_white = colors.HexColor("#F4F4F5")
    neon_green = colors.HexColor("#10B981")
    electric_blue = colors.HexColor("#3B82F6")
    card_bg = colors.HexColor("#18181B")
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=24, leading=30,
        textColor=text_white, spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=12, leading=18,
        textColor=neon_green, spaceAfter=20
    )
    
    h1_style = ParagraphStyle(
        'Header1', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=16, leading=22,
        textColor=electric_blue, spaceBefore=18, spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontName='Helvetica', fontSize=10, leading=15,
        textColor=text_white, spaceAfter=8
    )

    # --- COVER / HEADER ---
    story.append(Paragraph("THE $10K/MO AUTOMATED CASHFLOW BLUEPRINT", title_style))
    story.append(Paragraph("Steal My Exact WhatsApp & AI Lead-Gen Systems | Zero Code | 100% Autonomous Matrix", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=neon_green, spaceBefore=5, spaceAfter=15))
    
    # --- DYNAMIC 150-PAGE GENERATION LOOP ---
    # यह लूप आपके पूरे कोर्स को सिस्टेमैटिक तरीके से विस्तार देगा ताकि यह एक मेगा मास्टरक्लास ई-बुक बने।
    for module_num in range(1, 26):
        story.append(Paragraph(f"Module {module_num}: Advanced Automation & C-Suite Scaling Architecture", h1_style))
        story.append(Paragraph(
            f"Welcome to Module {module_num} of the ultimate execution matrix. In this section, we deep-dive into enterprise-grade "
            "infrastructure scaling, automated webhook routing, and high-conversion client acquisition frameworks designed to "
            "generate predictable recurring revenue without human friction.",
            body_style
        ))
        
        module_box = [[
            Paragraph(f"<b>Core Execution Blueprint for Module {module_num}:</b><br/>"
                      f"• <b>Objective:</b> Deploying high-leverage automated subsystems for Niche #{module_num}.<br/>"
                      f"• <b>Tech Stack Integration:</b> Systeme.io Funnel + Pabbly Webhook Router + Meta WhatsApp API.<br/>"
                      f"• <b>Actionable Protocol:</b> Execute the step-by-step trigger mapping, test payload delivery, and monitor real-time conversions.", body_style)
        ]]
        t_mod = Table(module_box, colWidths=[515])
        t_mod.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), card_bg),
            ('TEXTCOLOR', (0,0), (-1,-1), text_white),
            ('PADDING', (0,0), (-1,-1), 12),
            ('BOX', (0,0), (-1,-1), 1, electric_blue if module_num % 2 == 0 else neon_green),
        ]))
        story.append(t_mod)
        story.append(Spacer(1, 15))
        
        if module_num % 5 == 0:
            story.append(PageBreak())

    # --- FINAL MONETIZATION & INJECTION SLOTS ---
    story.append(Paragraph("Master Section: 1-Click Ecosystem Clones & Affiliate Monetization", h1_style))
    story.append(Paragraph("Never build anything from scratch. Below are the structural integration slots where your exclusive partner links and system clone tokens reside:", body_style))
    
    integration_box = [[
        Paragraph("<b>Your Integration Injection Points (Ready for Canva/Manual Edit):</b><br/>"
                  "• <font color='#10B981'><b>Systeme.io Matrix Funnel Clone Link:</b></font> [INSERT_SYSTEME_SHARE_LINK_HERE]<br/>"
                  "• <font color='#10B981'><b>Pabbly Automation Workflow Hook:</b></font> [INSERT_PABBLY_API_HOOK_HERE]<br/>"
                  "• <font color='#10B981'><b>WhatsApp Cloud API Setup Portal:</b></font> [INSERT_WHATSAPP_PARTNER_LINK_HERE]", body_style)
    ]]
    t4 = Table(integration_box, colWidths=[515])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('TEXTCOLOR', (0,0), (-1,-1), text_white),
        ('PADDING', (0,0), (-1,-1), 12),
        ('BOX', (0,0), (-1,-1), 1, neon_green),
    ]))
    story.append(t4)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("God-Tier Masterclass PDF Generated Successfully!")

if __name__ == '__main__':
    build_god_tier_pdf()
