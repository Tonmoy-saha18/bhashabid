# tools/bn_legal/writs.py
# High Court Constitutional Writ Petitions (বাংলাদেশ সংবিধানের অনুচ্ছেদ ১০২ এর অধীন রিট মামলা)
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from ..bn_normalize.unicode import canonicalize_unicode

class WritType(Enum):
    HABEAS_CORPUS = "হেবিয়াস কর্পাস (বন্দি প্রদর্শন)"
    MANDAMUS = "ম্যান্ডামাস (পরমাদেশ)"
    CERTIORARI = "সার্টিওরারি / উৎপ্রেষণ (বাতিল ও রদকরণ)"
    PROHIBITION = "প্রোহিবিশন / প্রতিষেধ (বারণাদেশ)"
    QUO_WARRANTO = "কুও ওয়ারেন্টো (অধিকার পৃচ্ছা)"

@dataclass
class WritDraft:
    writ_type: WritType
    article_ref: str
    bench_designation: str
    cause_title: str
    prayers: List[str]
    grounds: List[str]

CONSTITUTIONAL_PROVISIONS = {
    WritType.HABEAS_CORPUS: "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ১০২(২)(খ)(১)",
    WritType.MANDAMUS: "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ১০২(২)(ক)(১)",
    WritType.CERTIORARI: "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ১০২(২)(ক)(২)",
    WritType.PROHIBITION: "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ১০২(২)(ক)(১)",
    WritType.QUO_WARRANTO: "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ১০২(২)(খ)(২)",
}

def determine_writ_type(remedy_sought: str) -> WritType:
    """
    Deterministically determines the correct constitutional writ based on the core remedy sought.
    """
    remedy = remedy_sought.lower()
    if any(k in remedy for k in ["detention", "custody", "illegal arrest", "আটক", "হেফাজত", "মুক্তি", "বন্দি"]):
        return WritType.HABEAS_CORPUS
    elif any(k in remedy for k in ["quash", "set aside", "illegal order", "আদেশ বাতিল", "রদ", "কার্যকারিতাহীন"]):
        return WritType.CERTIORARI
    elif any(k in remedy for k in ["refrain", "prohibit", "stop proceeding", "বিরত", "নিষেধ", "বারণ"]):
        return WritType.PROHIBITION
    elif any(k in remedy for k in ["public office", "qualification", "authority to hold", "পদের বৈধতা", "কর্তৃত্ববলে", "পদ শূন্য"]):
        return WritType.QUO_WARRANTO
    else:
        # Default statutory duty enforcement
        return WritType.MANDAMUS

