def categorize(desc):
    desc = desc.lower()

    if any(x in desc for x in ["swiggy", "zomato"]):
        return "Food"
    elif any(x in desc for x in ["uber", "ola"]):
        return "Transport"
    elif any(x in desc for x in ["amazon", "flipkart"]):
        return "Shopping"
    elif "rent" in desc:
        return "Rent"
    elif "bill" in desc:
        return "Bills"
    elif "emi" in desc:
        return "Loan & EMI"
    else:
        return "Others"