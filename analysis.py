import matplotlib.pyplot as plt

# Quarterly MRR growth
quarters = ["Q1", "Q2", "Q3", "Q4"]
growth = [4.06, 8.76, 10.71, 8.02]
industry_target = 15
average_mrr = sum(growth) / len(growth)

print("Average MRR Growth =", round(average_mrr, 2))  # MUST be 7.89

plt.figure(figsize=(6,4))
plt.plot(quarters, growth, marker='o', label="Company MRR Growth")
plt.axhline(industry_target, color='red', linestyle='--', label="Industry Target (15)")
plt.title("MRR Growth vs Industry Benchmark")
plt.ylabel("Growth (%)")
plt.legend()
plt.tight_layout()
plt.savefig("mrr_chart.png", dpi=150)