def generate_writ_prayer(
    writ_type: WritType,
    subject: str,
    authority_name: str,
    style: str = "cholito"
) -> List[str]:
    """
    Generates standardized judicial Bengali prayers (প্রার্থিত প্রতিকার) matching Article 102 conventions.
    In modern Supreme Court practice in Bangladesh, petitions are drafted in formal Promito Cholito.
    """
    subject = canonicalize_unicode(subject.strip())
    authority = canonicalize_unicode(authority_name.strip())

    if style == "sadhu":
        if writ_type == WritType.HABEAS_CORPUS:
            return [
                f"আটককৃত ব্যক্তিকে অবিলম্বে অত্র মহামান্য আদালতের সম্মুখে হাজির করিবার জন্য {authority}-কে নির্দেশ প্রদান;",
                f"উক্ত আটকাদেশ কেন আইনগত কর্তৃত্ববহির্ভূত ও বেআইনি ঘোষণা করা হইবে না, তাহা প্রদর্শন করিবার জন্য রুল নিশি জারি;",
                "অত্র রিট পিটিশনের চূড়ান্ত শুনানি নিষ্পত্তির পূর্বে আটককৃত ব্যক্তিকে অন্তর্বর্তীকালীন জামিনে মুক্তির আদেশ প্রদান।"
            ]
        elif writ_type == WritType.MANDAMUS:
            return [
                f"{subject} বিষয়ে আইন অনুযায়ী অর্পিত দায়িত্ব পালন করিতে {authority}-কে বাধ্যকরণে উপযুক্ত নির্দেশ বা পরমাদেশ জারি;",
                f"{authority}-এর নিষ্ক্রিয়তা ও ব্যর্থতা কেন বেআইনি ও অসাংবিধানিক ঘোষণা করা হইবে না, তাহা প্রদর্শন করিবার জন্য রুল নিশি জারি।"
            ]
        elif writ_type == WritType.CERTIORARI:
            return [
                f"{authority} কর্তৃক প্রদত্ত উক্ত বিতর্কিত আদেশ ও কার্যধারা কেন আইনগত কর্তৃত্ববহির্ভূত ও আইনগত ফলাফলবিহীন ঘোষণা করা হইবে না, তাহা জানিতে চাহিয়া রুল নিশি জারি;",
                "উক্ত নথিপত্র অত্র আদালতে তলব করিয়া বিতর্কিত আদেশটি বাতিল ও প্রত্যাহার করিবার আদেশ প্রদান।"
            ]
        elif writ_type == WritType.PROHIBITION:
            return [
                f"{authority} যাহাতে এখতিয়ারবহির্ভূতভাবে {subject} সংক্রান্ত কোনো পদক্ষেপ গ্রহণ না করে, তজ্জন্য উপযুক্ত প্রতিষেধ আদেশ জারি;",
                "অত্র রুল নিষ্পত্তির পূর্ব পর্যন্ত সংশ্লিষ্ট সকল কার্যধারার ওপর স্থিতাবস্থা বজায় রাখিবার নির্দেশ।"
            ]
        elif writ_type == WritType.QUO_WARRANTO:
            return [
                f"{authority} কোন্ কর্তৃত্ববলে ও কী আইনি অধিকারে উক্ত পদ ধারণ করিতেছেন, তাহা আদালতকে প্রদর্শন করিবার নির্দেশ;",
                "উক্ত পদে অধিষ্ঠান কেন আইনবহির্ভূত ও অবৈধ ঘোষণা করিয়া পদটি শূন্য ঘোষণা করা হইবে না, তাহা প্রদর্শন করিবার জন্য রুল জারি।"
            ]
    else:
        # Default: Modern Promito Cholito (সুপ্রিম কোর্টের আধুনিক প্রমিত চলিত রীতি)
        if writ_type == WritType.HABEAS_CORPUS:
            return [
                f"আটক ব্যক্তিকে অবিলম্বে অত্র মহামান্য আদালতের সম্মুখে হাজির করার জন্য {authority}-কে নির্দেশ প্রদান;",
                f"উক্ত আটকাদেশ কেন আইনগত কর্তৃত্ববহির্ভূত ও বেআইনি ঘোষণা করা হবে না, তা প্রদর্শনের জন্য রুল নিশি জারি;",
                "অত্র রিট পিটিশনের চূড়ান্ত শুনানি নিষ্পত্তির পূর্বে আটক ব্যক্তিকে অন্তর্বর্তীকালীন জামিনে মুক্তির আদেশ প্রদান।"
            ]
        elif writ_type == WritType.MANDAMUS:
            return [
                f"{subject} বিষয়ে আইন অনুযায়ী অর্পিত দায়িত্ব পালন করতে {authority}-কে বাধ্য করার জন্য উপযুক্ত নির্দেশ বা পরমাদেশ জারি;",
                f"{authority}-এর নিষ্ক্রিয়তা ও ব্যর্থতা কেন বেআইনি ও অসাংবিধানিক ঘোষণা করা হবে না, তা প্রদর্শনের জন্য রুল নিশি জারি।"
            ]
        elif writ_type == WritType.CERTIORARI:
            return [
                f"{authority} কর্তৃক প্রদত্ত উক্ত বিতর্কিত আদেশ ও কার্যধারা কেন আইনগত কর্তৃত্ববহির্ভূত ও আইনগত ফলাফলবিহীন ঘোষণা করা হবে না, তা জানতে চেয়ে রুল নিশি জারি;",
                "উক্ত নথিপত্র অত্র আদালতে তলব করে বিতর্কিত আদেশটি বাতিল ও প্রত্যাহার করার আদেশ প্রদান।"
            ]
        elif writ_type == WritType.PROHIBITION:
            return [
                f"{authority} যাতে এখতিয়ারবহির্ভূতভাবে {subject} সংক্রান্ত কোনো পদক্ষেপ গ্রহণ না করে, সেজন্য উপযুক্ত প্রতিষেধ আদেশ জারি;",
                "অত্র রুল নিষ্পত্তির পূর্ব পর্যন্ত সংশ্লিষ্ট সকল কার্যধারার ওপর স্থিতাবস্থা বজায় রাখার নির্দেশ।"
            ]
        elif writ_type == WritType.QUO_WARRANTO:
            return [
                f"{authority} কোন্ কর্তৃত্ববলে ও কী আইনি অধিকারে উক্ত পদ ধারণ করছেন, তা আদালতকে প্রদর্শনের নির্দেশ;",
                "উক্ত পদে অধিষ্ঠান কেন আইনবহির্ভূত ও অবৈধ ঘোষণা করে পদটি শূন্য ঘোষণা করা হবে না, তা প্রদর্শনের জন্য রুল জারি।"
            ]

    return []
