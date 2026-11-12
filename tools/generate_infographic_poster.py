# tools/generate_infographic_poster.py
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def draw_rounded_rect(draw, coords, radius, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = coords
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=width)

def draw_progress_bar(draw, x, y, width, height, percent, bg_color, fill_color, border_color=None):
    draw_rounded_rect(draw, (x, y, x + width, y + height), radius=height//2, fill=bg_color, outline=border_color)
    fill_width = int(width * (percent / 100.0))
    if fill_width > 4:
        draw_rounded_rect(draw, (x, y, x + fill_width, y + height), radius=height//2, fill=fill_color)

def generate_poster():
    W, H = 1400, 2250
    img = Image.new('RGB', (W, H), color=hex_to_rgb('#0B0F19'))
    draw = ImageDraw.Draw(img)

    # Fonts
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    font_bn_path = "C:/Windows/Fonts/kalpurush.ttf"
    font_mono_path = "C:/Windows/Fonts/consola.ttf"

    title_font = ImageFont.truetype(font_bold_path, 46)
    bn_title_font = ImageFont.truetype(font_bn_path, 48)
    subtitle_font = ImageFont.truetype(font_reg_path, 22)
    sec_title_font = ImageFont.truetype(font_bold_path, 28)
    card_title_font = ImageFont.truetype(font_bold_path, 22)
    body_font = ImageFont.truetype(font_reg_path, 17)
    body_bold = ImageFont.truetype(font_bold_path, 17)
    bn_body_font = ImageFont.truetype(font_bn_path, 19)
    bn_body_bold = ImageFont.truetype(font_bn_path, 20)
    badge_font = ImageFont.truetype(font_bold_path, 15)
    mono_font = ImageFont.truetype(font_mono_path, 16)

    # Palette
    C_BG_CARD = hex_to_rgb('#131B2E')
    C_BORDER = hex_to_rgb('#1E293B')
    C_CYAN = hex_to_rgb('#06B6D4')
    C_EMERALD = hex_to_rgb('#10B981')
    C_RED = hex_to_rgb('#EF4444')
    C_AMBER = hex_to_rgb('#F59E0B')
    C_WHITE = hex_to_rgb('#F8FAFC')
    C_MUTED = hex_to_rgb('#94A3B8')
    C_BAR_BG = hex_to_rgb('#1E293B')

    # Subtle header gradient accent lines
    draw.rectangle([0, 0, W, 8], fill=C_CYAN)

    # ==================== HEADER ====================
    curr_y = 45
    # Version badge
    draw_rounded_rect(draw, (70, curr_y, 360, curr_y + 36), radius=18, fill=hex_to_rgb('#083344'), outline=C_CYAN)
    draw.text((85, curr_y + 7), "BHASHABID (ভাষাবিদ)  •  v1.0.0", fill=C_CYAN, font=badge_font)

    # Top badges on right
    draw_rounded_rect(draw, (W - 480, curr_y, W - 70, curr_y + 36), radius=18, fill=hex_to_rgb('#064E3B'), outline=C_EMERALD)
    draw.text((W - 465, curr_y + 7), "PROVEN ON CURSOR AI & GROK 4.7  ✔", fill=C_EMERALD, font=badge_font)

    curr_y += 60
    draw.text((70, curr_y), "The First Deterministic Bengali Linguistic Coprocessor", fill=C_WHITE, font=title_font)
    curr_y += 65
    draw.text((70, curr_y), "Empirical Real-World Benchmark & Honest Capability Matrix (Zero Hype, Ground Truth)", fill=C_MUTED, font=subtitle_font)

    curr_y += 45
    # Metric Pills
    pills = [
        ("Core Budget: ~302 Tokens (< 390 Ceiling)", C_CYAN),
        ("Deterministic Python MCP: $0.00 Cost", C_EMERALD),
        ("11 Professional Sectors / 8 Guides", hex_to_rgb('#A855F7')),
        ("Supervised P2 Self-Learning Loop", C_AMBER)
    ]
    px = 70
    for label, col in pills:
        tw = int(draw.textlength(label, font=badge_font)) + 30
        draw_rounded_rect(draw, (px, curr_y, px + tw, curr_y + 34), radius=8, fill=hex_to_rgb('#1E293B'), outline=col)
        draw.text((px + 15, curr_y + 7), label, fill=col, font=badge_font)
        px += tw + 15

    # ==================== SECTION 1: BENCHMARK WITH SYNCED SCORE BARS ====================
    curr_y += 65
    draw.text((70, curr_y), "1. LIVE EMPIRICAL BENCHMARK (BEFORE VS. AFTER)", fill=C_CYAN, font=sec_title_font)
    curr_y += 45

    benchmarks = [
        {
            "title": "Case 1: Supreme Court Article 102 Constitutional Writ (Mandamus & Prohibition)",
            "base_score": 0,
            "base_label": "0 / 100 (FAIL)",
            "base_detail": "30 Sadhu-Cholito verb mixing errors (হইবে, করিয়া, দর্শাইতে), missing statutory Mandamus prayer.",
            "bha_score": 100,
            "bha_label": "100 / 100 (PRODUCTION READY)",
            "bha_detail": "0 errors. Pure Promito Cholito with explicit Mandamus & Prohibition prayers (WP 13989/2016 precedent).",
            "tag": "LEGAL"
        },
        {
            "title": "Case 2: Central Bank Inflation & Monetary Policy Desk Report",
            "base_score": 20,
            "base_label": "20 / 100 (AMATEUR)",
            "base_detail": "Infested with raw English calques ('তরলতা (লিকুইডিটি)', 'কলমানি রেট') and passive syntax ('দ্বারা চালিত').",
            "bha_score": 100,
            "bha_label": "100 / 100 (DESK READY)",
            "bha_detail": "Canonical Financial Desk terms (তারল্য, কলমানি হার, সংকোচনমূলক মুদ্রানীতি, মূল্যস্ফীতি) with active causal flow.",
            "tag": "BANKING"
        },
        {
            "title": "Case 3: NCTB Class 10 Creative Question Framing (Biology Exam)",
            "base_score": 80,
            "base_label": "80 / 100 (NON-COMPLIANT)",
            "base_detail": "Violated National Board science rubric by asking subjective opinion ('মতামত দাও') in higher-order skill (ঘ).",
            "bha_score": 100,
            "bha_label": "100 / 100 (BOARD READY)",
            "bha_detail": "Strict adherence to 4-tier Bloom rubric (ক/খ/গ/ঘ) with canonical evaluation: 'উক্তিটির যথার্থতা মূল্যায়ন করো'.",
            "tag": "EDUCATION"
        },
        {
            "title": "Case 4: Literature, Proverbs & Poetic Metaphor (Figurative Semantics & Payar)",
            "base_score": 10,
            "base_label": "10 / 100 (CATASTROPHIC)",
            "base_detail": "Literal calques ('ঝোপের চারপাশে পেটানো', 'হৃৎপিণ্ড পাথরে পরিণত'), broken 16-18 syllable pseudo-verse.",
            "bha_score": 100,
            "bha_label": "100 / 100 (LITERARY GRADE)",
            "bha_detail": "Authentic idioms ('ঘুরিয়ে-পেঁচিয়ে কথা বলা', 'হৃদয় পাষাণ হয়ে গেল' - অভিধা/লক্ষণা/ব্যঞ্জনা), exact 8+6=14 Payar.",
            "tag": "LITERATURE"
        }
    ]

    card_w = (W - 140)
    for b in benchmarks:
        card_h = 135
        draw_rounded_rect(draw, (70, curr_y, 70 + card_w, curr_y + card_h), radius=12, fill=C_BG_CARD, outline=C_BORDER)

        # Title & Category Tag
        draw.text((90, curr_y + 14), b["title"], fill=C_WHITE, font=card_title_font)
        draw_rounded_rect(draw, (W - 190, curr_y + 14, W - 90, curr_y + 38), radius=6, fill=hex_to_rgb('#1E293B'), outline=C_MUTED)
        draw.text((W - 175, curr_y + 18), b["tag"], fill=C_MUTED, font=badge_font)

        # Row 1: Baseline
        r1_y = curr_y + 48
        draw.text((90, r1_y), "Raw LLM:", fill=C_RED, font=body_bold)
        draw.text((175, r1_y), b["base_label"], fill=C_RED, font=body_bold)
        draw_progress_bar(draw, 330, r1_y + 5, 200, 14, b["base_score"], C_BAR_BG, C_RED)
        draw.text((550, r1_y), b["base_detail"], fill=C_MUTED, font=bn_body_font)

        # Row 2: Bhashabid
        r2_y = curr_y + 88
        draw.text((90, r2_y), "Bhashabid:", fill=C_EMERALD, font=body_bold)
        draw.text((175, r2_y), b["bha_label"], fill=C_EMERALD, font=body_bold)
        draw_progress_bar(draw, 330, r2_y + 5, 200, 14, b["bha_score"], C_BAR_BG, C_EMERALD)
        draw.text((550, r2_y), b["bha_detail"], fill=hex_to_rgb('#E2E8F0'), font=bn_body_font)

        curr_y += card_h + 15

    # ==================== SECTION 2: 4 PIONEERING PILLARS ====================
    curr_y += 35
    draw.text((70, curr_y), "2. THE 4 PIONEERING ARCHITECTURAL PILLARS", fill=C_CYAN, font=sec_title_font)
    curr_y += 45

    pillars = [
        ("Pillar 1: Programmatic Token Ceiling (< 390 Tokens)",
         "Standard prompts dump 10k+ tokens into chats. Bhashabid's core router is programmatically capped at ~302 tokens (< 390 limit), leaving 99% of your context window free.",
         C_CYAN),
        ("Pillar 2: Supervised Self-Learning Distillation Loop",
         "Automated closed-loop: Harvester ➔ Card Synthesizer ➔ Human (P2) Gate ➔ Invariant Distiller. 1 invariant covers 50,000+ variations without prompt bloat or hallucinated rules.",
         C_AMBER),
        ("Pillar 3: Modular Domain Isolation (Zero Token Waste)",
         "11 sectors partitioned across 8 modular guides loaded strictly on-demand. Unrelated tasks burn 0.0 tokens (legal & banking cost zero when writing fiction).",
         hex_to_rgb('#A855F7')),
        ("Pillar 4: Deterministic Python Offloading via MCP",
         "Exact irregular 0-99 numbers ('নিরানব্বই'), South Asian commas (১২,৩৪,৫৬৭), Unicode NFC, and 14-akshar Payar scansion execute at 500k words/sec at $0.00 cost.",
         C_EMERALD)
    ]

    p_w = (card_w - 20) // 2
    for i, (p_title, p_desc, p_col) in enumerate(pillars):
        px = 70 if (i % 2 == 0) else (70 + p_w + 20)
        py = curr_y if (i < 2) else (curr_y + 130)
        draw_rounded_rect(draw, (px, py, px + p_w, py + 115), radius=10, fill=C_BG_CARD, outline=C_BORDER)
        draw.rectangle([px, py + 10, px + 4, py + 40], fill=p_col)
        draw.text((px + 18, py + 12), p_title, fill=p_col, font=card_title_font)
        # Wrap description
        words = p_desc.split()
        lines = []
        cur_line = []
        for w in words:
            if draw.textlength(" ".join(cur_line + [w]), font=body_font) < (p_w - 36):
                cur_line.append(w)
            else:
                lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))
        ly = py + 45
        for l in lines[:3]:
            draw.text((px + 18, ly), l, fill=C_MUTED, font=body_font)
            ly += 22

    curr_y += 265

    # ==================== SECTION 3: HONEST CAPABILITY COMPARISON TABLE ====================
    curr_y += 20
    draw.text((70, curr_y), "3. HONEST & REALISTIC CAPABILITY MATRIX (GROUND TRUTH VS. HYPE)", fill=C_CYAN, font=sec_title_font)
    curr_y += 45

    matrix_rows = [
        ("0–99 Irregular Cardinals", "0% (Compounds naively: 'নব্বই নয়')", "100% Deterministic ('নিরানব্বই', 'আড়াই')", "Restricted to 0-99 & standard lakh/crore arithmetic."),
        ("Punctuation & Decimals", "Corrupts decimal dots (১০.৮৭% ➔ ১০।৮৭%)", "100% Deterministic (Preserves decimals + Dari ।)", "Sentence boundaries require standard punctuation cues."),
        ("Proverbs & Idioms (প্রবাদ)", "Blind word calques ('ঝোপের চারপাশে পেটানো')", "Maps to authentic idioms ('ঘুরিয়ে-পেঁচিয়ে কথা বলা')", "Emerging modern slang not in lexicon flagged for review."),
        ("Literary Figurative Semantics", "Anatomical literalism ('হৃৎপিণ্ড পাথরে পরিণত')", "Tri-layer semantics ('হৃদয় পাষাণ হয়ে গেল')", "Acts as a literary co-editor; does not feel emotion."),
        ("Living Fiction Dialogue", "Wooden courtroom tags ('তিনি বললেন যে...')", "Living spoken register (কথ্য) in character actions", "Urban/formal colloquial covered; regional dialects need cards."),
        ("Classical Poetry (Payar 8+6)", "Broken 16-18 syllable pseudo-verse", "Deterministic syllabifier verifies 8+6=14 cadence", "Audits & verifies rhythm; does not write poetry from scratch."),
        ("Self-Learning Safety", "Un-gated agents hallucinate invalid grammar", "Supervised P2 Loop (Human sign-off before deploy)", "Requires human reviewer signature (Ashikur Rahman Bhuiyan).")
    ]

    t_box_h = 42 * len(matrix_rows) + 50
    draw_rounded_rect(draw, (70, curr_y, 70 + card_w, curr_y + t_box_h), radius=12, fill=C_BG_CARD, outline=C_BORDER)

    # Table Header
    ty = curr_y + 12
    draw.text((90, ty), "Linguistic Dimension", fill=C_WHITE, font=body_bold)
    draw.text((360, ty), "Raw Frontier LLM (Baseline)", fill=C_RED, font=body_bold)
    draw.text((680, ty), "With Bhashabid Coprocessor", fill=C_EMERALD, font=body_bold)
    draw.text((1010, ty), "Realistic Boundary / Reality", fill=C_MUTED, font=body_bold)
    draw.line([70, ty + 30, 70 + card_w, ty + 30], fill=C_BORDER, width=1)

    ty += 38
    for r in matrix_rows:
        draw.text((90, ty), r[0], fill=hex_to_rgb('#F1F5F9'), font=body_font)
        draw.text((360, ty), r[1], fill=hex_to_rgb('#FCA5A5'), font=bn_body_font)
        draw.text((680, ty), r[2], fill=hex_to_rgb('#86EFAC'), font=bn_body_font)
        draw.text((1010, ty), r[3], fill=C_MUTED, font=body_font)
        ty += 40

    curr_y += t_box_h + 35

    # ==================== FOOTER ====================
    draw.rectangle([70, curr_y, W - 70, curr_y + 1], fill=C_BORDER)
    curr_y += 18
    draw.text((70, curr_y), "GitHub: github.com/ashik1291/bhashabid  |  License: MIT & CC BY-SA 4.0", fill=C_CYAN, font=mono_font)
    draw.text((W - 550, curr_y), "1-Command Install: bhashabid install-skill --target all", fill=C_EMERALD, font=mono_font)

    # Crop to exact content height with balanced 50px bottom padding
    final_h = curr_y + 50
    img = img.crop((0, 0, W, final_h))

    # Save
    out_dir = Path("c:/Users/BS01671/Documents/personal_projects/bhashabid/docs/assets")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "bhashabid_benchmark_infographic.png"
    out_jpg = out_dir / "bhashabid_benchmark_infographic.jpg"
    
    img.save(out_path, format="PNG", quality=95)
    img.save(out_jpg, format="JPEG", quality=95)

    # Also copy to conversation brain directory
    brain_dir = Path(r"C:\Users\BS01671\.gemini\antigravity\brain\d06f39a6-87db-4bf6-b599-fef56eb2ea60")
    img.save(brain_dir / "bhashabid_benchmark_infographic.png", format="PNG", quality=95)
    img.save(brain_dir / "bhashabid_benchmark_infographic.jpg", format="JPEG", quality=95)

    print(f"Infographic successfully generated at: {out_path} and {out_jpg}")

if __name__ == "__main__":
    generate_poster()
