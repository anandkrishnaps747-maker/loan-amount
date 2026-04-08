import tkinter as tk
from tkinter import messagebox

def calculate_loan():
    """
    Function to process user inputs, apply simple business rules, 
    and output loan approval status.
    """
    try:
        # 1. Get user inputs from the Entry widgets
        income_text = entry_income.get()
        score_text = entry_score.get()

        # Check if fields are empty
        if not income_text or not score_text:
            messagebox.showwarning("Incomplete Input", "Please fill in all the fields.")
            return

        # Convert simple strings to numbers
        income = float(income_text)
        credit_score = int(score_text)

        # 2. Validate inputs
        if income <= 0:
            messagebox.showerror("Invalid Input", "Income must be strictly greater than zero.")
            return

        if not (300 <= credit_score <= 900):
            messagebox.showerror("Invalid Input", "Credit score must be realistically between 300 and 900.")
            return

        # 3. Estimate Eligible Loan Amount
        # Using a realistic Fixed Obligation to Income Ratio (FOIR) model.
        # Safe EMI is typically capped at ~40% of monthly income.
        # This translates to loan multipliers capping out around 10-12x for standard personal loans.
        if credit_score < 550:
            eligible_amount = 0  # Too risky, essentially un-loanable
        elif credit_score < 650:
            # High risk, strict lending
            eligible_amount = income * 2
        elif credit_score < 700:
            # Average score (around 6x multiplier)
            eligible_amount = income * 6
        elif credit_score < 750:
            # Good score (around 9x multiplier)
            eligible_amount = income * 9
        else:
            # Excellent score grants the maximum safe limit (12x multiplier)
            eligible_amount = income * 12

        # 4. Predict Approval Status
        # Simple logical rules instead of complex ML for ease of understanding
        if eligible_amount > 0:
            status = "Approved (Eligible for Loan)"
            status_color = "green"
        else:
            status = "Rejected (Reason: Credit Score too low)"
            status_color = "red"

        # 5. Suggest Banks in India
        banks = []
        if eligible_amount == 0:
            banks = ["None (Improve Credit Score First)"]
        elif credit_score >= 750:
            banks = ["SBI", "HDFC Bank", "ICICI Bank (Premium Rates)"]
        elif credit_score >= 650:
            banks = ["Axis Bank", "Kotak Mahindra Bank", "Bank of Baroda"]
        else:
            banks = ["Bajaj Finserv", "Muthoot Finance", "Local NBFCs"]

        # 6. Display results clearly in the interface
        lbl_status_result.config(text=f"Status: {status}", fg=status_color)
        lbl_eligible_result.config(text=f"Eligible Amount: ₹ {eligible_amount:,.2f}")
        lbl_banks_result.config(text=f"Suggested Banks: {', '.join(banks)}")

    except ValueError:
        # Handle non-numeric and invalid inputs safely
        messagebox.showerror("Format Error", "Please enter valid numerical values (e.g. 50000, 720, 100000).")

# ================================
#       Build the Tkinter UI
# ================================

# Initialize main window
root = tk.Tk()
root.title("Loan Approval Prediction System")
root.geometry("450x450")
root.configure(padx=20, pady=20)

# Title Label
tk.Label(root, text="Smart Loan Predictor", font=("Helvetica", 16, "bold")).pack(pady=10)

# Input Frame to organize entry boxes
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Labels & Entries
tk.Label(frame_inputs, text="Monthly Income (₹):").grid(row=0, column=0, sticky="e", pady=5)
entry_income = tk.Entry(frame_inputs, width=20)
entry_income.grid(row=0, column=1, pady=5)

tk.Label(frame_inputs, text="Credit Score (300-900):").grid(row=1, column=0, sticky="e", pady=5)
entry_score = tk.Entry(frame_inputs, width=20)
entry_score.grid(row=1, column=1, pady=5)


# Calculate/Predict Button
btn_calculate = tk.Button(
    root, 
    text="Predict Loan Status", 
    bg="#4CAF50",       # A pleasant green shade
    fg="white", 
    font=("Helvetica", 12, "bold"), 
    command=calculate_loan
)
btn_calculate.pack(pady=15)

# Output Frame for results
frame_results = tk.Frame(root, pady=10)
frame_results.pack(fill="both", expand=True)

# Result Labels
lbl_status_result = tk.Label(frame_results, text="Status: --", font=("Helvetica", 12, "bold"))
lbl_status_result.pack(pady=2)

lbl_eligible_result = tk.Label(frame_results, text="Eligible Amount: --", font=("Helvetica", 11))
lbl_eligible_result.pack(pady=2)

lbl_banks_result = tk.Label(frame_results, text="Suggested Banks: --", font=("Helvetica", 11), wraplength=400)
lbl_banks_result.pack(pady=2)

# Sample Input Text
sample_info = "Sample Input: 60000 Income | 720 Score\nSample Output: Approved"
tk.Label(root, text=sample_info, font=("Helvetica", 8, "italic"), fg="gray").pack(side="bottom", pady=5)

# Keep window open
if __name__ == "__main__":
    root.mainloop()
