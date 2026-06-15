import pdfplumber
import pandas as pd
import re

def extract_transactions(pdf_file):
    data = []

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if not text:
                continue

            lines = text.split("\n")

            for line in lines:
                # Extract ₹ amount
                match = re.search(r'₹\s?([\d,]+\.?\d*)', line)

                if match:
                    amount = float(match.group(1).replace(",", ""))

                    line_lower = line.lower()

                    # ✅ Smart detection
                    if "cr" in line_lower or "credited" in line_lower or "received" in line_lower:
                        amount = amount   # income
                    elif "dr" in line_lower or "debited" in line_lower or "paid" in line_lower:
                        amount = -amount  # expense
                    else:
                        # fallback → assume expense
                        amount = -amount

                    data.append([line, amount])

    df = pd.DataFrame(data, columns=["Description", "Amount"])
    return df