# tools/adversarial_generator.py
# Dynamic Adversarial Perturbation & Multi-Domain Linguistic Stress Generator
import random
import re
from typing import List, Tuple, Dict

# Known common LLM corruption patterns across Bengali sectors
ORTHOGRAPHIC_PERTURBATIONS = [
    ("পোস্ট", "পোষ্ট"),
    ("মাস্টার", "মাষ্টার"),
    ("স্টেশন", "ষ্টেশন"),
    ("স্টাফ", "ষ্টাফ"),
    ("বাড়ি", "বাড়ী"),
    ("শ্রেণি", "শ্রেণী"),
    ("পাখি", "পাখী"),
    ("বেশি", "বেশী"),
    ("ইতিমধ্যে", "ইতোমধ্যে"),
    ("পুরস্কার", "পুরষ্কার"),
    ("গীতাঞ্জলি", "গীতাঞ্জলী"),
    ("শ্রদ্ধাঞ্জলি", "শ্রদ্ধাঞ্জলী"),
    ("প্রমিত", "প্রমীত"),
]

SYNTACTIC_CALQUES = [
    ("কারণে", "দ্বারা চালিত হয়ে"),
    ("পরিচালিত হচ্ছে", "দ্বারা পরিচালিত হইতেছে"),
    ("অনুষ্ঠিত হয়", "দ্বারা অনুষ্ঠিত করা হয়"),
    ("নেতৃত্বে", "কর্তৃক চালিত হয়ে"),
    ("সিদ্ধান্ত গৃহীত হয়", "সিদ্ধান্ত নেওয়া হয়েছে"),
    ("সবশেষে", "দিনের শেষে"),
]

SADHU_CHOLITO_INJECTIONS = [
    ("হয়েছে", "হইয়াছে"),
    ("করেছেন", "করিয়াছেন"),
    ("করছে", "করিতেছে"),
    ("হবে", "হইবে"),
    ("বললেন", "বলিলেন"),
    ("যাচ্ছে", "যাইতেছে"),
]

NUMERAL_CORRUPTIONS = [
    ("১", "1"),
    ("২", "2"),
    ("৩", "3"),
    ("৪", "4"),
    ("৫", "5"),
    ("৬", "6"),
    ("৭", "7"),
    ("৮", "8"),
    ("৯", "9"),
    ("০", "0"),
]

class AdversarialGenerator:
    """
    Generates dynamic linguistic perturbations, synthetic edge cases,
    and adversarial sentence variants to ensure continuous learning and
    prevent stagnation on static benchmark data.
    """

    def __init__(self, seed: int = None):
        if seed is not None:
            random.seed(seed)

    def perturb_orthography(self, text: str) -> Tuple[str, str]:
        """Injects non-standard or pre-1992 spelling variants common in LLMs."""
        for clean, flawed in ORTHOGRAPHIC_PERTURBATIONS:
            if clean in text:
                return text.replace(clean, flawed, 1), f"Orthographic corruption: '{clean}' -> '{flawed}'"
        return text, "No orthographic pattern found"

    def perturb_calque(self, text: str) -> Tuple[str, str]:
        """Injects literal English passive syntax calques."""
        for clean, flawed in SYNTACTIC_CALQUES:
            if clean in text:
                return text.replace(clean, flawed, 1), f"Syntactic calque: '{clean}' -> '{flawed}'"
        return text, "No syntactic calque pattern found"

    def perturb_sadhu_cholito_mix(self, text: str) -> Tuple[str, str]:
        """Injects Guru-Chondali (Sadhu/Cholito verb clash) defect."""
        for cholito, sadhu in SADHU_CHOLITO_INJECTIONS:
            if cholito in text:
                # Replace only first occurrence so rest remains Cholito, creating a clash
                return text.replace(cholito, sadhu, 1), f"Guru-Chondali clash: injected Sadhu '{sadhu}' into Cholito sentence"
        return text, "No verb clash pattern found"

    def perturb_unicode(self, text: str) -> Tuple[str, str]:
        """Injects non-NFC decomposed Bengali Unicode (e.g. split O-kar into E-kar + Aa-kar)."""
        # Bengali O-kar is \u09cb; decomposed is \u09c7\u09be
        if "\u09cb" in text:
            return text.replace("\u09cb", "\u09c7\u09be", 1), "Unicode decomposition: NFC O-kar converted to split [E-kar + Aa-kar]"
        return text, "No decomposable vowel found"

    def generate_dynamic_batch(self, base_sentences: List[Tuple[str, str, str]], sample_size: int = 25) -> List[Tuple[str, str, str]]:
        """
        Takes base sentences (domain, text, category) and synthesizes fresh,
        adversarial test cases for practice rounds.
        """
        if not base_sentences:
            return []

        selected = random.sample(base_sentences, min(len(base_sentences), sample_size))
        dynamic_batch = []

        methods = [
            self.perturb_orthography,
            self.perturb_calque,
            self.perturb_sadhu_cholito_mix,
            self.perturb_unicode
        ]

        for domain, text, cat in selected:
            # 50% chance of introducing an adversarial perturbation
            if random.random() > 0.5:
                method = random.choice(methods)
                perturbed_text, label = method(text)
                dynamic_batch.append((domain, perturbed_text, f"DYNAMIC_ADVERSARIAL: {label}"))
            else:
                dynamic_batch.append((domain, text, cat))

        return dynamic_batch
