from image_analysis import analyze_image

result, _ = analyze_image("images/sample.jpg")

print("Blur Score:", result["blur_score"])
print("Edge Score:", result["edge_score"])

